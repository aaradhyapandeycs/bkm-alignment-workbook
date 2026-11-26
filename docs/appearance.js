"use strict";
(() => {
  const key = "alignment-workbook-appearance";
  const system = window.matchMedia("(prefers-color-scheme: dark)");
  let preference;
  try { preference = localStorage.getItem(key); } catch { /* Use this page's setting. */ }
  function apply() {
    const dark = preference === "dark" || (preference !== "light" && system.matches);
    document.documentElement.dataset.theme = dark ? "dark" : "light";
    const toggle = document.querySelector(".theme-toggle");
    if (toggle) {
      toggle.hidden = false;
      toggle.setAttribute("aria-pressed", String(dark));
      toggle.title = dark ? "Switch to light mode" : "Switch to dark mode";
    }
  }
  apply();
  document.addEventListener("DOMContentLoaded", () => {
    apply();
    document.querySelector(".theme-toggle")?.addEventListener("click", () => {
      preference = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
      try { localStorage.setItem(key, preference); } catch { /* Retain in memory. */ }
      apply();
    });
  });
  window.addEventListener("storage", event => {
    if (event.key === key || event.key === null) { preference = event.newValue; apply(); }
  });
  system.addEventListener("change", apply);
})();
