import os

from lib import g
from lib import components
from lib import blocks
from lib import sections

def gen():
    html_heading = blocks.heading_default_2(
        title = components.h1_default(
            text = f'''Servizi di Ozonogroup''',
            align = f'center',
        ),
        paragraph = components.paragraph_default(
            text = f'''''',
            align = f'center',
        ),
    )
    html_card_1 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'01',
        ),
        title = components.h3_default(
            text = f'Consulenza',
        ),
        paragraph = components.paragraph_default(
            text = f'''Offriamo consulenza tecnica telefonica per ottimizzare l’uso dell’ozono, adattandolo al tuo impianto, settore e obiettivi microbiologici specifici.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M480-340q33 0 56.5-23.5T560-420q0-33-23.5-56.5T480-500q-33 0-56.5 23.5T400-420q0 33 23.5 56.5T480-340ZM160-120q-33 0-56.5-23.5T80-200v-440q0-33 23.5-56.5T160-720h160v-80q0-33 23.5-56.5T400-880h160q33 0 56.5 23.5T640-800v80h160q33 0 56.5 23.5T880-640v440q0 33-23.5 56.5T800-120H160Zm0-80h640v-440H160v440Zm240-520h160v-80H400v80ZM160-200v-440 440Z"/></svg>
            ''',
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
    html_card_5 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'05',
        ),
        title = components.h3_default(
            text = f'Trasporto',
        ),
        paragraph = components.paragraph_default(
            text = f'''Spediamo i generatori con imballaggi sicuri e tracciabilità, garantendo consegna in perfette condizioni tramite tecnici interni o corrieri selezionati.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M240-160q-50 0-85-35t-35-85H40v-440q0-33 23.5-56.5T120-800h560v160h120l120 160v200h-80q0 50-35 85t-85 35q-50 0-85-35t-35-85H360q0 50-35 85t-85 35Zm0-80q17 0 28.5-11.5T280-280q0-17-11.5-28.5T240-320q-17 0-28.5 11.5T200-280q0 17 11.5 28.5T240-240ZM120-360h32q17-18 39-29t49-11q27 0 49 11t39 29h272v-360H120v360Zm600 120q17 0 28.5-11.5T760-280q0-17-11.5-28.5T720-320q-17 0-28.5 11.5T680-280q0 17 11.5 28.5T720-240Zm-40-200h170l-90-120h-80v120ZM360-540Z"/></svg>
            ''',
        ),
    )
    html_card_6 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'06',
        ),
        title = components.h3_default(
            text = f'Installazione',
        ),
        paragraph = components.paragraph_default(
            text = f'''Installiamo e collaudiamo il generatore con tecnici qualificati, garantendo sicurezza, conformità normativa e piena funzionalità prima della messa in servizio.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M686-132 444-376q-20 8-40.5 12t-43.5 4q-100 0-170-70t-70-170q0-36 10-68.5t28-61.5l146 146 72-72-146-146q29-18 61.5-28t68.5-10q100 0 170 70t70 170q0 23-4 43.5T584-516l244 242q12 12 12 29t-12 29l-84 84q-12 12-29 12t-29-12Zm29-85 27-27-256-256q18-20 26-46.5t8-53.5q0-60-38.5-104.5T386-758l74 74q12 12 12 28t-12 28L332-500q-12 12-28 12t-28-12l-74-74q9 57 53.5 95.5T360-440q26 0 52-8t47-25l256 256ZM472-488Z"/></svg>
            ''',
        ),
    )
    html_card_7 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'07',
        ),
        title = components.h3_default(
            text = f'Formazione',
        ),
        paragraph = components.paragraph_default(
            text = f'''Formiamo il personale sull’uso sicuro ed efficiente del sistema e forniamo documentazione tecnica completa dopo l’installazione.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M480-120 200-272v-240L40-600l440-240 440 240v320h-80v-276l-80 44v240L480-120Zm0-332 274-148-274-148-274 148 274 148Zm0 241 200-108v-151L480-360 280-470v151l200 108Zm0-241Zm0 90Zm0 0Z"/></svg>
            ''',
        ),
    )
    html_card_8 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'08',
        ),
        title = components.h3_default(
            text = f'Assistenza',
        ),
        paragraph = components.paragraph_default(
            text = f'''Offriamo assistenza post-vendita rapida e competente, con supporto tecnico continuativo da remoto o in sede per garantire sicurezza e continuità operativa.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M480-680q17 0 28.5-11.5T520-720q0-17-11.5-28.5T480-760q-17 0-28.5 11.5T440-720q0 17 11.5 28.5T480-680Zm-40 320h80v-240h-80v240ZM80-80v-720q0-33 23.5-56.5T160-880h640q33 0 56.5 23.5T880-800v480q0 33-23.5 56.5T800-240H240L80-80Zm126-240h594v-480H160v525l46-45Zm-46 0v-480 480Z"/></svg>
            ''',
        ),
    )
    html_card_9 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'09',
        ),
        title = components.h3_default(
            text = f'Manutenzione',
        ),
        paragraph = components.paragraph_default(
            text = f'''Offriamo manutenzione programmata su misura per garantire prestazioni ottimali, sicurezza costante e riduzione dei fermi impianto nel tempo.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M754-81q-8 0-15-2.5T726-92L522-296q-6-6-8.5-13t-2.5-15q0-8 2.5-15t8.5-13l85-85q6-6 13-8.5t15-2.5q8 0 15 2.5t13 8.5l204 204q6 6 8.5 13t2.5 15q0 8-2.5 15t-8.5 13l-85 85q-6 6-13 8.5T754-81Zm0-95 29-29-147-147-29 29 147 147ZM205-80q-8 0-15.5-3T176-92l-84-84q-6-6-9-13.5T80-205q0-8 3-15t9-13l212-212h85l34-34-165-165h-57L80-765l113-113 121 121v57l165 165 116-116-43-43 56-56H495l-28-28 142-142 28 28v113l56-56 142 142q17 17 26 38.5t9 45.5q0 24-9 46t-26 39l-85-85-56 56-42-42-207 207v84L233-92q-6 6-13 9t-15 3Zm0-96 170-170v-29h-29L176-205l29 29Zm0 0-29-29 15 14 14 15Zm549 0 29-29-29 29Z"/></svg>
            ''',
        ),
    )
    html_cards = ''
    html_cards += html_card_1
    html_cards += html_card_2
    html_cards += html_card_3
    html_cards += html_card_4
    html_cards += html_card_5
    html_cards += html_card_6
    html_cards += html_card_7
    html_cards += html_card_8
    html_cards += html_card_9


    with open('styles/tmp/pag-servizi.css', 'w') as f: f.write('')
    with open('styles/tmp-mobile/pag-servizi-mobile.css', 'w') as f: f.write('')
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
                {sections.grid_1_default(html_heading, html_cards)}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/servizi.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)

