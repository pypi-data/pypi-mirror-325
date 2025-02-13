"""Agent History Explorer built with MonsterUI"""

import json
from datetime import datetime

from fasthtml.common import *
from monsterui.all import *


def load_history(page=1, per_page=10, search=None):
    with open("data/history.json") as f:
        data = json.load(f)

    if search:
        search = search.lower()
        data = [
            d
            for d in data
            if search in d["agent_name"].lower() or search in d["location"].lower() or search in d["date"].lower()
        ]

    total = len(data)
    pages = (total + per_page - 1) // per_page
    start = (page - 1) * per_page
    return {"data": data[start : start + per_page], "total": total, "pages": pages, "page": page}


def format_date(iso_date):
    return datetime.fromisoformat(iso_date).strftime("%b %d, %Y %H:%M")


def json_preview(value):
    return Pre(json.dumps(value, indent=2), cls="text-xs p-2 bg-muted rounded-md max-h-40 overflow-auto")


def header_render(col):
    return Th(col, cls="p-2 text-left")


def cell_render(col, val):
    """Modified cell renderer that only uses column value"""
    match col:
        case "Agent":
            return Td(cls="p-2 font-medium")(Div(val))
        case "Date":
            return Td(cls="p-2 text-sm")(format_date(val))
        case "Location":
            return Td(cls="p-2 capitalize")(val)  # val is already location string
        case "Input" | "Output":
            return Td(cls="p-2")(json_preview(val))
        case "Details":
            # val contains the full record here
            return Td(cls="p-2")(Button("View", cls=ButtonT.primary, uk_toggle=f"target: #details-{val['agent_id']}"))


def details_modal(record):
    return Modal(
        Div(cls="p-6 space-y-4")(
            ModalTitle(f"{record['agent_name']} - {format_date(record['date'])}"),
            Grid(
                Div(cls="space-y-2")(H4("Input Details", cls="text-sm font-medium"), json_preview(record["input"])),
                Div(cls="space-y-2")(H4("Output Details", cls="text-sm font-medium"), json_preview(record["output"])),
            ),
            DivRAligned(ModalCloseButton("Close", cls=ButtonT.ghost)),
        ),
        id=f"details-{record['agent_id']}",
    )


def get_history(page: int = 1, per_page: int = 5, search: str = None, reduced=False):
    history = load_history(page, per_page, search)

    controls = DivFullySpaced(cls="mt-8")(
        Div(cls="flex gap-4 items-center")(
            Input(
                placeholder="Search agents...",
                value=search,
                name="search",
                hx_get="/history",
                hx_trigger="keyup changed delay:500ms",
                hx_target="#history-content",
                hx_include="[name='per_page']",
                cls="w-64",
            ),
            Select(
                Option("5", value="5"),
                Option("10", value="10"),
                Option("20", value="20"),
                name="per_page",
                value=str(per_page),
                hx_get="/history",
                hx_trigger="change",
                hx_target="#history-content",
                cls="w-24",
            ),
        )
    )

    if reduced:
        header_data = ["Agent", "Date", "Details"]
        bodydata = [
            {
                "Agent": d["agent_name"],
                "Date": d["date"],
                "Details": d,  # Store full record here
            }
            for d in history["data"]
        ]
    else:
        header_data = ["Agent", "Date", "Input", "Output", "Details"]
        bodydata = [
            {
                "Agent": d["agent_name"],
                "Date": d["date"],
                # "Location": d["input"]["location"],  # Pre-extract location
                "Input": d["input"],
                "Output": d["output"],
                "Details": d,  # Store full record here
            }
            for d in history["data"]
        ]

    table = TableFromDicts(
        header_data=header_data,
        body_data=bodydata,
        body_cell_render=cell_render,
        header_cell_render=header_render,
        cls=TableT.responsive,
    )

    footer = DivFullySpaced(cls="mt-4")(
        Div(
            f"Showing {min(history['total'], per_page)} of {history['total']} records",
            cls="text-sm text-muted-foreground",
        ),
        Div(cls="flex items-center gap-4")(
            Button(
                "< Prev",
                hx_get=f"/history?page={history['page'] - 1}",
                hx_target="#history-content",
                disabled=history["page"] == 1,
                cls=ButtonT.primary,
            ),
            Span(f"Page {history['page']} of {history['pages']}"),
            Button(
                "Next >",
                hx_get=f"/history?page={history['page'] + 1}",
                hx_target="#history-content",
                disabled=history["page"] == history["pages"],
                cls=ButtonT.primary,
            ),
        ),
    )

    return Div(id="history-content")(controls, table, footer, *[details_modal(d) for d in history["data"]])


def HistoryGrid(reduced=False):
    if reduced:
        return get_history(reduced)

    return Div(cls="flex flex-col")(
        Div(cls="px-4 py-2 ")(
            H3("Agent History Explorer"),
            P("Review historical agent executions and their outcomes", cls=TextFont.muted_sm),
        ),
        get_history(reduced),
    )
