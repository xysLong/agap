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

// Citations: hovering an inline citation shows its full reference entry
// (the chapter-end list item its href points at) in a floating tooltip.
document.addEventListener("DOMContentLoaded", () => {
  const cites = document.querySelectorAll("a.cite");
  if (!cites.length) return;

  const tip = document.createElement("div");
  tip.className = "cite-tooltip";
  tip.hidden = true;
  document.body.appendChild(tip);

  cites.forEach((a) => {
    const href = a.getAttribute("href") || "";
    if (!href.startsWith("#")) return;
    const anchor = document.getElementById(decodeURIComponent(href.slice(1)));
    if (!anchor) return;
    const entry = anchor.closest("li");
    if (!entry) return;

    a.addEventListener("mouseenter", () => {
      const clone = entry.cloneNode(true);
      clone.querySelectorAll("span[id]").forEach((s) => s.remove());
      tip.innerHTML = clone.innerHTML;
      tip.hidden = false;
      const r = a.getBoundingClientRect();
      const maxLeft = window.scrollX + window.innerWidth - tip.offsetWidth - 8;
      tip.style.left = Math.max(8, Math.min(window.scrollX + r.left, maxLeft)) + "px";
      tip.style.top = window.scrollY + r.bottom + 6 + "px";
    });
    a.addEventListener("mouseleave", () => {
      tip.hidden = true;
    });
  });
});
