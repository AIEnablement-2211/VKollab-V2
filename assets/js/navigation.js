/* ==========================================================================
   navigation.js — header behaviour, mega menu, mobile drawer
   Vanilla JS. Progressive enhancement: links work without this file.
   ========================================================================== */
(function () {
  "use strict";

  var header = document.querySelector(".site-header");
  var nav = document.getElementById("site-nav");
  var toggle = document.querySelector(".nav-toggle");
  var body = document.body;
  var mql = window.matchMedia("(max-width: 64em)");

  if (!header || !nav) return;

  /* ---- Scrolled state ---- */
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () {
      var bar = document.querySelector(".topbar");
      var th = (bar ? bar.offsetHeight : 0) + 4;
      header.classList.toggle("is-scrolled", window.scrollY > th);
      ticking = false;
    });
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  /* Pages without a dark hero get a light header from the start */


  /* ---- Mobile drawer ---- */
  var focusableSel =
    'a[href], button:not([disabled]), input:not([disabled]), select, textarea, [tabindex]:not([tabindex="-1"])';

  function openDrawer() {
    nav.classList.add("is-open");
    toggle.setAttribute("aria-expanded", "true");
    body.classList.add("nav-open");
    var first = nav.querySelector(focusableSel);
    if (first) first.focus();
  }
  function closeDrawer(returnFocus) {
    nav.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
    body.classList.remove("nav-open");
    closeAllSubmenus();
    if (returnFocus) toggle.focus();
  }
  function isDrawerOpen() {
    return nav.classList.contains("is-open");
  }

  if (toggle) {
    toggle.addEventListener("click", function () {
      if (isDrawerOpen()) closeDrawer(false);
      else openDrawer();
    });
  }

  /* Trap focus within the drawer while open (mobile only) */
  nav.addEventListener("keydown", function (e) {
    if (!isDrawerOpen() || !mql.matches || e.key !== "Tab") return;
    var nodes = Array.prototype.filter.call(nav.querySelectorAll(focusableSel), function (el) {
      return el.offsetParent !== null;
    });
    if (!nodes.length) return;
    var first = nodes[0];
    var last = nodes[nodes.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      toggle.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      toggle.focus();
    }
  });
  if (toggle) {
    toggle.addEventListener("keydown", function (e) {
      if (!isDrawerOpen() || e.key !== "Tab" || e.shiftKey) return;
      var first = nav.querySelector(focusableSel);
      if (first) {
        e.preventDefault();
        first.focus();
      }
    });
  }

  /* ---- Submenus (mega menu on desktop / accordion on mobile) ---- */
  var items = Array.prototype.slice.call(nav.querySelectorAll(".site-nav__item--has-menu"));

  function closeAllSubmenus(except) {
    items.forEach(function (item) {
      if (item === except) return;
      item.classList.remove("is-open");
      var btn = item.querySelector("[aria-expanded]");
      if (btn) btn.setAttribute("aria-expanded", "false");
    });
  }
  function setOpen(item, open) {
    item.classList.toggle("is-open", open);
    var btn = item.querySelector("[aria-expanded]");
    if (btn) btn.setAttribute("aria-expanded", open ? "true" : "false");
  }

  items.forEach(function (item) {
    var trigger = item.querySelector(".site-nav__link");
    var menu = item.querySelector(".mega");
    if (!trigger || !menu) return;

    var hoverTimer;

    trigger.addEventListener("click", function (e) {
      e.preventDefault();
      var open = !item.classList.contains("is-open");
      closeAllSubmenus(item);
      setOpen(item, open);
    });

    /* Desktop hover intent */
    item.addEventListener("mouseenter", function () {
      if (mql.matches) return;
      clearTimeout(hoverTimer);
      closeAllSubmenus(item);
      setOpen(item, true);
    });
    item.addEventListener("mouseleave", function () {
      if (mql.matches) return;
      hoverTimer = setTimeout(function () {
        setOpen(item, false);
      }, 120);
    });

    /* Keyboard */
    item.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        setOpen(item, false);
        trigger.focus();
      }
    });
    item.addEventListener("focusout", function (e) {
      if (mql.matches) return;
      if (!item.contains(e.relatedTarget)) setOpen(item, false);
    });
  });

  /* Close on outside click / Escape */
  document.addEventListener("click", function (e) {
    if (!nav.contains(e.target) && !(toggle && toggle.contains(e.target))) {
      closeAllSubmenus();
    }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      if (isDrawerOpen()) closeDrawer(true);
      else closeAllSubmenus();
    }
  });

  /* Reset on viewport change */
  function onViewportChange() {
    if (!mql.matches) closeDrawer(false);
  }
  if (mql.addEventListener) mql.addEventListener("change", onViewportChange);
  else if (mql.addListener) mql.addListener(onViewportChange);

  /* ---- Mark current page ---- */
  var path = window.location.pathname.replace(/\/index\.html$/, "/");
  var links = nav.querySelectorAll("a[href]");
  Array.prototype.forEach.call(links, function (a) {
    var href = a.getAttribute("href");
    if (!href || href.charAt(0) === "#" || /^(https?:|mailto:|tel:)/.test(href)) return;
    var resolved = new URL(href, window.location.href).pathname.replace(/\/index\.html$/, "/");
    if (resolved === path) {
      a.setAttribute("aria-current", "page");
      var parent = a.closest(".site-nav__item");
      if (parent) parent.classList.add("is-current");
    }
  });
})();
