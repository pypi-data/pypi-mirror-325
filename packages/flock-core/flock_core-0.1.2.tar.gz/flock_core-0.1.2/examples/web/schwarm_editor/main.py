from devtools import pprint
from fasthtml.common import *
from monsterui.all import *

from flock.core.agents.declarative_agent import DeclarativeAgent
from flock.core.flock import Flock

# App Instance + Routes

try:
    css = open("./examples/web/flock_editor/scripts/editor.css")
except NameError:
    css = open("./scripts/editor.css")

try:
    js = open("./examples/web/flock_editor/scripts/editor.js")
except NameError:
    js = open("./scripts/editor.js")


hdrs = (
    Theme.stone.headers(highlightjs=True),
    Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/codemirror.min.css"),
    Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/theme/monokai.min.css"),
    Script(src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/codemirror.min.js"),
    Script(src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/mode/javascript/javascript.min.js"),
    Script(src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/mode/xml/xml.min.js"),
    Script(src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/mode/css/css.min.js"),
    Script(src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/mode/python/python.min.js"),
    Script(src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/addon/edit/matchbrackets.min.js"),
    Script(src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/addon/edit/closebrackets.min.js"),
    Script(src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/addon/comment/comment.min.js"),
    Script(src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/addon/selection/active-line.min.js"),
    Style(css.read()),
)
app, rt = fast_app(hdrs=hdrs, live=True)


@rt("/")
def get():
    return Body(
        Div(
            Div(
                Style(
                    ".grid-container {max-width: 100%; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; padding: 1rem; } .sleek {  border-radius: 8px; box-shadow: 2px 2px 4px rgba(255, 255, 255, 0.1); padding: 1rem; } "
                )
            )
        )(
            Main(
                Div(
                    H2("Code Editor"),
                    # Div(
                    #     Button("Theme Switcher", uk_toggle="target: #my-modal"),
                    #     Modal(
                    #         ModalTitle("Theme Switcher"),
                    #         Uk_theme_switcher(),
                    #         footer=ModalCloseButton("Close", cls=ButtonT.primary),
                    #         id="my-modal",
                    #     ),
                    # ),
                    LabelInput(label="Saved html file", id="fileInput", type="file", cls="mt-4"),
                    # ex_form(),
                    Form(
                        hx_post="/html2ft",
                        target_id="ft",
                        hx_trigger="change from:#attr1st, change from:#editor",
                    )(
                        Div(cls="space-y-4")(
                            Grid(
                                LabelInput("Idea", id="idea", cls="idea", rows="1"),
                                Button(
                                    "Evaluate Idea",
                                    id="convertButton",
                                    hx_post="/evalIdea",
                                    hx_trigger="click",
                                    hx_target="#editor",
                                    hx_request="include:#idea",
                                    cls=ButtonT.primary + " mt-6",
                                ),
                            ),
                            Grid(
                                LabelSelect(
                                    *[
                                        Option("Children 1st", value="0", selected=True),
                                        Option("Attrs 1st", value="1"),
                                    ],
                                    label="Order of Attributes",
                                    id="attr1st",
                                    cls="space-y-2 space-x-2",
                                ),
                                LabelSelect(
                                    *[
                                        Option("none", value="0", selected=True),
                                        Option("tailwind", value="1"),
                                        Option("monsterio/shadcn", value="2"),
                                    ],
                                    label="Style Framework",
                                    id="styleframework",
                                    cls="space-y-2 space-x-2",
                                    rows="1",
                                ),
                                Button(
                                    "Convert HTML to FastHTML",
                                    id="convertButton",
                                    hx_post="/html2ft",
                                    target_id="ft",
                                    hx_trigger="click",
                                    hx_request="include:#styleframework,#editor,#attr1st",
                                    cls=ButtonT.primary + " mt-8",
                                ),
                            ),
                        ),
                        Div(Textarea(id="editor", cls="editor mt-8"), cls="mt-4"),
                        cls="sleek input-area editor-container",
                    ),
                ),
                Div(H1("Preview"), id="ft", cls="sleek preview-area"),
                cls="grid-container container w-max",
                style="./scripts/editor.css",
            ),
            Script(code=js.read()),
        )
    )


@rt("/evalIdea")
async def post(idea: str):
    flock = Flock()
    agent = DeclarativeAgent(
        name="io_agent",
        input="idea_for_webcomponent",
        output="div_container_implemented_with_static_html_and_with_js_and_css",
    )
    flock._add_agent(agent)

    _res = await flock.run_async(start_agent=agent, input=idea)
    pprint(_res)
    raw_output = _res["agents"][0]["io_agent"]["div_container_implemented_with_static_html_and_with_js_and_css"]
    pprint(raw_output)
    with open("out.html", "w") as f:
        f.write(raw_output)
    return Script(f"load_from_file();")


@rt("/html2ft")
def post(idea: str, editor: str, attr1st: bool, styleframework: int):
    ft = html2ft(editor, attr1st=str2bool(attr1st))

    pprint(editor)

    pprint(styleframework)
    if styleframework == 1:
        editor = f'<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">{editor}'

    if styleframework == 1 or styleframework == 0:
        rendered_preview = Iframe(
            id="preview-frame",
            style="width: 1024px; min-height: 500px; border: none; ",
            srcdoc=editor,
        )
    else:
        rendered_preview = Div(
            id="preview-frame",
            style="width: 1024px; min-height: 500px; border: none; ",
        )(NotStr(editor))

    return Div(
        Div(
            H3("Preview"),
            Div(
                rendered_preview,
                cls="preview-area",
            ),
            H3("Python/FastHTML Code", style="margin-top: 1rem;margin-bottom: 0rem;"),
            Div(
                CodeBlock(ft),
                CodeBlock(ft),
                cls="preview-area",
                style="max-width: 1024px; overflow-wrap: break-word; white-space: pre-wrap;",
            ),
            cls="sleek preview-areas",
        )
        if editor
        else ""
    )


serve()
