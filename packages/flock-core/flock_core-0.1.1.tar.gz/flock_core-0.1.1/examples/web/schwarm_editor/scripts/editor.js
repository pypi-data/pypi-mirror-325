// Initialize CodeMirror
let editor = CodeMirror.fromTextArea(document.getElementById("editor"), {
    mode: "xml",
    theme: "monokai",
    lineNumbers: true,
    autoCloseBrackets: true,
    matchBrackets: true,
    styleActiveLine: true,
    indentUnit: 4,
    tabSize: 4,
    indentWithTabs: false,
    lineWrapping: true,

    extraKeys: {
        "Ctrl-/": "toggleComment",
        "Cmd-/": "toggleComment",
        "Tab": function (cm) {
            if (cm.somethingSelected()) {
                cm.indentSelection("add");
            } else {
                cm.replaceSelection("    ", "end");
            }
        }
    }


});
window.codeMirrorEditor = editor;
// Set initial content
editor.setValue(`

`);

// let updateListenerExtension = editor.updateListener.of((update) => {
//     if (update.docChanged) {
//         const editorTextarea = document.getElementById("#editor");
//         editorTextarea.value = editor.getValue();
//     }
// });

// Change language mode
function changeLanguage() {
    const language = document.getElementById("language").value;
    editor.setOption("mode", language);
}

// Toggle comment
function toggleComment() {
    editor.toggleComment();
}

// Basic code formatting
function formatCode() {
    const totalLines = editor.lineCount();
    editor.autoFormatRange(
        { line: 0, ch: 0 },
        { line: totalLines }
    );
}

function evalIdea() {
    const editorTextarea = document.getElementById("editor");
    editorTextarea.value = editor.getValue();
}


function load_from_file() {
    fetch("out.html")
        .then((response) => response.blob())
        .then((blob) => {
            if (blob) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    // Set the content of CodeMirror editor
                    editor.setValue(e.target.result);
                };
                reader.readAsText(blob); // Read file as text
            }
            console.log(blob); // Blob object
        })
        .catch((error) => console.error("Error fetching file:", error));

}

// Auto-resize on window change
window.addEventListener('resize', () => {
    editor.refresh();
});

document.getElementById('fileInput').addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            // Set the content of CodeMirror editor
            editor.setValue(e.target.result);
        };
        reader.readAsText(file); // Read file as text
    }
});


document.addEventListener("DOMContentLoaded", () => {
    const editorTextarea = document.getElementById("editor");


    // Sync editor content to textarea on every change
    editor.on("change", () => {
        editorTextarea.value = editor.getValue(); // Sync content
    });

    // Ensure the button includes updated editor value
    //const convertButton = document.getElementById("convertButton");
    //convertButton.addEventListener("click", () => {
    //    editorTextarea.value = editor.getValue(); // Ensure textarea is updated
    //});
});