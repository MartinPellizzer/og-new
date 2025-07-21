import os

from lib import g
from lib import components
from lib import blocks
from lib import sections

def gen():
    html_heading = blocks.heading_2col_1(
        title = components.h2_default(
            text = f'''Altri Servizi''',
        ),
        paragraph = components.button_fill_default(
            text = f'''''',
        ),
    )
    
    html_card_2 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'02',
        ),
        title = components.h3_default(
            text = f'Sopralluogo',
        ),
        paragraph = components.paragraph_default(
            text = f'''Eseguiamo sopralluoghi tecnici in sede per valutare ambienti e processi, garantendo soluzioni ozono compatibili con le tue reali esigenze operative.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M80-80v-481l280-119v80l200-80v120h320v480H80Zm80-80h640v-320H480v-82l-200 80v-78l-120 53v347Zm280-80h80v-160h-80v160Zm-160 0h80v-160h-80v160Zm320 0h80v-160h-80v160Zm280-320H680l40-320h120l40 320ZM160-160h640-640Z"/></svg>
            ''',
        ),
    )
    html_card_3 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'03',
        ),
        title = components.h3_default(
            text = f'Dimensionamento',
        ),
        paragraph = components.paragraph_default(
            text = f'''Calcoliamo il dimensionamento ideale del generatore ozono, basandoci su dati reali per garantire efficacia, sicurezza e ottimizzazione energetica.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M208-120q-37 0-62.5-25.5T120-208v-548q0-29 27-40.5t47 8.5l90 90-54 54 28 28 54-54 104 104-54 54 28 28 54-54 104 104-54 54 28 28 54-54 104 104-54 54 28 28 54-54 80 80q20 20 8.5 47T756-120H208Zm32-120h332L240-572v332Z"/></svg>
            ''',
        ),
    )
    html_card_4 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'04',
        ),
        title = components.h3_default(
            text = f'Progettazione',
        ),
        paragraph = components.paragraph_default(
            text = f'''Offriamo generatori di ozono standard e su misura, progettati internamente per adattarsi a ogni contesto produttivo, dai laboratori alle linee industriali complesse.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="m352-522 86-87-56-57-44 44-56-56 43-44-45-45-87 87 159 158Zm328 329 87-87-45-45-44 43-56-56 43-44-57-56-86 86 158 159Zm24-567 57 57-57-57ZM290-120H120v-170l175-175L80-680l200-200 216 216 151-152q12-12 27-18t31-6q16 0 31 6t27 18l53 54q12 12 18 27t6 31q0 16-6 30.5T816-647L665-495l215 215L680-80 465-295 290-120Zm-90-80h56l392-391-57-57-391 392v56Zm420-419-29-29 57 57-28-28Z"/></svg>
            ''',
        ),
    )

    html_cards = ''
    html_cards += html_card_2
    html_cards += html_card_3
    html_cards += html_card_4

    html_altri_servizi_grid = sections.grid_1_default(
        html_heading, 
        html_cards,
    )

    with open('styles/tmp/pag-servizi-servizio.css', 'w') as f: f.write('')
    with open('styles/tmp-mobile/pag-servizi-servizio-mobile.css', 'w') as f: f.write('')
    html_index = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/style.css">
        </head>
        <body>
            {sections.header_light()}
            <main>
                {sections.hero_2_reverse()}
                {sections.spacer_1()}
                {sections.layout_2col_5x4()}
                {html_altri_servizi_grid}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/servizi/consulenza.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)

