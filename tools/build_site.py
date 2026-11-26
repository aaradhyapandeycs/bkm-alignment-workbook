#!/usr/bin/env python3
"""Build the static workbook with Python 3.9+. No packages are needed to read it.

Existing pages cache their MathML. For new formulas install Node and KaTeX
(npm install --no-save --package-lock=false katex@0.16.22), then rerun.
Pass --fresh to regenerate every equation. An existing KaTeX installation
can be specified with --katex; --node selects the Node executable.
"""
import argparse
from collections import namedtuple
from html import escape, unescape
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit
import unicodedata

from paper_results import NUMBERED, RESULTS, result_id

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PAPER = "https://arxiv.org/html/2609.01595v1"
INSPIRATION = "https://ultronozm.github.io/grh-workbook/"
PARTS = [
    ("The single-agent model", "Begin with the timing of a contract. Which deviations survive when an agent can hide its tools and still use them later?", 1, 4),
    ("What should the designer permit?", "Use the implementability conditions to choose a spending limit, then ask when one cap works for every type.", 5, 6),
    ("Agents who can discipline one another", "Build a team’s beliefs, score a prediction against another report, and use disagreement between two actions to infer biases.", 7, 9),
    ("Oversight and deployment", "Give a monitor authority, design its menu, and test what the guarantees require of a deployment contract.", 10, 12),
]
MAP = [
    ("§§1–2.2", "S2.SS1"), ("§2.3 · Proposition 1", "S2.SS3"),
    ("§2.4 · Lemma 1", "S2.SS4"), ("§§2.4–2.5 · Proposition 2", "S2.SS4"),
    ("§3 · Example I · Proposition 3 · Lemma 2", "S3"), ("§3 · Example II · Propositions 4–5", "S3"),
    ("§4 · Proposition 6", "S4"), ("§5 · Example III · Proposition 7", "S5"),
    ("§5 · Example IV · Proposition 8", "S5"), ("§5 · Example V · Proposition 9", "S5"),
    ("§5 · Example V · Proposition 10", "S5"), ("§6 · Discussion", "S6"),
]
PAPER_ANCHORS = ["model", "model", "cycles", "cycles", "single", "single", "team", "team",
                 "competition", "oversight", "oversight", "discussion"]
Lesson = namedtuple("Lesson", "path title introduction exercises")
Formula = namedtuple("Formula", "tex display")
MATH = re.compile(r"\$\$(?P<block>.*?)\$\$|\$(?P<inline>[^$\n]+?)\$", re.S)
EXERCISE = re.compile(r"^## Exercise (\d+)\. (.+)$", re.M)


def read_sheet(path):
    title, source = path.read_text().split("\n", 1)
    if not title.startswith("# "):
        raise ValueError(f"{path.name}: expected a title")
    parts = EXERCISE.split(source)
    exercises = []
    for num, heading, body in zip(parts[1::3], parts[2::3], parts[3::3]):
        groups = re.split(r"^### (?:Hint|Solution)\s*$", body, flags=re.M)
        if len(groups) != 3 or int(num) != len(exercises) + 1:
            raise ValueError(f"{path.name}: check the question/hint/solution for exercise {num}")
        exercises.append((num, heading, *groups))
    if not exercises:
        raise ValueError(f"{path.name}: empty sheet")
    return Lesson(path, title[2:], parts[0], exercises)


def formula(match):
    is_block = match["block"] is not None
    return Formula(match["block" if is_block else "inline"].strip(), is_block)


def load_math(paths, node, katex, fresh):
    wanted = {formula(m) for p in paths for m in MATH.finditer(p.read_text())}
    rendered = {}
    if not fresh:
        for page in DOCS.glob("*.html"):
            for tag in re.findall(r"<math\b.*?</math>", page.read_text(), re.S):
                annotation = re.search(r'<annotation encoding="application/x-tex">(.*?)</annotation>', tag, re.S)
                if annotation:
                    key = Formula(unescape(annotation[1]), 'display="block"' in tag.partition(">")[0])
                    if key in wanted:
                        rendered[key] = tag
    missing = sorted(wanted - rendered.keys())
    if missing:
        cmd = [node, str(Path(__file__).with_suffix(".cjs")), katex]
        try:
            proc = subprocess.run(cmd, input=json.dumps(missing), capture_output=True, text=True)
        except FileNotFoundError:
            raise SystemExit("New formulas require Node and KaTeX. See tools/build_site.py --help.")
        if proc.returncode:
            raise SystemExit(proc.stderr)
        tags = json.loads(proc.stdout)
        if len(tags) != len(missing):
            raise RuntimeError("Renderer returned an incomplete formula batch")
        for key, tag in zip(missing, tags):
            rendered[key] = modern_math_alphabet(tag)
    return rendered


def modern_math_alphabet(markup):
    # MathML Core uses mathematical Unicode characters for styled alphabets.
    names = {"double-struck": "DOUBLE-STRUCK", "script": "SCRIPT", "fraktur": "FRAKTUR",
             "bold": "BOLD", "bold-italic": "BOLD ITALIC"}
    def convert(m):
        element, variant, ch = m.groups()
        if variant not in names:
            return m[0]
        if ch.isdigit():
            suffix = "DIGIT " + unicodedata.name(ch).split()[-1]
        else:
            suffix = ("CAPITAL " if ch.isupper() else "SMALL ") + ch.upper()
        style = names[variant]
        for candidate in ["MATHEMATICAL " + style + " " + suffix, style + " " + suffix,
                          "BLACK-LETTER " + suffix if style == "FRAKTUR" else ""]:
            if candidate:
                try:
                    return f"<{element}>{unicodedata.lookup(candidate)}</{element}>"
                except KeyError:
                    pass
        return m[0]
    return re.sub(r'<(mi|mn) mathvariant="([^"]+)">([a-zA-Z0-9])</\1>', convert, markup)


def inline(text):
    # Math has already been replaced by opaque tokens. Escape all prose.
    text = escape(text)
    def link(m):
        title, href = m.groups()
        dest = unescape(href)
        if not urlsplit(dest).scheme:
            href = re.sub(r"\.md(?=#|$)", ".html", href)
        elif urlsplit(dest).scheme not in ("http", "https"):
            raise ValueError(f"Unsupported link: {dest}")
        return f'<a href="{href}">{title}</a>'
    text = re.sub(r"\[([^\]\n]+)\]\(([^()\s]+)\)", link, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", text)
    return re.sub(r"\x60([^\x60\n]+)\x60", r"<code>\1</code>", text)


def prose(source, math):
    items = []
    def insert(m):
        key = formula(m)
        element = "div" if key.display else "span"
        cl = "display-math" if key.display else "inline-math"
        items.append(f'<{element} class="{cl}">{math[key]}</{element}>')
        marker = f"@@M{len(items) - 1}@@"
        return f"\n\n{marker}\n\n" if key.display else marker
    source = MATH.sub(insert, source)
    result = []
    for block in re.split(r"\n\s*\n", source.strip()):
        if not block.strip():
            continue
        if re.fullmatch(r"@@M\d+@@", block) and items[int(block[3:-2])].startswith("<div"):
            result.append(block)
        elif all(line.startswith("- ") for line in block.splitlines()):
            result.append("<ul>" + "".join(f"<li>{inline(line[2:])}</li>" for line in block.splitlines()) + "</ul>")
        else:
            result.append("<p>" + inline(" ".join(block.splitlines())) + "</p>")
    return re.sub(r"@@M(\d+)@@", lambda m: items[int(m[1])], "\n".join(result))


def short_link(lesson):
    return f'<a href="{lesson.path.stem}.html">{escape(lesson.title)}</a>'


REPOSITORY = "https://github.com/aaradhyapandeycs/bkm-alignment-workbook"
PRINT_PDF = f"{REPOSITORY}/raw/refs/heads/main/print/workbook.pdf"
THEME_ASSETS = '<link rel="stylesheet" href="workbook.css?v=4"><script src="appearance.js"></script>'


def masthead(current):
    links = [("overview", "index.html", "Overview"), ("paper", "paper.html", "Paper reader"),
             ("exercises", "index.html#contents", "Exercises"), ("study", "study.html", "Study side by side")]
    items = []
    for key, href, label in links:
        active = ' aria-current="page"' if key == current else ''
        items.append(f'<a href="{href}"{active}>{label}</a>')
    return f'''<header><div class="frame top"><a class="home" href="index.html">Alignment workbook</a>
<nav aria-label="Project">{''.join(items)}</nav><button class="theme-toggle" type="button" hidden aria-label="Dark mode" aria-pressed="false"><span aria-hidden="true">◐</span></button></div></header>'''


def shell(title, contents, current="exercises"):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} · Alignment workbook</title>{THEME_ASSETS}
<script src="mathjax-config.js"></script>
<script id="MathJax-script" src="vendor/mathjax-3.2.2/tex-mml-svg.js" defer></script>
<script src="workbook.js" defer></script></head>
<body><a class="skip" href="#main">Skip to content</a>
{masthead(current)}
{contents}
<footer><div class="frame">An independent exercise companion to <a href="{PAPER}">Bergemann, Koh and Morris</a>. Workbook format inspired by <a href="{INSPIRATION}">GRH via exercises</a>.</div></footer>
</body></html>
"""


def sheet_page(lessons, index, math):
    lesson = lessons[index]
    number = index + 1
    ref, anchor = MAP[index]
    questions = []
    for num, heading, question, hint, solution in lesson.exercises:
        questions.append(f"""<section class="exercise" id="exercise-{num}">
<h2><a href="#exercise-{num}" aria-label="Link to exercise {num}">Exercise {num}</a><span>{inline(heading)}</span></h2>
{prose(question, math)}
<details class="hint"><summary>Hint</summary><div>{prose(hint, math)}</div></details>
<details class="solution"><summary>Worked solution</summary><div>{prose(solution, math)}</div></details>
</section>""")
    previous = short_link(lessons[index-1]) if index else '<a href="index.html">Contents</a>'
    following = short_link(lessons[index+1]) if index+1 < len(lessons) else '<a href="index.html">Contents</a>'
    menu = "".join(f'<li><a href="#exercise-{n}">{inline(h)}</a></li>' for n, h, *_ in lesson.exercises)
    contents = f"""<main id="main" class="frame sheet"><div class="sheet-head"><div class="kicker">Sheet {number:02} · <a href="{PAPER}#{anchor}">{escape(ref)}</a></div>
<h1>{escape(lesson.title)}</h1><p class="reading-links"><a href="paper.html#{PAPER_ANCHORS[index]}">Read the corresponding paper section</a><a href="study.html?sheet={number}">Study side by side</a></p><div class="intro">{prose(lesson.introduction, math)}</div></div>
<div class="work-area"><aside aria-label="On this sheet"><div><h2>Exercises</h2><ol>{menu}</ol><button type="button" data-toggle hidden>Show all answers</button><button type="button" data-print hidden>Print sheet</button></div></aside>
<article>{''.join(questions)}<nav class="prev-next" aria-label="Adjacent sheets"><div><small>Previous</small>{previous}</div><div><small>Next</small>{following}</div></nav></article></div></main>"""
    return shell(lesson.title, contents)


def index_page(lessons):
    total = sum(len(s.exercises) for s in lessons)
    parts = []
    for title, summary, start, end in PARTS:
        rows = []
        for n in range(start, end+1):
            lesson = lessons[n-1]
            ref, anchor = MAP[n-1]
            rows.append(f'<li><span class="num">{n:02}</span><div>{short_link(lesson)}<small><a href="{PAPER}#{anchor}">{escape(ref)}</a></small></div></li>')
        parts.append(f'<section class="part"><h3>{escape(title)}</h3><p>{escape(summary)}</p><ol start="{start}">{"".join(rows)}</ol></section>')
    def route(nums):
        return " → ".join(f'<a href="{lessons[n-1].path.stem}.html">{n:02}</a>' for n in nums)
    titles = {}
    for chapter in (ROOT / "reader").glob("*.md"):
        for line in chapter.read_text().splitlines():
            heading = re.fullmatch(r"#{2,4} (.*)", line)
            if heading and (numbered := NUMBERED.fullmatch(heading[1])):
                titles[result_id(heading[1])] = numbered.groups()
    result_rows = []
    for key, (page, n) in RESULTS.items():
        kind, number, label = titles[key]
        result_rows.append(f'<tr><th scope="row"><a href="paper.html#{key}">{kind} {number}</a></th>'
                           f'<td>{escape(label)}</td><td><a href="{lessons[n-1].path.stem}.html">Sheet {n:02}</a></td>'
                           f'<td><a href="https://arxiv.org/pdf/2609.01595v1#page={page}">p. {page}</a></td></tr>')
    contents = f"""<main id="main" class="landing"><section class="topband" aria-labelledby="project-title"><div class="frame">
<div class="index-head"><p class="byline">Dirk Bergemann · Andrew Koh · Stephen Morris</p>
<h1 id="project-title">Mechanism design for alignment and control</h1>
<p class="subtitle">A mathematical workbook on what a designer can learn about an agent’s capabilities, and which actions a contract can induce.</p>
<nav class="resource-links" aria-label="Project resources"><a href="paper.html">Paper reader</a><a href="#contents">Exercise sheets</a><a href="study.html">Study side by side</a><a href="{PRINT_PDF}">Workbook PDF</a><a href="{PAPER}">Original paper ↗</a><a href="{REPOSITORY}">GitHub ↗</a></nav></div></div></section>
<div class="frame landing-body"><section class="overview" aria-labelledby="overview-title"><div><h2 id="overview-title">About the workbook</h2>
<p>An agent can hide a tool when it reports its capabilities and still use it after signing a contract. What makes it willing to report honestly and follow an instruction once its private signal arrives?</p>
<p>Work through the <a href="{PAPER}">paper</a> in {total} exercises across twelve sheets. Each sheet opens with a modeling vignette and includes hints and worked solutions.</p></div>
<nav class="on-page" aria-label="On this page"><h2>On this page</h2><a href="#contents">Sheets and source map</a><a href="#results">Propositions and lemmas</a><a href="#seminar">Seminar routes</a></nav></section>
<section id="contents"><h2 class="section-title">Sheets and source map</h2><div class="parts">{''.join(parts)}</div></section>
<section id="results"><h2 class="section-title">Propositions and lemmas</h2><div class="results-scroll" role="region" aria-label="Numbered results in paper order" tabindex="0"><table><thead><tr><th>Result</th><th>Statement in the reader</th><th>Exercises</th><th>Original PDF</th></tr></thead><tbody>{''.join(result_rows)}</tbody></table></div></section>
<section id="seminar"><h2 class="section-title">Seminar routes</h2><div class="routes"><div><h3>From the model to the characterization</h3><p>{route([1,2,3,4])}. Build both deviation tests and construct supporting rewards.</p></div>
<div><h3>Capability and discretion</h3><p>{route([1,2,5,6])}. Use a capability certificate to reason about pooling and caps.</p></div>
<div><h3>From peers to oversight</h3><p>{route([1,7,8,9,10,11,12])}. Follow the flow of private information, compare instruments and finish with the deployment capstone.</p></div></div></section></div></main>"""
    return shell("Mechanism design for alignment and control", contents, "overview")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--node", default="node")
    parser.add_argument("--katex", default="katex")
    parser.add_argument("--fresh", action="store_true")
    args = parser.parse_args()
    paths = sorted((ROOT / "sheets").glob("*.md"))
    if [p.name[:2] for p in paths] != [f"{i:02}" for i in range(1, 13)]:
        raise SystemExit("Expected twelve sheets numbered 01 through 12")
    lessons = [read_sheet(p) for p in paths]
    math = load_math(paths, args.node, args.katex, args.fresh)
    DOCS.mkdir(exist_ok=True)
    (DOCS / "index.html").write_text(index_page(lessons))
    for i, sheet in enumerate(lessons):
        (DOCS / f"{sheet.path.stem}.html").write_text(sheet_page(lessons, i, math))
    (DOCS / ".nojekyll").touch()
    print(f"Built {len(lessons)} sheets, {sum(len(s.exercises) for s in lessons)} exercises, {len(math)} distinct formulas.")


if __name__ == "__main__":
    main()
