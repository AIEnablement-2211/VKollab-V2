/* ==========================================================================
   main.js — small shared behaviours
   • Flags JS availability for CSS (.no-js → .js)
   • Current-year in footer
   • External links open safely in a new tab
   Load order (deferred): main.js → navigation.js → animations.js → forms.js
   ========================================================================== */
(function () {
  "use strict";

  var root = document.documentElement;
  root.classList.remove("no-js");
  root.classList.add("js");

  /* Footer year */
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());

  /* Links whose URL is not configured yet (Alumni Portal, HR App) */
  Array.prototype.forEach.call(document.querySelectorAll("a[data-pending-link]"), function (a) {
    if (a.getAttribute("href") === "#") {
      a.setAttribute("title", "Link coming soon");
      a.addEventListener("click", function (e) { e.preventDefault(); });
    }
  });

  /* External links */
  var host = window.location.hostname;
  Array.prototype.forEach.call(document.querySelectorAll('a[href^="http"]'), function (a) {
    try {
      var url = new URL(a.href);
      if (url.hostname && url.hostname !== host) {
        a.setAttribute("target", "_blank");
        a.setAttribute("rel", "noopener noreferrer");
      }
    } catch (err) {
      /* ignore malformed hrefs */
    }
  });
})();
