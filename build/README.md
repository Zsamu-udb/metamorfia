# Generador de páginas

`generate_pages.py` define las plantillas compartidas (header, footer, sprite del logo) y
`content.py` arma el contenido propio de cada una de las 6 páginas y las escribe en la raíz
del proyecto.

No es un build obligatorio: las páginas ya generadas (`*.html` en la raíz) son estáticas y se
pueden editar directamente a mano. Este script es solo una ayuda para cuando un cambio
(como el de renombrar la marca) afecta a las 6 páginas a la vez.

```bash
python3 content.py   # regenera las 6 páginas a partir de las plantillas
```
