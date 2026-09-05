// Sidebar nav: split "N. Title" into a number span + plain title,
// so the number and title can carry different colors (no period).
document.addEventListener("DOMContentLoaded", () => {
  // home entry: "About the Book" instead of repeating the book title
  const home = document.querySelector(".bd-sidenav__home-link a");
  if (home) home.textContent = "About the Book";

  const links = document.querySelectorAll(
    ".bd-sidebar-primary nav.bd-links a.reference.internal"
  );
  links.forEach((a) => {
    const m = a.textContent.trim().match(/^(\d+)\.\s+(.*)$/);
    if (!m) return;
    a.textContent = "";
    const num = document.createElement("span");
    num.className = "toc-chapter-number";
    num.textContent = m[1];
    a.append(num, m[2]);
  });
});
