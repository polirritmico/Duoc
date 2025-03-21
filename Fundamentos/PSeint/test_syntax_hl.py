#!/usr/bin/env python
# -*- coding: utf-8 -*-


from syntax_hl import apply_html_syntax, highlight_and_extract_comment


def test_basic() -> None:
    case = "Definir test"
    expected = '<span class="code-keyword">Definir</span> test'
    output = apply_html_syntax(case)
    assert expected == output


def test_first_line() -> None:
    case = "Definir booleano Como Logico;"
    expected = '<span class="code-keyword">Definir</span> booleano <span class="code-keyword">Como</span> <span class="code-type">Logico</span><span class="code-secondary">;</span>'
    output = apply_html_syntax(case)
    assert expected == output


def test_geater() -> None:
    case = "Si foo > 1 Entonces"
    expected = '<span class="code-keyword">Si</span> foo <span class="code-keyword">&gt;</span> <span class="code-number">1</span> <span class="code-keyword">Entonces</span>'
    output = apply_html_syntax(case)
    assert expected == output


def test_greater_and_lesser() -> None:
    case = "Si foo > 1 Y foo < 3 Entonces"
    expected = '<span class="code-keyword">Si</span> foo <span class="code-keyword">&gt;</span> <span class="code-number">1</span> <span class="code-keyword">Y</span> foo <span class="code-keyword">&lt;</span> <span class="code-number">3</span> <span class="code-keyword">Entonces</span>'
    output = apply_html_syntax(case)
    assert expected == output


def test_strings1() -> None:
    case = 'foo = "Foo";'
    expected = 'foo <span class="code-keyword">=</span> <span class="code-string">"Foo"</span><span class="code-secondary">;</span>'
    output = apply_html_syntax(case)
    assert expected == output


def test_strings2() -> None:
    case = 'Si foo == "Bar" O foo <> "Foo" Entonces'
    expected = '<span class="code-keyword">Si</span> foo <span class="code-keyword">==</span> <span class="code-string">"Bar"</span> <span class="code-keyword">O</span> foo <span class="code-keyword">&lt;&gt;</span> <span class="code-string">"Foo"</span> <span class="code-keyword">Entonces</span>'
    output = apply_html_syntax(case)
    assert expected == output


def test_comments() -> None:
    case = 'foo = "Foo"; // Some comment'
    expected_line = 'foo = "Foo"; '
    expected_comment = '<span class="code-comment">// Some comment</span>'
    output_line, output_comment = highlight_and_extract_comment(case)
    assert expected_line == output_line
    assert expected_comment == output_comment


def test_replace_html_characters() -> None:
    case = 'Si foo <> "Foo" Entonces'
    expected = '<span class="code-keyword">Si</span> foo <span class="code-keyword">&lt;&gt;</span> <span class="code-string">"Foo"</span> <span class="code-keyword">Entonces</span>'
    output = apply_html_syntax(case)
    assert expected == output


def test_handle_strings() -> None:
    case = 'matrix[0,0] = "0";'
    expected = 'matrix<span class="code-keyword">[</span><span class="code-number">0</span><span class="code-secondary">,</span><span class="code-number">0</span><span class="code-keyword">]</span> <span class="code-keyword">=</span> <span class="code-string">"0"</span><span class="code-secondary">;</span>'
    output = apply_html_syntax(case)
    assert expected == output


def test_all_colors() -> None:
    case = """Definir booleano Como Logico;
booleano = Verdadero;

Si booleano Entonces
    Escribir "True";
SiNo
    Escribir "False";
FinSi // output: True
    """
    expected_str = """<span class="code-keyword">Definir</span> booleano <span class="code-keyword">Como</span> <span class="code-type">Logico</span><span class="code-secondary">;</span>
booleano <span class="code-keyword">=</span> <span class="code-boolean">Verdadero</span><span class="code-secondary">;</span>

<span class="code-keyword">Si</span> booleano <span class="code-keyword">Entonces</span>
    <span class="code-function">Escribir</span> <span class="code-string">"True"</span><span class="code-secondary">;</span>
<span class="code-keyword">SiNo</span>
    <span class="code-function">Escribir</span> <span class="code-string">"False"</span><span class="code-secondary">;</span>
<span class="code-keyword">FinSi</span> <span class="code-comment">// output: True</span>
    """

    output_str = apply_html_syntax(case)

    expected_multi = expected_str.splitlines()
    output_multi = output_str.splitlines()

    assert len(expected_multi) == len(output_multi)
    for expected, output in zip(expected_multi, output_multi):
        assert expected == output
