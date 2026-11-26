"use strict";
// The versioned local bundle handles both the reader's TeX and semantic MathML.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true
  },
  svg: {fontCache: "local"},
  options: {enableMenu: false, enableAssistiveMml: true},
  startup: {elements: ["main"]}
};
if (window.self !== window.top && new URLSearchParams(window.location.search).get("embed") === "1") {
  document.documentElement.classList.add("embedded");
}
