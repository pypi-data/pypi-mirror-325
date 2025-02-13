from fasthtml.common import *
from fasthtml.svg import *
from monsterui.all import *


def SidebarLi(icon, title=None, href=None):
    if icon == "---":
        return Li(Hr())
    return Li(
        AX(DivLAligned(Span(UkIcon(icon)), Span(title)), hx_get=href, hx_target="#main-grid", hx_swap="outerHTML")
    )


def Sidebar(sidebar):
    return NavContainer(
        NavHeaderLi(H1("Flock UI", cls="text-xxl font-semibold")),
        *[SidebarLi(icon, title, href) for icon, title, href in sidebar],
        cls="space-y-6 mt-3",
    )
