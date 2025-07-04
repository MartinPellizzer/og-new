import os

from lib import g
from lib import sections

def gen():
    with open('styles/tmp/pag-prodotti.css', 'w') as f: f.write('')
    with open('styles/tmp-mobile/pag-prodotti-mobile.css', 'w') as f: f.write('')
    html_index = f'''
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
                {sections.prodotti_hero()}
                {sections.separator('Piccole')}
                {sections.prodotti_piccole()}
                {sections.separator('Medie')}
                {sections.prodotti_medie()}
                {sections.separator('Grandi')}
                {sections.prodotti_grandi()}
                {sections.separator('Contatti')}
                {sections.home_contact()}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_filepath = 'public/prodotti.html'
    with open(html_filepath, 'w') as f: f.write(html_index)

