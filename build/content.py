# -*- coding: utf-8 -*-
from generate_pages import write, icon, WA_LINK, ICON_WHATSAPP

# ============================================================== INICIO

HERO_ART = """        <div class="hero__visual" aria-hidden="true">
          <svg class="hero-art" viewBox="0 0 480 540" focusable="false">
            <defs>
              <linearGradient id="g-up" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0" stop-color="#8A9459"/>
                <stop offset="1" stop-color="#5A6535"/>
              </linearGradient>
              <linearGradient id="g-low" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0" stop-color="#B0B788"/>
                <stop offset="1" stop-color="#7E884F"/>
              </linearGradient>
              <path id="a-petal" d="M0 0C-9 -9 -9 -22 0 -30C9 -22 9 -9 0 0Z"/>
              <g id="a-flower">
                <use href="#a-petal" fill="#F4EEE2" fill-opacity=".92"/>
                <use href="#a-petal" fill="#F4EEE2" fill-opacity=".92" transform="rotate(72)"/>
                <use href="#a-petal" fill="#F4EEE2" fill-opacity=".92" transform="rotate(144)"/>
                <use href="#a-petal" fill="#F4EEE2" fill-opacity=".92" transform="rotate(216)"/>
                <use href="#a-petal" fill="#F4EEE2" fill-opacity=".92" transform="rotate(288)"/>
                <circle r="5" fill="#4E5730"/>
              </g>
              <g id="a-wing">
                <path d="M241 240C266 130 372 64 434 102C470 126 448 208 402 244C362 274 292 274 241 254Z" fill="url(#g-up)"/>
                <path d="M241 258C292 278 366 276 384 322C398 366 346 414 306 392C268 370 250 310 241 282Z" fill="url(#g-low)"/>
                <g fill="none" stroke="#F4EEE2" stroke-opacity=".5" stroke-width="1.4" stroke-linecap="round">
                  <path d="M250 240C290 190 340 140 420 112"/>
                  <path d="M252 248C300 228 360 202 428 162"/>
                  <path d="M252 256C300 258 350 248 396 230"/>
                  <path d="M254 266C300 292 340 322 372 344"/>
                  <path d="M252 274C290 304 316 350 316 386"/>
                </g>
                <use href="#a-flower" transform="translate(374 160) scale(.85)"/>
                <use href="#a-flower" transform="translate(322 346) scale(.5) rotate(20)"/>
              </g>
            </defs>
            <path d="M52 540V232A188 188 0 0 1 428 232V540" fill="none" stroke="#B0B788" stroke-width="1.5"/>
            <path d="M70 540V232A170 170 0 0 1 410 232V540Z" fill="#E9DFCB"/>
            <path d="M16 539H464" stroke="#B0B788" stroke-width="1.5" stroke-linecap="round"/>
            <g>
              <path d="M58 540C60 500 74 470 92 446" fill="none" stroke="#767F4B" stroke-width="2" stroke-linecap="round"/>
              <use href="#a-petal" fill="#767F4B" transform="translate(63 512) rotate(-50) scale(.7)"/>
              <use href="#a-petal" fill="#929B63" transform="translate(68 494) rotate(55) scale(.7)"/>
              <use href="#a-petal" fill="#767F4B" transform="translate(77 474) rotate(-45) scale(.6)"/>
              <use href="#a-petal" fill="#929B63" transform="translate(85 458) rotate(60) scale(.55)"/>
              <use href="#a-petal" fill="#767F4B" transform="translate(92 446) rotate(28) scale(.5)"/>
            </g>
            <g class="hero-art__wing"><use href="#a-wing"/></g>
            <g class="hero-art__wing"><use href="#a-wing" transform="translate(480 0) scale(-1 1)"/></g>
            <ellipse cx="240" cy="272" rx="6" ry="60" fill="#2C311C"/>
            <circle cx="240" cy="208" r="8" fill="#2C311C"/>
            <path d="M237 202C232 182 222 170 210 164M243 202C248 182 258 170 270 164" fill="none" stroke="#2C311C" stroke-width="2" stroke-linecap="round"/>
            <circle cx="210" cy="164" r="3" fill="#2C311C"/>
            <circle cx="270" cy="164" r="3" fill="#2C311C"/>
            <g class="hero-art__petal" style="--i:0"><use href="#a-petal" fill="#767F4B" transform="translate(340 432) rotate(25) scale(.9)"/></g>
            <g class="hero-art__petal" style="--i:1"><use href="#a-petal" fill="#929B63" transform="translate(380 468) rotate(70) scale(.8)"/></g>
            <g class="hero-art__petal" style="--i:2"><use href="#a-petal" fill="#B0B788" transform="translate(426 502) rotate(110) scale(.7)"/></g>
            <g class="hero-art__petal" style="--i:3"><use href="#a-petal" fill="#929B63" transform="translate(150 424) rotate(-35) scale(.85)"/></g>
            <g class="hero-art__petal" style="--i:4"><use href="#a-petal" fill="#B0B788" transform="translate(112 466) rotate(-80) scale(.75)"/></g>
            <g class="hero-art__petal" style="--i:5"><use href="#a-petal" fill="#767F4B" transform="translate(176 494) rotate(-20) scale(.65)"/></g>
            <g class="hero-art__petal" style="--i:6"><use href="#a-petal" fill="#B0B788" transform="translate(58 92) rotate(-25) scale(.6)"/></g>
            <g class="hero-art__petal" style="--i:7"><use href="#a-petal" fill="#CDD1A9" transform="translate(30 134) rotate(-55) scale(.5)"/></g>
          </svg>
        </div>"""

teasers = [
    ("sobre-mi.html", "sobre-mi", "Sobre mí", "Formación, enfoque y la historia detrás de la mariposa."),
    ("servicios.html", "servicios", "Servicios", "Psicoterapia, duelo, crianza y talleres."),
    ("testimonios.html", "testimonios", "Testimonios", "Lo que cuentan quienes ya hicieron el proceso."),
    ("contacto.html", "contacto", "Contacto", "Escríbeme por WhatsApp y agendamos."),
]
teaser_cards = "\n".join(f"""          <a class="teaser-card" href="{href}">
            {icon(name)}
            <span class="teaser-card__title">{title}</span>
            <span class="teaser-card__text">{text}</span>
          </a>""" for href, name, title, text in teasers)

INDEX_MAIN = f"""    <section class="hero" aria-labelledby="hero-title">
      <div class="container hero__inner">
        <div class="hero__copy">
          <h1 class="hero__title" id="hero-title">Todo cambio merece un buen acompañamiento.</h1>
          <p class="hero__lead">
            Psicoterapia clínica con cercanía y respaldo científico. Te acompaño en la gestión emocional, el duelo, la crianza y el cuidado de adultos mayores, de forma presencial o virtual.
          </p>
          <div class="hero__actions">
            <a class="btn btn--primary" href="{WA_LINK}">
              {ICON_WHATSAPP}
              Escríbeme por WhatsApp
            </a>
            <a class="btn btn--ghost" href="servicios.html">Ver servicios</a>
          </div>
          <ul class="hero__credentials" aria-label="Formación">
            <li>Psicóloga de la UPTC</li>
            <li>Especialista en trastornos afectivos y emocionales</li>
            <li>Terapias de tercera y cuarta generación, basadas en evidencia</li>
          </ul>
        </div>
{HERO_ART}
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <h2 class="section__title" style="margin-bottom: 0;">Explorar</h2>
        <div class="teaser-grid">
{teaser_cards}
        </div>
      </div>
    </section>"""

write(
    "index.html",
    "METAMORPHIA | Psicología clínica y acompañamiento emocional",
    "Psicoterapia clínica con cercanía y respaldo científico: gestión emocional, duelo, crianza y acompañamiento a adultos mayores. Atención presencial y virtual.",
    INDEX_MAIN,
)

# ============================================================== SOBRE MÍ

SOBRE_MI_MAIN = f"""    <section class="section">
      <div class="container" style="display:grid; grid-template-columns: minmax(0,0.9fr) minmax(0,1.4fr); gap: var(--space-8); align-items: start;">
        <div class="image-frame">{icon('sobre-mi', cls='btn__icon')} Foto profesional — pendiente sesión con la clienta</div>

        <div>
          <p class="page-head__kicker">Quién te acompaña</p>
          <h1 class="section__title" style="margin-bottom: var(--space-5);">Sobre mí</h1>

          <p style="margin-bottom: var(--space-4); color: var(--color-text-muted);">
            Soy psicóloga clínica y trabajo en todo lo relacionado con trastornos afectivos y emocionales:
            gestión del estrés, procesos de duelo y acompañamiento a personas en momentos de cambio.
            Más allá de lo profesional, creo que lo que marca la diferencia es la parte humana — la empatía
            y el reconocimiento genuino del dolor de quien tengo al frente.
          </p>
          <p style="margin-bottom: var(--space-6); color: var(--color-text-muted);">
            Trabajo con terapias de tercera y cuarta generación: la intervención más reciente en psicología,
            con una estructura científica detrás. No se trata solo de escuchar y comprender, sino de
            acompañar con herramientas basadas en evidencia.
          </p>

          <h2 style="font-family: var(--font-body); font-size: var(--fs-md); margin-bottom: var(--space-4);">Formación</h2>
          <ul class="hero__credentials" aria-label="Formación" style="border-top:none; padding-top:0; margin-top:0; margin-bottom: var(--space-7);">
            <li>Psicóloga — Universidad Pedagógica y Tecnológica de Colombia (UPTC)</li>
            <li>Especialización en Evaluación Clínica y Tratamiento de Trastornos Afectivos y Emocionales</li>
            <li>Maestría en Psicología Clínica (en curso)</li>
          </ul>

          <h2 style="font-family: var(--font-body); font-size: var(--fs-md); margin-bottom: var(--space-3);">El símbolo — la mariposa</h2>
          <p style="color: var(--color-text-muted);">
            La mariposa representa transformación: avanzar, cambiar, evolucionar. Las flores que nacen de
            ella hablan de lo mismo — de acompañar a cada persona en su propio proceso de evolución.
          </p>
        </div>
      </div>
    </section>"""

write(
    "sobre-mi.html",
    "Sobre mí | METAMORPHIA",
    "Formación y enfoque: psicoterapia clínica basada en evidencia, cercana y cálida. Conoce la historia detrás de METAMORPHIA.",
    SOBRE_MI_MAIN,
)

# ============================================================== SERVICIOS

services = [
    ("psicoterapia", "Psicoterapia", "Para cualquier etapa del ciclo vital — niños, adultos y adultos mayores — según las necesidades de cada quien. En promedio, un proceso dura alrededor de 10 sesiones."),
    ("duelo", "Acompañamiento en duelo", "Un proceso distinto al terapéutico, enfocado en adaptarse y encontrar sentido después de una pérdida."),
    ("crianza", "Pautas de crianza", "Trabajo con niños y con familias para fortalecer la gestión emocional desde casa."),
    ("talleres", "Talleres y charlas", "Espacios grupales sobre gestión emocional y manejo del estrés, a la medida de cada grupo."),
]
service_cards = "\n".join(f"""          <div class="service-card">
            <div class="service-card__icon">{icon(name, cls='')}</div>
            <h2 class="service-card__title">{title}</h2>
            <p class="service-card__text">{text}</p>
          </div>""" for name, title, text in services)

SERVICIOS_MAIN = f"""    <section class="section">
      <div class="container">
        <div class="page-head">
          <p class="page-head__kicker">Cómo puedo acompañarte</p>
          <h1 class="section__title" style="margin-bottom:0;">Servicios</h1>
          <p class="page-head__lead">Todo el trabajo parte de la gestión emocional, con un enfoque que se adapta a lo que cada persona necesita.</p>
        </div>

        <div class="service-grid">
{service_cards}
        </div>

        <h2 style="font-family: var(--font-body); font-size: var(--fs-md); margin-top: var(--space-8); margin-bottom: 0;">Modalidad de atención</h2>
        <div class="modality-row">
          <span class="modality-chip">Presencial</span>
          <span class="modality-chip">Virtual</span>
          <span class="modality-chip">Híbrida — tú eliges</span>
        </div>
      </div>
    </section>"""

write(
    "servicios.html",
    "Servicios | METAMORPHIA",
    "Psicoterapia, acompañamiento en duelo, pautas de crianza y talleres. Atención híbrida: presencial y virtual.",
    SERVICIOS_MAIN,
)

# ============================================================== PROCESO / FAQ

steps = [
    ("Escríbeme", "Por WhatsApp — cuéntame brevemente qué necesitas."),
    ("Agendamos", "Buscamos el horario que mejor te quede, presencial o virtual."),
    ("Consentimiento informado", "Firmas la autorización para iniciar el proceso terapéutico."),
    ("Primera sesión", "Empezamos a construir el proceso juntas."),
]
step_html = "\n".join(f"""          <div class="process-step">
            <h3 class="process-step__title">{title}</h3>
            <p class="process-step__text">{text}</p>
          </div>""" for title, text in steps)

faqs = [
    ("¿Cómo es el proceso terapéutico?",
     "Depende de las necesidades de cada persona: trabajo con niños, adultos y adultos mayores, en cualquier etapa del ciclo vital. En promedio, un proceso dura alrededor de 10 sesiones, aunque esto varía caso a caso."),
    ("¿Cuánto cuesta?",
     "El valor se maneja por sesión, no por paquete cerrado. Escríbeme por WhatsApp y te cuento la tarifa vigente. <!-- TODO: confirmar tarifa exacta con la clienta antes de publicar -->"),
    ("¿Qué tipo de atención se ofrece?",
     "Híbrida: presencial o virtual, como prefieras. Podemos definirlo juntas desde el primer contacto."),
    ("¿Atienden niños y adultos mayores?",
     "Sí. Trabajo con todas las etapas del ciclo vital, incluyendo acompañamiento a familias con niños y procesos de adaptación en adultos mayores."),
    ("¿Qué es el consentimiento informado?",
     "Es la autorización que firmas antes de iniciar el proceso: explica en qué consiste la terapia y cómo se protege tu confidencialidad."),
]
faq_html = "\n".join(f"""          <div class="faq-item">
            <button class="faq-item__question" aria-expanded="false">
              <span>{q}</span>
              <span class="faq-item__icon" aria-hidden="true">+</span>
            </button>
            <div class="faq-item__answer">
              <div class="faq-item__answer-inner"><p>{a}</p></div>
            </div>
          </div>""" for q, a in faqs)

PROCESO_MAIN = f"""    <section class="section">
      <div class="container">
        <div class="page-head">
          <p class="page-head__kicker">Antes de escribir por WhatsApp</p>
          <h1 class="section__title" style="margin-bottom:0;">Proceso y preguntas frecuentes</h1>
          <p class="page-head__lead">Así funciona el acompañamiento, paso a paso — para que llegues con las dudas más importantes ya resueltas.</p>
        </div>

        <div class="process-steps">
{step_html}
        </div>

        <h2 style="font-family: var(--font-body); font-size: var(--fs-md); margin-bottom: var(--space-4);">Preguntas frecuentes</h2>
        <div class="faq-list">
{faq_html}
        </div>
        <p class="faq-note">¿Tu duda no está aquí? <a href="{WA_LINK}">Escríbeme directamente por WhatsApp</a>.</p>
      </div>
    </section>"""

write(
    "proceso-faq.html",
    "Proceso y preguntas frecuentes | METAMORPHIA",
    "Cómo es el proceso terapéutico paso a paso y respuestas a las dudas más frecuentes antes de escribir por WhatsApp.",
    PROCESO_MAIN,
)

# ============================================================== TESTIMONIOS

sample_quotes = [
    "“Encontré un espacio donde de verdad me sentí escuchada, sin sentirme juzgada en ningún momento.”",
    "“El proceso se sintió cercano y humano, muy distinto a lo que esperaba de una consulta clínica.”",
    "“Agradezco mucho el acompañamiento en un momento tan difícil para mi familia.”",
]
testimonial_cards = "\n".join(f"""          <article class="testimonial-card">
            <p class="testimonial-card__quote">{q}</p>
            <div class="testimonial-card__author">
              <span class="testimonial-card__avatar" aria-hidden="true"></span>
              <span>Testimonio de ejemplo — consultante anónimo</span>
            </div>
          </article>""" for q in sample_quotes)

TESTIMONIOS_MAIN = f"""    <section class="section">
      <div class="container">
        <div class="page-head">
          <p class="page-head__kicker">Experiencias</p>
          <h1 class="section__title" style="margin-bottom:0;">Testimonios</h1>
          <p class="page-head__lead">
            Los testimonios reales se publican solo con autorización explícita de cada persona.
            Mientras se recopilan los definitivos, estas tarjetas muestran el formato.
          </p>
        </div>

        <div class="testimonial-grid">
{testimonial_cards}
        </div>

        <div class="testimonial-form">
          <div class="testimonial-form__text">
            <strong style="color: var(--color-text); display:block; margin-bottom: var(--space-2);">Dejar un comentario</strong>
            Formulario de ejemplo — la conexión a un servicio de envío queda pendiente para una próxima entrega.
          </div>
          <button class="btn btn--ghost btn--sm" type="button" disabled>Enviar comentario</button>
        </div>
      </div>
    </section>"""

write(
    "testimonios.html",
    "Testimonios | METAMORPHIA",
    "Experiencias de quienes ya han tomado el proceso de acompañamiento con METAMORPHIA.",
    TESTIMONIOS_MAIN,
)

# ============================================================== CONTACTO

CONTACTO_MAIN = f"""    <section class="section">
      <div class="container contact-grid">
        <div>
          <p class="page-head__kicker">Hablemos</p>
          <h1 class="section__title" style="margin-bottom: var(--space-4);">Contacto</h1>
          <p style="color: var(--color-text-muted); max-width: 46ch;">
            La forma más rápida de escribirme es por WhatsApp. Cuéntame brevemente qué necesitas y te respondo
            para agendar tu primera sesión.
          </p>

          <div class="contact-info">
            <span>📍 Atención presencial y virtual</span>
            <span>💬 Respuesta más ágil por WhatsApp</span>
          </div>

          <div class="hero__actions" style="margin-top:0;">
            <a class="btn btn--primary" href="{WA_LINK}">
              {ICON_WHATSAPP}
              Escríbeme por WhatsApp
            </a>
          </div>

          <h2 style="font-family: var(--font-body); font-size: var(--fs-md); margin-top: var(--space-7); margin-bottom: 0;">Modalidad</h2>
          <div class="modality-row">
            <span class="modality-chip">Presencial</span>
            <span class="modality-chip">Virtual</span>
          </div>
        </div>

        <div class="image-frame image-frame--wide">Mapa o foto — por definir</div>
      </div>
    </section>"""

write(
    "contacto.html",
    "Contacto | METAMORPHIA",
    "Escríbeme por WhatsApp para agendar tu primera sesión, presencial o virtual.",
    CONTACTO_MAIN,
)

print("Listo: 6 páginas generadas.")
