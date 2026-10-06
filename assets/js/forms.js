/* ==========================================================================
   forms.js — contact / careers form handling
   -------------------------------------------------------------------------
   CONFIGURATION
   Set FORM_ENDPOINT to your production endpoint (Formspree, Netlify Forms,
   Cloudflare Worker, your own API, etc.). It must accept a JSON POST and
   respond 2xx on success. Leave it empty to use the mailto fallback, which
   opens the visitor's mail client with the message pre-filled.

   The form markup also carries a real action/method so it still submits
   without JavaScript when FORM_ENDPOINT is set in the HTML.
   ========================================================================== */
(function () {
  "use strict";

  var FORM_ENDPOINT = ""; /* e.g. "https://formspree.io/f/xxxxxxx" */
  var FALLBACK_EMAIL = "info@vkollab.com";

  var forms = document.querySelectorAll("form[data-form]");
  if (!forms.length) return;

  var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  function fieldWrap(input) {
    return input.closest(".field") || input.parentNode;
  }
  function setError(input, message) {
    var wrap = fieldWrap(input);
    wrap.classList.add("is-invalid");
    input.setAttribute("aria-invalid", "true");
    var err = wrap.querySelector(".field__error");
    if (err) err.textContent = message;
  }
  function clearError(input) {
    var wrap = fieldWrap(input);
    wrap.classList.remove("is-invalid");
    input.removeAttribute("aria-invalid");
  }
  function validate(input) {
    var value = (input.value || "").trim();
    var label = input.getAttribute("data-label") || "This field";
    if (input.type === "checkbox") {
      if (input.required && !input.checked) {
        setError(input, "Please confirm before sending.");
        return false;
      }
      clearError(input);
      return true;
    }
    if (input.required && !value) {
      setError(input, label + " is required.");
      return false;
    }
    if (input.type === "email" && value && !emailRe.test(value)) {
      setError(input, "Enter a valid email address.");
      return false;
    }
    if (input.minLength > 0 && value && value.length < input.minLength) {
      setError(input, label + " should be at least " + input.minLength + " characters.");
      return false;
    }
    clearError(input);
    return true;
  }

  function setStatus(form, type, html) {
    var box = form.querySelector(".form__status");
    if (!box) return;
    box.className = "form__status is-" + type;
    box.innerHTML = html;
    box.setAttribute("tabindex", "-1");
    box.focus({ preventScroll: false });
  }

  function serialize(form) {
    var data = {};
    Array.prototype.forEach.call(form.elements, function (el) {
      if (!el.name || el.type === "submit" || el.type === "button" || el.type === "file") return;
      if (el.type === "checkbox") data[el.name] = el.checked ? "yes" : "no";
      else data[el.name] = el.value.trim();
    });
    data.page = window.location.href;
    return data;
  }

  function buildMailto(data) {
    var subject = "[vkollab.com] " + (data.topic || "Enquiry") + " — " + (data.name || "");
    var lines = [];
    Object.keys(data).forEach(function (k) {
      if (k === "website" || k === "page") return;
      lines.push(k.charAt(0).toUpperCase() + k.slice(1) + ": " + data[k]);
    });
    lines.push("", "Sent from: " + data.page);
    return (
      "mailto:" +
      FALLBACK_EMAIL +
      "?subject=" +
      encodeURIComponent(subject) +
      "&body=" +
      encodeURIComponent(lines.join("\n"))
    );
  }

  Array.prototype.forEach.call(forms, function (form) {
    var submitBtn = form.querySelector('[type="submit"]');
    var inputs = form.querySelectorAll("input, select, textarea");

    Array.prototype.forEach.call(inputs, function (input) {
      input.addEventListener("blur", function () {
        if (input.value || input.type === "checkbox") validate(input);
      });
      input.addEventListener("input", function () {
        if (fieldWrap(input).classList.contains("is-invalid")) validate(input);
      });
    });

    form.setAttribute("novalidate", "novalidate");

    form.addEventListener("submit", function (e) {
      e.preventDefault();

      /* Honeypot */
      var hp = form.querySelector('input[name="website"]');
      if (hp && hp.value) return;

      var valid = true;
      var firstInvalid = null;
      Array.prototype.forEach.call(inputs, function (input) {
        if (input.name === "website") return;
        var ok = validate(input);
        if (!ok) {
          valid = false;
          if (!firstInvalid) firstInvalid = input;
        }
      });
      if (!valid) {
        setStatus(form, "error", "Please correct the highlighted fields and try again.");
        if (firstInvalid) firstInvalid.focus();
        return;
      }

      var data = serialize(form);
      var endpoint = FORM_ENDPOINT || form.getAttribute("data-endpoint") || "";

      if (!endpoint) {
        /* Mailto fallback: open the mail client with the message pre-filled. */
        window.location.href = buildMailto(data);
        setStatus(
          form,
          "info",
          "Your email client should open with the message pre-filled. If it doesn't, write to <a href=\"mailto:" +
            FALLBACK_EMAIL +
            '">' +
            FALLBACK_EMAIL +
            "</a>."
        );
        return;
      }

      if (submitBtn) {
        submitBtn.classList.add("is-loading");
        submitBtn.setAttribute("aria-disabled", "true");
        submitBtn.disabled = true;
      }

      var hasFile = form.querySelector('input[type="file"]');
      var req = hasFile
        ? { method: "POST", headers: { Accept: "application/json" }, body: new FormData(form) }
        : { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) };
      fetch(endpoint, req)
        .then(function (res) {
          if (!res.ok) throw new Error("Request failed with status " + res.status);
          form.reset();
          setStatus(
            form,
            "success",
            "Thank you — your message has been received. A member of the VKollab team will reply within one working day."
          );
        })
        .catch(function () {
          setStatus(
            form,
            "error",
            "We couldn't send your message right now. Please try again, or email <a href=\"mailto:" +
              FALLBACK_EMAIL +
              '">' +
              FALLBACK_EMAIL +
              "</a> directly."
          );
        })
        .then(function () {
          if (submitBtn) {
            submitBtn.classList.remove("is-loading");
            submitBtn.removeAttribute("aria-disabled");
            submitBtn.disabled = false;
          }
        });
    });
  });
})();
