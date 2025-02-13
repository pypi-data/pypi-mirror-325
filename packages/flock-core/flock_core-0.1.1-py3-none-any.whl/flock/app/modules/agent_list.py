import json
import pathlib

from fasthtml.common import *
from fasthtml.svg import *
from monsterui.all import *

from flock.app.components.util import format_date

agent_data = json.load(open(pathlib.Path("data/mock.json")))


def AgentItem(agent):
    cls_base = "space-y-4 relative rounded-lg border border-border p-3 text-sm hover:bg-primary"
    cls = f"{cls_base} {'bg-muted' if agent == agent_data[0] else ''} {'tag-unread' if not agent['production_ready'] else 'tag-mail'}"

    return Li(cls=cls)(
        DivFullySpaced(
            DivLAligned(
                Span(UkIcon(agent["icon"]), cls="flex h-10 w-10 items-center justify-center"),
                Div(agent["title"], cls="font-semibold"),
                Span(cls="flex h-2 w-2 rounded-full bg-green-600") if agent["production_ready"] else "",
            ),
            Div(format_date(agent["created_at"]), cls="text-xs"),
            cls="mb-4",
        ),
        A(agent["name"], cls=TextFont.bold_sm, href=f"#agent-{agent['id']}"),
        Div(agent["description"][:100] + "...", cls=TextFont.muted_sm),
        DivLAligned(*[
            A(label, cls=f"uk-label relative z-10 {'uk-label-primary' if label == 'analysis' else ''}", href="#")
            for label in agent["labels"]
        ]),
    )


def AgentList(agents):
    return Ul(cls="js-filter space-y-4 p-4 pt-0")(*[AgentItem(agent) for agent in agents])


def AgentContent():
    return Div(cls="flex flex-col", uk_filter="target: .js-filter")(
        Div(cls="flex px-4 py-2 ")(
            H3("Agents"),
            TabContainer(
                Li(A("All Agents", href="#", role="button"), cls="uk-active", uk_filter_control="filter: .tag-mail"),
                Li(A("Production Ready", href="#", role="button"), uk_filter_control="filter: .tag-unread"),
                alt=True,
                cls="ml-auto max-w-80",
            ),
        ),
        Div(cls="flex flex-1 flex-col")(
            Div(cls="p-4")(
                Div(cls="uk-inline w-full")(
                    Span(cls="uk-form-icon text-muted-foreground")(UkIcon("search")), Input(placeholder="Search")
                )
            ),
            Div(cls="flex-1 overflow-y-auto max-h-[800px]")(AgentList(agent_data)),
        ),
    )
