import os

from lib import g
from lib import sections

def gen():
    with open('styles/tmp/pag-home.css', 'w') as f: f.write('')
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write('')
    html_index = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            {sections.header_dark()}
            <main>
                {sections.home_hero()}
                {sections.home_proof()}
                {sections.separator('Benefici')}
                {sections.home_benefits()}
                {sections.separator('Servizi')}
                {sections.home_services()}
                {sections.separator('Settori')}
                {sections.home_sectors()}
                {sections.separator('Azienda')}
                {sections.home_about()}
                {sections.separator('Contatti')}
                {sections.home_contact()}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/index.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)

