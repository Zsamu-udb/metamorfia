/* ==========================================================================
   METAMORFIA — Interacciones mínimas
   Solo el menú móvil. Sin dependencias.
   ========================================================================== */

(function () {
  "use strict";

  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (!toggle || !nav) return;

  function setOpen(open) {
    nav.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", String(open));
  }

  toggle.addEventListener("click", function () {
    setOpen(toggle.getAttribute("aria-expanded") !== "true");
  });

  // Cierra el menú al elegir una sección
  nav.addEventListener("click", function (e) {
    if (e.target.closest("a")) setOpen(false);
  });

  // Cierra con Escape y devuelve el foco al botón
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
      setOpen(false);
      toggle.focus();
    }
  });
})();

/* ---------------------------------------------------------------------
   Acordeón de Preguntas frecuentes (página Proceso / FAQ).
   Cada pregunta puede abrirse de forma independiente; no se cierran
   las demás al abrir una (mejor para quien compara respuestas).
   --------------------------------------------------------------------- */
(function () {
  "use strict";

  var questions = document.querySelectorAll(".faq-item__question");
  if (!questions.length) return;

  questions.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var expanded = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", String(!expanded));
    });
  });
})();
