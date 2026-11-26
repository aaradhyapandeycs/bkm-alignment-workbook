"""Generate the two-pane reader from the Markdown sheet titles and the v1 PDF contents."""
from html import escape
from pathlib import Path

from build_site import THEME_ASSETS, masthead

ROOT = Path(__file__).resolve().parents[1]
PDF = "https://arxiv.org/pdf/2609.01595v1"
# Sheet order. Pages are one-based in the published PDF.
SECTIONS = [
    ("model", 3), ("model", 9), ("cycles", 14), ("cycles", 16),
    ("single", 22), ("single", 30), ("team", 36), ("team", 42),
    ("competition", 45), ("oversight", 48), ("oversight", 54), ("discussion", 58),
]


def build():
    sheets = sorted((ROOT / "sheets").glob("*.md"))
    if len(sheets) != len(SECTIONS):
        raise ValueError("The paper page map must cover every exercise sheet.")
    options = []
    for number, (sheet, (section, page)) in enumerate(zip(sheets, SECTIONS), 1):
        title = sheet.read_text().splitlines()[0].removeprefix("# ")
        options.append(f'<option value="{number}" data-file="{sheet.stem}.html" data-section="{section}" data-page="{page}">{number:02} · {escape(title)}</option>')
    contents = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Study side by side · Alignment workbook</title>
{THEME_ASSETS}<link rel="stylesheet" href="study.css?v=3"><script defer src="study.js"></script></head>
<body><a class="skip" href="#main">Skip to reading controls</a>
{masthead("study")}
<main id="main"><div class="controls"><h1>Study side by side</h1>
<label for="sheet">Exercise sheet<select id="sheet">{''.join(options)}</select></label>
<label for="edition">Paper view<select id="edition"><option value="notes">MathJax reading notes</option><option value="original">Authors’ full paper (PDF)</option></select></label>
</div>
<noscript><p>Open the <a href="paper.html">paper reader</a>, the <a href="{PDF}">original PDF</a>, or the <a href="index.html#contents">exercise sheets</a> directly.</p></noscript>
<div class="panes"><section aria-label="Paper pane"><div class="pane-head"><h2 id="paper-label">Paper reader</h2><a id="paper-link" target="_blank" rel="noopener" href="paper.html#model">Open reader ↗</a><a id="pdf-link" target="_blank" rel="noopener" href="{PDF}#page=3">Original PDF · p. 3 ↗</a></div><iframe title="Paper reading pane" id="paper-frame" src="paper.html?embed=1#model"></iframe></section>
<section aria-label="Exercise pane"><div class="pane-head"><h2 id="exercise-label">Exercise sheet</h2><a id="exercise-link" target="_blank" rel="noopener" href="01-model.html">Open sheet ↗</a></div><iframe title="Exercise sheet with hints and worked solutions" id="exercise-frame" src="01-model.html?embed=1"></iframe></section></div>
</main></body></html>"""
    (ROOT / "docs/study.html").write_text(contents)


if __name__ == "__main__":
    build()
