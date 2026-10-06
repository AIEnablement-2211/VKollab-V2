/* ==========================================================================
   animations.js — scroll reveal, animated counters, light parallax
   Vanilla JS. Respects prefers-reduced-motion. Safe without IntersectionObserver.
   ========================================================================== */
(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hasIO = "IntersectionObserver" in window;

  /* ---- Reveal ---- */
  var targets = document.querySelectorAll("[data-reveal], [data-reveal-stagger]");
  function showAll() {
    Array.prototype.forEach.call(targets, function (el) { el.classList.add("is-visible"); });
  }
  if (targets.length) {
    if (reduce || !hasIO) {
      showAll();
    } else {
      var io = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add("is-visible"); obs.unobserve(e.target); }
        });
      }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
      Array.prototype.forEach.call(targets, function (el) {
        if (el.getBoundingClientRect().top < window.innerHeight * 0.9) el.classList.add("is-visible");
        else io.observe(el);
      });
      window.addEventListener("beforeprint", showAll);
      window.setTimeout(function () { showAll(); io.disconnect(); }, 6000);
    }
  }

  /* ---- Counters: <span data-count="11" data-suffix="+"> ---- */
  var counters = document.querySelectorAll("[data-count]");
  function runCounter(el) {
    var end = parseFloat(el.getAttribute("data-count")) || 0;
    var suffix = el.getAttribute("data-suffix") || "";
    var dur = 1400;
    var start = null;
    function frame(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(end * eased) + suffix;
      if (p < 1) window.requestAnimationFrame(frame);
    }
    window.requestAnimationFrame(frame);
  }
  if (counters.length) {
    if (reduce || !hasIO) {
      Array.prototype.forEach.call(counters, function (el) {
        el.textContent = el.getAttribute("data-count") + (el.getAttribute("data-suffix") || "");
      });
    } else {
      var cio = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { runCounter(e.target); obs.unobserve(e.target); }
        });
      }, { threshold: 0.4 });
      Array.prototype.forEach.call(counters, function (el) { cio.observe(el); });
    }
  }

  /* ---- Parallax on media: [data-parallax="0.15"] ---- */
  var px = document.querySelectorAll("[data-parallax]");
  if (px.length && !reduce) {
    var ticking = false;
    function update() {
      var vh = window.innerHeight;
      Array.prototype.forEach.call(px, function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) return;
        var f = parseFloat(el.getAttribute("data-parallax")) || 0.12;
        var offset = (r.top + r.height / 2 - vh / 2) * -f;
        el.style.transform = "translate3d(0," + offset.toFixed(1) + "px,0)";
      });
      ticking = false;
    }
    window.addEventListener("scroll", function () {
      if (!ticking) { ticking = true; window.requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }

  /* ---- Photo fallback: hide images that fail to load so the designed
     gradient underneath shows instead of a broken-image icon. ---- */
  Array.prototype.forEach.call(document.querySelectorAll("img[data-photo]"), function (img) {
    function missing() { img.classList.add("is-missing"); }
    if (img.complete && img.naturalWidth === 0) missing();
    img.addEventListener("error", missing);
  });
})();
