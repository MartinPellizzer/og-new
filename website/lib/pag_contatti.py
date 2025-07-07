import os

from lib import g
from lib import sections

def gen():
    with open('styles/tmp/pag-contatti.css', 'w') as f: f.write('')
    with open('styles/tmp-mobile/pag-contatti-mobile.css', 'w') as f: f.write('')
    html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            {sections.header_light()}
            <main>
                {sections.contatti_section_1()}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_filepath = 'public/contatti.html'
    with open(html_filepath, 'w') as f: f.write(html)

