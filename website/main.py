import os

from lib import g

try: os.remove(g.styles_components_filepath)
except: pass

if 1:
    from lib import pag_home
    pag_home.gen()

with open('styles/core.css') as f: css_core = f.read()
css = ''
css += css_core
for filename in os.listdir('styles/tmp'):
    filepath = f'styles/tmp/{filename}'
    with open(filepath) as f: content = f.read()
    css += content
with open('public/style.css', 'w') as f: f.write(css)