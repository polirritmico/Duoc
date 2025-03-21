#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from pathlib import Path

highlights = {
    "keyword": [
        "Definir",
        "Como",
        "Hasta",
        "Hacer",
        "Repetir",
        "Que",
        "Entonces",
        "Con Paso",
        "Dimension",
        "De Otro Modo",
        "SiNo",
        r"\bSi(?!\w)\b",
        r"\bNo(?!\w)\b",
        r"\bMientras(?!\w)\b",
        r"\bProceso(?!\w)\b",
        r"\bFuncion(?!\w)\b",
        r"\bPara(?!\w)\b",
        r"\bSegun(?!\w)\b",
        "FinSi",
        "FinPara",
        "FinFuncion",
        "FinProceso",
        "FinMientras",
        "FinSegun",
        " = ",
        " == ",
        " - ",
        r" \+ ",
        r" \* ",
        " O ",
        " Y ",
        r"\(",
        r"\)",
        r"\[",
        r"\]",
        "<-",
        "<>",
        " < ",
        " > ",
    ],
    "type": ["Caracter", "Numero", "Real", "Entero", "Logico"],
    "boolean": ["Verdadero", "Falso"],
    "number": [r"\d+"],
    "secondary": [";", ",", ":"],
    "function": ["Escribir", "Leer", "Main", "Bar"],
}
html_characters = {
    "<>": "&lt;&gt;",
    "><<": ">&lt;<",
    ">><": ">&gt;<",
    " > ": " &gt; ",
    " < ": " &lt; ",
}
base_tag = '<span class="code-{}">{}</span>'


def apply_pattern(text: str, pattern: str, highlight: str) -> str:
    tag = "{}" + base_tag + "{}"

    def tag_match(match_str):
        wrap_char = ""
        match_group = match_str.group(0)
        if match_group[0] == " " and match_group[-1] == " ":
            wrap_char = " "
            match_group = match_group.strip()
        return tag.format(wrap_char, highlight, match_group, wrap_char)

    tagged_matches = re.sub(pattern, tag_match, text)
    return tagged_matches


def highlight_and_extract_comment(text: str) -> tuple[str, str]:
    # TODO: handle full-line comment
    comment_hl = "comment"
    pattern = r"(//.*)"

    sections: list[str] = re.split(pattern, text)
    sections = list(filter(None, sections))
    if len(sections) < 2:
        return text, ""

    text = sections[0]
    comment = sections[1]
    highlighted_comment = base_tag.format(comment_hl, comment)
    return text, highlighted_comment


def extract_strings(text: str, placeholder: str) -> tuple[str, list[str]]:
    pattern = r'"[^"]*"'

    matches = re.findall(pattern, text)
    matches = list(filter(None, matches))
    if len(matches) < 1:
        return text, []

    marked_text = re.sub(pattern, placeholder, text)
    return marked_text, matches


def replace_marks_with_strings(text: str, content: list[str], placeholder: str) -> str:
    highlight = "string"
    for stored_string in content:
        highlighted_string = base_tag.format(highlight, stored_string)
        text = text.replace(placeholder, highlighted_string, 1)
    return text


def replace_characters(text: str, characters: dict[str, str]) -> str:
    for old_character, replacement in characters.items():
        text = text.replace(old_character, replacement)
    return text


def apply_highlights(line, highlights) -> str:
    for hl, patterns in highlights.items():
        for pattern in patterns:
            line = apply_pattern(line, pattern, hl)
    return line


def apply_html_syntax(text: str) -> str:
    str_mark = "@@@"
    lines = text.splitlines()

    highlighted_text = []
    for line in lines:
        line, comment = highlight_and_extract_comment(line)
        line, collected_strings = extract_strings(line, str_mark)
        line = apply_highlights(line, highlights)
        line = replace_characters(line, html_characters)
        line = replace_marks_with_strings(line, collected_strings, str_mark)
        line += comment

        highlighted_text.append(line)

    output = "\n".join(highlighted_text)
    return output


def read_file(filename: Path) -> str:
    try:
        with open(filename, "r", encoding="utf-8") as stream:
            raw_data = stream.read()
    except Exception:
        raise IOError(f"Can't read file {filename}:\n")
    return raw_data


def write_file(text: str, filename: Path) -> None:
    output_file = filename.with_name(f"hl-{filename.name}")
    with open(output_file, "w", encoding="utf-8") as stream:
        stream.write(text)


def main() -> None:
    filename = Path("notes_raw")
    print(f"reading file '{filename}'...")
    content = read_file(filename)
    print("reading done")

    print("applying highlight...")
    output = apply_html_syntax(content)
    print("highlight done")

    print("writing file...")
    write_file(output, filename)
    print("All done")

    return 0


if __name__ == "__main__":
    main()
