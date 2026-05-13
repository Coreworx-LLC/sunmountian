// ============================================================
// Sun Mountain brand site — shared JS
// ============================================================

(function () {
  // Mark the active nav link based on the current page filename
  const path = location.pathname.split("/").pop() || "index.html";
  const links = document.querySelectorAll(".site-nav__item");
  links.forEach((link) => {
    const target = link.getAttribute("data-page");
    if (target && (path === target || path.endsWith("/" + target))) {
      link.classList.add("is-active");
    }
  });

  // Mobile menu toggle (animated hamburger)
  const nav = document.querySelector(".site-nav");
  const toggle = document.querySelector(".site-nav__menu-toggle");
  if (nav && toggle) {
    toggle.addEventListener("click", () => {
      nav.classList.toggle("is-open");
      const open = nav.classList.contains("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
    // Close menu when a nav link is tapped (mobile UX)
    document.querySelectorAll(".site-nav__item").forEach((item) => {
      item.addEventListener("click", () => {
        if (nav.classList.contains("is-open")) {
          nav.classList.remove("is-open");
          toggle.setAttribute("aria-expanded", "false");
          toggle.setAttribute("aria-label", "Open menu");
        }
      });
    });
  }

  // Year stamp in footer (if present)
  const yr = document.querySelector("[data-year]");
  if (yr) yr.textContent = new Date().getFullYear();
})();
