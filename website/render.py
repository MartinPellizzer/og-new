### generate list of facilities
### normalize / resolve (canonicalize)

### for each facility generate list of processes

### for each facility generate list of problems


import os
import json
import shutil

from lorem_text import lorem

from lib import g
from lib import io
from lib import llm
from lib import polish
from lib import components

model_filepath = '/home/ubuntu/vault-tmp/llm/gemma-4-12b-it-Q4_K_S.gguf'
model_filepath = '/home/ubuntu/vault-tmp/llm/gemma-4-12B-it-qat-UD-Q4_K_XL.gguf'
model_filepath = '/home/ubuntu/vault-tmp/llm/gemma-4-26B-A4B-it-UD-Q4_K_M.gguf'


import sectors_data
# import facilities_data


def sectors_gen():
    prompt = f'''
        Write a list of sectors where ozone is being used.
        Use as few words as possible.
        Write only one sector per line.
        By sectors, i mean like food and beverage, hospitality, etc.
    '''.strip()
    print(prompt)
    reply = llm.reply(prompt, model_filepath)
    if '</think>' in reply: reply = reply.split('</think>')[1].strip()
    reply = polish.vanilla(reply)
    print()
    print('########################################################################')
    print(reply)
    print('########################################################################')
    print()

def facility_gen():
    prompt = f'''
        Write a list of facility types in the food industry where ozone is being used.
        Use as few words as possible.
        Write only one facility per line.
        Give me the normalized, canonical name for each facility type.
        Use the minimum amount of words as term for each facility type.
    '''.strip()
    print(prompt)
    reply = llm.reply(prompt, model_filepath)
    if '</think>' in reply: reply = reply.split('</think>')[1].strip()
    reply = polish.vanilla(reply)
    print()
    print('########################################################################')
    print(reply)
    print('########################################################################')
    print()

def render_sectors_html():
    input_data = sectors_data.data
    for sector_item in input_data:
        sector_name = sector_item['sector_name']
        sector_name_simple = sector_item['sector_name_simple']
        sector_slug = sector_item['sector_slug']
        ###
        children = []
        for candidate_child_item in input_data:
            if sector_item['sector_name_normalize'] == candidate_child_item['sector_parent_name_normalize']:
                print(sector_item['sector_name'])
                children.append(candidate_child_item)
        ###
        html_children = ''
        if children != []:
            html_children += '<ul>'
            for child in children:
                html_children += f'''<li><a href="/settori/{child['sector_slug']}">{child['sector_name']}</a></li>'''
            html_children += '</ul>'
        
    sectors_lvl_1 = [item for item in input_data if item['sector_parent_name_normalize'] == None]

    ###
    html_h1 = f'''<h1>Settori</h1>'''
    ###
    sectors_cards_html = ''
    if sectors_lvl_1 != []:
        for sector in sectors_lvl_1:
            print(sector)
            if sector['sector_name'].lower() == 'acqua':
                sector_image = 'https://plus.unsplash.com/premium_photo-1733266883899-29971ddbe5e3?q=80&w=1075&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            elif sector['sector_name'].lower() == 'alimentare':
                sector_image = 'https://images.unsplash.com/photo-1651525669944-00de65d3b8a5?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            elif sector['sector_name'].lower() == 'agricoltura':
                sector_image = 'https://images.unsplash.com/photo-1563514227147-6d2ff665a6a0?q=80&w=1471&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            elif sector['sector_name'].lower() == 'sanità':
                sector_image = 'https://images.unsplash.com/photo-1640876777002-badf6aee5bcc?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            elif sector['sector_name'].lower() == 'ospitalità':
                sector_image = 'https://images.unsplash.com/photo-1618773928121-c32242e63f39?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            elif sector['sector_name'].lower() == 'edilizia':
                sector_image = 'https://images.unsplash.com/photo-1497366754035-f200968a6e72?q=80&w=1469&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            elif sector['sector_name'].lower() == 'manifatturiero':
                sector_image = 'https://images.unsplash.com/photo-1717386255773-1e3037c81788?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            elif sector['sector_name'].lower() == 'energia':
                sector_image = 'https://images.unsplash.com/photo-1467533003447-e295ff1b0435?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            elif sector['sector_name'].lower() == 'ambiente':
                sector_image = 'https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?q=80&w=1613&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            elif sector['sector_name'].lower() == 'trasporti':
                sector_image = 'https://images.unsplash.com/photo-1578575437130-527eed3abbec?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            elif sector['sector_name'].lower() == 'residenziale':
                sector_image = 'https://images.unsplash.com/photo-1570129477492-45c003edd2be?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            elif sector['sector_name'].lower() == 'ricerca':
                sector_image = 'https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            else:
                sector_image = 'https://images.unsplash.com/photo-1787540757892-cab3118bd223?q=80&w=1074&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            sectors_cards_html += f'''
                <div class="card">
                    <div class="card-image">
                        <img src="{sector_image}" alt="Example Image" height="200">
                    </div>
                    <div class="card-content">
                        <h3>
                            <a href="/settori/{sector['sector_slug']}">
                                {sector['sector_name']}
                            </a>
                        </h3>
                        <p class="author-date">
                            Sarah Chen · 1 Jan 2024
                        </p>
                        <p class="description">
                            Learn how to quickly integrate and customize shadcn/ui components in your Next.js projects. We'll cover installation, theming, and best practices for building modern interfaces.
                        </p>
                    </div>
                </div>
            '''

    sectors_html = f'''
        <section style="margin-top: 5rem; margin-bottom: 5rem;">
            <h1 style="text-align: center;">Settori</h1>
            <p class="intro">Discover the latest trends, tips, and best practices in modern web development. From UI components to design systems, stay updated with our expert insights.</p>
            <div class="cards">
                {sectors_cards_html}
            </div>
        </section>
    '''
    ###
    article_html = f'''
        {sectors_html}
    '''

    ###
    url_slug = f'''settori'''
    meta_title = f'''Settori'''
    html = f''' 
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>{meta_title}</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="/styles.css">
        </head>
        <body>
            {components.header_light_logo()}
            <main class="hub-sectors container-xl">
                {article_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''.strip()
    ###
    html_folderpath = f'{g.website_folderpath}/{url_slug}'
    io.folders_recursive_gen(html_folderpath)
    html_filepath = f'{g.website_folderpath}/{url_slug}/index.html'
    with open(html_filepath, 'w') as f: f.write(html)
    print(html_filepath)

def render_sector_html_backup():
    input_data = sectors_data.data
    for sector_item in input_data:
        sector_name = sector_item['sector_name']
        sector_name_simple = sector_item['sector_name_simple']
        sector_slug = sector_item['sector_slug']
        ###
        children = []
        for candidate_child_item in input_data:
            if sector_item['sector_name_normalize'] == candidate_child_item['sector_parent_name_normalize']:
                print(sector_item['sector_name'])
                children.append(candidate_child_item)
        ###
        title = f'''Ozono nel settore {sector_name_simple}'''.capitalize()
        title = 'ozono nel settore lattiero-caseario'.capitalize()
        html_h1 = f'''<h1>{title}</h1>'''
        html_children = ''
        if children != []:
            html_children += '<ul>'
            for child in children:
                html_children += f'''<li><a href="/settori/{child['sector_slug']}">{child['sector_name']}</a></li>'''
            html_children += '</ul>'
        
        ###
        article_html = f'''
            {html_h1}
            {html_children}
        '''

        html_article = f''

        ###
        url_slug = f'''settori/{sector_slug}'''
        meta_title = f'''{sector_name_simple}'''

        html_intro = f'''
            <p class="usa-intro">{lorem.words(16)}</p>
            <p>{lorem.paragraph()}</p>
        '''


        ### SECTIONS
        html_h2 = f'''<h2 id="section-heading-h2">Il settore lattiero-caseario: struttura, filiera e caratteristiche</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'struttura'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Il settore lattiero-caseario: struttura, filiera e caratteristiche
                    Devi seguire le regole che trovi qui sotto.
                    Obiettivo: identificare senza ambiguità l'entità settore lattiero-caseario e definirne la posizione, i confini e l'organizzazione. Questa è la parte che permette al documento di stabilire il contesto macro prima di entrare nella relazione con l'ozono.
                    Target: 350–500 parole
                    Attributi da coprire
                    Attributo EAV	Cosa fornire come valore
                    Definizione	Che cos'è il settore lattiero-caseario
                    Tipo di entità	Settore industriale / comparto agroalimentare
                    Classificazione industriale	Posizione nelle classificazioni economiche/industriali pertinenti
                    Appartenenza	Relazione con agricoltura, zootecnia, industria alimentare
                    Confini del settore	Cosa rientra e cosa non rientra nel lattiero-caseario
                    Denominazioni	Lattiero-caseario, industria lattiero-casearia, dairy industry, ecc.
                    Segmentazione primaria	Principali segmenti del settore
                    Dimensione/scala	Piccoli, medi, grandi operatori; artigianale vs industriale
                    Tipologie di operatori	Aziende agricole, cooperative, trasformatori, industriali
                    Funzione economica	Ruolo del settore nella filiera alimentare
                    Dipendenze principali	Relazioni con agricoltura, allevamento, logistica, packaging
                    Caratteristiche distintive	Elementi che rendono il settore diverso da altri comparti alimentari
                    NON coprire qui
                    prodotti specifici in dettaglio → H2 2
                    singoli processi produttivi → H2 2
                    contaminanti → H2 3
                    applicazioni dell'ozono → H2 4
                    costi degli impianti → H2 11
                    normative specifiche → H2 12
                    progettazione degli impianti → H2 13
                    Regola: questa sezione deve rispondere a “che cos'è il settore?”, non a “come si usa l'ozono nel settore?”.
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non riscrivere il titolo.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
            <ul class="usa-list">
              <li>Unordered list item</li>
              <li>Unordered list item</li>
              <li>Unordered list item</li>
            </ul>
        '''

        html_h2 = f'''<h2 id="section-heading-h2">Prodotti, processi e ambienti della produzione lattiero-casearia</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'prodotti_processi_ambienti'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Prodotti, processi e ambienti della produzione lattiero-casearia
                    Obiettivo: costruire la rappresentazione interna dell'entità: cosa produce, come lo produce e dove avvengono le attività.
                    Target: 700–900 parole
                    Qui hai tre insiemi distinti ma strettamente collegati.
                    Attributi — Prodotti
                    Attributo	Valore da fornire
                    Categorie di prodotto	Latte, formaggi, yogurt, burro, panna, ecc.
                    Tipologie di prodotto	Sottocategorie rilevanti
                    Materia prima	Latte e relative caratteristiche
                    Composizione	Grassi, proteine, lattosio, acqua, ecc.
                    Stato fisico	Liquido, solido, semisolido, polvere
                    Caratteristiche qualitative	Proprietà rilevanti per la lavorazione
                    Conservazione	Refrigerazione, congelamento, ecc.
                    Shelf life	Durata e fattori che la determinano
                    Packaging	Principali modalità di confezionamento
                    Attributi — Processi
                    Attributo	Valore
                    Fasi produttive	Ricevimento, trattamento, trasformazione, confezionamento
                    Processi unitari	Pastorizzazione, omogeneizzazione, separazione, fermentazione, ecc.
                    Input di processo	Materie prime e risorse per ciascun processo
                    Output di processo	Prodotto, sottoprodotti, reflui
                    Sequenza	Ordine delle principali operazioni
                    Condizioni generali	Temperatura, tempo, pressione quando pertinenti
                    Flussi di processo	Movimento di materia e fluidi
                    Punti di transizione	Passaggi critici tra fasi
                    Attributi — Ambienti
                    Attributo	Valore
                    Tipologie di ambiente	Area produttiva, confezionamento, celle, magazzini
                    Aree di lavorazione	Dove avvengono i processi
                    Superfici	Pavimenti, pareti, equipment, superfici di contatto
                    Impianti	Linee, serbatoi, tubazioni, sistemi CIP
                    Aree di stoccaggio	Celle frigorifere, magazzini
                    Aree di servizio	Utilities, trattamento acque, depurazione
                    NON coprire qui
                    quali contaminanti sono presenti → H2 3
                    problemi igienico-sanitari → H2 3
                    come l'ozono tratta queste aree → H2 4
                    meccanismo chimico dell'ozono → H2 5
                    apparecchiature per generare ozono → H2 6
                    Importante: puoi nominare un processo come CIP, ma non spiegare qui la chimica dell'ozono applicata al CIP.
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
        '''

        ################################################################################
        # PRODOTTI
        ################################################################################
        html_heading = f'''<h3 id="section-heading-h2">Prodotti</h3>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'prodotti'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Prodotti del settore lattiero-caseario
                    Target: 100 parole
                    
                    Attributi — Prodotti
                    Attributo	Valore da fornire
                    Categorie di prodotto	Latte, formaggi, yogurt, burro, panna, ecc.
                    Tipologie di prodotto	Sottocategorie rilevanti
                    Materia prima	Latte e relative caratteristiche
                    Composizione	Grassi, proteine, lattosio, acqua, ecc.
                    Stato fisico	Liquido, solido, semisolido, polvere
                    Caratteristiche qualitative	Proprietà rilevanti per la lavorazione
                    Conservazione	Refrigerazione, congelamento, ecc.
                    Shelf life	Durata e fattori che la determinano
                    Packaging	Principali modalità di confezionamento
                    
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_heading}
            {html_p}
        '''

        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'prodotti_lst'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una lista dei prodotti del seguente settore: settore lattiero-caseario.
                    Ogni elemento della lista deve essere separato da una virgola.
                    La lista deve essere MECE.
                    Rispondi solo con la lista.
                    Rispondi in italiano.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_ul = f''''''
        html_ul += f'''<ul>'''
        for item in json_data[key].split(','):
            html_ul += f'''<li>{item}</li>'''
        html_ul += f'''</ul>'''
        html_article += f'''
            <p>Lista prodotti principali:</p>
            {html_ul}
        '''

        ################################################################################
        # PROCESSI
        ################################################################################
        html_heading = f'''<h3 id="section-heading-h2">Processi</h3>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'processi'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Processi del settore lattiero-caseario
                    Target: 100 parole
                    
                    Attributi — Processi
                    Attributo	Valore
                    Fasi produttive	Ricevimento, trattamento, trasformazione, confezionamento
                    Processi unitari	Pastorizzazione, omogeneizzazione, separazione, fermentazione, ecc.
                    Input di processo	Materie prime e risorse per ciascun processo
                    Output di processo	Prodotto, sottoprodotti, reflui
                    Sequenza	Ordine delle principali operazioni
                    Condizioni generali	Temperatura, tempo, pressione quando pertinenti
                    Flussi di processo	Movimento di materia e fluidi
                    Punti di transizione	Passaggi critici tra fasi
                    
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_heading}
            {html_p}
        '''

        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'processi_lst'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una lista dei processi principali del seguente settore: settore lattiero-caseario.
                    Scrivi un solo processo per linea.
                    La lista deve essere MECE.
                    Rispondi solo con la lista.
                    Rispondi in italiano.
                    Rispondi con il minor numero di parole possibili.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_ul = f''''''
        html_ul += f'''<ul>'''
        for item in json_data[key].split('\n'):
            html_ul += f'''<li>{item}</li>'''
        html_ul += f'''</ul>'''
        html_article += f'''
            <p>Lista processi principali:</p>
            {html_ul}
        '''

        ################################################################################
        # AMBIENTI
        ################################################################################
        html_heading = f'''<h3 id="section-heading-h2">Ambienti</h3>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'ambienti'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Ambienti del settore lattiero-caseario
                    Target: 100 parole
                    
                    Attributi
                    Tipologie di ambiente
                    Aree di lavorazione	
                    Superfici	
                    Impianti
                    Aree di stoccaggio	
                    Aree di servizio
                    
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_heading}
            {html_p}
        '''

        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'ambienti_lst'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una lista dei ambienti principali del seguente settore: settore lattiero-caseario.
                    Scrivi un solo ambiente per linea.
                    La lista deve essere MECE.
                    Rispondi solo con la lista.
                    Rispondi in italiano.
                    Rispondi con il minor numero di parole possibili.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_ul = f''''''
        html_ul += f'''<ul>'''
        for item in json_data[key].split('\n'):
            html_ul += f'''<li>{item}</li>'''
        html_ul += f'''</ul>'''
        html_article += f'''
            <p>Lista ambienti principali:</p>
            {html_ul}
        '''

        html_h2 = f'''<h2 id="section-heading-h2">Acqua, contaminanti e criticità igienico-sanitarie</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'acqua'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Acqua, contaminanti e criticità igienico-sanitarie
                    Obiettivo: descrivere ciò che il settore deve controllare. Questa è la sezione che crea il ponte causale verso le applicazioni dell'ozono.
                    Target: 600–800 parole
                    Attributi — Acqua
                    Attributo	Valore
                    Tipologie di acqua	Acqua di processo, lavaggio, servizio, ecc.
                    Fonti	Origine dell'acqua
                    Usi dell'acqua	Produzione, lavaggio, risciacquo, utilities
                    Requisiti qualitativi	Parametri microbiologici/chimici pertinenti
                    Consumo	Dove e perché viene utilizzata
                    Riutilizzo	Possibilità e condizioni
                    Scarichi	Relazione con reflui
                    Attributi — Contaminanti
                    Attributo	Valore
                    Batteri	Classi/specie rilevanti
                    Virus	Se pertinenti
                    Lieviti	Contesti pertinenti
                    Muffe	Contesti pertinenti
                    Spore	Dove rilevanti
                    Biofilm	Presenza, formazione, localizzazione
                    Materia organica	Carico organico
                    Solidi sospesi	Quando rilevanti
                    Composti chimici	Contaminanti pertinenti
                    Odori	Dove costituiscono un problema
                    Carico microbiologico	Misura/concetto pertinente
                    Attributi — Criticità
                    Attributo	Valore
                    Contaminazione	Tipologie
                    Contaminazione crociata	Fonti e percorsi
                    Fouling	Dove e perché
                    Biofilm	Cause e conseguenze
                    Deterioramento microbiologico	Relazione con qualità/shelf life
                    Qualità dell'acqua	Problemi
                    Igiene delle superfici	Necessità
                    Qualità del prodotto	Problemi microbiologici pertinenti
                    Gestione dei reflui	Problemi
                    Rischi igienico-sanitari	Categorie di rischio
                    NON coprire qui
                    efficacia dell'ozono contro ogni contaminante → H2 8
                    meccanismo di ossidazione → H2 5
                    dose necessaria → H2 7
                    sistemi di ozonizzazione → H2 6
                    confronto con PAA/cloro → H2 10
                    Puoi dire “questo contaminante costituisce un target di trattamento”, ma non devi ancora spiegare come trattarlo.
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
        '''

        html_h2 = f'''<h2 id="section-heading-h2">Applicazioni dell'ozono nel settore lattiero-caseario</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'applicazioni'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Applicazioni dell'ozono nel settore lattiero-caseario
                    Obiettivo: è il cuore semantico della pagina. Devi mappare le relazioni O₃ → applicazione → elemento del settore → finalità.
                    Target: 900–1.200 parole
                    Attributi
                    Attributo	Cosa deve contenere
                    Applicazione	Ogni utilizzo documentato dell'ozono
                    Oggetto trattato	Acqua, superfici, ambiente, reflui, ecc.
                    Punto della filiera	Dove avviene l'applicazione
                    Processo associato	Processo lattiero-caseario coinvolto
                    Finalità	Disinfezione, ossidazione, controllo odori, ecc.
                    Target	Microorganismo, composto, biofilm, ecc.
                    Mezzo di trattamento	Acqua, aria, gas, superficie, ecc.
                    Modalità di applicazione	Come viene introdotto l'ozono
                    Risultato atteso	Quale cambiamento si cerca
                    Prerequisiti	Condizioni necessarie
                    Contesto di utilizzo	Industriale, impianto, linea, area
                    Maturità dell'applicazione	Consolidata, sperimentale, emergente
                    Struttura EAV fondamentale
                    Non:
                    “L'ozono è utile nel settore lattiero-caseario.”
                    Ma:
                    Ozone → is used for → water disinfection → in → dairy processing → to control → microorganisms.
                    E poi:
                    Ozone → is applied to → wastewater → to → oxidize/remove → specific contaminants.
                    Questo è molto più vicino a una rappresentazione semantica per entità/predicati.
                    NON coprire qui
                    spiegazione dettagliata della chimica → H2 5
                    specifiche tecniche dell'impianto → H2 6
                    valori di dose/concentrazione → H2 7
                    dati quantitativi di efficacia → H2 8
                    ROI → H2 11
                    Questa sezione deve rispondere a:
                    “Dove si usa l'ozono?”
                    non ancora:
                    “Quanto ozono devo usare?”
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
        '''

        html_h2 = f'''<h2 id="section-heading-h2">Meccanismi d'azione dell'ozono nei processi lattiero-caseari</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'meccanismi'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Meccanismi d'azione dell'ozono nei processi lattiero-caseari
                    Obiettivo: spiegare perché l'applicazione funziona, collegando chimica e microbiologia agli specifici contesti lattiero-caseari.
                    Target: 500–700 parole
                    Attributi
                    Proprietà ossidanti dell'ozono
                    Potenziale ossidativo
                    Decomposizione dell'ozono
                    Specie reattive secondarie
                    Reazioni di ossidazione
                    Inattivazione microbica
                    Danno cellulare
                    Ossidazione di componenti cellulari
                    Interazione con biofilm
                    Ossidazione di composti organici
                    Reazioni con contaminanti
                    Trasferimento gas-liquido
                    Influenza della matrice
                    Influenza del carico organico
                    Influenza della chimica dell'acqua
                    NON coprire
                    valori numerici di dose → H2 7
                    risultati percentuali → H2 8
                    generatori → H2 6
                    sicurezza occupazionale → H2 12
                    confronto con altre tecnologie → H2 10
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
        '''

        html_h2 = f'''<h2 id="section-heading-h2">Sistemi e tecnologie per il trattamento con ozono</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'sistemi'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Sistemi e tecnologie per il trattamento con ozono
                    Obiettivo: descrivere con cosa viene realizzato il trattamento, dalla generazione alla distribuzione, al contatto e alla gestione dell'ozono residuo.
                    Target: 600–800 parole
                    Attributi
                    Generatore di ozono
                    Fonte di ossigeno
                    Preparazione del gas
                    Alimentazione
                    Sistema di iniezione
                    Venturi
                    Diffusori
                    Contattore
                    Reattore
                    Sistema di miscelazione
                    Pompe
                    Tubazioni
                    Valvole
                    Sensori
                    Analizzatori
                    Controllo automatico
                    PLC/automazione
                    Monitoraggio del residuo
                    Sistema di distruzione dell'off-gas
                    Sistemi di sicurezza integrati
                    Materiali costruttivi
                    Configurazioni dell'impianto
                    NON coprire
                    come dimensionare l'impianto → H2 13
                    dose → H2 7
                    costo dell'apparecchiatura → H2 11
                    manutenzione dettagliata → H2 13
                    efficacia → H2 8
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
        '''

        html_h2 = f'''<h2 id="section-heading-h2">Parametri e condizioni di trattamento</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'parametri'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Parametri e condizioni di trattamento
                    Obiettivo: definire le variabili operative che determinano il trattamento.
                    Target: 500–700 parole
                    Attributi
                    Concentrazione di ozono
                    Dose
                    Produzione di ozono
                    Dose trasferita
                    Concentrazione disciolta
                    Tempo di contatto
                    CT
                    Portata
                    Pressione
                    Temperatura
                    pH
                    ORP
                    Carico organico
                    TOC
                    COD
                    BOD
                    Torbidità
                    Alcalinità
                    Composizione dell'acqua
                    Richiesta di ozono
                    Umidità — quando pertinente
                    Rapporto gas/liquido
                    Efficienza di trasferimento
                    Ozone residual
                    NON coprire
                    cosa fa ciascun parametro biologicamente → H2 5
                    risultati ottenibili → H2 8
                    selezione dell'impianto → H2 13
                    sicurezza → H2 12
                    Nota importante: qui non devi inventare un “dosaggio standard per il settore lattiero-caseario”. Il valore EAV deve essere contestualizzato.
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
        '''

        html_h2 = f'''<h2 id="section-heading-h2">Prestazioni, risultati e criteri di efficacia</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'prestazioni'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Prestazioni, risultati e criteri di efficacia
                    Obiettivo: stabilire cosa significa che il trattamento funziona e quali risultati sono stati osservati sotto determinate condizioni.
                    Target: 500–700 parole
                    Attributi
                    Riduzione microbica
                    Log reduction
                    Inattivazione
                    Riduzione del carico organico
                    Rimozione di contaminanti
                    Riduzione degli odori
                    Riduzione del colore
                    Riduzione del biofilm
                    Qualità dell'acqua
                    Qualità microbiologica
                    Qualità del prodotto — solo quando direttamente pertinente
                    Shelf life — solo quando direttamente documentata
                    Efficienza di trattamento
                    Tempo necessario
                    Dose-response
                    Riproducibilità
                    Criteri di accettazione
                    Baseline
                    Risultato post-trattamento
                    Condizioni sperimentali associate al risultato
                    NON coprire
                    perché funziona → H2 5
                    quanto costa → H2 11
                    come progettare l'impianto → H2 13
                    limiti → H2 9
                    Qui devi essere particolarmente disciplinato con l'evidenza: un risultato è sempre associato alle condizioni nelle quali è stato ottenuto.
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
        '''

        html_h2 = f'''<h2 id="section-heading-h2">Limiti e fattori che influenzano l'efficacia dell'ozono</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'limiti'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Limiti e fattori che influenzano l'efficacia dell'ozono
                    Obiettivo: definire quando e perché l'ozono può funzionare meno bene, non essere appropriato o richiedere condizioni particolari.
                    Target: 500–650 parole
                    Attributi
                    Richiesta di ozono
                    Elevato carico organico
                    Torbidità
                    Scarsa penetrazione
                    Limitazioni di trasferimento di massa
                    Miscelazione insufficiente
                    Tempo di contatto insufficiente
                    Dose insufficiente
                    Decomposizione rapida
                    Interferenti chimici
                    Matrice del prodotto
                    Sensibilità del prodotto
                    Materiali incompatibili
                    Recontaminazione
                    Dipendenza dalle condizioni operative
                    By-product potenziali
                    Limiti applicativi
                    Necessità di pretrattamento
                    Necessità di post-trattamento
                    Situazioni in cui l'ozono non è la soluzione ottimale
                    NON coprire
                    Non trasformarla in:
                    “svantaggi dell'ozono” generici
                    sicurezza → H2 12
                    costi → H2 11
                    confronto → H2 10
                    parametri → H2 7
                    Il focus è:
                    Fattore → effetto sul trattamento → conseguenza sull'applicazione.
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
        '''

        html_h2 = f'''<h2 id="section-heading-h2">Ozono e tecnologie alternative</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'alternative'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Ozono e tecnologie alternative
                    Obiettivo: aiutare a comprendere quando l'ozono è un'opzione rispetto ad altre tecnologie.
                    Target: 400–600 parole
                    Attributi
                    Tecnologia alternativa
                    Meccanismo alternativo
                    Applicazione comparabile
                    Target comparabile
                    Efficacia relativa
                    Dose relativa
                    Tempo di contatto relativo
                    Residuo
                    By-product
                    Consumo di sostanze chimiche
                    Consumo energetico
                    Gestione operativa
                    Compatibilità
                    Sicurezza comparativa
                    Impatto ambientale comparativo
                    Adeguatezza applicativa
                    Criterio di scelta
                    Tecnologie da considerare solo se semanticamente concorrenti nell'applicazione specifica:
                    acido peracetico
                    cloro
                    biossido di cloro
                    UV
                    perossido di idrogeno
                    trattamento termico
                    altre tecnologie pertinenti.
                    NON coprire
                    confronto prezzi dettagliato → H2 11
                    progettazione → H2 13
                    spiegazione completa della chimica delle alternative → contenuto dedicato
                    elenco indiscriminato di tutte le tecnologie di trattamento dell'acqua.
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
        '''

        html_h2 = f'''<h2 id="section-heading-h2">Costi, consumi e convenienza economica</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'costi'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Costi, consumi e convenienza economica
                    Obiettivo: tradurre l'applicazione tecnica in modello economico.
                    Target: 350–500 parole
                    Attributi
                    CAPEX
                    OPEX
                    Costo energetico
                    Costo dell'ossigeno
                    Consumo energetico
                    Consumo di acqua
                    Consumo di prodotti chimici
                    Manodopera
                    Manutenzione
                    Ricambi
                    Downtime
                    Costo per m³
                    Costo per batch
                    Costo per unità trattata
                    Costo totale di proprietà
                    Risparmio operativo
                    Payback period
                    ROI
                    Driver economici
                    Variabili che influenzano la redditività
                    NON coprire
                    specifiche tecniche dell'impianto → H2 6
                    dimensionamento → H2 13
                    sicurezza → H2 12
                    performance microbiologica → H2 8
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
        '''

        html_h2 = f'''<h2 id="section-heading-h2">Sicurezza, normativa e standard</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'sicurezza'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Sicurezza, normativa e standard
                    Obiettivo: definire i vincoli legali, normativi, sanitari e di sicurezza che condizionano l'utilizzo dell'ozono nel settore.
                    Target: 500–700 parole
                    Qui terrei rigorosamente separati i valori normativi dalla semplice buona pratica.
                    Attributi — Sicurezza
                    Esposizione occupazionale
                    Limiti di esposizione
                    Concentrazione ambientale
                    Rilevazione delle perdite
                    Ventilazione
                    Distruzione dell'off-gas
                    Interlock
                    Allarmi
                    Monitoraggio
                    Procedure di emergenza
                    Sicurezza dell'impianto
                    Sicurezza del prodotto
                    Gestione del residuo
                    Attributi — Normativa
                    Legislazione
                    Regolamenti
                    Norme
                    Standard tecnici
                    Requisiti alimentari
                    Requisiti microbiologici
                    Requisiti per acqua
                    Requisiti per reflui
                    Requisiti occupazionali
                    Autorizzazioni
                    Certificazioni
                    Validazione normativa
                    Giurisdizione
                    NON coprire
                    progettazione tecnica → H2 13
                    parametri di processo → H2 7
                    performance → H2 8
                    costi di conformità → H2 11
                    Fondamentale: normativa e valori di esposizione devono essere geograficamente contestualizzati. Non creare un valore “universale”.
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
        '''

        html_h2 = f'''<h2 id="section-heading-h2">Progettazione, implementazione e gestione degli impianti a ozono</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'progettazione'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Progettazione, implementazione e gestione degli impianti a ozono
                    Obiettivo: descrivere il percorso che porta dall'esigenza del sito a un sistema funzionante e gestito correttamente.
                    Target: 600–800 parole
                    Attributi
                    Site assessment
                    Analisi dell'applicazione
                    Caratterizzazione del fluido
                    Caratterizzazione del carico
                    Definizione della capacità
                    Sizing
                    Dimensionamento del generatore
                    Dimensionamento del contattore
                    Dimensionamento dell'iniezione
                    Scelta dei materiali
                    Configurazione dell'impianto
                    Integrazione con il processo
                    Installazione
                    Commissioning
                    Avviamento
                    Integrazione con automazione
                    Formazione operatori
                    Manutenzione
                    Ricambi
                    Ottimizzazione
                    Troubleshooting
                    Ciclo di vita dell'impianto
                    NON coprire
                    spiegare cos'è un generatore → H2 6
                    definire i parametri chimici → H2 7
                    risultati → H2 8
                    ROI → H2 11
                    normativa → H2 12
                    Qui la domanda è:
                    “Come si porta l'ozono dall'idea all'operatività in uno stabilimento lattiero-caseario?”
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
        '''

        html_h2 = f'''<h2 id="section-heading-h2">Monitoraggio e validazione dei trattamenti</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'monitoraggio'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Monitoraggio e validazione dei trattamenti
                    Obiettivo: spiegare come si dimostra e mantiene sotto controllo l'efficacia del trattamento.
                    Target: 450–600 parole
                    Attributi
                    Parametro monitorato
                    KPI
                    Punto di misura
                    Metodo di misura
                    Strumento
                    Sensore
                    Campionamento
                    Frequenza di campionamento
                    Baseline
                    Target
                    Limite di accettazione
                    Registrazione dei dati
                    Trend
                    Controllo del processo
                    Verifica
                    Validazione
                    Revalidazione
                    Test microbiologici
                    Test chimici
                    Calibrazione
                    Tracciabilità
                    Documentazione
                    Corrective action
                    NON coprire
                    quali parametri esistono in generale → H2 7
                    risultati pubblicati → H2 8
                    progettazione dell'impianto → H2 13
                    requisiti normativi → H2 12
                    La differenza è sottile ma importante:
                    H2 7: Quali condizioni determinano il trattamento?
                    H2 14: Come controllo che il trattamento stia effettivamente funzionando?
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
        '''

        html_h2 = f'''<h2 id="section-heading-h2">Evidenze scientifiche e sviluppo delle applicazioni</h2>'''
        html_p = f'''<p>{lorem.paragraph()}</p>'''
        ###
        regen = False
        dispel = False
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_dairy.json'
        json_data = io.json_read(json_data_filepath, create=True)
        ###
        key = 'evidenze'
        if key not in json_data: json_data[key] = ''
        if regen: json_data[key] = ''
        if dispel: 
            json_data[key] = ''
            io.json_write(json_data_filepath, json_data)
        if not dispel:
            if json_data[key] == '':
                prompt = f'''
                    Scrivi una sezione di un articolo (documentazione tecnica) sul seguente argomento: {title}.
                    La sezione ha il seguente titolo come H2: Evidenze scientifiche e sviluppo delle applicazioni
                    Obiettivo: stabilire quanto è solida la conoscenza disponibile, distinguendo applicazioni consolidate da risultati sperimentali e aree ancora in sviluppo.
                    Target: 400–600 parole
                    Attributi
                    Studi scientifici
                    Studi di laboratorio
                    Studi pilota
                    Studi industriali
                    Studi sul campo
                    Evidenza disponibile
                    Metodologia
                    Condizioni sperimentali
                    Campione
                    Endpoint
                    Risultati
                    Riproducibilità
                    Limitazioni degli studi
                    Convergenza delle evidenze
                    Contraddizioni tra studi
                    Livello di maturità tecnologica
                    Applicazioni emergenti
                    Aree di ricerca
                    Sviluppi futuri
                    Gap di conoscenza
                    NON coprire
                    ripetere la performance già spiegata → H2 8
                    ripetere i limiti applicativi → H2 9
                    spiegare nuovamente il meccanismo → H2 5
                    fare una bibliografia indiscriminata.
                    Qui la domanda è:
                    “Quanto sappiamo davvero, sulla base delle evidenze disponibili?”
                    Rispondi solo con il contenuto richiesto.
                    Rispondi solo con paragrafi.
                    Non devi mai riscrivere il titolo H2 all inizio della risposta.
                '''
                print(prompt)
                reply = llm.reply(prompt, model_filepath)
                if '</think>' in reply: reply = reply.split('</think>')[1].strip()
                reply = polish.vanilla(reply)
                print()
                print('########################################################################')
                print(reply)
                print('########################################################################')
                print()
                json_data[key] = reply
                io.json_write(json_data_filepath, json_data)
        html_p = f''''''
        for p in json_data[key].split('\n'):
            html_p += f'''<p>{p}</p>'''
        html_article += f'''
            {html_h2}
            {html_p}
        '''

        html_article = f'''
            <h1>{title}</h1>
            <p class="intro">{lorem.words(16)}</p>
            <p>{lorem.paragraph()}</p>
            <h2>Prodotti</h2>
            {json_data['prodotti']}
            {json_data['prodotti_lst']}
            <h2>Processi</h2>
            {json_data['processi']}
            {json_data['processi_lst']}
            <h2>Ambienti</h2>
            {json_data['ambienti']}
            {json_data['ambienti_lst']}
        '''
        html_article_new = f''
        html_toc = f''
        i = 0
        for line in html_article.strip().split('\n'):
            if '<h2>' in line:
                line_toc = line.replace('<h2>', '').replace('</h2>', '')
                line_article = line.replace('<h2', f'<h2 id="{i}"')
                html_toc += f'''<li style="font-weight: 700;"><a href="#{i}">{line_toc}</a></li>\n'''
                html_article_new += f'''{line_article}'''
                i += 1
            else:
                html_article_new += f'''{line}'''
        html_article = html_article_new

        html_body = f'''
<body>
    {components.header_light_logo()}
    <div class="article">
        <div class="grid">
            <nav>
                test
            </nav>
            <main>
                {html_article}
            </main>
            <aside class="toc">
                <h2>Tabella dei contenuti</h2>
                <nav>
                    <ul>
                        {html_toc}
                    </ul>
                </nav>
            </aside>
        </div>
    </div>

  <div class="usa-section">
    <div class="grid-container">
      <div class="grid-row grid-gap">
        <div
          class="usa-layout-docs__sidenav display-none desktop:display-block desktop:grid-col-3"
        >
          <nav aria-label="Secondary navigation">
            <ul class="usa-sidenav">
              <li class="usa-sidenav__item">
                <a href="javascript:void(0);">Parent link</a>
              </li>
              <li class="usa-sidenav__item">
                <a href="javascript:void(0);" class="usa-current"
                  >Current page</a
                >
                <ul class="usa-sidenav__sublist">
                  <li class="usa-sidenav__item">
                    <a href="javascript:void(0);">Child link</a>
                  </li>
                  <li class="usa-sidenav__item">
                    <a href="javascript:void(0);" class="usa-current"
                      >Child link</a
                    >
                    <ul class="usa-sidenav__sublist">
                      <li class="usa-sidenav__item">
                        <a href="javascript:void(0);">Grandchild link</a>
                      </li>
                      <li class="usa-sidenav__item">
                        <a href="javascript:void(0);" class="usa-current"
                          >Grandchild link</a
                        >
                      </li>
                      <li class="usa-sidenav__item">
                        <a href="javascript:void(0);">Grandchild link</a>
                      </li>
                    </ul>
                  </li>
                  <li class="usa-sidenav__item">
                    <a href="javascript:void(0);">Child link</a>
                  </li>
                </ul>
              </li>
              <li class="usa-sidenav__item">
                <a href="javascript:void(0);">Parent link</a>
              </li>
            </ul>
          </nav>
        </div>
        <main class="desktop:grid-col-9 usa-prose" id="main-content">
            {html_h1}
            {html_intro}
            {html_article}
        </main>
      </div>
      <div class="usa-layout-docs__sidenav desktop:display-none">
        <nav aria-label="Secondary navigation">
          <ul class="usa-sidenav">
            <li class="usa-sidenav__item">
              <a href="javascript:void(0);">Parent link</a>
            </li>
            <li class="usa-sidenav__item">
              <a href="javascript:void(0);" class="usa-current">Current page</a>
              <ul class="usa-sidenav__sublist">
                <li class="usa-sidenav__item">
                  <a href="javascript:void(0);">Child link</a>
                </li>
                <li class="usa-sidenav__item">
                  <a href="javascript:void(0);" class="usa-current"
                    >Child link</a
                  >
                  <ul class="usa-sidenav__sublist">
                    <li class="usa-sidenav__item">
                      <a href="javascript:void(0);">Grandchild link</a>
                    </li>
                    <li class="usa-sidenav__item">
                      <a href="javascript:void(0);" class="usa-current"
                        >Grandchild link</a
                      >
                    </li>
                    <li class="usa-sidenav__item">
                      <a href="javascript:void(0);">Grandchild link</a>
                    </li>
                  </ul>
                </li>
                <li class="usa-sidenav__item">
                  <a href="javascript:void(0);">Child link</a>
                </li>
              </ul>
            </li>
            <li class="usa-sidenav__item">
              <a href="javascript:void(0);">Parent link</a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
  <footer class="usa-footer">
    <div class="grid-container usa-footer__return-to-top">
      <a href="#">Return to top</a>
    </div>
    <div class="usa-footer__primary-section">
      <nav class="usa-footer__nav" aria-label="Footer navigation">
        <ul class="grid-row grid-gap">
          <li
            class="mobile-lg:grid-col-4 desktop:grid-col-auto usa-footer__primary-content"
          >
            <a class="usa-footer__primary-link" href="javascript:void(0);"
              >&lt;Primary link&gt;</a
            >
          </li>
          <li
            class="mobile-lg:grid-col-4 desktop:grid-col-auto usa-footer__primary-content"
          >
            <a class="usa-footer__primary-link" href="javascript:void(0);"
              >&lt;Primary link&gt;</a
            >
          </li>
          <li
            class="mobile-lg:grid-col-4 desktop:grid-col-auto usa-footer__primary-content"
          >
            <a class="usa-footer__primary-link" href="javascript:void(0);"
              >&lt;Primary link&gt;</a
            >
          </li>
          <li
            class="mobile-lg:grid-col-4 desktop:grid-col-auto usa-footer__primary-content"
          >
            <a class="usa-footer__primary-link" href="javascript:void(0);"
              >&lt;Primary link&gt;</a
            >
          </li>
        </ul>
      </nav>
    </div>
    <div class="usa-footer__secondary-section">
      <div class="grid-container">
        <div class="grid-row grid-gap">
          <div
            class="usa-footer__logo grid-row mobile-lg:grid-col-6 mobile-lg:grid-gap-2"
          >
            <div class="mobile-lg:grid-col-auto">
              <img
                class="usa-footer__logo-img"
                src="/assets/img/logo-img.png"
                alt=""
              />
            </div>
            <div class="mobile-lg:grid-col-auto">
              <p class="usa-footer__logo-heading">&lt;Name of Agency&gt;</p>
            </div>
          </div>
          <div class="usa-footer__contact-links mobile-lg:grid-col-6">
            <div class="usa-footer__social-links grid-row grid-gap-1">
              <div class="grid-col-auto">
                <a class="usa-social-link" href="javascript:void(0);"
                  ><img
                    class="usa-social-link__icon"
                    src="/assets/img/usa-icons/facebook.svg"
                    alt="Facebook"
                /></a>
              </div>
              <div class="grid-col-auto">
                <a class="usa-social-link" href="javascript:void(0);"
                  ><img
                    class="usa-social-link__icon"
                    src="/assets/img/usa-icons/twitter.svg"
                    alt="Twitter"
                /></a>
              </div>
              <div class="grid-col-auto">
                <a class="usa-social-link" href="javascript:void(0);"
                  ><img
                    class="usa-social-link__icon"
                    src="/assets/img/usa-icons/youtube.svg"
                    alt="YouTube"
                /></a>
              </div>
              <div class="grid-col-auto">
                <a class="usa-social-link" href="javascript:void(0);"
                  ><img
                    class="usa-social-link__icon"
                    src="/assets/img/usa-icons/instagram.svg"
                    alt="Instagram"
                /></a>
              </div>
              <div class="grid-col-auto">
                <a class="usa-social-link" href="javascript:void(0);"
                  ><img
                    class="usa-social-link__icon"
                    src="/assets/img/usa-icons/rss_feed.svg"
                    alt="RSS"
                /></a>
              </div>
            </div>
            <p class="usa-footer__contact-heading">
              &lt;Agency Contact Center&gt;
            </p>
            <address class="usa-footer__address">
              <div class="usa-footer__contact-info grid-row grid-gap">
                <div class="grid-col-auto">
                  <a href="tel:1-800-555-5555">&lt;(800) 555-GOVT&gt;</a>
                </div>
                <div class="grid-col-auto">
                  <a href="mailto:info@agency.gov">&lt;info@agency.gov&gt;</a>
                </div>
              </div>
            </address>
          </div>
        </div>
      </div>
    </div>
  </footer>
  <div class="usa-identifier">
    <section
      class="usa-identifier__section usa-identifier__section--masthead"
      aria-label="Agency identifier"
    >
      <div class="usa-identifier__container">
        <div class="usa-identifier__logos">
          <a href="javascript:void(0)" class="usa-identifier__logo"
            ><img
              class="usa-identifier__logo-img"
              src="/assets/img/circle-gray-20.svg"
              alt="&lt;Parent agency&gt; logo"
              role="img"
          /></a>
        </div>
        <section
          class="usa-identifier__identity"
          aria-label="Agency description"
        >
          <p class="usa-identifier__identity-domain">domain.gov</p>
          <p class="usa-identifier__identity-disclaimer">
            <span aria-hidden="true">An </span>official website of the
            <a href="">&lt;Parent agency&gt;</a>
          </p>
        </section>
      </div>
    </section>
    <nav
      class="usa-identifier__section usa-identifier__section--required-links"
      aria-label="Important links"
    >
      <div class="usa-identifier__container">
        <ul class="usa-identifier__required-links-list">
          <li class="usa-identifier__required-links-item">
            <a
              href="javascript:void(0)"
              class="usa-identifier__required-link usa-link"
              >About &lt;Parent shortname&gt;</a
            >
          </li>
          <li class="usa-identifier__required-links-item">
            <a href="" class="usa-identifier__required-link usa-link"
              >Accessibility support</a
            >
          </li>
          <li class="usa-identifier__required-links-item">
            <a href="" class="usa-identifier__required-link usa-link"
              >FOIA requests</a
            >
          </li>
          <li class="usa-identifier__required-links-item">
            <a href="" class="usa-identifier__required-link usa-link"
              >No FEAR Act data</a
            >
          </li>
          <li class="usa-identifier__required-links-item">
            <a href="" class="usa-identifier__required-link usa-link"
              >Office of the Inspector General</a
            >
          </li>
          <li class="usa-identifier__required-links-item">
            <a href="" class="usa-identifier__required-link usa-link"
              >Performance reports</a
            >
          </li>
          <li class="usa-identifier__required-links-item">
            <a href="" class="usa-identifier__required-link usa-link"
              >Privacy policy</a
            >
          </li>
        </ul>
      </div>
    </nav>
    <section
      class="usa-identifier__section usa-identifier__section--usagov"
      aria-label="U.S. government information and services"
    >
      <div class="usa-identifier__container">
        <div class="usa-identifier__usagov-description">
          Looking for U.S. government information and services?
        </div>
        <a href="https://www.usa.gov/" class="usa-link">Visit USA.gov</a>
      </div>
    </section>
  </div>
</body>
        '''

        '''
                <!-- USWDS initializer -->
                <script src="/assets/uswds/dist/js/uswds-init.min.js"></script>

                <!-- USWDS -->
                <link rel="stylesheet" href="/assets/uswds/dist/css/uswds.min.css">
        '''
        html = f''' 
            <!DOCTYPE html>
            <html lang="it">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>{meta_title}</title>

                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">

                <link rel="stylesheet" href="/styles-custom.css">

            </head>
            {html_body}
            </html>
        '''.strip()

        ###
        html_folderpath = f'{g.website_folderpath}/{url_slug}'
        io.folders_recursive_gen(html_folderpath)
        html_filepath = f'{g.website_folderpath}/{url_slug}/index.html'
        with open(html_filepath, 'w') as f: f.write(html)
        print(html_filepath)
        quit()


'''
        contaminations_items = []
        for input_item in input_data[:]:
            nature_found = False
            ### NATURE
            for contamination_item in contaminations_items:
                if input_item['nature'] in contamination_item['nature']:
                    nature_found = True
                    ### CLASS
                    class_found = False
                    for contamination_class in contamination_item['classes']:
                        if input_item['_class'] == contamination_class['class']:
                            class_found = True
                            break
                    if not class_found:
                        class_item = {
                            'class': input_item['_class'],
                        }
                        contamination_item['classes'].append(class_item)
                    break
            if not nature_found:
                contamination_item = {
                    'nature': input_item['nature'],
                    'classes': [],
                }
                contaminations_items.append(contamination_item)
        # print(json.dumps(contaminations_items, indent=4))
        # quit()
'''

def contaminations_groups_gen(json_data_filepath):
    json_data = io.json_read(json_data_filepath)
    contaminations_items = [
        {
            "nature": "Biological",
            "classes": [
                {
                    "class": "Bacterium",
                    "entities": [],
                },
                {
                    "class": "Fungus",
                    "entities": [],
                },
                {
                    "class": "Parasite",
                    "entities": [],
                },
                {
                    "class": "Virus",
                    "entities": [],
                },
                {
                    "class": "Microbial Community",
                    "entities": [],
                },
            ]
        }
    ]
    input_data = json_data['contaminants']
    for input_item in input_data:
        nature = input_item['nature']
        _class = input_item['_class']
        entity = input_item['entity']
        if entity == 'NONE': continue
        for nature_item in contaminations_items:
            if nature_item['nature'] == nature:
                for class_item in nature_item['classes']:
                    if class_item['class'] == _class:
                        found = False
                        for entity_name in class_item['entities']:
                            if entity_name == entity:
                                found = True
                                break
                        if not found:
                            class_item['entities'].append(entity)
    return contaminations_items

def contaminations_biological_bacterium_content_llm(context_data, regen=False):
    json_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_food.json'
    json_data = io.json_read(json_filepath, create=True)
    key = 'contaminations_biological_bacterium_content_llm'
    if key not in json_data: json_data[key] = ''
    if regen: json_data[key] = ''
    if json_data[key] == '':
        prompt = f'''
            Write a paragraph for an article about: ozone in the food industry.
            The paragraph is about "bacterium contamination".
            Use the following CONTEXT data to write the paragraph:
            {context_data}
            OUTPUT STURCTURE:
            Start by explaining what are the most important contaminats in the food industry.
            Then explain why they are a problem.
            RULES:
            Use line breaks when appropriate.
            Mention the bacterium in the first sentence.
            Use a simple, technical, straightforward, professional language.
            You must absolutely answer in Italian.
        '''.strip()
        print(prompt)
        reply = llm.reply(prompt, model_filepath)
        if '</think>' in reply: reply = reply.split('</think>')[1].strip()
        reply = polish.vanilla(reply)
        print()
        print('########################################################################')
        print(reply)
        print('########################################################################')
        print()
        json_data[key] = reply
        io.json_write(json_filepath, json_data)
    return json_data

"""
                contamination_table_html = f'''
                    <table>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Function</th>
                                <th>Industries</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Bacillus cereus</td>
                                <td>Bacillus cereus</td>
                                <td>Bacillus cereus</td>
                            </tr>
                            <tr>
                                <td>Bacillus spp.</td>
                                <td>Bacillus spp.</td>
                                <td>Bacillus spp.</td>
                            </tr>
                            <tr>
                                <td>Bacillus stearothermophilus</td>
                                <td>Bacillus stearothermophilus</td>
                                <td>Bacillus stearothermophilus</td>
                            </tr>
                            <tr>
                                <td>Listeria monocytogenes</td>
                                <td>Listeria monocytogenes</td>
                                <td>Listeria monocytogenes</td>
                            </tr>
                            <tr>
                                <td>Pseudomonas fluorescens</td>
                                <td>Pseudomonas fluorescens</td>
                                <td>Pseudomonas fluorescens</td>
                            </tr>
                        </tbody>
                    </table>
                '''
                # for contamination_entity in sorted(contamination_class['entities'][:5]):
                    # contaminations_html += f'''<p>{contamination_entity}</p>'''
                # contaminations_html += contamination_table_html
"""

def contaminations_biological_content_llm(context_data, regen=False):
    json_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_food.json'
    json_data = io.json_read(json_filepath, create=True)
    key = 'contaminations_biological_content_llm'
    if key not in json_data: json_data[key] = ''
    if regen: json_data[key] = ''
    if json_data[key] == '':
        prompt = f'''
            Write a paragraph for an article about: ozone in the food industry.
            The paragraph is about "biological contamination".
            Use the following CONTEXT data to write the paragraph:
            {context_data}
            OUTPUT STURCTURE:
            Start by explaining what are the most important biological contaminats in the food industry.
            Then explain why they are a problem.
            RULES:
            Use line breaks when appropriate.
            Mention the bacterium in the first sentence.
            Use a simple, technical, straightforward, professional language.
            You must absolutely answer in Italian.
        '''.strip()
        print(prompt)
        reply = llm.reply(prompt, model_filepath)
        if '</think>' in reply: reply = reply.split('</think>')[1].strip()
        reply = polish.vanilla(reply)
        print()
        print('########################################################################')
        print(reply)
        print('########################################################################')
        print()
        json_data[key] = reply
        io.json_write(json_filepath, json_data)
    return json_data

def section_intro_llm(regen=False):
    json_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_food.json'
    json_data = io.json_read(json_filepath)
    key = 'section_intro_llm'
    if key not in json_data: json_data[key] = ''
    if regen: json_data[key] = ''
    if json_data[key] == '':
        Sector = 'settore alimentare'
        prompt = f'''
You are an expert technical writer and semantic SEO content architect.
## Context
This page is about the use of ozone in the {Sector}. It is part of a larger topical knowledge base about ozone and belongs to the website's sector-level architecture.
The introduction is the semantic entry point to the page. Its primary function is to establish the relationship between the entity "Ozone" and the entity "{Sector}", define the scope of the page, and prepare the reader for the sections that follow.
The introduction must complement the rest of the page rather than duplicate it.
## Objective
Write a concise, information-dense introduction explaining the role of ozone within {Sector}.
The reader should immediately understand:
- what {Sector} is in relation to ozone
- why ozone is relevant to this sector
- the broad categories of activities or problems in which ozone is relevant
- what the page covers
Do not attempt to comprehensively explain the applications, mechanisms, benefits, operational considerations, safety, regulations, limitations, or related applications. Those topics are developed in the body of the page.
## Semantic Role
Establish the primary contextual relationship:
Ozone → is used within → {Sector}
Then establish the broader topical relationships:
{Sector} → contains → processes, environments, and activities relevant to ozone
Ozone → addresses → sector-specific needs
Ozone → is applied across → relevant stages or functions of the sector
The introduction should establish these relationships at a high level without expanding them into detailed explanations.
## Information Architecture
The introduction should naturally prepare the reader for the page's major information dimensions:
- the role of ozone in {Sector}
- applications of ozone
- mechanisms by which ozone acts
- benefits and outcomes
- operational considerations
- safety, regulations, and limitations
- related ozone applications
Mention these dimensions only as needed to establish scope. Do not mechanically reproduce the section titles as a list.
## Scope
Describe {Sector} specifically in the context of ozone.
Focus on the intersection:
Ozone × {Sector}
Do not write a generic introduction to ozone.
Do not write a generic introduction to {Sector}.
Every substantive statement should help establish why the intersection of these two entities is meaningful.
## Exclusions
DO NOT:
- provide a detailed definition of ozone
- provide a history of ozone
- provide a history of ozone use in {Sector}
- list specific applications
- describe individual subsectors in detail
- explain scientific mechanisms
- explain oxidation chemistry
- make detailed benefit claims
- provide operating parameters
- discuss equipment
- discuss safety procedures
- discuss regulations
- discuss limitations in detail
- compare ozone with competing technologies
- provide statistics unless they are essential and verified
- make unsupported claims
- repeat information that belongs to the body sections
- include a conclusion
## Writing Style
- Write for technically informed readers, industry professionals, and decision makers.
- Use authoritative, precise, neutral language.
- Avoid promotional language such as "revolutionary", "powerful solution", "game-changing", or "best".
- Avoid generic SEO filler.
- Avoid rhetorical questions.
- Avoid unnecessary background information.
- Prefer concrete terminology over vague statements.
- Introduce the topic directly.
- Keep the introduction concise and information-dense.
## Semantic SEO Requirements
Use "Ozone" as the primary entity and "{Sector}" as the contextual entity.
Naturally establish relevant attributes and relationships without keyword stuffing.
Use terminology that is genuinely characteristic of {Sector}.
Do not force semantic entities into the text merely because they are associated with ozone.
Prioritize information gain: every sentence should either define the topic, establish an important relationship, clarify scope, or orient the reader toward the page's information architecture.
## Paragraph Structure
Write 2–4 paragraphs.
Paragraph 1: Directly establish what the use of ozone in {Sector} means and why the relationship is relevant.
Paragraph 2: Explain the broad sector needs, processes, or conditions that create a role for ozone, without discussing individual applications in detail.
Paragraph 3: Where useful, establish the breadth of the page by indicating that ozone's role can be examined through its applications, mechanisms, outcomes, operational requirements, and constraints.
Use paragraph 3 only if it adds genuine information; do not add it merely to reach a word count.
## Length
Aim for approximately 120–200 words.
Prioritize semantic completeness and information density over length.
Do not exceed 250 words unless the complexity of {Sector} genuinely requires additional context.
## Accuracy
Make only claims that are broadly established and defensible.
Do not imply that ozone is universally used throughout {Sector}.
Distinguish between established uses and potential uses when relevant.
Do not imply regulatory approval, safety, efficacy, or superiority without appropriate context.
## Final Quality Check
Before producing the output, verify:
1. The introduction clearly establishes Ozone × {Sector}.
2. The introduction explains why the relationship matters.
3. The introduction defines the page's scope.
4. No major body section is unnecessarily reproduced.
5. No application is explained in detail.
6. No mechanism is explained in detail.
7. No benefit, regulation, safety issue, or limitation is developed beyond introductory context.
8. Every paragraph provides distinct information.
9. The introduction could stand alone as an accurate description of what the page covers.
## Output
Return only the finished introduction in Markdown.
Use paragraphs only.
Do not use bullet points.
Do not use numbered lists.
Do not use tables.
Do not use H2 or H3 headings.
Do not add a conclusion.
Reply only with paragraphs. Never use lists.
Reply only in Italian.
        '''.strip()
        print(prompt)
        reply = llm.reply(prompt, model_filepath)
        if '</think>' in reply: reply = reply.split('</think>')[1].strip()
        reply = polish.vanilla(reply)
        print()
        print('########################################################################')
        print(reply)
        print('########################################################################')
        print()
        json_data[key] = reply
        io.json_write(json_filepath, json_data)
    return json_data

def section_role_llm(regen=False):
    json_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_food.json'
    json_data = io.json_read(json_filepath, create=True)
    key = 'section_role_llm'
    if key not in json_data: json_data[key] = ''
    if regen: json_data[key] = ''
    if json_data[key] == '':
        Sector = 'settore alimentare'
        prompt = f'''
You are an expert technical writer and semantic SEO content architect.
## Context
This page is about the use of ozone in the {Sector}. It belongs to a larger knowledge base about ozone.
This section is ONLY responsible for explaining the overall role of ozone within this sector. It establishes the relationship between the entity "Ozone" and the entity "{Sector}" before discussing specific applications.
This section must serve as the conceptual foundation for the rest of the page.
---
## Objective
Explain WHY ozone is used in the {Sector}.
Do NOT explain HOW it is used in specific applications, operational procedures, regulations, equipment, or safety. Those are covered in later sections.
The reader should finish this section understanding:
- why ozone has value in this sector
- what industry challenges it addresses
- what objectives organizations aim to achieve by using ozone
- why ozone is selected instead of, or alongside, conventional treatment methods
---
## Cover ONLY these topics
### 1. Purpose
Explain the overall purpose of ozone in this sector.
Examples:
- sanitation
- preservation
- oxidation
- water treatment
- air treatment
- process optimization
- quality improvement
Only include purposes that are genuinely relevant to this sector.
---
### 2. Industry Challenges
Describe the problems that create the need for ozone.
Examples:
- microbial contamination
- odors
- organic pollutants
- biofilms
- product degradation
- process efficiency
- environmental impact
- regulatory pressure
Do not explain the solutions in detail.
---
### 3. Primary Objectives
Explain what organizations hope to achieve by adopting ozone.
Examples:
- improve hygiene
- extend product quality
- reduce chemical usage
- improve sustainability
- increase operational efficiency
- improve water reuse
- improve product safety
Focus on objectives, not implementation.
---
### 4. Why Ozone
Explain the characteristics of ozone that make it suitable.
Examples:
- strong oxidizing agent
- broad antimicrobial activity
- decomposes back into oxygen
- residue-free
- generated on-site
- compatible with automated processes
Explain these only at a high level.
---
## Exclusions
DO NOT discuss:
- specific applications
- subsectors
- process workflows
- equipment
- generators
- gaseous ozone
- ozonated water
- concentrations
- contact time
- operating parameters
- regulations
- standards
- worker safety
- limitations
- costs
- comparisons with chlorine or other technologies
These belong to later sections.
---
## Writing Style
- Write for technical professionals and decision makers.
- Use clear, authoritative language.
- Be factual and objective.
- Avoid marketing language.
- Avoid repeating ideas.
- Avoid unnecessary history.
- Prefer concise paragraphs.
- Define terms only when necessary.
- Introduce concepts before mentioning related entities.
---
## Semantic SEO Requirements
Use the entity "{Sector}" as the contextual anchor.
Maintain a clear relationship between:
Ozone → solves → Sector challenges
Ozone → enables → Sector objectives
Ozone → provides → Sector value
Avoid introducing unrelated entities.
---
## Output
Produce:
- an introductory paragraph
- a subsection titled "Purpose of Ozone in the {Sector}"
- a subsection titled "Industry Challenges"
- a subsection titled "Primary Objectives"
- a subsection titled "Why Ozone is Used"
Do not generate any conclusion.
Return only Markdown.
Reply only with paragraphs. Never use lists.
Reply only in Italian.
        '''.strip()
        print(prompt)
        reply = llm.reply(prompt, model_filepath)
        if '</think>' in reply: reply = reply.split('</think>')[1].strip()
        reply = polish.vanilla(reply)
        print()
        print('########################################################################')
        print(reply)
        print('########################################################################')
        print()
        json_data[key] = reply
        io.json_write(json_filepath, json_data)
    return json_data

def section_applications_llm(regen=False):
    json_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_food.json'
    json_data = io.json_read(json_filepath, create=True)
    key = 'section_applications_llm'
    if key not in json_data: json_data[key] = ''
    if regen: json_data[key] = ''
    if json_data[key] == '':
        Sector = 'settore alimentare'
        prompt = f'''
You are an expert technical writer and semantic SEO content architect.
## Context
This page is about the use of ozone in the {Sector}. It belongs to a larger knowledge base about ozone.
This section is ONLY responsible for explaining WHERE and FOR WHAT PURPOSE ozone is applied within the {Sector}. Section 1 already explains the overall role of ozone in the sector. Later sections explain mechanisms, benefits and outcomes, operational considerations, safety, regulations, limitations, and related ozone applications.
The purpose of this section is to build a comprehensive semantic inventory of the distinct applications of ozone within {Sector}.
## Objective
Identify and explain the major applications of ozone across the entire {Sector}.
The reader should finish this section understanding:
- where ozone is used
- what ozone is used for in each context
- what is being treated, controlled, processed, or affected
- where each application occurs within the sector's value chain or operational environment
Do not explain in depth why ozone works, how ozone works, what benefits it produces, how to implement it, or what regulations govern it.
## Coverage Requirement
Before writing, mentally map the complete {Sector} value chain and operational ecosystem.
Consider, where relevant:
- raw materials and inputs
- production and processing
- intermediate processes
- sanitation and hygiene
- water
- air and environmental treatment
- equipment and facility treatment
- storage
- preservation
- packaging
- transportation
- waste and wastewater
- quality control
- specialized and emerging uses
Then identify the distinct ozone applications that occur across these areas.
Do not assume every category applies to {Sector}. Include only genuinely relevant applications.
## MECE Requirement
Applications must be mutually exclusive and collectively exhaustive.
Mutually exclusive means that two applications must not represent the same underlying use case expressed with different wording.
Collectively exhaustive means that the set of applications should cover the meaningful ozone use cases across {Sector}, including important upstream, downstream, facility-level, process-level, and specialized applications where they genuinely exist.
Choose the correct level of abstraction. Do not create separate applications merely because the same application is performed on different products unless the treatment context, objective, or process is materially different.
Conversely, do not combine distinct applications merely because they use the same ozone delivery method.
For example, "ozonated water" is generally a treatment medium or delivery method, not automatically an application. Determine what the ozone is actually being used to accomplish before defining the application.
## Application Definition
Treat an application as a distinct use of ozone characterized by a specific sector context, purpose, and target.
For each application, establish:
Application → occurs in → Sector context
Application → serves → Purpose
Application → targets → Target
Application → occurs during → Process or stage
Avoid creating applications based only on equipment, ozone form, concentration, or technology.
## Application Selection
Prioritize applications according to:
1. Established and significant uses
2. Common industrial uses
3. Sector-specific uses
4. Important specialized uses
5. Emerging uses, only when sufficiently relevant and established
Do not include speculative, fringe, or hypothetical uses merely to increase topical breadth.
## For Each Application
Explain the application in paragraph form.
The paragraph or paragraphs should naturally establish:
- what the application is
- where it occurs
- what ozone is intended to accomplish
- what the treatment target is
- what process or stage it belongs to
Do not turn these into labels such as "Purpose:", "Target:", or "Context:". Integrate the information naturally into prose.
## Appropriate Depth
Give major applications enough explanation to establish their semantic relationship with ozone and {Sector}, but do not turn this section into a detailed guide.
Use approximately 1–3 paragraphs per major application depending on its importance and complexity.
Give closely related minor applications shorter treatment when appropriate.
Do not artificially make every application the same length.
## Exclusions
DO NOT discuss:
- detailed scientific mechanisms
- oxidation chemistry
- microbial inactivation mechanisms
- detailed benefits or outcomes
- economic benefits
- environmental benefits
- operating parameters
- concentration
- dosage
- contact time
- temperature
- humidity
- flow rate
- monitoring procedures
- automation
- equipment specifications
- generator sizing
- installation
- worker safety
- exposure limits
- regulations
- standards
- detailed limitations
- comparisons with chlorine, hydrogen peroxide, UV, or other technologies
- step-by-step implementation
These topics belong to other sections or dedicated pages.
You may mention a technical term briefly when necessary to identify an application, but do not develop that topic.
## Avoiding Semantic Redundancy
Do not repeat the same application under multiple names.
Do not repeat information that belongs to Section 1.
Do not explain the same mechanism repeatedly for different applications.
Do not repeat benefits in every application.
Do not turn every possible target into a separate application.
Do not confuse:
- application with mechanism
- application with benefit
- application with equipment
- application with delivery method
- application with operational parameter
- application with regulation
If several applications share the same mechanism or technology, keep them separate only when their sector context and purpose are materially different.
## Information Architecture
Organize applications in the most logical order for {Sector}.
Prefer a progression through the sector value chain:
upstream → processing → sanitation/treatment → storage → distribution → downstream
When a value-chain structure is unsuitable, use the most natural functional or process-based order.
Do not organize alphabetically unless there is a strong semantic reason.
## Semantic SEO Requirements
Use "Ozone" as the primary entity and "{Sector}" as the contextual entity.
Build explicit but natural entity relationships:
Ozone → is used in → Application
Application → occurs in → Sector process/context
Application → targets → Target
Application → serves → Purpose
Application → belongs to → Sector stage
Prioritize entities and relationships that provide genuine information gain.
Use precise sector terminology and distinguish synonymous terms where they represent different concepts.
Do not insert keywords unnaturally.
Do not optimize for keyword density.
## Completeness Check
Before producing the final output, verify that the application inventory covers the meaningful ozone use cases across {Sector}.
Check for:
- upstream uses
- core production/processing uses
- sanitation/hygiene uses
- water-related uses
- air/environmental uses
- facility/equipment-related uses
- storage/preservation uses
- packaging-related uses
- waste/wastewater uses
- specialized sector-specific uses
Only include categories that genuinely exist within {Sector}.
If an important application is missing, add it.
If two applications overlap, merge or redefine them.
## Output
Produce a short introductory paragraph followed by the application sections.
Use H3 headings for major application categories.
Under each application heading, write 1–3 paragraphs of continuous prose.
The output must consist of paragraphs, headings, and normal inline formatting only.
Do not use bullet points.
Do not use numbered lists.
Do not use tables.
Do not use key-value labels.
Do not provide a conclusion.
Do not add a separate list of applications before explaining them.
Return only Markdown.
Reply using only paragraphs.
Give each application a heading ### with the name of the application.
Reply only in Italian.
        '''.strip()
        print(prompt)
        reply = llm.reply(prompt, model_filepath)
        if '</think>' in reply: reply = reply.split('</think>')[1].strip()
        reply = polish.vanilla(reply)
        print()
        print('########################################################################')
        print(reply)
        print('########################################################################')
        print()
        json_data[key] = reply
        io.json_write(json_filepath, json_data)
    return json_data

def section_mechanisms_llm(regen=False):
    json_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_food.json'
    json_data = io.json_read(json_filepath, create=True)
    key = 'section_mechanisms_llm'
    if key not in json_data: json_data[key] = ''
    if regen: json_data[key] = ''
    if json_data[key] == '':
        Sector = 'settore alimentare'
        prompt = f'''
You are an expert technical writer and semantic SEO content architect.
## Context
This page is about the use of ozone in the {Sector}. It belongs to a larger knowledge base about ozone.
This section is ONLY responsible for explaining HOW ozone acts within the {Sector}. It explains the scientific and technical mechanisms that make ozone effective, independent of any specific application.
The previous section explained where ozone is used. This section explains how ozone works. Later sections will explain benefits, operational considerations, safety, regulations, and limitations.
## Objective
Explain the fundamental mechanisms by which ozone performs its functions within the {Sector}.
The reader should finish this section understanding:
- the fundamental physical, chemical, and biological mechanisms of ozone
- how these mechanisms enable ozone's use across different applications
- which sector processes rely on each mechanism
Do NOT explain specific applications, operational procedures, equipment, regulations, or benefits in detail.
## Scope
Identify every major mechanism that is relevant to ozone in the {Sector}. Include only mechanisms that directly contribute to ozone's role within this sector.
Typical mechanisms may include, where relevant:
- Oxidation
- Microbial inactivation
- Organic compound degradation
- Biofilm disruption
- Odor compound oxidation
- VOC oxidation
- Ethylene oxidation
- Color removal
- Oxidation of inorganic compounds
- Advanced oxidation reactions
Only include mechanisms that genuinely apply to the selected sector.
## For each mechanism, explain:
### What the mechanism is
Provide a concise technical explanation.
### How ozone performs this mechanism
Explain the scientific process without excessive chemistry.
### Relevance to the sector
Briefly explain why this mechanism is important within the {Sector}.
Do not describe specific implementations or applications beyond what is necessary to establish context.
## Exclusions
DO NOT discuss:
- specific applications
- subsectors
- process workflows
- equipment
- ozone generators
- gaseous versus aqueous ozone
- concentrations
- contact time
- operating parameters
- monitoring
- automation
- safety
- regulations
- limitations
- costs
- implementation guidance
- detailed operational benefits
These belong to later sections.
## Writing Style
- Write for technical professionals and decision makers.
- Be technically accurate.
- Use clear, authoritative language.
- Avoid marketing language.
- Avoid unnecessary chemistry or academic detail.
- Avoid repeating concepts between mechanisms.
- Introduce mechanisms from the most fundamental to the most specialized.
- Keep each mechanism conceptually independent.
## Semantic SEO Requirements
Use the entity "{Sector}" as the contextual anchor.
Use "Ozone" as the primary entity.
Model the relationships as:
Ozone → performs → Mechanism
Mechanism → affects → Target
Mechanism → enables → Sector process
Avoid describing outcomes, advantages, or implementation details except where necessary to explain the mechanism.
Ensure each mechanism represents a unique concept without overlapping another mechanism.
## Output
Produce:
- a short introductory paragraph
- one H3 subsection for each major mechanism
Each subsection must consist of 2–4 well-structured paragraphs that naturally explain the mechanism from definition to sector relevance. Do not use bullet points, numbered lists, tables, or key-value labels. Write entirely in paragraph form.
Do not generate a conclusion.
Return only Markdown.
Reply using only paragraphs.
Reply only in Italian.
        '''.strip()
        print(prompt)
        reply = llm.reply(prompt, model_filepath)
        if '</think>' in reply: reply = reply.split('</think>')[1].strip()
        reply = polish.vanilla(reply)
        print()
        print('########################################################################')
        print(reply)
        print('########################################################################')
        print()
        json_data[key] = reply
        io.json_write(json_filepath, json_data)
    return json_data

def section_benefits_llm(regen=False):
    json_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_food.json'
    json_data = io.json_read(json_filepath, create=True)
    key = 'section_benefits_llm'
    if key not in json_data: json_data[key] = ''
    if regen: json_data[key] = ''
    if json_data[key] == '':
        Sector = 'settore alimentare'
        prompt = f'''
You are an expert technical writer and semantic SEO content architect.
## Context
This page is about the use of ozone in the {Sector}. It belongs to a larger knowledge base about ozone.
This section is ONLY responsible for explaining the benefits and outcomes achieved through the use of ozone within the {Sector}. Previous sections explained why ozone is used, where it is applied, and how it works. This section explains the results organizations seek and obtain from adopting ozone. Later sections will cover operational considerations, safety, regulations, limitations, and related topics.
## Objective
Explain the operational, quality, environmental, economic, and compliance outcomes associated with the use of ozone in the {Sector}.
The reader should finish this section understanding:
- what improvements ozone can deliver
- how those improvements affect sector performance
- why organizations value ozone beyond its technical mechanisms
Focus on outcomes rather than implementation or scientific explanation.
## Scope
Organize the section into the major categories of benefits that are relevant to the {Sector}. Include only categories that genuinely apply.
Typical categories may include:
- Operational benefits
- Product or service quality improvements
- Environmental benefits
- Economic benefits
- Compliance and food/product safety benefits
- Sustainability benefits
- Resource efficiency benefits
- Process reliability benefits
Adapt the categories to the selected sector instead of forcing irrelevant ones.
## For each benefit category, explain:
### What the benefit is
Define the improvement in clear technical language.
### Why it matters
Explain why this outcome is valuable for organizations operating within the {Sector}.
### Typical impact
Describe the general operational or business impact without making unsupported quantitative claims.
Keep the discussion at a strategic level rather than describing specific applications or technologies.
## Exclusions
DO NOT discuss:
- specific applications
- scientific mechanisms
- oxidation chemistry
- microbial inactivation processes
- equipment
- ozone generators
- operating parameters
- concentrations
- contact time
- monitoring
- automation
- implementation procedures
- regulations in detail
- safety practices
- limitations
- disadvantages
- comparisons with competing technologies
These belong to other sections.
## Writing Style
- Write for technical professionals and decision makers.
- Be factual, balanced, and objective.
- Avoid promotional or exaggerated language.
- Do not guarantee outcomes.
- Explain benefits as typical or potential results depending on implementation.
- Avoid repeating the same idea across multiple categories.
- Progress from operational outcomes to broader organizational outcomes.
- Keep each category conceptually independent.
## Semantic SEO Requirements
Use the entity "{Sector}" as the contextual anchor.
Use "Ozone" as the primary entity.
Model the relationships as:
Ozone → produces → Outcome
Outcome → improves → Sector objective
Outcome → creates → Organizational value
Ensure every benefit represents a unique outcome rather than a mechanism or an application.
Avoid overlapping categories and avoid introducing concepts that belong in later sections.
## Output
Produce:
- a short introductory paragraph
- one H3 subsection for each major benefit category
Each subsection must consist of 2–4 well-structured paragraphs that explain the benefit category, its importance, and its broader impact within the {Sector}. Do not use bullet points, numbered lists, tables, or key-value labels. Write entirely in paragraph form.
Do not generate a conclusion.
Return only Markdown.
Return only Markdown.
Reply using only paragraphs.
Reply only in Italian.
        '''.strip()
        print(prompt)
        reply = llm.reply(prompt, model_filepath)
        if '</think>' in reply: reply = reply.split('</think>')[1].strip()
        reply = polish.vanilla(reply)
        print()
        print('########################################################################')
        print(reply)
        print('########################################################################')
        print()
        json_data[key] = reply
        io.json_write(json_filepath, json_data)
    return json_data

def section_considerations_llm(regen=False):
    json_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_food.json'
    json_data = io.json_read(json_filepath, create=True)
    key = 'section_considerations_llm'
    if key not in json_data: json_data[key] = ''
    if regen: json_data[key] = ''
    if json_data[key] == '':
        Sector = 'settore alimentare'
        prompt = f'''
You are an expert technical writer and semantic SEO content architect.
## Context
This page is about the use of ozone in the {Sector}. It belongs to a larger knowledge base about ozone.
This section is ONLY responsible for explaining the operational considerations that influence the successful use of ozone within the {Sector}. Previous sections explained why ozone is used, where it is applied, how it works, and the outcomes it can deliver. This section explains the practical factors that determine whether ozone performs effectively in real-world operations. Later sections will cover safety, regulations, limitations, and related topics.
## Objective
Explain the technical and operational factors that influence ozone performance within the {Sector}.
The reader should finish this section understanding:
- which operating conditions affect ozone performance
- why these factors must be controlled
- how organizations optimize ozone use at a high level
Focus on operational principles rather than implementation procedures.
## Scope
Identify the major operational considerations that are relevant to ozone in the {Sector}. Include only factors that genuinely influence ozone performance within this sector.
Typical considerations may include:
- Ozone delivery medium (gas or water, where relevant)
- Ozone concentration
- Contact time
- Temperature
- Humidity
- Water quality
- Organic load
- pH
- Flow rate
- Mixing efficiency
- Mass transfer
- Exposure conditions
- Process consistency
- Monitoring and verification
- System maintenance
- Automation and process control
Adapt the topics to the selected sector and exclude factors that are not applicable.
## For each operational consideration, explain:
### What the factor is
Provide a concise technical explanation.
### Why it influences ozone performance
Explain the relationship between the factor and ozone effectiveness.
### Operational importance
Describe why organizations monitor or control this factor without providing procedural instructions or implementation guidance.
## Exclusions
DO NOT discuss:
- specific applications
- scientific mechanisms in detail
- oxidation chemistry
- benefits
- business outcomes
- equipment specifications
- ozone generator design
- installation procedures
- safety practices
- worker exposure
- regulations
- legal requirements
- limitations unrelated to operation
- comparisons with competing technologies
- step-by-step operating instructions
These belong to other sections.
## Writing Style
- Write for technical professionals and decision makers.
- Be technically accurate and objective.
- Use clear, concise language.
- Avoid marketing language.
- Avoid excessive engineering detail.
- Avoid repeating concepts across operational factors.
- Present the factors from the most fundamental to the more specialized where appropriate.
- Keep each operational consideration conceptually independent.
## Semantic SEO Requirements
Use the entity "{Sector}" as the contextual anchor.
Use "Ozone" as the primary entity.
Model the relationships as:
Operational factor → influences → Ozone performance
Ozone performance → affects → Process effectiveness
Operational factor → requires → Operational control
Ensure each operational consideration represents a unique influencing factor rather than a mechanism, application, benefit, or limitation.
Avoid overlap between factors whenever possible.
## Output
Produce:
- a short introductory paragraph
- one H3 subsection for each major operational consideration
Each subsection must consist of 2–4 well-structured paragraphs that explain the factor, why it matters, and its influence on ozone performance within the {Sector}. Do not use bullet points, numbered lists, tables, or key-value labels. Write entirely in paragraph form.
Do not generate a conclusion.
Return only Markdown.
Reply using only paragraphs.
Reply only in Italian.
        '''.strip()
        print(prompt)
        reply = llm.reply(prompt, model_filepath)
        if '</think>' in reply: reply = reply.split('</think>')[1].strip()
        reply = polish.vanilla(reply)
        print()
        print('########################################################################')
        print(reply)
        print('########################################################################')
        print()
        json_data[key] = reply
        io.json_write(json_filepath, json_data)
    return json_data

def section_safety_llm(regen=False):
    json_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_food.json'
    json_data = io.json_read(json_filepath, create=True)
    key = 'section_safety_llm'
    if key not in json_data: json_data[key] = ''
    if regen: json_data[key] = ''
    if json_data[key] == '':
        Sector = 'settore alimentare'
        prompt = f'''
You are an expert technical writer and semantic SEO content architect.
## Context
This page is about the use of ozone in the {Sector}. It belongs to a larger knowledge base about ozone.
This section is ONLY responsible for explaining the constraints surrounding the use of ozone within the {Sector}. It combines three distinct but related dimensions: safety, regulatory requirements, and technical or practical limitations.
Previous sections explained why ozone is used, where it is applied, how it works, the outcomes it can provide, and the operational factors that influence its performance. This section explains what must be considered to use ozone responsibly and within applicable requirements.
The three dimensions MUST remain conceptually distinct:
- Safety = protecting people, facilities, products, and the surrounding environment from hazards associated with ozone.
- Regulations = laws, standards, approvals, codes, guidelines, and compliance requirements governing ozone use.
- Limitations = technical, practical, material, process, economic, or performance constraints that can restrict ozone use or affect its suitability.
Do not merge these dimensions.
## Objective
Provide a comprehensive but concise explanation of the safety considerations, regulatory landscape, and practical limitations associated with ozone in the {Sector}.
The reader should finish this section understanding:
- what hazards and safety considerations are relevant
- what regulatory and standards framework governs or influences ozone use
- what limitations may affect the suitability or effectiveness of ozone
- which considerations require sector-specific or jurisdiction-specific verification
Do not provide detailed operating procedures, legal advice, or unsupported regulatory claims.
## Scope
Cover the following three areas where relevant to the {Sector}:
### Safety
Address the major hazards and protective considerations associated with ozone use, such as:
- human exposure
- inhalation hazards
- occupational exposure
- ozone leakage
- off-gas
- ventilation
- exposure monitoring
- detection and alarms
- containment
- emergency response
- material compatibility where it creates a safety concern
- protection of products, facilities, or surrounding environments where relevant
Focus on identifying and explaining the safety issue, not providing step-by-step safety procedures.
### Regulations and standards
Identify the regulatory and standards landscape relevant to ozone in the {Sector}.
Where applicable, distinguish between:
- laws and regulations
- regulatory approvals or permitted uses
- occupational exposure requirements
- food/product safety requirements
- environmental requirements
- industry standards
- voluntary standards or guidelines
- validation or documentation expectations
Do not assume that approval in one jurisdiction applies globally.
When discussing regulations, identify the jurisdiction or geographic scope whenever possible.
Do not invent regulatory requirements. If a requirement varies by jurisdiction, product, application, or concentration, explicitly state that it varies.
### Limitations
Explain the major factors that can restrict or complicate ozone use, such as:
- ozone instability
- lack of persistent residual
- high ozone demand from organic matter
- material compatibility
- process sensitivity
- treatment penetration limitations
- monitoring requirements
- validation requirements
- capital or operating complexity
- dependence on process conditions
- limitations specific to the {Sector}
Only include limitations that are genuinely relevant.
## MECE Requirements
Keep Safety, Regulations, and Limitations mutually exclusive.
Do not classify a regulatory requirement as a technical limitation.
Do not classify a technical limitation as a safety issue unless the primary issue is actually safety.
Do not repeat operational factors already covered in Section 5 unless they are necessary to explain a limitation.
Do not repeat benefits from Section 4 except when directly explaining a trade-off or limitation.
Within each subsection, avoid repeating the same constraint in different wording.
The complete section should cover the major constraint landscape without expanding into unrelated ozone topics.
## Exclusions
DO NOT provide:
- detailed application descriptions
- detailed scientific mechanisms
- extensive chemistry
- step-by-step operating procedures
- equipment selection guides
- generator sizing
- installation instructions
- concentration recommendations unless essential to explain a regulatory or safety distinction
- detailed monitoring procedures
- marketing claims
- unsupported claims of regulatory approval
- legal advice
- universal claims that ozone is "approved" or "safe" without specifying the relevant context
- a generic conclusion
These topics belong elsewhere or require dedicated pages.
## Regulatory Accuracy Requirements
Treat regulations as jurisdiction- and application-dependent.
When mentioning a regulation, standard, agency, approval, or exposure limit, use its correct name and distinguish mandatory requirements from voluntary guidance.
Do not infer legal status from industry practice.
If the regulatory situation is complex or varies substantially by jurisdiction, describe the variation rather than presenting one jurisdiction as universal.
Prioritize authoritative regulatory sources when factual verification is available.
## Writing Style
- Write for technical professionals, engineers, compliance professionals, and decision makers.
- Be factual, precise, balanced, and objective.
- Use cautious language for variable regulatory requirements.
- Avoid alarmist language when discussing safety.
- Avoid promotional language.
- Explain constraints clearly without portraying ozone as universally suitable or unsuitable.
- Use terminology appropriate to {Sector}.
- Avoid repeating the same information between Safety, Regulations, and Limitations.
## Semantic SEO Requirements
Use "{Sector}" as the contextual entity.
Use "Ozone" as the primary entity.
Model the relationships as:
Ozone → creates → Safety consideration
Ozone use → is governed by → Regulation / Standard
Sector application → is constrained by → Limitation
Safety consideration → requires → Protective control
Regulation → defines → Permitted or required practice
Limitation → affects → Suitability or performance
Ensure every paragraph contributes a distinct entity relationship or attribute.
Do not introduce entities merely to increase topical breadth.
## Output
Produce:
- a short introductory paragraph
- an H3 subsection titled "Safety"
- an H3 subsection titled "Regulations and Standards"
- an H3 subsection titled "Limitations"
Under each H3, use further H4 subsections only when multiple distinct topics need to be separated for clarity.
Each subsection must consist primarily of 2–4 well-structured paragraphs per distinct topic.
Write in paragraph form.
Do not use bullet points, numbered lists, tables, checklists, or key-value labels.
Do not generate a conclusion.
Return only Markdown.
Reply using only paragraphs.
Reply only in Italian.
Alway write the headings, titles in Italian.
        '''.strip()
        print(prompt)
        reply = llm.reply(prompt, model_filepath)
        if '</think>' in reply: reply = reply.split('</think>')[1].strip()
        reply = polish.vanilla(reply)
        print()
        print('########################################################################')
        print(reply)
        print('########################################################################')
        print()
        json_data[key] = reply
        io.json_write(json_filepath, json_data)
    return json_data

def section_related_llm(regen=False):
    json_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/sector_food.json'
    json_data = io.json_read(json_filepath, create=True)
    key = 'section_related_llm'
    if key not in json_data: json_data[key] = ''
    if regen: json_data[key] = ''
    if json_data[key] == '':
        Sector = 'settore alimentare'
        prompt = f'''
You are an expert technical writer and semantic SEO content architect.
## Context
This page is about the use of ozone in the {Sector}. It belongs to a larger knowledge base about ozone.
This section is ONLY responsible for establishing the semantic relationships between the {Sector} and other closely related ozone entities, applications, processes, technologies, and sectors.
Previous sections have already explained the role of ozone, applications, mechanisms, benefits, operational considerations, safety, regulations, and limitations within {Sector}. This section must NOT repeat those topics. Its purpose is to connect the {Sector} page to adjacent areas of the broader ozone knowledge graph.
Think of this section as a semantic bridge, not a summary or conclusion.
## Objective
Identify and explain the most contextually relevant entities that a reader studying ozone in the {Sector} would naturally need to understand next.
The reader should finish this section understanding:
- which related ozone applications are closely connected to {Sector}
- which related processes or technologies provide additional context
- which adjacent sectors or subsectors share meaningful ozone relationships
- how these entities relate to ozone and to {Sector}
Only include relationships that add genuine contextual information.
## Scope
Identify related entities from the following relationship classes where relevant:
### Related Applications
Identify ozone applications that are closely related to the {Sector} but were not already covered as primary applications in Section 2.
### Related Processes
Identify processes that interact with, support, precede, or follow ozone treatment within the broader {Sector} context.
### Related Technologies
Identify technologies that are technically or operationally adjacent to ozone, including treatment, monitoring, control, or complementary technologies where relevant.
### Related Equipment
Mention equipment entities only when they represent an important adjacent concept that warrants deeper coverage elsewhere. Do not turn this section into an equipment guide.
### Related Subsector Entities
Identify important subsectors, industries, or specialized environments within or adjacent to {Sector} that have a meaningful relationship with ozone.
### Related Sectors
Identify other sectors where ozone serves a related function and where understanding the relationship would expand the reader's understanding of ozone.
## Relationship Test
For every entity considered, ask:
1. Is this entity meaningfully related to ozone?
2. Is it meaningfully related to {Sector}?
3. Does understanding this entity add information that is not already provided elsewhere on this page?
4. Does it naturally lead to a deeper topic elsewhere in the ozone knowledge base?
If the answer to these questions is not sufficiently strong, exclude the entity.
Do not add entities simply because they are semantically associated with ozone.
## MECE Requirements
Keep relationship categories distinct:
- Related applications = other ozone use cases.
- Related processes = processes connected to ozone treatment.
- Related technologies = technologies that interact with or complement ozone.
- Related equipment = physical systems used to enable or control ozone-related processes.
- Related subsectors = specialized areas within or adjacent to {Sector}.
- Related sectors = distinct industries or sectors with meaningful ozone relationships.
Do not duplicate entities across categories unless the entity genuinely has different relationships that cannot be represented without duplication.
Do not repeat applications, mechanisms, benefits, operational factors, safety issues, regulations, or limitations already covered in Sections 1–6.
## Exclusions
DO NOT:
- summarize the preceding sections
- repeat the benefits of ozone
- explain ozone mechanisms again
- provide detailed application descriptions
- provide operational instructions
- provide equipment specifications
- provide safety procedures
- explain regulations
- compare ozone with competing technologies
- introduce unrelated entities
- create a generic "see also" list without contextual explanation
- write a conclusion
## Semantic SEO Requirements
Use "{Sector}" as the contextual entity.
Use "Ozone" as the primary entity.
Prioritize meaningful entity relationships such as:
Ozone → relates to → Related application
{Sector} → contains → Subsector
{Sector} → connects to → Related sector
Ozone application → interacts with → Related process
Ozone → complements → Related technology
Ozone process → requires or interacts with → Related equipment
For each entity, explain the relationship rather than merely naming it.
Favor entities that can naturally become dedicated pages or meaningful internal links within the broader ozone topical map.
## Internal-Linking Intent
The entities identified in this section should function as potential semantic destinations within the wider website.
Prioritize:
- high topical relevance
- strong entity relationship
- distinct search intent
- useful information gain
- logical progression from {Sector}
Do not force internal-link opportunities where no meaningful relationship exists.
## Writing Style
- Write for technically informed readers and decision makers.
- Be factual, concise, and objective.
- Explain relationships naturally in prose.
- Avoid promotional language.
- Avoid generic statements such as "ozone has many applications across many industries."
- Avoid producing a disconnected catalog of entities.
- Each paragraph should explain a meaningful relationship.
## Output
Produce:
- a short introductory paragraph explaining how {Sector} connects to the broader ozone ecosystem
- one H3 subsection for each relevant relationship category
- under each H3, use H4 subsections for individual high-value related entities when this improves clarity
For every related entity, write 1–2 concise paragraphs explaining what the entity is and why it is related to ozone and {Sector}.
Write entirely in paragraph form.
Do not use bullet points, numbered lists, tables, or key-value labels.
Only create a relationship category if it contains genuinely relevant entities.
Do not force all six relationship categories to appear.
Do not generate a conclusion.
Return only Markdown.
Reply using only paragraphs.
Reply only in Italian.
        '''.strip()
        print(prompt)
        reply = llm.reply(prompt, model_filepath)
        if '</think>' in reply: reply = reply.split('</think>')[1].strip()
        reply = polish.vanilla(reply)
        print()
        print('########################################################################')
        print(reply)
        print('########################################################################')
        print()
        json_data[key] = reply
        io.json_write(json_filepath, json_data)
    return json_data

def render_sector(target_sector_name='Food & Beverage'):
    input_data = sectors_data.data
    for sector_item in input_data:
        sector_name_eng = sector_item['sector_name_eng']
        sector_name = sector_item['sector_name']
        sector_slug = sector_item['sector_slug']
        url_slug = f'''settori/{sector_slug}'''

        if sector_name_eng.lower() != target_sector_name.lower(): continue

        # print(json.dumps(sector_item, indent=4))
        # quit()

        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/{target_sector_name}.json'
        json_data = io.json_read(json_data_filepath, create=True)


        ################################################################################
        # 0. INTRO
        ################################################################################
        json_data = section_intro_llm(regen=False)
        role_html = f''''''
        intro_html = f'''
        '''
        paragraphs = f''
        for line in json_data['section_intro_llm'].split('\n'):
            if line.strip().startswith('##'): continue
            if line.strip().startswith('###'): continue
            if line.strip().startswith('####'): continue
            paragraphs += f'<p class="block-blogpost-5-paragraph">{line}</p>\n'
        intro_html += f'''{paragraphs}'''

        ################################################################################
        # 1. ROLE
        ################################################################################
        json_data = section_role_llm(regen=False)
        role_html = f''''''
        role_html = f'''
            <h2 class="block-blogpost-5-h2">Il ruolo dell'ozono nel settore {sector_name}</h2>\n
        '''
        paragraphs = f''
        for line in json_data['section_role_llm'].split('\n'):
            if line.strip().startswith('##'): continue
            if line.strip().startswith('###'): continue
            if line.strip().startswith('####'): continue
            paragraphs += f'<p class="block-blogpost-5-paragraph">{line}</p>\n'
        role_html += f'''{paragraphs}'''

        ################################################################################
        # 2. APPLICATIONS
        ################################################################################
        json_data = section_applications_llm(regen=False)
        applications_html = f''''''
        applications_html = f'''
            <h2 class="block-blogpost-5-h2">Applicazioni</h2>\n
        '''
        paragraphs = f''
        for line in json_data['section_applications_llm'].split('\n'):
            # if line.strip().startswith('####'): continue
            # if line.strip().startswith('##'): continue
            if line.strip().startswith('###'): 
                line = line.replace('###', '').strip()
                paragraphs += f'<h3 class="block-blogpost-5-h3">{line}</h3>\n'
            else:
                paragraphs += f'<p class="block-blogpost-5-paragraph">{line}</p>\n'
        applications_html += f'''{paragraphs}'''

        ################################################################################
        # 3. MECHANISMS
        ################################################################################
        json_data = section_mechanisms_llm(regen=False)
        mechanisms_html = f''''''
        mechanisms_html = f'''
            <h2 class="block-blogpost-5-h2">Meccanismi</h2>\n
        '''
        paragraphs = f''
        for line in json_data['section_mechanisms_llm'].split('\n'):
            # if line.strip().startswith('####'): continue
            # if line.strip().startswith('##'): continue
            if line.strip().startswith('###'): 
                line = line.replace('###', '').strip()
                paragraphs += f'<h3 class="block-blogpost-5-h3">{line}</h3>\n'
            else:
                paragraphs += f'<p class="block-blogpost-5-paragraph">{line}</p>\n'
        mechanisms_html += f'''{paragraphs}'''

        ################################################################################
        # 4. BENEFITS
        ################################################################################
        json_data = section_benefits_llm(regen=False)
        benefits_html = f''''''
        benefits_html = f'''
            <h2 class="block-blogpost-5-h2">Benefici e risultati</h2>\n
        '''
        paragraphs = f''
        for line in json_data['section_benefits_llm'].split('\n'):
            # if line.strip().startswith('####'): continue
            # if line.strip().startswith('##'): continue
            if line.strip().startswith('###'): 
                line = line.replace('###', '').strip()
                paragraphs += f'<h3 class="block-blogpost-5-h3">{line}</h3>\n'
            else:
                paragraphs += f'<p class="block-blogpost-5-paragraph">{line}</p>\n'
        benefits_html += f'''{paragraphs}'''

        ################################################################################
        # 5. CONSIDERATIONS
        ################################################################################
        json_data = section_considerations_llm(regen=False)
        considerations_html = f''''''
        considerations_html = f'''
            <h2 class="block-blogpost-5-h2">Considerazioni Operative</h2>\n
        '''
        paragraphs = f''
        for line in json_data['section_considerations_llm'].split('\n'):
            # if line.strip().startswith('####'): continue
            # if line.strip().startswith('##'): continue
            if line.strip().startswith('###'): 
                line = line.replace('###', '').strip()
                paragraphs += f'<h3 class="block-blogpost-5-h3">{line}</h3>\n'
            else:
                paragraphs += f'<p class="block-blogpost-5-paragraph">{line}</p>\n'
        considerations_html += f'''{paragraphs}'''

        ################################################################################
        # 6. SAFETY
        ################################################################################
        json_data = section_safety_llm(regen=False)
        safety_html = f''''''
        safety_html = f'''
            <h2 class="block-blogpost-5-h2">Sicurezza, regolamenti e limiti</h2>\n
        '''
        paragraphs = f''
        for line in json_data['section_safety_llm'].split('\n'):
            # if line.strip().startswith('####'): continue
            # if line.strip().startswith('##'): continue
            if line.strip().startswith('####'): 
                line = line.replace('####', '').strip()
                paragraphs += f'<h4 class="block-blogpost-5-h4">{line}</h4>\n'
            elif line.strip().startswith('###'): 
                line = line.replace('###', '').strip()
                paragraphs += f'<h3 class="block-blogpost-5-h3">{line}</h3>\n'
            else:
                paragraphs += f'<p class="block-blogpost-5-paragraph">{line}</p>\n'
        safety_html += f'''{paragraphs}'''

        ################################################################################
        # 7. RELATED
        ################################################################################
        json_data = section_related_llm(regen=False)
        related_html = f''''''
        related_html = f'''
            <h2 class="block-blogpost-5-h2">Applicazioni correlate</h2>\n
        '''
        paragraphs = f''
        for line in json_data['section_related_llm'].split('\n'):
            # if line.strip().startswith('####'): continue
            # if line.strip().startswith('##'): continue
            if line.strip().startswith('####'): 
                line = line.replace('####', '').strip()
                paragraphs += f'<h4 class="block-blogpost-5-h4">{line}</h4>\n'
            elif line.strip().startswith('###'): 
                line = line.replace('###', '').strip()
                paragraphs += f'<h3 class="block-blogpost-5-h3">{line}</h3>\n'
            else:
                paragraphs += f'<p class="block-blogpost-5-paragraph">{line}</p>\n'
        related_html += f'''{paragraphs}'''

        ################################################################################
        # SUBSECTORS
        ################################################################################
        pubmed_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/subsectors/sort/{sector_name_eng}'
        pubmed_filenames = sorted(os.listdir(pubmed_folderpath))
        contaminants_names = []
        pubmed_sectors_names = []
        for pubmed_filename in pubmed_filenames:
            pubmed_filepath = f'{pubmed_folderpath}/{pubmed_filename}'
            pubmed_data = io.json_read(pubmed_filepath)
            # print(json.dumps(pubmed_data, indent=4))
            # quit()
            for item in pubmed_data['reply']:
                print(json.dumps(item, indent=4))
                try: pubmed_sectors_names.append(item['subsector_name'].lower())
                except: pubmed_sectors_names.append(item['subsector'].lower())
        sectors_html = ''
        sectors_html += '<h1>Sectors</h1>'
        sectors_html += '<ul>'
        for pubmed_sector_name in sorted(pubmed_sectors_names):
            sectors_html += f'''<li>{pubmed_sector_name}</li>'''
        sectors_html += '</ul>'

        ################################################################################
        # CONTAMINATIONS
        ################################################################################
        contaminations_items = contaminations_groups_gen(json_data_filepath)
        contaminations_html = f'''
            <h2 class="block-blogpost-5-h2">Contaminations</h2>
            <p class="block-blogpost-5-paragraph">{lorem.sentence()}</p>
        '''
        for contamination_item in contaminations_items:
            contaminations_html += f'''<h3 class="block-blogpost-5-h3">{contamination_item['nature']}</h3>'''
            context_data = f'''
                {contamination_item['nature']}
            '''
            json_data = contaminations_biological_content_llm(context_data, regen=False)
            paragraphs = f''
            for line in json_data['contaminations_biological_content_llm'].split('\n'):
                paragraphs += f'<p class="block-blogpost-5-paragraph">{line}</p>'
            contaminations_html += f'''{paragraphs}'''
            ###
            for contamination_class in contamination_item['classes']:
                contaminations_html += f'''<h4 class="block-blogpost-5-h4">{contamination_class['class']}</h4>'''
                context_data = f'''
                    {contamination_item['nature']}
                    {contamination_class}
                '''
                json_data = contaminations_biological_bacterium_content_llm(context_data, regen=False)
                paragraphs = f''
                for line in json_data['contaminations_biological_bacterium_content_llm'].split('\n'):
                    paragraphs += f'<p class="block-blogpost-5-paragraph">{line}</p>'
                contaminations_html += f'''{paragraphs}'''

        ###
        title = f'''Ozono nel settore {sector_name}'''.capitalize()
        html_h1 = f'''<h1 class="block-blogpost-5-h1">{title}</h1>'''
        
        featuredimage_html = f'''
            <img class="block-blogpost-5-featuredimage" src="https://images.unsplash.com/photo-1651525669944-00de65d3b8a5?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
        '''
        
        subsectors_html = f'''
            <h2 class="block-blogpost-5-h2">Subsectors</h2>
            <div class="block-list-panel-default">
                <div class="component-list-panel-default">Ortofrutticolo</div>
                <div class="component-list-panel-default">Cerealicolo</div>
                <div class="component-list-panel-default">Frutta secca</div>
                <div class="component-list-panel-default">Spezie</div>
                <div class="component-list-panel-default">Carne</div>
                <div class="component-list-panel-default">Ittico</div>
                <div class="component-list-panel-default">Lattiero-caseario</div>
                <div class="component-list-panel-default">Uova</div>
                <div class="component-list-panel-default">Bevande</div>
                <div class="component-list-panel-default">Oleario</div>
                <div class="component-list-panel-default">Pet Food</div>
                <div class="component-list-panel-default">Altri</div>
            </div>
        '''

        article_html = f'''
            {intro_html}
            {role_html}
            {applications_html}
            {mechanisms_html}
            {benefits_html}
            {considerations_html}
            {safety_html}
            {related_html}
        '''

        toc_list_elements_html = f''
        for line in article_html.strip().split('\n'):
            if line.strip().startswith('<h2'):
                line = line.split('>', 1)[1].split('<', 1)[0]
                toc_list_elements_html += f'''<li><a class="block-blogpost-5-toc-li-h2" href="#">{line}</a></li>'''
            elif line.strip().startswith('<h3'):
                line = line.split('>', 1)[1].split('<', 1)[0]
                toc_list_elements_html += f'''<li><a class="block-blogpost-5-toc-li-h3" href="#">{line}</a></li>'''
            else:
                print(line)
            
        

        html_body = f'''
            <body>
                <main class="container-xl block-blogpost-5">
                    {html_h1}
                    <div class="block-blogpost-5-layout">
                        <div>
                            {featuredimage_html}
                            {article_html}
                        </div>
                        <aside class="block-blogpost-5-toc">
                            <div class="block-blogpost-5-toc-nav">
                            <h2 class="block-blogpost-5-toc-title" style="margin-bottom: 1.25rem;">SU QUESTA PAGINA</h2>
                                <nav>
                                    <ul class="block-blogpost-5-toc-nav-ul">
                                        {toc_list_elements_html}
                                    </ul>
                                </nav>
                            <div>
                        </aside>
                    </div>
                <main>
            </body>
        '''

        meta_title = f'''{sector_name}'''
        html = f''' 
            <!DOCTYPE html>
            <html lang="it">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>{meta_title}</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Geist:wght@100..900&display=swap" rel="stylesheet">
                <link rel="stylesheet" href="/styles.css">
            </head>
            {html_body}
            </html>
        '''.strip()

        ###
        html_folderpath = f'{g.website_folderpath}/{url_slug}'
        io.folders_recursive_gen(html_folderpath)
        html_filepath = f'{g.website_folderpath}/{url_slug}/index.html'
        with open(html_filepath, 'w') as f: f.write(html)
        print(html_filepath)

def run():
    shutil.copy2(f'styles.css', f'{g.WEBSITE_FOLDERPATH}/styles.css')

    output_folderpath = f'{g.WEBSITE_FOLDERPATH}/settori'
    try: shutil.rmtree(output_folderpath)
    except: pass
    io.folders_recursive_gen(output_folderpath)
    ###

    render_sectors_html()
    ###
    # render_sector_html_backup()
    render_sector()

run()
