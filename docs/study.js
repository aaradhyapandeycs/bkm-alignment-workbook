"use strict";

const sheet = document.getElementById("sheet");
const edition = document.getElementById("edition");
const paperFrame = document.getElementById("paper-frame");
const exerciseFrame = document.getElementById("exercise-frame");

function showSelection() {
  const chosen = sheet.selectedOptions[0];
  const pdf = "https://arxiv.org/pdf/2609.01595v1#page=" + chosen.dataset.page;
  const isOriginal = edition.value === "original";
  const reader = "paper.html#" + chosen.dataset.section;
  const nextPaper = isOriginal ? pdf : "paper.html?embed=1#" + chosen.dataset.section;
  const nextExercise = chosen.dataset.file + "?embed=1";
  if (paperFrame.getAttribute("src") !== nextPaper) paperFrame.src = nextPaper;
  if (exerciseFrame.getAttribute("src") !== nextExercise) exerciseFrame.src = nextExercise;
  document.getElementById("pdf-link").href = pdf;
  document.getElementById("pdf-link").textContent = "Original PDF · p. " + chosen.dataset.page + " ↗";
  document.getElementById("paper-link").href = reader;
  document.getElementById("paper-label").textContent = isOriginal ? "Authors’ full paper" : "Paper reader";
  document.getElementById("exercise-link").href = chosen.dataset.file;
  document.getElementById("exercise-label").textContent = "Sheet " + chosen.value.padStart(2, "0");
}

function restore() {
  const params = new URLSearchParams(location.search);
  const choice = Number(params.get("sheet"));
  sheet.value = String(Number.isInteger(choice) && choice >= 1 && choice <= sheet.options.length ? choice : 1);
  edition.value = params.get("view") === "original" ? "original" : "notes";
  showSelection();
}

function navigate() {
  const url = new URL(location.href);
  url.searchParams.set("sheet", sheet.value);
  url.searchParams.set("view", edition.value);
  history.pushState(null, "", url);
  showSelection();
}

sheet.addEventListener("change", navigate);
edition.addEventListener("change", navigate);
window.addEventListener("popstate", restore);
restore();
