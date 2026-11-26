"""Typeset the Markdown exercise sheets into print/workbook.pdf with pdfLaTeX."""

import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SHEETS = ROOT / "sheets"
PDF = ROOT / "print" / "workbook.pdf"

PREAMBLE = r"""
\documentclass[11pt,letterpaper]{article}
\usepackage[T1]{fontenc}
\usepackage{newpxtext,amsmath,newpxmath,microtype,graphicx}
\usepackage[top=0.93in,bottom=0.88in,left=0.98in,right=0.98in,headheight=15pt]{geometry}
\usepackage{xcolor,needspace,fancyhdr,enumitem}
\usepackage[unicode,hidelinks,bookmarksnumbered]{hyperref}
\definecolor{ink}{HTML}{173B42}
\definecolor{hintink}{HTML}{505859}
\hypersetup{pdftitle={Alignment and control through exercises},pdfsubject={A mathematical workbook on the paper of Bergemann, Koh and Morris}}
\pdfinfoomitdate=1
\pdftrailerid{}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt plus 1pt minus 1pt}
\setlength{\emergencystretch}{2em}
\setlength{\abovedisplayskip}{7pt plus 2pt minus 2pt}
\setlength{\belowdisplayskip}{7pt plus 2pt minus 2pt}
\setlist{nosep,topsep=4pt,leftmargin=1.5em}
\raggedbottom
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\sffamily Alignment and control through exercises}
\fancyhead[R]{\small\sffamily\leftmark}
\fancyfoot[C]{\small\thepage}
\renewcommand{\headrulewidth}{0.25pt}
\newcommand{\sheettitle}[2]{\clearpage\phantomsection
 \label{sheet:#1}\markboth{Sheet #1}{Sheet #1}
 \addcontentsline{toc}{section}{#1.\enspace #2}
 {\color{ink}\sffamily\bfseries Sheet #1\par}
 \vspace{2pt}{\color{ink}\LARGE\bfseries #2\par}\vspace{6pt}}
\newcommand{\problem}[2]{\Needspace{5\baselineskip}\par\addvspace{10pt}
 {\large\color{ink}\bfseries Exercise #1.\enspace #2\par}\nobreak}
\newcommand{\hinthead}{\Needspace{3\baselineskip}\par\addvspace{3pt}
 {\sffamily\small\bfseries\color{hintink}Hint\par}\nobreak}
\newcommand{\solvehead}{\Needspace{3\baselineskip}\par\addvspace{3pt}
 {\sffamily\small\bfseries\color{ink}Solution\par}\nobreak}
\newsavebox{\displayequation}
\newcommand{\fitformula}[1]{\sbox{\displayequation}{$\displaystyle #1$}
 \ifdim\wd\displayequation>\linewidth
 \resizebox{\linewidth}{!}{\usebox{\displayequation}}\else\usebox{\displayequation}\fi}
\begin{document}
\thispagestyle{empty}
{\sffamily\color{ink}\bfseries A mathematical workbook\par}
\vspace{10pt}
{\Huge\bfseries Alignment and control\\[3pt]through exercises\par}
\vspace{9pt}
{\large On \emph{Mechanism Design for Alignment and Control}\\
by Dirk Bergemann, Andrew Koh and Stephen Morris\par}
\vspace{12pt}
An agent chooses a report before seeing its private signal and acts after seeing it.
The exercises start with this timing, build the implementation results, and use them to study sandbagging, delegation, peer discipline, competition and oversight.
Read the opening situation in each sheet, attempt the exercises in order, and use the hint before consulting the worked solution.
\vspace{3pt}
\href{https://arxiv.org/abs/2609.01595v1}{Original paper: arXiv:2609.01595v1}
\quad\textperiodcentered\quad
\href{https://ultronozm.github.io/grh-workbook/}{Exercise-sheet inspiration: \emph{GRH via exercises}}
\vspace{5pt}
\tableofcontents
"""

SPECIAL = {
    "\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "$": r"\$",
    "&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_",
    "^": r"\textasciicircum{}", "~": r"\textasciitilde{}",
}
INLINE = re.compile(
    r"(\$[^$\n]+\$|\[[^\]\n]+\]\([^\s)]+\)|\*\*[^*\n]+\*\*|\*[^*\n]+\*|"
    r"\x60[^\x60\n]+\x60)"
)


def escape(value):
    return "".join(SPECIAL.get(char, char) for char in value)


def inline(value):
    parts = []
    for i, token in enumerate(INLINE.split(value)):
        if i % 2 == 0:
            parts.append(escape(token))
        elif token.startswith("$"):
            parts.append(token)
        elif token.startswith("["):
            label, target = token[1:-1].split("](", 1)
            if target.startswith(("https://", "http://")):
                url = target.replace("%", r"\%").replace("#", r"\#")
                parts.append(r"\href{" + url + "}{" + inline(label) + "}")
            else:
                linked_sheet = re.match(r"(?:.*/)?(\d\d)-[^#]+\.md(?:#.*)?$", target)
                parts.append(r"\hyperref[sheet:" + linked_sheet[1] + "]{" + inline(label) + "}"
                             if linked_sheet else inline(label))
        elif token.startswith("**"):
            parts.append(r"\textbf{" + inline(token[2:-2]) + "}")
        elif token.startswith("*"):
            parts.append(r"\emph{" + inline(token[1:-1]) + "}")
        else:
            parts.append(r"\texttt{" + escape(token[1:-1]) + "}")
    return "".join(parts)


def tex_for_sheet(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"Missing title in {path.name}")
    number = path.name.split("-", 1)[0]
    output = [r"\sheettitle{" + number + "}{" + inline(lines[0][2:]) + "}"]
    paragraph = []
    display = None
    current_list = None

    def end_paragraph():
        if paragraph:
            output.append(inline(" ".join(paragraph)) + "\n")
            paragraph.clear()

    def end_list():
        nonlocal current_list
        if current_list:
            output.append(r"\end{" + current_list + "}")
            current_list = None

    for line in lines[1:]:
        line = line.strip()
        if line == "$$":
            end_paragraph()
            end_list()
            if display is None:
                display = []
            else:
                output.append("\\[\n\\fitformula{" + "\n".join(display) + "}\n\\]")
                display = None
            continue
        if display is not None:
            display.append(line)
            continue
        if not line:
            end_paragraph()
            continue
        item = re.fullmatch(r"([-*]|\d+\.) (.+)", line)
        if item:
            end_paragraph()
            style = "itemize" if item[1] in ("-", "*") else "enumerate"
            if current_list != style:
                end_list()
                output.append(r"\begin{" + style + "}")
                current_list = style
            output.append(r"\item " + inline(item[2]))
            continue
        end_list()
        if line.startswith("#"):
            end_paragraph()
            heading = re.fullmatch(r"## Exercise (\d+)\.\s+(.+)", line)
            if heading:
                output.append(r"\problem{" + heading[1] + "}{" + inline(heading[2]) + "}")
            elif line in ("### Hint", "### Solution"):
                output.append(r"\hinthead" if line == "### Hint" else r"\solvehead")
            else:
                output.append(r"\subsection*{" + inline(line.lstrip("# ")) + "}")
        else:
            paragraph.append(line)
    if display is not None:
        raise ValueError(f"Unclosed display in {path.name}")
    end_paragraph()
    end_list()
    return "\n".join(output)


def main():
    sources = sorted(SHEETS.glob("[0-9][0-9]-*.md"))
    expected = [f"{i:02d}" for i in range(1, 13)]
    if [source.name[:2] for source in sources] != expected:
        raise SystemExit("Expected one Markdown source for each of sheets 01 through 12.")
    tex = PREAMBLE + "\n".join(tex_for_sheet(path) for path in sources) + "\n\\end{document}\n"
    pdf_output = PDF.parent
    pdf_output.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as directory:
        work = Path(directory)
        (work / "workbook.tex").write_text(tex, encoding="utf-8")
        cmd = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "workbook.tex"]
        env = dict(os.environ, SOURCE_DATE_EPOCH="946684800", FORCE_SOURCE_DATE="1")
        for _ in range(2):
            result = subprocess.run(cmd, cwd=work, env=env, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, text=True)
            if result.returncode:
                raise SystemExit("\n".join(result.stdout.splitlines()[-24:]))
        log = (work / "workbook.log").read_text(encoding="utf-8", errors="replace")
        for problem in ("undefined references", "multiply defined", "Missing character:",
                        "Overfull \\hbox", "Overfull \\vbox"):
            if problem.lower() in log.lower():
                messages = [line for line in log.splitlines() if problem.lower() in line.lower()]
                raise SystemExit("\n".join(messages))
        contents = (work / "workbook.toc").read_text(encoding="utf-8")
        if contents.count(r"\contentsline {section}") != len(sources):
            raise SystemExit("Table of contents does not contain all twelve sheets.")
        shutil.copyfile(work / "workbook.pdf", PDF)
    print(f"Built print/{PDF.name} from {len(sources)} sheets.")


if __name__ == "__main__":
    main()
