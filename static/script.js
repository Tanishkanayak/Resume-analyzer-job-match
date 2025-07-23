document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  form.addEventListener("submit", () => {
    const button = form.querySelector("button");
    button.innerText = "Analyzing...";
    button.disabled = true;
  });
});
