from fasthtml.common import *
from fasthtml.svg import *
from monsterui.all import *

from flock.app.components import CoreArchitectureChart


def AboutPage():
    return Div(cls="flex flex-col", uk_filter="target: .js-filter")(
        Div(cls="flex px-4 py-2 ")(
            H3("About & Help"),
        ),
        Div(
            Div(cls="p-4")(CoreArchitectureChart()),
            cls="w-[1200px]",
        ),
    )
