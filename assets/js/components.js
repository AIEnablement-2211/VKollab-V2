/* ==========================================================================
   components.js — service switcher, industry tabs, apply modal, dropzone
   Vanilla JS; everything degrades to static content without it.
   ========================================================================== */
(function () {
  "use strict";

  /* ---- Services: list drives the feature panel ---- */
  var svcItems = document.querySelectorAll(".svc-list__item");
  var svcPanels = document.querySelectorAll(".svc-panel__item");
  if (svcItems.length && svcPanels.length) {
    function activate(k) {
      Array.prototype.forEach.call(svcItems, function (b) {
        var on = b.getAttribute("data-svc") === String(k);
        b.classList.toggle("is-active", on);
        b.setAttribute("aria-pressed", on ? "true" : "false");
      });
      Array.prototype.forEach.call(svcPanels, function (p) {
        p.classList.toggle("is-active", p.getAttribute("data-svc-panel") === String(k));
      });
    }
    Array.prototype.forEach.call(svcItems, function (b) {
      var k = b.getAttribute("data-svc");
      b.addEventListener("mouseenter", function () { activate(k); });
      b.addEventListener("focus", function () { activate(k); });
      b.addEventListener("click", function () {
        activate(k);
        var link = document.querySelector('.svc-panel__item[data-svc-panel="' + k + '"] a');
        if (link && window.matchMedia("(max-width: 64em)").matches) link.scrollIntoView({ block: "nearest" });
      });
    });
  }

  /* ---- Tabs ---- */
  Array.prototype.forEach.call(document.querySelectorAll("[data-tabs]"), function (root) {
    var tabs = root.querySelectorAll('[role="tab"]');
    var panels = root.querySelectorAll('[role="tabpanel"]');
    function select(tab) {
      Array.prototype.forEach.call(tabs, function (t) {
        var on = t === tab;
        t.setAttribute("aria-selected", on ? "true" : "false");
        t.setAttribute("tabindex", on ? "0" : "-1");
      });
      Array.prototype.forEach.call(panels, function (p) {
        var on = p.id === tab.getAttribute("aria-controls");
        p.hidden = !on;
        p.classList.toggle("is-active", on);
      });
    }
    Array.prototype.forEach.call(tabs, function (t, i) {
      t.addEventListener("click", function () { select(t); });
      t.addEventListener("keydown", function (e) {
        var dir = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
        if (!dir) return;
        e.preventDefault();
        var next = tabs[(i + dir + tabs.length) % tabs.length];
        next.focus();
        select(next);
      });
    });
  });

  /* ---- Apply modal ---- */
  var modal = document.getElementById("apply-modal");
  if (modal) {
    var lastFocus = null;
    var positionEl = modal.querySelector("[data-apply-position]");
    var positionInput = modal.querySelector('input[name="position"]');
    function openModal(position) {
      lastFocus = document.activeElement;
      if (positionEl) positionEl.textContent = position;
      if (positionInput) positionInput.value = position;
      modal.hidden = false;
      document.body.classList.add("nav-open");
      var first = modal.querySelector("input:not([type=hidden]), textarea");
      if (first) first.focus();
    }
    function closeModal() {
      modal.hidden = true;
      document.body.classList.remove("nav-open");
      if (lastFocus) lastFocus.focus();
    }
    Array.prototype.forEach.call(document.querySelectorAll("[data-apply]"), function (b) {
      b.addEventListener("click", function () { openModal(b.getAttribute("data-apply")); });
    });
    Array.prototype.forEach.call(modal.querySelectorAll("[data-modal-close]"), function (b) {
      b.addEventListener("click", closeModal);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !modal.hidden) closeModal();
    });
    modal.addEventListener("keydown", function (e) {
      if (e.key !== "Tab") return;
      var nodes = modal.querySelectorAll('button, [href], input:not([type=hidden]), select, textarea, [tabindex]:not([tabindex="-1"])');
      var first = nodes[0], last = nodes[nodes.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
  }

  /* ---- Dropzone label ---- */
  Array.prototype.forEach.call(document.querySelectorAll(".dropzone"), function (zone) {
    var input = zone.querySelector("input[type=file]");
    var label = zone.querySelector("[data-file-label]");
    if (!input) return;
    input.addEventListener("change", function () {
      if (label) label.textContent = input.files.length ? input.files[0].name : "Drag file or click to upload (PDF, DOC)";
    });
    ["dragenter", "dragover"].forEach(function (ev) {
      zone.addEventListener(ev, function (e) { e.preventDefault(); zone.classList.add("is-drag"); });
    });
    ["dragleave", "drop"].forEach(function (ev) {
      zone.addEventListener(ev, function (e) { e.preventDefault(); zone.classList.remove("is-drag"); });
    });
    zone.addEventListener("drop", function (e) {
      if (e.dataTransfer && e.dataTransfer.files.length) {
        input.files = e.dataTransfer.files;
        if (label) label.textContent = e.dataTransfer.files[0].name;
      }
    });
  });
})();
