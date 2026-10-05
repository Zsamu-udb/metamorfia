# METAMORPHIA

Sitio web de presentación y contacto para una psicóloga clínica (acompañamiento emocional, terapias de tercera y cuarta generación). Proyecto en sprints de 15 días con la clienta.

> Estado: avance al **2 de octubre de 2026** — sitio reestructurado en pantallas independientes,
> sección de Proceso/FAQ integrada, y paleta oliva + morado en prueba. Pendiente: logo final,
> fotografía profesional y validación de todo esto con la clienta (reunión R2, ventana 9–16 oct).
> Ver `docs/backlog-siguiente-entrega.md` para el detalle.

## Stack

HTML + CSS + JavaScript vanilla. Sin build ni dependencias: cada `.html` se abre directo en el navegador o se publica tal cual en GitHub Pages.

## Estructura

```
metamorphia/
├── index.html              Inicio — hero + accesos a cada sección
├── sobre-mi.html           Formación, enfoque y el símbolo de la mariposa
├── servicios.html          Psicoterapia, duelo, crianza, talleres + modalidad
├── proceso-faq.html        Pasos del proceso + preguntas frecuentes (acordeón)
├── testimonios.html        Testimonios (de ejemplo) + formulario de comentario
├── contacto.html           WhatsApp, modalidad, mapa/foto
├── css/
│   ├── tokens.css          Variables globales: color (oliva + morado), tipografía, espaciado
│   ├── base.css            Reset, tipografía global, accesibilidad
│   ├── layout.css          Contenedor, header, navegación, secciones, footer
│   └── components.css      Botones, hero, tarjetas, pasos, acordeón FAQ, testimonios
├── js/
│   └── main.js             Menú móvil + acordeón de FAQ
├── assets/
│   ├── logo/               Isotipo provisional (SVG). Aquí irán las propuestas finales
│   ├── img/                Imágenes optimizadas (WebP/AVIF/JPG)
│   └── icons/              Íconos SVG sueltos
└── docs/
    ├── brief.md                      Resumen del levantamiento de requerimientos
    ├── backlog-siguiente-entrega.md  Backlog activo (próxima entrega)
    ├── sprint-1-checklist.md         Registro histórico del primer corte
    ├── actas/                        Actas de las reuniones con la clienta
    ├── wireframes/                   Wireframe de baja fidelidad (PDF)
    └── mockups/
        └── hero-mockup.html          Mockup de alta fidelidad del hero (autocontenido)
```

Cada página HTML repite el mismo header/nav/footer (sin framework ni build), marcando la
pestaña activa con `aria-current="page"`. Si cambias el nav o el footer, replica el cambio en
las 6 páginas — o regenera con `build/generate_pages.py` si ese script está disponible en tu
copia de trabajo.

## Sistema de diseño

Todo se define en `css/tokens.css` y se consume con `var(--token)`. Nunca escribir colores, tamaños o fuentes “sueltos” en otros archivos.

| Eje | Decisión |
| --- | --- |
| Color | Beige (`--lino-*`) + verde oliva (`--oliva-*`, color principal) + morado (`--ciruela-*`, acento secundario **en prueba**) |
| Titulares | Newsreader (serif editorial y cálida) |
| Cuerpo | Figtree (sans amable y legible) |
| Tono visual | Cálido y cercano; ni médico ni infantil |

El morado es una prueba pedida por la clienta el 25 de septiembre (combinar con el oliva,
sin amarillo). Por ahora se usa solo en acentos puntuales — kickers de página, pasos del
proceso, íconos de FAQ — para no desplazar el oliva como color principal hasta que se valide.

Orden de carga de CSS: `tokens → base → layout → components`.

## Cómo trabajar

- **Ver el sitio:** abrir `index.html` (o usar la extensión Live Server de VS Code).
- **Ramas:** `main` (estable, lo que se muestra a la clienta), `develop` (integración) y `feature/<nombre>` para cada tarea.
- **Commits:** [Conventional Commits](https://www.conventionalcommits.org/es/) → `feat:`, `fix:`, `style:`, `docs:`, `chore:`.
- **Nombres de clases:** estilo BEM ligero (`.hero__title`, `.btn--primary`).
- **Accesibilidad:** foco visible, enlace “Saltar al contenido”, `prefers-reduced-motion` respetado. Mantener contraste AA.

## Publicar en GitHub

```bash
cd metamorphia
git init -b main
git add .
git commit -m "chore: estructura inicial y sistema de diseño (Sprint 1)"

# Crea un repositorio vacío en GitHub y luego:
git remote add origin https://github.com/<usuario>/metamorphia.git
git push -u origin main

git checkout -b develop && git push -u origin develop
```

Vista en línea (opcional): *Settings → Pages → Deploy from a branch → `main` / `/ (root)`*.

## Pendientes antes de publicar

- Reemplazar `57XXXXXXXXXX` por el número real de WhatsApp (busca `wa.me` en las 6 páginas).
- Confirmar con la clienta el valor de la sesión (hay un `<!-- TODO -->` en `proceso-faq.html`).
- Cambiar el isotipo provisional por el logotipo aprobado (mariposa + símbolo ψ).
- Validar con la clienta la combinación oliva + morado antes de aplicarla también al logo.
- Sustituir los `.image-frame` (foto de Sobre mí y de Contacto) por las fotos reales, una vez
  hecha la sesión profesional.
- Reemplazar los testimonios de ejemplo por los reales, solo con autorización explícita.
- Redactar la política de tratamiento de datos (ver `docs/brief.md`).
