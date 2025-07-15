import os

from lib import g

css_tmp_folderpath = 'styles/tmp'
for css_filename in os.listdir(css_tmp_folderpath):
    css_filepth = f'{css_tmp_folderpath}/{css_filename}'
    os.remove(css_filepth)
css_tmp_folderpath = 'styles/tmp-mobile'
for css_filename in os.listdir(css_tmp_folderpath):
    css_filepth = f'{css_tmp_folderpath}/{css_filename}'
    os.remove(css_filepth)

if 1:
    from lib import pag_home
    pag_home.gen()
if 1:
    from lib import pag_prodotti
    pag_prodotti.gen()
if 1:
    from lib import pag_servizi
    pag_servizi.gen()
if 1:
    from lib import pag_settori
    pag_settori.gen()
if 1:
    from lib import pag_settori_articoli
    pag_settori_articoli.gen()
if 1:
    from lib import pag_chi_siamo
    pag_chi_siamo.gen()
if 1:
    from lib import pag_contatti
    pag_contatti.gen()

css_core = f'''
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}

    body {{
        font-family: inter-regular, sans-serif;
        color: {g.color_black_pearl};
        font-size: {g.typography_size_md};
        line-height: {g.typography_line_height_md};
    }}

    img {{
        width: 100%;
    }}
'''

# with open('styles/core.css') as f: css_core = f.read()
css = ''
css += css_core
for filename in os.listdir('styles/tmp'):
    filepath = f'styles/tmp/{filename}'
    with open(filepath) as f: content = f.read()
    css += content
for filename in os.listdir('styles/tmp-mobile'):
    filepath = f'styles/tmp-mobile/{filename}'
    with open(filepath) as f: content = f.read()
    css += content
with open('public/style.css', 'w') as f: f.write(css)