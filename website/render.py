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
    html_sectors = ''
    if sectors_lvl_1 != []:
        html_sectors += '<ul>'
        for sector in sectors_lvl_1:
            html_sectors += f'''<li><a href="/settori/{sector['sector_slug']}">{sector['sector_name']}</a></li>'''
        html_sectors += '</ul>'
    article_html = f'''
        {html_h1}
        {html_sectors}
    '''

    ###
    url_slug = f'''settori'''
    meta_title = f'''Settori'''
            # <link rel="stylesheet" href="/styles.css">
    html = f''' 
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>{meta_title}</title>

            <!-- USWDS initializer -->
            <script src="/assets/uswds/dist/js/uswds-init.min.js"></script>

            <!-- USWDS -->
            <link rel="stylesheet" href="/assets/uswds/dist/css/uswds.min.css">

        </head>
        <body>
            {components.header_light_logo()}
            <main class="listing container-md">
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

def render_sector_html():
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
        html_toc = f''''''
        for line in html_article.strip().split('\n'):
            if '<h1>' in line:
                pass
            elif '<h2>' in line:
                line = line.replace('<h2>', '').replace('</h2>', '')
                html_toc += f'''<li style="font-weight: 700;"><a href="">{line}</a></li>\n'''

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

def run():
    shutil.copy2(f'styles-custom.css', f'{g.WEBSITE_FOLDERPATH}/styles-custom.css')

    output_folderpath = f'{g.WEBSITE_FOLDERPATH}/settori'
    try: shutil.rmtree(output_folderpath)
    except: pass
    io.folders_recursive_gen(output_folderpath)
    ###

    render_sectors_html()
    ###
    render_sector_html()

run()
