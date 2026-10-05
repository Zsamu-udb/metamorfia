# -*- coding: utf-8 -*-
"""Genera las 6 páginas independientes de METAMORPHIA a partir de plantillas
compartidas (header/footer), para no duplicar manualmente el markup."""

import pathlib

# Raíz del proyecto = carpeta que contiene este archivo /build/
ROOT = pathlib.Path(__file__).resolve().parent.parent

NAV = [
    ("index.html", "Inicio"),
    ("sobre-mi.html", "Sobre mí"),
    ("servicios.html", "Servicios"),
    ("proceso-faq.html", "Proceso / FAQ"),
    ("testimonios.html", "Testimonios"),
    ("contacto.html", "Contacto"),
]

WA_LINK = "https://wa.me/57XXXXXXXXXX?text=Hola%2C%20quisiera%20informaci%C3%B3n%20sobre%20las%20sesiones."

SPRITE = """  <svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
    <symbol id="mark" viewBox="0 0 64 64">
      <g id="mark-wing" fill="currentColor">
        <path d="M33 30C38 15 53 9 60 16C63 24 56 32 47 35C41 37 36 35 33 33Z"/>
        <path d="M33 35C41 36 52 39 52 47C52 55 43 58 39 52C35 47 34 41 33 37Z" fill-opacity=".7"/>
      </g>
      <use href="#mark-wing" transform="translate(64 0) scale(-1 1)"/>
      <rect x="30.8" y="21" width="2.4" height="31" rx="1.2" fill="currentColor"/>
      <path d="M32 22C31 16 28 13 25 12M32 22C33 16 36 13 39 12" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
    </symbol>
  </svg>"""

ICON_WHATSAPP = '<svg class="btn__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 5.5h16v11H10l-5 4v-4H4z"/></svg>'

def icon(name, cls="teaser-card__icon"):
    paths = {
        "sobre-mi": '<circle cx="12" cy="8" r="3.3"/><path d="M5.5 20c1-4 4-6 6.5-6s5.5 2 6.5 6"/>',
        "servicios": '<path d="M12 20s-7-4.4-9.3-9C1.4 7.8 3 4.5 6.3 4.3c1.9-.1 3.4 1 4.7 2.6 1.3-1.6 2.8-2.7 4.7-2.6 3.3.2 4.9 3.5 3.6 6.7C19 15.6 12 20 12 20z"/>',
        "testimonios": '<path d="M7 9.5c0-2 1.5-3.5 3.5-3.5v2c-1 0-1.6.6-1.6 1.5h1.6v4H7z"/><path d="M14 9.5c0-2 1.5-3.5 3.5-3.5v2c-1 0-1.6.6-1.6 1.5h1.6v4H14z"/>',
        "contacto": '<path d="M4 5.5h16v11H10l-5 4v-4H4z"/>',
        "psicoterapia": '<path d="M12 4c-3 0-5 2.3-5 5 0 1.7.8 2.9 1.7 3.9.5.6.8 1 .8 1.6V16h5v-1.5c0-.6.3-1 .8-1.6.9-1 1.7-2.2 1.7-3.9 0-2.7-2-5-5-5Z"/><path d="M9.5 18.5h5M10 20.5h4"/>',
        "duelo": '<path d="M12 4c2 3 4 5.2 4 8a4 4 0 0 1-8 0c0-2.8 2-5 4-8Z"/>',
        "crianza": '<circle cx="9" cy="9" r="2.6"/><circle cx="16" cy="10.5" r="1.9"/><path d="M4.5 19c.6-3 2.3-5 4.5-5s3.9 2 4.5 5M13.7 19c.4-2.2 1.6-3.8 3.3-3.8s2.9 1.6 3.3 3.8"/>',
        "talleres": '<path d="M4 6.5h16v10H8l-4 3z"/><path d="M7.5 9.5h9M7.5 12.5h6"/>',
    }
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>'

def header(active_file):
    links = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == active_file else ""
        links.append(f'          <li><a class="site-nav__link" href="{href}"{current}>{label}</a></li>')
    links_html = "\n".join(links)
    return f"""  <a class="skip-link" href="#contenido">Saltar al contenido</a>

  <header class="site-header">
    <div class="container site-header__inner">
      <a class="brand" href="index.html" aria-label="METAMORPHIA, ir al inicio">
        <svg class="brand__mark" aria-hidden="true"><use href="#mark"/></svg>
        <span class="brand__name">METAMORPHIA</span>
      </a>

      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
        <span class="nav-toggle__bars" aria-hidden="true"></span>
        <span>Menú</span>
      </button>

      <nav class="site-nav" id="site-nav" aria-label="Principal">
        <ul class="site-nav__list">
{links_html}
        </ul>
        <a class="btn btn--primary btn--sm" href="{WA_LINK}">Escribir por WhatsApp</a>
      </nav>
    </div>
  </header>"""

def footer():
    return f"""  <footer class="site-footer">
    <div class="container site-footer__grid">
      <div class="site-footer__brand">
        <a class="brand" href="index.html" aria-label="METAMORPHIA, volver al inicio">
          <svg class="brand__mark" aria-hidden="true"><use href="#mark"/></svg>
          <span class="brand__name">METAMORPHIA</span>
        </a>
        <p class="site-footer__tagline">Acompañamiento emocional y psicología clínica.</p>
      </div>

      <nav aria-label="Secciones del sitio">
        <h2 class="site-footer__heading">Explorar</h2>
        <ul class="site-footer__list">
          <li><a href="sobre-mi.html">Sobre mí</a></li>
          <li><a href="servicios.html">Servicios</a></li>
          <li><a href="proceso-faq.html">Proceso / FAQ</a></li>
          <li><a href="testimonios.html">Testimonios</a></li>
          <li><a href="contacto.html">Contacto</a></li>
        </ul>
      </nav>

      <div>
        <h2 class="site-footer__heading">Escríbeme</h2>
        <ul class="site-footer__list">
          <li><a href="{WA_LINK}">WhatsApp</a></li>
          <li>Atención presencial y virtual</li>
        </ul>
      </div>
    </div>

    <div class="container site-footer__legal">
      <p>© 2026 METAMORPHIA. Todos los derechos reservados.</p>
      <a href="#">Política de tratamiento de datos</a>
    </div>
  </footer>"""

def page(filename, title, description, main_html, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="es-CO">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#F4EEE2">
  <link rel="icon" href="assets/logo/metamorphia-mark.svg" type="image/svg+xml">

  <script>document.documentElement.classList.add("js");</script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,300&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/base.css">
  <link rel="stylesheet" href="css/layout.css">
  <link rel="stylesheet" href="css/components.css">
{extra_head}</head>
<body>

{SPRITE}

{header(filename)}

  <main id="contenido">
{main_html}
  </main>

{footer()}

  <script src="js/main.js" defer></script>
</body>
</html>
"""

def write(filename, title, description, main_html, extra_head=""):
    out = page(filename, title, description, main_html, extra_head)
    (ROOT / filename).write_text(out, encoding="utf-8")
    print("escrito:", filename, len(out), "bytes")
