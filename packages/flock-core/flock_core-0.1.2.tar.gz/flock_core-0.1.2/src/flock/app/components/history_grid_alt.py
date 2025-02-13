"""Agent History Explorer built with MonsterUI"""

import json
from datetime import datetime

from fasthtml.common import *
from monsterui.all import *


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


def load_history(page=1, per_page=10, search=None):
    with open("data/history.json") as f:
        data = json.load(f)

    # Full-text search across all fields
    if search:
        search = search.lower()
        data = [
            d
            for d in data
            if any(search in str(v).lower() for v in d.values())
            or any(search in str(v).lower() for sub in [d["input"], d["output"]] for v in sub.values())
        ]

    total = len(data)
    pages = (total + per_page - 1) // per_page
    start = (page - 1) * per_page
    return {"data": data[start : start + per_page], "total": total, "pages": pages, "page": page}


def json_tree(value, depth=0):
    if isinstance(value, dict):
        return Div(cls=f"ml-{depth * 2} space-y-1")(
            *[Details(Summary(k, cls="inline-flex items-center"), json_tree(v, depth + 1)) for k, v in value.items()]
        )
    elif isinstance(value, list):
        return Div(cls=f"ml-{depth * 2} space-y-1")(
            *[
                Div(cls="flex items-center gap-2")(Span("•", cls="text-muted-foreground"), json_tree(item, depth + 1))
                for item in value
            ]
        )
    return Span(str(value), cls="text-muted-foreground")


def render_cell(col, val):
    match col:
        case "date":
            return datetime.fromisoformat(val).strftime("%b %d, %Y %H:%M")
        case "input" | "output":
            return Div(cls="max-w-[300px] overflow-auto p-2 bg-muted rounded-md")(json_tree(val))
        case "_expand":
            return Button("Expand", cls=ButtonT.primary, uk_toggle=f"target: #details-{val['agent_id']}")
        case _:
            return val if isinstance(val, str) else json.dumps(val, default=str)


def details_modal(record):
    return Modal(
        Div(cls="p-6 space-y-4")(
            ModalTitle(f"Agent Execution Details - {record['agent_id']}"),
            Div(cls="space-y-4")(
                Div(cls="grid grid-cols-2 gap-4")(
                    Div(cls="space-y-2")(H4("Input", cls="text-sm font-medium"), json_tree(record["input"])),
                    Div(cls="space-y-2")(H4("Output", cls="text-sm font-medium"), json_tree(record["output"])),
                ),
                Div(cls="space-y-2")(
                    H4("Metadata", cls="text-sm font-medium"),
                    json_tree({k: v for k, v in record.items() if k not in ["input", "output"]}),
                ),
            ),
            DivRAligned(ModalCloseButton("Close", cls=ButtonT.ghost)),
        ),
        id=f"details-{record['agent_id']}",
    )


def Pagination(current_page, total_pages, hx_get, hx_target):
    return Div(cls="flex items-center gap-2")(
        Button(
            "Previous",
            disabled=current_page == 1,
            hx_get=f"{hx_get}?page={current_page - 1}",
            hx_target=hx_target,
            cls=ButtonT.primary,
        ),
        Span(f"Page {current_page} of {total_pages}", cls="text-sm"),
        Button(
            "Next",
            disabled=current_page >= total_pages,
            hx_get=f"{hx_get}?page={current_page + 1}",
            hx_target=hx_target,
            cls=ButtonT.primary,
        ),
    )


def get_history(page: int = 1, per_page: int = 10, search: str = None):
    history = load_history(page, per_page, search)

    # Dynamic columns from first record (if exists)
    columns = []
    if history["data"]:
        sample = history["data"][0]
        columns = [k for k in sample.keys() if k not in ["input", "output", "agent_id"]]
        columns += ["input", "output", "_expand"]

    controls = DivFullySpaced(cls="mt-8")(
        Input(
            placeholder="Search history...",
            value=search,
            name="search",
            hx_get="/history",
            hx_trigger="keyup changed delay:500ms",
            hx_target="#history-content",
            hx_include="[name='per_page']",
            cls="w-64",
        ),
        Select(
            *[Option(str(n), value=str(n)) for n in [5, 10, 20, 50]],
            name="per_page",
            value=str(per_page),
            hx_get="/history",
            hx_trigger="change",
            hx_target="#history-content",
            cls="w-24",
        ),
    )

    table = TableFromDicts(
        header_data=columns,
        body_data=[{**d, "_expand": d} for d in history["data"]],
        body_cell_render=lambda col, val: Td(render_cell(col, val)),
        header_cell_render=lambda col: Th(col.replace("_", " ").title(), cls="p-2 text-left"),
        cls=f"{TableT.responsive} {TableT.hover}",
    )

    footer = DivFullySpaced(cls="mt-4")(
        Div(
            f"Showing {(page - 1) * per_page + 1}-{min(page * per_page, history['total'])} of {history['total']} records",
            cls="text-sm text-muted-foreground",
        ),
        Pagination(current_page=page, total_pages=history["pages"], hx_get="/history", hx_target="#history-content"),
    )

    return Div(id="history-content")(
        controls,
        table if history["data"] else P("No records found", cls=TextFont.muted),
        footer,
        *[details_modal(d) for d in history["data"]],
    )


def HistoryGrid(reduced=False):
    return Container(
        Div(cls="space-y-4")(
            H1("Agent History Explorer"),
            P("Inspect agent executions with dynamic JSON exploration", cls=TextFont.muted_sm),
        ),
        get_history(),
        cls="p-8",
    )
