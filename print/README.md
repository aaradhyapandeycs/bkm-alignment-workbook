# Print edition

[Download the workbook](workbook.pdf). The PDF contains all twelve sheets, including the hints and worked solutions. Its table of contents links to each sheet.

To rebuild it from the repository root, run:

~~~sh
python3 tools/build_print.py
~~~

The builder uses Python 3.9+ and pdfLaTeX on the command path. A full TeX Live installation includes the fonts and packages it uses. Edit the Markdown files in the sheets directory, then regenerate the PDF.
