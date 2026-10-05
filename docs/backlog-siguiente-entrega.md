# Backlog — Siguiente entrega (≈15 días)

Derivado de la reunión del 25 de septiembre. Ver acta completa en
`docs/actas/2026-09-25-revision-wireframe-y-marca.md`.

## 1. Reestructuración web — ✅ avanzado al 2 de octubre

- [x] Cambiar el nombre del proyecto a **METAMORPHIA** en código, `README.md` y documentos.
- [x] Convertir el layout de una sola página (scroll) a pantallas/secciones independientes:
      `index.html`, `sobre-mi.html`, `servicios.html`, `proceso-faq.html`, `testimonios.html`,
      `contacto.html`. Cada página comparte header/footer y marca la pestaña activa con
      `aria-current="page"`.
- [x] Integrar la sección de Proceso / Preguntas frecuentes (`proceso-faq.html`): 4 pasos del
      proceso + acordeón con 5 preguntas, redactadas a partir de la entrevista inicial.
      ⚠️ **Pendiente validar con la clienta:** el valor exacto de la sesión (quedó como
      marcador `TODO` en el HTML, no se inventó una cifra).

## 2. Rediseño de identidad visual

- [ ] Desarrollar 3 propuestas finales de logo: silueta de mariposa + símbolo de psicología (ψ).
      Sin exceso de flores, sin amarillo.
- [x] *(adelantado)* Probar la paleta verde oliva + morado en el sitio: se agregó la escala
      `--ciruela-*` en `css/tokens.css` como acento secundario (kickers, pasos del proceso,
      íconos de FAQ). El oliva se mantiene como color principal — **falta validar con la
      clienta en la reunión de R2**.
- [ ] Definir y documentar la guía tipográfica y de color final en `css/tokens.css` (se define
      una vez el logo esté aprobado, para que ambos queden consistentes).

## 3. Fotografía e imágenes

- [ ] Coordinar con Lina Gabriela la sesión de fotos profesional.
- [ ] Sustituir los recursos genéricos del sitio por sus fotos reales.

## 4. Demostración y ajustes

- [ ] Entregar el enlace del prototipo actualizado a Lina Gabriela para revisión previa.
- [ ] Reunión de aprobación final (ventana estimada: 9–16 de octubre).

---

*Este documento reemplaza como prioridad activa a `sprint-1-checklist.md`, que queda como
registro histórico del primer corte de entregables.*
