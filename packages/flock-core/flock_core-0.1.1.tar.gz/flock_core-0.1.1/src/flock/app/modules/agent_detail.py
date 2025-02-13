from fasthtml.common import *
from fasthtml.svg import *
from monsterui.all import *

from flock.app.components import HistoryGrid
from flock.app.components.util import IconNav, IconNavItem, format_date

##############################
# Agents
##############################


def AgentDetailView(agent):
    action_icons = [("copy", "Duplicate"), ("pencil", "Edit"), ("cloud-upload", "Deploy")]
    status_items = ["Toggle Production", "Arcflock", "Add Label", "Monitor Usage"]

    return Div(cls="flex flex-col")(
        Div(cls="flex h-14 flex-none items-center border-b border-border p-2")(
            DivFullySpaced(
                DivLAligned(
                    IconNav(*IconNavItem(*action_icons)),
                    IconNav(Li(A(UkIcon("activity"), uk_tooltip="Metrics")), cls="pl-2"),
                    cls="gap-x-2 divide-x divide-border",
                ),
                IconNav(
                    *IconNavItem(("trash", "Delete"), ("code", "View JSON")),
                    Li(A(UkIcon("ellipsis-vertical", button=True))),
                    DropDownNavContainer(*map(lambda x: Li(A(x)), status_items)),
                ),
            )
        ),
        Div(cls="flex-1")(
            DivLAligned(
                DivLAligned(
                    Span(UkIcon(agent["icon"]), cls="flex h-10 w-10 items-center justify-center rounded-full bg-muted"),
                    Div(cls="grid gap-1")(
                        Div(agent["title"], cls=TextT.bold),
                        Div(agent["name"], cls="text-xs"),
                        #                        DivLAligned("Type:", agent["type"], cls=TextT.sm),
                    ),
                    cls="gap-4 text-sm",
                ),
                Div(format_date(agent["created_at"]), cls=TextFont.muted_sm),
                cls="p-4",
            ),
            Div(cls="flex-1 space-y-4 border-t border-border p-4 text-sm")(
                P(agent["description"]),
                Dl(cls="grid grid-cols-2 gap-4")(
                    DivLAligned(
                        Dt("Production Ready", cls=TextT.muted), Dd("✅" if agent["production_ready"] else "❌")
                    ),
                    DivLAligned(Dt("Last Updated", cls=TextT.muted), Dd(format_date(agent["last_updated"]))),
                    DivLAligned(Dt("Input Schema", cls=TextT.muted), Dd(agent["input"], cls="font-mono text-xs")),
                    DivLAligned(Dt("Output Schema", cls=TextT.muted), Dd(agent["output"], cls="font-mono text-xs")),
                ),
            ),
        ),
        Div(cls="flex-none space-y-4 border-t border-border p-4")(
            DivFullySpaced(
                HistoryGrid(reduced=True),
            ),
        ),
        Div(cls="flex-none space-y-4 border-t border-border p-4")(
            DivFullySpaced(
                LabelSwitch("Monitoring Enabled", id="monitoring"),
                Button("Export Configuration", cls=ButtonT.secondary),
                Button("Run Agent", cls=ButtonT.primary),
            ),
        ),
    )
