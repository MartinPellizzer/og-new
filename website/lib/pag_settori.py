import os

from lib import g
from lib import sections

def gen():
    with open('styles/tmp/pag-settori.css', 'w') as f: f.write('')
    with open('styles/tmp-mobile/pag-settori-mobile.css', 'w') as f: f.write('')
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
                {sections.settori_grid()}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/settori.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)

