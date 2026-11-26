// Build-time renderer. Reader-facing pages contain native MathML.
const fs = require("node:fs");
const katex = require(process.argv[2]);
const input = JSON.parse(fs.readFileSync(0, "utf8"));
const results = input.map(([tex, display]) => {
  let markup;
  function render(source) {
    return katex.renderToString(source, {displayMode: display, output: "mathml", throwOnError: true, strict: "ignore"});
  }
  try {
    // Prevent the opening bracket of an interval becoming a TeX row height.
    const source = tex.replace(/\\\\(\s*)\[/g, "\\\\$1{}[");
    try {
      markup = render(source);
    } catch {
      // Earlier KaTeX bundles accept the equivalent upright-word syntax.
      markup = render(source.replace(/\\operatorname\{([^{}]+)\}/g, "\\mathrm{$1}")
        .replace(/\{\\rm ([A-Za-z ]+)\}/g, "{\\mathrm{$1}}")
        .replaceAll("{smallmatrix}", "{matrix}"));
    }
    const math = markup.match(/<math\b[^>]*>([\s\S]*?)<\/math>/);
    if (!math) throw Error("Renderer produced no MathML");
    const escaped = tex.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");
    const contents = math[1].replace(/(<annotation encoding="application\/x-tex">)[\s\S]*?(<\/annotation>)/,
      (_, start, end) => start + escaped + end);
    return '<math xmlns="http://www.w3.org/1998/Math/MathML"' + (display ? ' display="block"' : '') + '>' + contents + '</math>';
  } catch (error) {
    throw new Error("Cannot render formula " + tex + "\n" + error.message);
  }
});
process.stdout.write(JSON.stringify(results));
