"""FrankenUI Forms Example built with MonsterUI (original design by ShadCN)"""

from fasthtml.common import *
from fasthtml.svg import *
from monsterui.all import *

from flock.app.components import ThemeDialog


def HelpText(c):
    return P(c, cls=TextFont.muted_sm)


def heading():
    return Div(cls="px-4 py-2 ")(
        H3("Settings"),
        P("Manage your account settings and set e-mail preferences.", cls=TextFont.muted_lg),
        DividerSplit(),
    )


sidebar_items = ["API Keys", "Appearance", "Display"]

sidebar = NavContainer(
    *map(lambda x: Li(A(x)), sidebar_items),
    uk_switcher="connect: #component-nav; animation: uk-animation-fade",
    cls=(NavT.secondary, "space-y-4 p-4 w-1/5"),
)


def FormSectionDiv(*c, cls="space-y-2", **kwargs):
    return Div(*c, cls=cls, **kwargs)


def api_key_form():
    content = (
        FormSectionDiv(
            LabelInput("Open AI API Key", placeholder="sk-...", id="username"),
            HelpText("This is your Open AI API key. You can find it in your account settings. "),
        ),
    )

    return UkFormSection("API Keys", "Manage API keys of your agents", button_txt="Update api keys", *content)


def appearance_form():
    content = (
        FormSectionDiv(
            LabelUkSelect(
                *Options("Select a font family", "Inter", "Geist", "Open Sans", selected_idx=2, disabled_idxs={0}),
                label="Font Family",
                id="font_family",
            ),
            HelpText("Set the font you want to use in the dashboard."),
        ),
        FormSectionDiv(
            FormLabel("Theme"),
            HelpText("Select the theme for the dashboard."),
            ThemeDialog(),
        ),
    )

    return UkFormSection(
        "Appearance",
        "Customize the appearance of the app. Automatically switch between day and night themes.",
        button_txt="Update preferences",
        *content,
    )


def display_form():
    content = Div(cls="space-y-2")(
        Div(cls="mb-4")(
            Span("Sidebar", cls="text-base font-medium"),
            HelpText("Select the items you want to display in the sidebar."),
        ),
        *[
            Div(CheckboxX(id=f"display_{i}", checked=i in [0, 1, 2]), FormLabel(label))
            for i, label in enumerate(["Recents", "Home", "Applications", "Desktop", "Downloads", "Documents"])
        ],
    )
    return UkFormSection(
        "Display", "Turn items on or off to control what's displayed in the app.", button_txt="Update display", *content
    )


def Settings():
    return Title("Settings form"), Container(
        heading(),
        Div(cls="flex gap-x-12")(
            sidebar,
            Ul(id="component-nav", cls="uk-switcher max-w-2xl")(
                Li(cls="uk-active")(api_key_form(), *map(Li, [appearance_form(), display_form()]))
            ),
        ),
    )
