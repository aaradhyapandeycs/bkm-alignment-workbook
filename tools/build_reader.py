#!/usr/bin/env python3
"""Build the companion reader from reader/*.md using the workbook's renderer.

The static HTML includes working links, the complete reader and native MathML.
For new equations, pass the same --node and --katex options as build_site.py.
"""
import argparse
from dataclasses import dataclass
from html import escape
import re

from paper_results import RESULTS, result_id
from build_site import DOCS, ROOT, PAPER, load_math, prose, shell

PDF = "https://arxiv.org/pdf/2609.01595v1"
RECORD = "https://arxiv.org/abs/2609.01595v1"


@dataclass(frozen=True)
class Part:
    file: str
    label: str
    source_section: str
    page: int
    sheets: tuple


PARTS = (
    Part("model", "§§1–2.3 · Model and revelation", "S1", 3, (1, 2)),
    Part("cycles", "§§2.4–2.5 · Implementability", "S2.SS4", 14, (3, 4)),
    Part("single", "§3 · Sandbagging and delegation", "S3", 21, (5, 6)),
    Part("team", "§§4–5 · Teams and peer discipline", "S4", 36, (7, 8)),
    Part("competition", "§5 · Competition", "S5", 45, (9,)),
    Part("oversight", "§5 · Oversight", "S5", 48, (10, 11)),
    Part("discussion", "§6 and Appendix A · Discussion and proofs", "S6", 58, (12,)),
)

HEADINGS = re.compile(r"^(#{2,4})\s+(.+)$", re.M)


def read_part(part):
    path = ROOT / "reader" / f"{part.file}.md"
    first, remainder = path.read_text(encoding="utf-8").split("\n", 1)
    if not first.startswith("# "):
        raise ValueError(f"{path.name} must start with a chapter title")
    return path, first[2:], remainder


def sheet_links():
    links = {}
    for path in sorted((ROOT / "sheets").glob("[0-9][0-9]-*.md")):
        number = int(path.name[:2])
        title = path.read_text(encoding="utf-8").splitlines()[0].removeprefix("# ")
        links[number] = (f"{path.stem}.html", title)
    if set(links) != set(range(1, 13)):
        raise ValueError("Reader links require sheets 01 through 12")
    return links


def sheet_link(links, number, include_title=False):
    href, title = links[number]
    label = f"Sheet {number:02}"
    if include_title:
        label += f" · {title}"
    return f'<a href="{href}">{escape(label)}</a>'


def chapter_html(part, title, source, math, links):
    bits = [f'<section class="paper-section exercise" id="{part.file}" aria-labelledby="{part.file}-title">',
            f'<h2 id="{part.file}-title">{escape(title)}</h2>',
            f'<p class="kicker">{escape(part.label)} · '
            f'<a href="{PAPER}#{part.source_section}">Original HTML</a> · '
            f'<a href="{PDF}#page={part.page}">PDF p. {part.page}</a></p>']
    position = 0
    for heading in HEADINGS.finditer(source):
        bits.append(prose(source[position:heading.start()], math))
        level = min(len(heading[1]) + 1, 5)
        label = heading[2]
        key = result_id(label)
        if key:
            page, sheet = RESULTS[key]
            bits.append(f'<h{level} id="{key}"><a class="result-link" href="#{key}">'
                        f'{escape(label)}</a></h{level}>')
            bits.append(f'<p class="kicker"><a href="{PDF}#page={page}">'
                        f'Original statement · p. {page}</a> · {sheet_link(links, sheet)}</p>')
        else:
            bits.append(f'<h{level}>{escape(label)}</h{level}>')
        position = heading.end()
    bits.append(prose(source[position:], math))
    bits.append('<p>Exercises: ' + ' · '.join(sheet_link(links, i, True) for i in part.sheets) + '</p>')
    bits.append('</section>')
    return "\n".join(bits)


def build(node="node", katex="katex", fresh=False):
    chapters = [read_part(part) for part in PARTS]
    math = load_math([p for p, _, _ in chapters], node, katex, fresh)
    links = sheet_links()
    results = [(result_id(m[2]), m[2]) for _, _, body in chapters for m in HEADINGS.finditer(body)
               if result_id(m[2])]
    if len(results) != len(RESULTS) or set(key for key, _ in results) != set(RESULTS):
        raise ValueError("Each of Propositions 1–10 and Lemmas 1–2 must have a unique titled heading")
    sections = "".join(
        f'<li><a href="#{p.file}">{escape(p.label)}</a><br>'
        f'{" · ".join(sheet_link(links, i) for i in p.sheets)}</li>'
        for p in PARTS
    )
    result_list = "".join(f'<li><a href="#{key}">{escape(title)}</a></li>' for key, title in results)
    body = "\n".join(chapter_html(p, title, content, math, links)
                     for p, (_, title, content) in zip(PARTS, chapters))
    contents = f"""<main id="main" class="frame sheet reader">
<div class="sheet-head"><div class="kicker">Companion reader</div>
<h1>Mechanism Design for Alignment and Control</h1>
<p>Dirk Bergemann, Andrew Koh and Stephen Morris · <a href="{RECORD}">arXiv:2609.01595v1</a> · September 2026</p>
<div class="intro"><p>An agent can understate what it knows or can do, then use its full capabilities after the contract is in force. Which contracts make it willing to report honestly and follow its instructions? This independent reader explains the authors’ model, propositions and examples in the order of the paper, with links to worked exercises at the step where each enters.</p></div>
<p><a class="start" href="{PAPER}">Read the full paper</a> &nbsp; <a href="study.html">Read beside the exercises</a></p>
</div><div class="work-area"><aside aria-label="Reader contents"><nav>
<h2>Sections and sheets</h2><ul>{sections}</ul>
<details><summary>Propositions and lemmas</summary><ul>{result_list}</ul></details>
</nav></aside><article>
<details id="original-paper"><summary>Read the original PDF here</summary>
<p>The full 71-page preprint is served by arXiv. <a href="{PDF}">Open the original PDF directly</a> or <a href="{PAPER}">read the accessible HTML edition</a>.</p>
<iframe title="Original paper by Bergemann, Koh and Morris (PDF)" loading="lazy" src="{PDF}" width="100%" height="680"></iframe>
</details>
{body}
<p><a href="{PAPER}#A1">Appendix A in the original paper</a> · <a href="{PDF}#page=65">Appendix PDF p. 65</a> · <a href="index.html#contents">All twelve exercise sheets</a></p>
</article></div></main>"""
    DOCS.mkdir(exist_ok=True)
    (DOCS / "paper.html").write_text(shell("Paper reader", contents, "paper"), encoding="utf-8")
    print(f"Built paper reader: {len(chapters)} sections, {len(results)} named results, {len(math)} distinct formulas.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--node", default="node")
    parser.add_argument("--katex", default="katex")
    parser.add_argument("--fresh", action="store_true")
    options = parser.parse_args()
    build(options.node, options.katex, options.fresh)
