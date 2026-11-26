"use strict";
const answers = Array.from(document.querySelectorAll(".exercise details"));
const toggle = document.querySelector("[data-toggle]");
if (toggle) {
  toggle.hidden = false;
  const update = () => {
    const open = answers.every(answer => answer.open);
    toggle.textContent = open ? "Hide all answers" : "Show all answers";
    toggle.setAttribute("aria-pressed", String(open));
  };
  toggle.addEventListener("click", () => {
    const desired = !answers.every(answer => answer.open);
    answers.forEach(answer => answer.open = desired);
    update();
  });
  answers.forEach(answer => answer.addEventListener("toggle", update));
  update();
}
const printButton = document.querySelector("[data-print]");
if (printButton) {
  printButton.hidden = false;
  printButton.addEventListener("click", () => window.print());
}
let beforePrint;
window.addEventListener("beforeprint", () => {
  if (beforePrint) return;
  beforePrint = answers.map(answer => answer.open);
  answers.forEach(answer => answer.open = true);
});
window.addEventListener("afterprint", () => {
  if (beforePrint) answers.forEach((answer, i) => answer.open = beforePrint[i]);
  beforePrint = undefined;
});
