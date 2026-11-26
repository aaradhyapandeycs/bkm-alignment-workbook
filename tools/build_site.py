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


def shell(title, contents):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} · Alignment workbook</title><link rel="stylesheet" href="workbook.css"><script src="workbook.js" defer></script></head>
<body><a class="skip" href="#main">Skip to content</a>
<header><div class="frame top"><a class="home" href="index.html">Alignment workbook</a><nav aria-label="Workbook"><a href="index.html#contents">Contents</a><a href="index.html#seminar">Seminar routes</a><a href="{PAPER}">Paper ↗</a></nav></div></header>
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
<h1>{escape(lesson.title)}</h1><div class="intro">{prose(lesson.introduction, math)}</div></div>
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
    contents = f"""<main id="main" class="frame"><div class="index-head"><div class="kicker">A mathematical exercise companion</div>
<h1>Mechanism design for<br>alignment and control</h1>
<p>A designer can ask an agent to describe its abilities and tell it what to do. What makes it profitable for the agent to tell the truth, then follow the instruction after it learns something new?</p>
<p>These twelve sheets reconstruct the framework and all five applications of <a href="{PAPER}">Bergemann, Koh and Morris (2026)</a> through {total} exercises. Each begins with a modeling vignette. Try the problem first, then open its hint or its worked solution.</p>
<p><a href="https://github.com/aaradhyapandeycs/bkm-alignment-workbook/raw/refs/heads/main/print/workbook.pdf">Download the solved workbook (PDF)</a> · <a href="https://github.com/aaradhyapandeycs/bkm-alignment-workbook">GitHub repository</a></p>
<a class="start" href="{lessons[0].path.stem}.html">Begin with sheet 01 <span aria-hidden="true">→</span></a></div>
<section id="contents"><h2 class="section-title">Sheets and source map</h2><div class="parts">{''.join(parts)}</div></section>
<section id="seminar"><h2 class="section-title">Seminar routes</h2><div class="routes"><div><h3>From the model to the characterization</h3><p>{route([1,2,3,4])}. Build both deviation tests and construct supporting rewards.</p></div>
<div><h3>Capability and discretion</h3><p>{route([1,2,5,6])}. Use a capability certificate to reason about pooling and caps.</p></div>
<div><h3>From peers to oversight</h3><p>{route([1,7,8,9,10,11,12])}. Follow the flow of private information, compare instruments and finish with the deployment capstone.</p></div></div></section></main>"""
    return shell("Mechanism design for alignment and control", contents)


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
