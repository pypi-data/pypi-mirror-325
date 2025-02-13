from fasthtml.common import *
from fasthtml.svg import *
from monsterui.all import *

from flock.app.components import HistoryGrid, Sidebar
from flock.app.modules import AgentContent, AgentDetailView, Playground, Settings, agent_data
from flock.app.modules.about import AboutPage

hdrs = Theme.blue.headers()

app, rt = fast_app(hdrs=hdrs, live=True)

##############################
# Sidebar
##############################

sidebar = (
    ("layout-dashboard", "Dashboard", "/"),
    ("---", "", ""),
    ("bot", "Agents", "/agents"),
    ("server", "Agent Systems", "/systems"),
    ("scroll", "History", "/history"),
    ("---", "", ""),
    ("wrench", "Tools", "/tools"),
    ("test-tube", "Playground", "/playground"),
    ("---", "", ""),
    ("settings", "Settings", "/settings"),
    ("info", "About", "/about"),
)


##############################
# MAIN
##############################


@rt
def index():
    return (
        Title("Flock UI"),
        Container(
            Grid(
                Div(Sidebar(sidebar), cls="col-span-1 w-48 flex"),
                Grid(
                    Div(AgentContent(), cls="col-span-2"),
                    Div(AgentDetailView(agent_data[0]), cls="col-span-3"),
                    cols=5,
                    cls="col-span-5",
                    id="main-grid",
                ),
                cols_sm=2,
                cols_md=2,
                cols_lg=6,
                cols_xl=6,
                gap=5,
                cls="flex-1",
            ),
            cls=("flex", ContainerT.xl),
        ),
    )


@rt("/history")
def get():
    return Grid(
        Div(HistoryGrid(), cls="col-span-5"),
        cols=5,
        cls="col-span-5",
        id="main-grid",
    )


@rt("/playground")
def get():
    return Grid(
        Div(Playground(), cls="col-span-5"),  # noqa: F405
        cols=5,
        cls="col-span-5",
        id="main-grid",
    )


@rt("/settings")
def get():
    return Grid(
        Div(Settings(), cls="col-span-5"),
        cols=5,
        cls="col-span-5",
        id="main-grid",
    )


@rt("/agents")
def get():
    return Grid(
        Div(AgentContent(), cls="col-span-2"),
        Div(AgentDetailView(agent=agent_data[0]), cls="col-span-3"),
        cols=5,
        cls="col-span-5",
        id="main-grid",
    )


@rt("/about")
def get():
    return Grid(
        Div(AboutPage(), cls="col-span-5"),
        cols=5,
        cls="col-span-5",
        id="main-grid",
    )


serve()


def main():
    serve()
