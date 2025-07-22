import os

from lib import g
from lib import components
from lib import blocks
from lib import sections

def consulenza():
    ### hero
    html_hero_heading = blocks.heading_default_3(
        title = components.h1_reverse(
            text = f'''Consulenza''',
            align = f'''center''',

        ),
        paragraph = components.paragraph_reverse(
            text = f'''Offriamo consulenza tecnica telefonica per ottimizzare l'uso dell'ozono, adattandolo al tuo impianto, settore e obiettivi microbiologici specifici.''',
            align = f'''center''',
        ),
        button = components.button_fill_reverse(
            text = f'''Contattaci''',
            link = f'''/contatti.html''',
        ),
    )
    image_url = f'/immagini/home/sanificazione-ozono.png'
    ### content
    html_content = ''
    html_content += components.h2_default(
        text = 'Descrizione',
    )
    html_content += components.paragraph_default(
        text = 'La consulenza è il punto di partenza fondamentale per una corretta integrazione dell’ozono nei processi aziendali. Ogni impianto, per essere efficace, deve nascere da un’analisi accurata delle reali esigenze produttive, sanitarie e strutturali dell’azienda. In questa fase, vengono valutati numerosi fattori: obiettivi di trattamento, caratteristiche degli ambienti, prodotti coinvolti, frequenza operativa, limiti normativi. L’esperienza maturata nel settore alimentare e industriale consente al nostro team tecnico di guidare il cliente verso soluzioni sicure, efficienti e su misura.',
    )
    html_content += components.h2_default(
        text = 'In cosa consiste?',
    )
    html_content += components.paragraph_default(
        text = 'Questo servizio consiste in:',
    )
    html_content += components.list_unordered_default(
        [
            'Analisi degli obiettivi specifici (es. sanificazione, deodorazione, abbattimento microbico, risparmio operativo)',
            'Valutazione della reale applicabilità dell’ozono nel tuo contesto',
            'Discussione preliminare sui rischi e benefici',
            'Pianificazione del sopralluogo tecnico',
            'Primi consigli pratici per ottimizzare spazi e trattamenti',
        ]
    )
    html_content += components.image_sm_default(
        src = '/immagini/home/sanificazione-ozono.png',
        alt = ''
    )
    ### contatti
    html_contatti = blocks.contact_col()
    ### altri servizi
    html_heading = blocks.heading_2col_1(
        title = components.h2_default(
            text = f'''Altri servizi''',
        ),
        button = components.button_ghost_default(
            text = f'''Vedi tutti i servizi''',
            link = f'''/servizi.html''',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/sopralluogo.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/dimensionamento.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/progettazione.html',
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
                {sections.hero_2_reverse(html_hero_heading, image_url)}
                {sections.spacer_1()}
                {sections.layout_2col_5x4(html_content, html_contatti)}
                {sections.separator('Altri servizi')}
                {html_altri_servizi_grid}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/servizi/consulenza.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)

def sopralluogo():
    ### hero
    html_hero_heading = blocks.heading_default_3(
        title = components.h1_reverse(
            text = f'''Sopralluogo''',
            align = f'''center''',

        ),
        paragraph = components.paragraph_reverse(
            text = f'''Eseguiamo sopralluoghi tecnici in sede per valutare ambienti e processi, garantendo soluzioni ozono compatibili con le tue reali esigenze operative.''',
            align = f'''center''',
        ),
        button = components.button_fill_reverse(
            text = f'''Contattaci''',
            link = f'''/contatti.html''',
        ),
    )
    image_url = f'/immagini/home/sanificazione-ozono.png'
    ### content
    html_content = ''
    html_content += components.h2_default(
        text = 'Descrizione',
    )
    html_content += components.paragraph_default(
        text = 'Il sopralluogo è una fase essenziale per progettare un impianto all’ozono efficace, sicuro e conforme alle reali condizioni operative dell’azienda. Ogni ambiente presenta caratteristiche uniche che possono influenzare significativamente la scelta delle tecnologie, la disposizione degli impianti e la modalità di trattamento. Grazie alla nostra esperienza nei settori alimentare, industriale e sanitario, il team Ozonogroup è in grado di eseguire valutazioni tecniche approfondite direttamente sul campo, rilevando criticità e opportunità che solo un’analisi in loco può evidenziare. Questo ci permette di fornire soluzioni realmente su misura, evitando interventi standardizzati e massimizzando l’efficacia del trattamento con ozono.',
    )
    html_content += components.h2_default(
        text = 'In cosa consiste?',
    )
    html_content += components.paragraph_default(
        text = 'Questo servizio consiste in:',
    )
    html_content += components.list_unordered_default(
        [
            'Visita tecnica presso il sito produttivo o commerciale',
            'Analisi delle caratteristiche strutturali e impiantistiche degli ambienti',
            'Rilevazione di criticità e punti strategici per il trattamento all’ozono',
            'Valutazione della sicurezza operativa per il personale e per i prodotti',
            'Raccolta di dati necessari al dimensionamento e alla progettazione dell’impianto',
        ]
    )
    html_content += components.image_sm_default(
        src = '/immagini/home/sanificazione-ozono.png',
        alt = ''
    )
    ### contatti
    html_contatti = blocks.contact_col()
    ### altri servizi
    html_heading = blocks.heading_2col_1(
        title = components.h2_default(
            text = f'''Altri servizi''',
        ),
        button = components.button_ghost_default(
            text = f'''Vedi tutti i servizi''',
            link = f'''/servizi.html''',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/dimensionamento.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/progettazione.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/trasporto.html',
        ),
    )
    html_cards = ''
    html_cards += html_card_3
    html_cards += html_card_4
    html_cards += html_card_5
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
                {sections.hero_2_reverse(html_hero_heading, image_url)}
                {sections.spacer_1()}
                {sections.layout_2col_5x4(html_content, html_contatti)}
                {sections.separator('Altri servizi')}
                {html_altri_servizi_grid}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/servizi/sopralluogo.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)
    
def dimensionamento():
    ### hero
    html_hero_heading = blocks.heading_default_3(
        title = components.h1_reverse(
            text = f'''Dimensionamento''',
            align = f'''center''',

        ),
        paragraph = components.paragraph_reverse(
            text = f'''Calcoliamo il dimensionamento ideale del generatore ozono, basandoci su dati reali per garantire efficacia, sicurezza e ottimizzazione energetica.''',
            align = f'''center''',
        ),
        button = components.button_fill_reverse(
            text = f'''Contattaci''',
            link = f'''/contatti.html''',
        ),
    )
    image_url = f'/immagini/home/sanificazione-ozono.png'
    ### content
    html_content = ''
    html_content += components.h2_default(
        text = 'Descrizione',
    )
    html_content += components.paragraph_default(
        text = 'Il dimensionamento è il primo passo per garantire l’efficacia e la sicurezza di un impianto ad ozono. Definire con precisione i parametri di funzionamento consente di adattare l’impianto alle reali caratteristiche dell’ambiente da trattare, evitando sprechi e ottimizzando le prestazioni. Il nostro team tecnico esegue rilievi puntuali direttamente sul campo, applicando criteri oggettivi per determinare il corretto fabbisogno di ozono in funzione dei volumi, delle condizioni ambientali e degli obiettivi specifici. In questo modo, si ottiene un sistema perfettamente calibrato, affidabile e coerente con le esigenze operative del cliente.',
    )
    html_content += components.h2_default(
        text = 'In cosa consiste?',
    )
    html_content += components.paragraph_default(
        text = 'Questo servizio consiste in:',
    )
    html_content += components.list_unordered_default(
        [
            'Rilievi tecnici in loco: volumetrie, superfici, temperature, umidità, materiali',
            'Analisi della carica microbica presente e dei punti critici di contaminazione',
            'Calcolo accurato del fabbisogno di ozono in funzione dei tuoi obiettivi',
            'Definizione della modalità di trattamento: shock, ciclico, continuo, automatizzato',
            'Verifica dell’idoneità all’uso in presenza di personale (conforme alle normative)',
        ]
    )
    html_content += components.image_sm_default(
        src = '/immagini/home/sanificazione-ozono.png',
        alt = ''
    )
    ### contatti
    html_contatti = blocks.contact_col()
    ### altri servizi
    html_heading = blocks.heading_2col_1(
        title = components.h2_default(
            text = f'''Altri servizi''',
        ),
        button = components.button_ghost_default(
            text = f'''Vedi tutti i servizi''',
            link = f'''/servizi.html''',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/progettazione.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/trasporto.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/installazione.html',
        ),
    )
    html_cards = ''
    html_cards += html_card_4
    html_cards += html_card_5
    html_cards += html_card_6
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
                {sections.hero_2_reverse(html_hero_heading, image_url)}
                {sections.spacer_1()}
                {sections.layout_2col_5x4(html_content, html_contatti)}
                {sections.separator('Altri servizi')}
                {html_altri_servizi_grid}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/servizi/dimensionamento.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)

def progettazione():
    ### hero
    html_hero_heading = blocks.heading_default_3(
        title = components.h1_reverse(
            text = f'''Progettazione''',
            align = f'''center''',

        ),
        paragraph = components.paragraph_reverse(
            text = f'''Offriamo generatori di ozono standard e su misura, progettati internamente per adattarsi a ogni contesto produttivo, dai laboratori alle linee industriali complesse.''',
            align = f'''center''',
        ),
        button = components.button_fill_reverse(
            text = f'''Contattaci''',
            link = f'''/contatti.html''',
        ),
    )
    image_url = f'/immagini/home/sanificazione-ozono.png'
    ### content
    html_content = ''
    html_content += components.h2_default(
        text = 'Descrizione',
    )
    html_content += components.paragraph_default(
        text = 'Ogni ambiente produttivo ha caratteristiche uniche. Per questo motivo, forniamo generatori di ozono non solo standardizzati, ma anche completamente personalizzati. Quando le condizioni operative richiedono soluzioni su misura, per potenza, dimensioni, installazione o automazione, il nostro ufficio tecnico è in grado di progettare e realizzare internamente il sistema più adatto. Dalla piccola cella frigorifera al tunnel industriale, ogni macchina può essere costruita su specifica richiesta, con materiali, funzioni e tecnologie modulabili.',
    )
    html_content += components.h2_default(
        text = 'In cosa consiste?',
    )
    html_content += components.paragraph_default(
        text = 'Questo servizio consiste in:',
    )
    html_content += components.list_unordered_default(
        [
            'Progettazione meccanica ed elettronica personalizzata',
            'Scelta dei materiali in base all’ambiente (inox alimentare, alluminio, tecnopolimeri)',
            'Regolazione della potenza produttiva da pochi grammi/ora fino a oltre 500 g/h',
            'Personalizzazione del metodo di erogazione: diretta, canalizzata, automatizzata',
            'Integrazione con sistemi HVAC, serbatoi, tunnel, camere, linee di processo',
            'Predisposizione per automazione e controllo remoto via PLC o pannello touch',
            'Redazione progetto tecnico preliminare e proposta economica personalizzata',
        ]
    )
    html_content += components.image_sm_default(
        src = '/immagini/home/sanificazione-ozono.png',
        alt = ''
    )
    ### contatti
    html_contatti = blocks.contact_col()
    ### altri servizi
    html_heading = blocks.heading_2col_1(
        title = components.h2_default(
            text = f'''Altri servizi''',
        ),
        button = components.button_ghost_default(
            text = f'''Vedi tutti i servizi''',
            link = f'''/servizi.html''',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/trasporto.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/installazione.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/formazione.html',
        ),
    )
    html_cards = ''
    html_cards += html_card_5
    html_cards += html_card_6
    html_cards += html_card_7
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
                {sections.hero_2_reverse(html_hero_heading, image_url)}
                {sections.spacer_1()}
                {sections.layout_2col_5x4(html_content, html_contatti)}
                {sections.separator('Altri servizi')}
                {html_altri_servizi_grid}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/servizi/progettazione.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)

def trasporto():
    ### hero
    html_hero_heading = blocks.heading_default_3(
        title = components.h1_reverse(
            text = f'''Trasporto''',
            align = f'''center''',

        ),
        paragraph = components.paragraph_reverse(
            text = f'''Spediamo i generatori con imballaggi sicuri e tracciabilità, garantendo consegna in perfette condizioni tramite tecnici interni o corrieri selezionati.''',
            align = f'''center''',
        ),
        button = components.button_fill_reverse(
            text = f'''Contattaci''',
            link = f'''/contatti.html''',
        ),
    )
    image_url = f'/immagini/home/sanificazione-ozono.png'
    ### content
    html_content = ''
    html_content += components.h2_default(
        text = 'Descrizione',
    )
    html_content += components.paragraph_default(
        text = 'Il trasporto dei generatori di ozono è una fase delicata che richiede attenzione, competenza e mezzi adeguati. A seconda delle dimensioni dell’impianto e della destinazione, può essere effettuato internamente dalla nostra azienda oppure affidato a corrieri selezionati. In entrambi i casi, l’obiettivo è garantire l’integrità dei dispositivi, il rispetto dei tempi di consegna e la sicurezza logistica dell’intero processo.',
    )
    html_content += components.h2_default(
        text = 'In cosa consiste?',
    )
    html_content += components.paragraph_default(
        text = 'Questo servizio consiste in:',
    )
    html_content += components.list_unordered_default(
        [
            'Imballaggio tecnico con materiali antiurto e impermeabili',
            'Etichettatura conforme, tracciabilità logistica e identificazione del contenuto',
            'Spedizione organizzata con mezzi propri o corrieri specializzati',
            'Coordinamento con il tuo personale per il ricevimento in azienda',
            'Monitoraggio costante delle fasi di spedizione',
        ]
    )
    html_content += components.image_sm_default(
        src = '/immagini/home/sanificazione-ozono.png',
        alt = ''
    )
    ### contatti
    html_contatti = blocks.contact_col()
    ### altri servizi
    html_heading = blocks.heading_2col_1(
        title = components.h2_default(
            text = f'''Altri servizi''',
        ),
        button = components.button_ghost_default(
            text = f'''Vedi tutti i servizi''',
            link = f'''/servizi.html''',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/installazione.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/formazione.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/assistenza.html',
        ),
    )
    html_cards = ''
    html_cards += html_card_6
    html_cards += html_card_7
    html_cards += html_card_8
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
                {sections.hero_2_reverse(html_hero_heading, image_url)}
                {sections.spacer_1()}
                {sections.layout_2col_5x4(html_content, html_contatti)}
                {sections.separator('Altri servizi')}
                {html_altri_servizi_grid}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/servizi/trasporto.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)

def installazione():
    ### hero
    html_hero_heading = blocks.heading_default_3(
        title = components.h1_reverse(
            text = f'''Installazione''',
            align = f'''center''',

        ),
        paragraph = components.paragraph_reverse(
            text = f'''Installiamo e collaudiamo il generatore con tecnici qualificati, garantendo sicurezza, conformità normativa e piena funzionalità prima della messa in servizio.''',
            align = f'''center''',
        ),
        button = components.button_fill_reverse(
            text = f'''Contattaci''',
            link = f'''/contatti.html''',
        ),
    )
    image_url = f'/immagini/home/sanificazione-ozono.png'
    ### content
    html_content = ''
    html_content += components.h2_default(
        text = 'Descrizione',
    )
    html_content += components.paragraph_default(
        text = 'L’installazione è una fase cruciale per garantire la piena operatività e l’efficacia del sistema ad ozono. Una corretta posa in opera evita malfunzionamenti, consente il massimo rendimento e riduce i rischi legati all’utilizzo scorretto. I nostri tecnici specializzati seguono tutte le operazioni direttamente in sede cliente, coordinandosi con il personale interno e adattando l’impianto alle specifiche strutturali e produttive.',
    )
    html_content += components.h2_default(
        text = 'In cosa consiste?',
    )
    html_content += components.paragraph_default(
        text = 'Questo servizio consiste in:',
    )
    html_content += components.list_unordered_default(
        [
            'Posizionamento del generatore (a parete, a terra, su staffe, sospeso)',
            'Collegamenti elettrici e pneumatici (se previsti)',
            'Installazione di tubazioni, diffusori, valvole e accessori specifici',
            'Verifica della sicurezza secondo le direttive CE',
            'Test preliminare di funzionamento',
            'Tutto viene svolto da personale certificato e con DPI obbligatori',
        ]
    )
    html_content += components.image_sm_default(
        src = '/immagini/home/sanificazione-ozono.png',
        alt = ''
    )
    ### contatti
    html_contatti = blocks.contact_col()
    ### altri servizi
    html_heading = blocks.heading_2col_1(
        title = components.h2_default(
            text = f'''Altri servizi''',
        ),
        button = components.button_ghost_default(
            text = f'''Vedi tutti i servizi''',
            link = f'''/servizi.html''',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/formazione.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/assistenza.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/manutenzione.html',
        ),
    )
    html_cards = ''
    html_cards += html_card_7
    html_cards += html_card_8
    html_cards += html_card_9
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
                {sections.hero_2_reverse(html_hero_heading, image_url)}
                {sections.spacer_1()}
                {sections.layout_2col_5x4(html_content, html_contatti)}
                {sections.separator('Altri servizi')}
                {html_altri_servizi_grid}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/servizi/installazione.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)

def formazione():
    ### hero
    html_hero_heading = blocks.heading_default_3(
        title = components.h1_reverse(
            text = f'''Formazione''',
            align = f'''center''',

        ),
        paragraph = components.paragraph_reverse(
            text = f'''Formiamo il personale sull'uso sicuro ed efficiente del sistema e forniamo documentazione tecnica completa dopo l'installazione.''',
            align = f'''center''',
        ),
        button = components.button_fill_reverse(
            text = f'''Contattaci''',
            link = f'''/contatti.html''',
        ),
    )
    image_url = f'/immagini/home/sanificazione-ozono.png'
    ### content
    html_content = ''
    html_content += components.h2_default(
        text = 'Descrizione',
    )
    html_content += components.paragraph_default(
        text = 'Per garantire un uso efficace e sicuro del generatore, è fondamentale formare il personale che lo utilizzerà. Una buona formazione riduce i margini di errore, migliora l’efficienza nei cicli di trattamento e assicura il rispetto delle procedure aziendali e normative. Offriamo sessioni di formazione direttamente in sede, con contenuti tecnici personalizzati sul tipo di impianto e sul contesto operativo.',
    )
    html_content += components.h2_default(
        text = 'In cosa consiste?',
    )
    html_content += components.paragraph_default(
        text = 'Questo servizio consiste in:',
    )
    html_content += components.list_unordered_default(
        [
            'Descrizione ai principi di funzionamento dell’ozono e suoi effetti',
            'Presentazione delle componenti e delle modalità di utilizzo dell’impianto',
            'Simulazione dei cicli di trattamento e procedure operative passo-passo',
            'Formazione sull’uso di timer, sensori e controlli digitali/PLC',
            'Focus sulla sicurezza: allarmi, segnalazioni e uso corretto dei DPI',
            'Indicazioni su pulizia, manutenzione ordinaria e piccoli controlli',
            'Consegna di schede sintetiche operative (cartacee o digitali)',
        ]
    )
    html_content += components.image_sm_default(
        src = '/immagini/home/sanificazione-ozono.png',
        alt = ''
    )
    ### contatti
    html_contatti = blocks.contact_col()
    ### altri servizi
    html_heading = blocks.heading_2col_1(
        title = components.h2_default(
            text = f'''Altri servizi''',
        ),
        button = components.button_ghost_default(
            text = f'''Vedi tutti i servizi''',
            link = f'''/servizi.html''',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/assistenza.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/manutenzione.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/consulenza.html',
        ),
    )
    html_cards = ''
    html_cards += html_card_8
    html_cards += html_card_9
    html_cards += html_card_1
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
                {sections.hero_2_reverse(html_hero_heading, image_url)}
                {sections.spacer_1()}
                {sections.layout_2col_5x4(html_content, html_contatti)}
                {sections.separator('Altri servizi')}
                {html_altri_servizi_grid}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/servizi/formazione.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)

def assistenza():
    ### hero
    html_hero_heading = blocks.heading_default_3(
        title = components.h1_reverse(
            text = f'''Assistenza''',
            align = f'''center''',

        ),
        paragraph = components.paragraph_reverse(
            text = f'''Offriamo assistenza post-vendita rapida e competente, con supporto tecnico continuativo da remoto o in sede per garantire sicurezza e continuità operativa.''',
            align = f'''center''',
        ),
        button = components.button_fill_reverse(
            text = f'''Contattaci''',
            link = f'''/contatti.html''',
        ),
    )
    image_url = f'/immagini/home/sanificazione-ozono.png'
    ### content
    html_content = ''
    html_content += components.h2_default(
        text = 'Descrizione',
    )
    html_content += components.paragraph_default(
        text = 'Un impianto ad ozono efficiente deve essere supportato da un servizio di assistenza tecnica affidabile, tempestivo e competente. I tempi di fermo impianto possono incidere sulla produttività e sull’organizzazione del lavoro, per questo è fondamentale poter contare su interventi rapidi e risolutivi. Per questo motivo, il nostro team tecnico fornisce assistenza specializzata, sia in fase post-installazione sia durante l’intero ciclo di vita dell’impianto.',
    )
    html_content += components.h2_default(
        text = 'In cosa consiste?',
    )
    html_content += components.paragraph_default(
        text = 'Questo servizio consiste in:',
    )
    html_content += components.list_unordered_default(
        [
            'Supporto telefonico e da remoto per diagnosi iniziali',
            'Interventi in loco per guasti o anomalie operative',
            'Fornitura di ricambi originali e componenti rigenerati',
            'Verifica della produzione di ozono e controllo della cella',
            'Taratura e aggiornamento di sensori e software',
        ]
    )
    html_content += components.image_sm_default(
        src = '/immagini/home/sanificazione-ozono.png',
        alt = ''
    )
    ### contatti
    html_contatti = blocks.contact_col()
    ### altri servizi
    html_heading = blocks.heading_2col_1(
        title = components.h2_default(
            text = f'''Altri servizi''',
        ),
        button = components.button_ghost_default(
            text = f'''Vedi tutti i servizi''',
            link = f'''/servizi.html''',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/manutenzione.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/consulenza.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/sopralluogo.html',
        ),
    )
    html_cards = ''
    html_cards += html_card_9
    html_cards += html_card_1
    html_cards += html_card_2
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
                {sections.hero_2_reverse(html_hero_heading, image_url)}
                {sections.spacer_1()}
                {sections.layout_2col_5x4(html_content, html_contatti)}
                {sections.separator('Altri servizi')}
                {html_altri_servizi_grid}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/servizi/assistenza.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)

def manutenzione():
    ### hero
    html_hero_heading = blocks.heading_default_3(
        title = components.h1_reverse(
            text = f'''Manutenzione''',
            align = f'''center''',

        ),
        paragraph = components.paragraph_reverse(
            text = f'''Offriamo manutenzione programmata su misura per garantire prestazioni ottimali, sicurezza costante e riduzione dei fermi impianto nel tempo.''',
            align = f'''center''',
        ),
        button = components.button_fill_reverse(
            text = f'''Contattaci''',
            link = f'''/contatti.html''',
        ),
    )
    image_url = f'/immagini/home/sanificazione-ozono.png'
    ### content
    html_content = ''
    html_content += components.h2_default(
        text = 'Descrizione',
    )
    html_content += components.paragraph_default(
        text = 'La manutenzione periodica è la chiave per mantenere l’impianto ad ozono sempre efficiente, sicuro e performante nel tempo.  Offriamo piani di manutenzione su misura, pensati in base alla frequenza d’uso, alle condizioni ambientali e alle caratteristiche dell’impianto installato. L’obiettivo è prevenire guasti, preservare la potenza di trattamento e mantenere l’impianto in perfette condizioni operative.',
    )
    html_content += components.h2_default(
        text = 'In cosa consiste?',
    )
    html_content += components.paragraph_default(
        text = 'Questo servizio consiste in:',
    )
    html_content += components.list_unordered_default(
        [
            'Verifica e pulizia delle celle di generazione',
            'Controllo di valvole, filtri, tenute e raffreddamento',
            'Misurazione della produzione di ozono e confronto con i valori nominali',
            'Taratura periodica di sensori, timer, flussometri e controlli digitali',
            'Controllo cablaggi e componenti elettrici',
            'Sostituzione preventiva delle parti soggette a usura',
            'Interventi su contratto annuale o su chiamata, anche in orari non produttivi',
        ]
    )
    html_content += components.image_sm_default(
        src = '/immagini/home/sanificazione-ozono.png',
        alt = ''
    )
    ### contatti
    html_contatti = blocks.contact_col()
    ### altri servizi
    html_heading = blocks.heading_2col_1(
        title = components.h2_default(
            text = f'''Altri servizi''',
        ),
        button = components.button_ghost_default(
            text = f'''Vedi tutti i servizi''',
            link = f'''/servizi.html''',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/consulenza.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/sopralluogo.html',
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
        link = components.link_default(
            link_text = f'Vedi servizio',
            link_href = f'/servizi/dimensionamento.html',
        ),
    )
    html_cards = ''
    html_cards += html_card_1
    html_cards += html_card_2
    html_cards += html_card_3
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
                {sections.hero_2_reverse(html_hero_heading, image_url)}
                {sections.spacer_1()}
                {sections.layout_2col_5x4(html_content, html_contatti)}
                {sections.separator('Altri servizi')}
                {html_altri_servizi_grid}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/servizi/manutenzione.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)
    

def gen():
    consulenza()
    sopralluogo()
    dimensionamento()
    progettazione()
    trasporto()
    installazione()
    formazione()
    assistenza()
    manutenzione()
    

