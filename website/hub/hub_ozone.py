import os

from lib import g
from lib import sections

def gen():
    with open('styles/tmp/hub-ozono.css', 'w') as f: f.write('')
    with open('styles/tmp-mobile/hub-ozono-mobile.css', 'w') as f: f.write('')
    
    html_heading = sections.heading_1()

    html_article = ''
    html_article += html_heading

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
                {html_article}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/ozono.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)

