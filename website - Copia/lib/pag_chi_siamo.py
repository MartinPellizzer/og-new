import os

from lib import g
from lib import sections

def gen():
    with open('styles/tmp/pag-chi-siamo.css', 'w') as f: f.write('')
    with open('styles/tmp-mobile/pag-chi-siamo-mobile.css', 'w') as f: f.write('')
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
                {sections.chi_siamo_hero()}
                {sections.separator('Azienda')}
                {sections.chi_siamo_azienda()}
                {sections.separator('Storia')}
                {sections.chi_siamo_storia()}
                {sections.separator('Missione')}
                {sections.chi_siamo_missione()}
                {sections.separator('Tecnologia')}
                {sections.chi_siamo_tecnologia()}
                {sections.separator('Industrie')}
                {sections.chi_siamo_industrie()}
                {sections.separator('Sonstenibile')}
                {sections.chi_siamo_sostenibilita()}
                {sections.separator('Contatti')}
                {sections.home_contact()}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_filepath = 'public/chi-siamo.html'
    with open(html_filepath, 'w') as f: f.write(html)

