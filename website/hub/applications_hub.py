import os
import shutil

from lib import g
from lib import io
# from lib import llm
from lib import components

from data import settori_data

section_hero_py = '5rem'
section_py = '8rem'

def index_to_string(i):
    i_str = ''
    if i >= 1000: i_str = f'{i}'
    elif i >= 100: i_str = f'0{i}'
    elif i >= 10: i_str = f'00{i}'
    else: i_str = f'000{i}'
    return i_str

def cta():
    html = f'''
        <section class="container-xl" style="margin-top: 6rem; margin-bottom: 6rem;">
            <div style="display: flex; align-items: center; gap: 3rem; margin-bottom: 2rem;">
                <h2 style="color: {g.color_black_pearl}; font-size: 1.25rem; font-weight: normal;">Contattaci</h2>
                <div style="display: flex; align-items: center; gap: 1.5rem;">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="{g.color_black_pearl}">
                            <path
                                d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm320-280L160-640v400h640v-400L480-440Zm0-80 320-200H160l320 200ZM160-640v-80 480-400Z" />
                        </svg>
                        <span>Email: info@ozonogroup.it</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="{g.color_black_pearl}">
                            <path
                                d="M798-120q-125 0-247-54.5T329-329Q229-429 174.5-551T120-798q0-18 12-30t30-12h162q14 0 25 9.5t13 22.5l26 140q2 16-1 27t-11 19l-97 98q20 37 47.5 71.5T387-386q31 31 65 57.5t72 48.5l94-94q9-9 23.5-13.5T670-390l138 28q14 4 23 14.5t9 23.5v162q0 18-12 30t-30 12ZM241-600l66-66-17-94h-89q5 41 14 81t26 79Zm358 358q39 17 79.5 27t81.5 13v-88l-94-19-67 67ZM241-600Zm358 358Z" />
                        </svg>
                        <span>Telefono: +39 0423 952833</span>
                    </div>
                </div>
            </div>
            <div style="">
                <div style="display: inline-block;">
                    <a class="button-default-3" href="/contatti.html">
                        <span>Prenota Consulenza Gratuita</span>
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#ffffff"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                    </a>
                </div>
            </div>
        </section>
    '''
    return html

def hero_gen(settore):
    opacity = '0.66'
    section_1 = f'''
        <section style="
                background: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), 
                    url('/immagini/settori-industria-alimentare.jpg');                background-size: cover;
                background-size: cover;
                background-position: center;
                padding-top: 8rem;
                padding-bottom: 8rem;
                display: flex;
                flex-direction: column;
                align-items: center;
        ">
    '''
    section_2 = f'''
        <section style="
                background: blue;
                padding-top: 8rem;
                padding-bottom: 8rem;
                display: flex;
                flex-direction: column;
                align-items: center;
        ">
    '''
    title_1 = f'''
        <h1 class="container-lg" style="color: #ffffff; font-size: 4rem; line-height: 1; font-weight: normal; text-align: center; margin-bottom: 1rem;">
            L'ozono nel settore {settore}
        </h1>
    '''
    subtitle_1 = f'''
        <p class="container-md" style="color: #ffffff; font-size: 1.25rem; line-height: 1.4; text-align: center; margin-bottom: 2rem;">
            Soluzioni per la sicurezza alimentare e la conformità HACCP.
        </p>
    '''
    cta_1 = f'''
        <div>
            <a class="button-invert" href="/contatti.html">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M680-80v-120H560v-80h120v-120h80v120h120v80H760v120h-80Zm-480-80q-33 0-56.5-23.5T120-240v-480q0-33 23.5-56.5T200-800h40v-80h80v80h240v-80h80v80h40q33 0 56.5 23.5T760-720v244q-20-3-40-3t-40 3v-84H200v320h280q0 20 3 40t11 40H200Zm0-480h480v-80H200v80Zm0 0v-80 80Z"/></svg>
                <span>Prenota Consulenza</span>
            </a>
        </div>
    '''
    html = f'''
            {section_2}
            {title_1}
        </section>      
    '''
    return html

def outline_gen(settore):
    try: os.makedirs(f'./database/hubs/settori/{settore}')
    except: pass
    output_filepath = f'./database/hubs/settori/{settore}/outline.txt'
    if os.path.exists(output_filepath): return
    prompt = f'''
        Devo scrivere un articolo sul mio sito per il seguente argomento: L'ozono per l'industria {settore}.
        Dammi un outline per questo articolo.
        Nella outline, inserisci solo sezioni specifiche sull'ozono per questo settore, mai inserire informazioni generali sull'ozono.
        Rispondi solo con i titoli delle sezioni dell'outline.
        Rispondi in italiano.
        /no_think
    '''
    reply = llm.reply(prompt)
    if '</think>' in reply:
        reply = reply.split('</think>')[1].strip()
    print('#################################################')
    print(reply)
    print('#################################################')
    with open(output_filepath, 'w') as f: f.write(reply)

def outline_details_gen(settore):
    with open(f'./database/hubs/settori/{settore}/outline.txt') as f: titoli = f.read()
    output_filepath = f'./database/hubs/settori/{settore}/outline-dettagli.txt'
    if os.path.exists(output_filepath): return
    prompt = f'''
        Devo scrivere un articolo sul mio sito per il seguente argomento: L'ozono per l'industria {settore}.
        Questi sono i titoli delle mie sezioni che devo scrivere.
        {titoli}
        Voglio che ripeti i titoli e sotto ogni titolo mi dai una breve descrizione del contenuto che devo scrivere.
        Separa le descrizioni con ---.
        Rispondi solo con i titoli, le descrizioni, e i separatori ---.
        Rispondi in italiano.
        /no_think
    '''
    reply = llm.reply(prompt)
    if '</think>' in reply:
        reply = reply.split('</think>')[1].strip()
    print('#################################################')
    print(reply)
    print('#################################################')
    with open(output_filepath, 'w') as f: f.write(reply)

def sezioni_gen(settore, regen=False):
    sezioni_folderpath = f'./database/hubs/settori/{settore}/sezioni'
    if regen:
        try: shutil.rmtree(sezioni_folderpath)
        except: pass
    try: os.makedirs(sezioni_folderpath)
    except: pass
    with open(f'./database/hubs/settori/{settore}/outline-dettagli.txt') as f: outline_dettagli = f.read()
    sezioni = outline_dettagli.split('---')
    with open(f'./database/hubs/settori/{settore}/outline.txt') as f: outline = f.read()
    titles = outline.split('\n')
    if len(sezioni) != len(titles): return False
    for sezione_i, sezione in enumerate(sezioni):
        sezione_i_str = index_to_string(sezione_i)
        sezione_filepath = f'{sezioni_folderpath}/{sezione_i_str}.txt'
        if os.path.exists(sezione_filepath): continue
        ###
        prompt = f'''
            Devo scrivere un articolo sul mio sito per il seguente argomento: L'ozono per l'industria {settore}.
            Queste sono le sezioni che devo scrivere.
            {outline_dettagli}
            Voglio che ti concentri sulla seguente sezione e che scrivi 400 parole per questa sezione:
            {sezione}
            Rispondi solo con il contenuto della sezione richiesta.
            Rispondi in italiano.
            /no_think
        '''
        reply = llm.reply(prompt)
        if '</think>' in reply:
            reply = reply.split('</think>')[1].strip()
        print('#################################################')
        print(reply)
        print('#################################################')
        with open(sezione_filepath, 'w') as f: f.write(reply)
    return True

def article_gen(settore):
    output_filepath = f'./database/hubs/settori/{settore}/article.txt'
    if os.path.exists(output_filepath): return
    ###
    sezioni_folderpath = f'./database/hubs/settori/{settore}/sezioni'
    sezioni_filepaths = [f'{sezioni_folderpath}/{filename}' for filename in sorted(os.listdir(sezioni_folderpath))]
    with open(f'./database/hubs/settori/{settore}/outline.txt') as f: outline = f.read()
    titles = outline.split('\n')
    html = f''
    for i in range(len(sezioni_filepaths)):
        title = titles[i]
        title_html = f'''<h2 style="margin-top: 3rem; margin-bottom: 1rem; line-height: 1;">{title}</h2>'''
        ###
        sezione_filepath = sezioni_filepaths[i]
        with open(sezione_filepath) as f: content = f.read()
        content = content.replace('*', '')
        content = content.replace('’', "'")
        paragraphs = content.split('\n')
        paragraphs_html = '\n'.join([
            f'''<p style="margin-bottom: 1rem;">{paragraph}</p>''' 
            for paragraph in paragraphs if paragraph.strip() != ''
        ])
        html += f'''
            {title_html}
            {paragraphs_html}
        '''
    with open(output_filepath, 'w') as f: f.write(html)

def settori_settore_gen(settore, side_level_sectors=None):
    running = True 
    while running:
        outline_gen(settore)
        outline_details_gen(settore)
        res_ok = sezioni_gen(settore, regen=False)
        if not res_ok: continue
        article_gen(settore)
        running = False 
    with open(f'./database/hubs/settori/{settore}/article.txt') as f: article_html = f.read()
    article_html = f'''
        <div class="container-lg">
            {article_html}
        </div>
    '''
    side_level_sectors_html = f''
    if side_level_sectors:
        cards = f''
        for sector in side_level_sectors:
            card = f'''
                <div>
                    <a href="/settori/{sector}.html" style="text-decoration: none;">
                        <h3 style="margin-bottom: 1rem;">
                            {sector.title()}
                        </h3>
                        <img src="/immagini/home/{sector}.jpg" style="margin-bottom: 1rem;">
                        <p>
                            {sector}
                        </p>
                    </a>
                </div>
            '''
            cards += card
        side_level_sectors_html = f'''
            <div class="container-lg">
                <div class="grid-3" style="padding-top: 3rem; row-gap: 3rem;">
                    {cards}
                </div>
            </div>
        '''
    # quit()
    hero = hero_gen(settore)
    ########################################
    # html
    ########################################
    html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/style.css">
        </head>
        <body>
            {components.header_light()}
            <main>
                {hero}
                {article_html}
                {side_level_sectors_html}
                {cta()}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_filepath = f'{g.WEBSITE_FOLDERPATH}/settori/{settore}.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)

def sectors_sector_subsector_gen(item):
    sector_name = item['sector_name']
    subsector_name = item['subsector_name']
    sector_slug = sector_name.lower().strip().replace(' ', '-')
    subsector_slug = subsector_name.lower().strip().replace(' ', '-')
    ###
    html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/style.css">
        </head>
        <body>
            {components.header_light()}
            <main>
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_filepath = f'{g.WEBSITE_FOLDERPATH}/settori/{sector_slug}/{subsector_slug}.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)

def sectors_sector_gen(item):
    sector_name = item['name']
    sector_slug = sector_name.lower().strip().replace(' ', '-')
    ###
    subsectors_cards_html = ''
    subsectors = item['subsectors']
    for subsector in subsectors:
        subsector_name = subsector['name']
        subsector_image_src = subsector['image_src']
        subsector_slug = subsector_name.lower().strip().replace(' ', '-')
        subsector_href = f'/settori/{sector_slug}/{subsector_slug}.html'
        subsectors_cards_html += f'''
            <div>
                <img src="{subsector_image_src}">
                <a href="{subsector_href}">{subsector_name}</a>
            </div>
        '''
    ###
    subsectors_html = f'''
        <div class="container-lg">
            <div class="grid-3" style="padding-top: 3rem; row-gap: 3rem;">
                {subsectors_cards_html}
            </div>
        </div>
    '''
    ###
    html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/style.css">
        </head>
        <body>
            {components.header_light()}
            <main>
                {subsectors_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_filepath = f'{g.WEBSITE_FOLDERPATH}/settori/{sector_slug}.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)

def sectors_gen(item):    
    sectors_cards_html = ''
    sectors = item
    for sector in sectors:
        sector_name = sector['name']
        sector_image_src = sector['image_src']
        sector_slug = sector_name.lower().strip().replace(' ', '-')
        sector_href = f'/settori/{sector_slug}.html'
        '''
        <div>
                <a href="{sector_href}" style="display: block;">
                    <img src="{sector_image_src}">
                    <h2>{sector_name}</h2>
                </a>
            </div>
            '''
        sectors_cards_html += f'''
            <div>
                <a href="/settori/alimentare.html" style="text-decoration: none;">
                    <img src="{sector_image_src}" style="margin-bottom: 1rem;">
                    <h3 style="margin-bottom: 1rem;">
                        {sector_name}
                    </h3>
                </a>
            </div>
        '''
    ###
    sectors_html = f'''
        <section style="padding-top: 6rem;">
            <div class="container-xl">
                <div class="grid-4" style="padding-top: 3rem; row-gap: 3rem;">
                    {sectors_cards_html}
                </div>
            </div>
        </section>
    '''
    print(sectors_html)
    ###
    html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/style.css">
        </head>
        <body>
            {components.header_light()}
            <main>
                {sectors_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_filepath = f'{g.WEBSITE_FOLDERPATH}/settori.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)

def applications_gen():
    ###
    html = f'''
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="robots" content="index, follow">

            <title>Applicazioni dell'Ozono | Ozonogroup</title>
            <meta name="description" content="Scopri le diverse applicazioni dell'ozono in ambienti residenziali, commerciali e industriali. Questa pagina presenta i principali ambiti in cui l'ozono può essere utilizzato.">
        </head>

        <body>

            <header>
                <nav>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="applications.html">Applicazioni</a></li>
                        <li><a href="#">Problemi</a></li>
                        <li><a href="#">Prodotti</a></li>
                        <li><a href="#">Chi Siamo</a></li>
                    </ul>
                </nav>
            </header>

            <main>
                <h1>Applicazioni dell'Ozono</h1>

                <!-- Lead paragraph immediately under H1 -->
                <p>
                    Questa pagina introduce le principali aree in cui l'ozono può essere applicato in diversi ambienti.
                    È il punto di partenza per esplorare le applicazioni residenziali, commerciali e industriali.
                </p>

                <!-- STEP 5: Introductory explanatory section -->
                <section>
                    <h2>Cos'è un'Applicazione dell'Ozono?</h2>
                    <p>
                        Le applicazioni dell'ozono rappresentano tutti i modi in cui questo gas può essere utilizzato per migliorare la qualità dell'aria, dell'acqua e degli ambienti in cui viviamo o lavoriamo. 
                        Grazie alle sue proprietà ossidanti e purificanti, l'ozono trova impiego in contesti residenziali, commerciali e industriali.
                    </p>
                    <p>
                        Questa pagina funge da punto di partenza per comprendere i diversi ambienti in cui l'ozono può essere applicato e i benefici che può portare. 
                        In seguito, sarà possibile esplorare le applicazioni specifiche per ciascun tipo di ambiente o struttura.
                    </p>
                    <p>
                        L'obiettivo è fornire un quadro completo e chiaro delle possibilità offerte dall'ozono, aiutando sia chi cerca informazioni generali sia chi desidera approfondire casi specifici.
                    </p>
                </section>

                <!-- STEP 6: Primary Applications Categories Section -->
                <section>
                    <h2>Tipologie di Applicazioni</h2>

                    <article>
                        <h3>Applicazioni Residenziali</h3>
                        <p>
        Le applicazioni dell'ozono in ambito residenziale migliorano la qualità dell'aria e aiutano a eliminare odori e allergeni presenti nelle abitazioni. 
        Sono soluzioni pensate per case, appartamenti e spazi privati, contribuendo a creare ambienti più salubri e confortevoli. 
        In futuro, sarà possibile approfondire le applicazioni specifiche per ogni ambiente domestico.
    </p>
                    </article>

                    <article>
                        <h3>Applicazioni Commerciali</h3>
                        <p>
        In ambito commerciale, l'ozono viene utilizzato per igienizzare uffici, negozi, ristoranti e strutture pubbliche, migliorando la qualità dell'aria e delle superfici. 
        Queste applicazioni garantiscono spazi sicuri e salubri per clienti e personale. 
        Successivamente sarà possibile esplorare i casi specifici per ciascun tipo di attività commerciale.
    </p>
                    </article>

                    <article>
                        <h3>Applicazioni Industriali</h3>
                        <p>
        Le applicazioni industriali comprendono stabilimenti produttivi, magazzini e processi industriali in cui l'ozono aiuta a controllare odori, batteri e contaminanti. 
        Queste soluzioni migliorano la sicurezza e la qualità degli ambienti su larga scala. 
        In futuro, saranno disponibili approfondimenti per i diversi settori industriali e le loro aree operative specifiche.
    </p>
                    </article>
                </section>

                <section>
                    <h2>Come Esplorare le Applicazioni dell'Ozono</h2>
                    <p>
                        Le applicazioni dell'ozono possono essere esplorate in diversi modi, a seconda del punto di partenza e delle esigenze specifiche. 
                        Questa sezione ti aiuta a orientarti all'interno del sito e a comprendere come trovare le informazioni più rilevanti per il tuo contesto.
                    </p>
                    <p>
                        Se conosci già il tipo di ambiente o struttura da trattare, puoi esplorare le applicazioni partendo dalle categorie principali, come residenziale, commerciale o industriale. 
                        Ogni categoria verrà progressivamente approfondita con sezioni dedicate a singole strutture, aree operative e contesti specifici.
                    </p>
                    <p>
                        Se invece il tuo punto di partenza è un problema o un obiettivo, come il controllo degli odori, il miglioramento della qualità dell'aria o la sanificazione degli ambienti, sarà possibile esplorare le applicazioni partendo da queste esigenze, indipendentemente dal tipo di ambiente.
                    </p>
                    <p>
                        In entrambi i casi, l'obiettivo è accompagnarti passo dopo passo verso la soluzione più adatta, fornendo informazioni chiare, approfondimenti tecnici e una visione completa delle possibilità offerte dall'ozono.
                    </p>
                </section>

                <section>
                    <h2>Il Nostro Approccio alle Applicazioni dell'Ozono</h2>

                    <p>
                        Questo sito nasce dall'esperienza diretta nella progettazione e realizzazione di sistemi a ozono per diversi contesti applicativi. 
                        L'approccio adottato si basa sulla conoscenza pratica delle tecnologie a ozono e sul loro utilizzo reale in ambienti residenziali, commerciali e industriali.
                    </p>

                    <p>
                        Ogni applicazione descritta è il risultato di anni di studio, test sul campo e sviluppo di soluzioni personalizzate. 
                        La combinazione tra progettazione tecnica e osservazione dei risultati operativi permette di affrontare le applicazioni dell'ozono in modo concreto e consapevole.
                    </p>

                    <p>
                        L'obiettivo è coprire in modo completo tutte le principali applicazioni dell'ozono, dalle più comuni alle più specialistiche, includendo ambienti, strutture, aree operative e processi. 
                        Questo consente di offrire una visione coerente e approfondita dell'utilizzo dell'ozono in diversi settori.
                    </p>

                    <p>
                        Le informazioni presenti su questo sito hanno uno scopo informativo ed educativo, pensato per accompagnare il lettore nella comprensione delle possibilità offerte dall'ozono. 
                        Ogni sezione verrà progressivamente ampliata per fornire contenuti sempre più dettagliati e specifici.
                    </p>
                </section>


                <section>
                    <h2>Aree e Applicazioni che Verranno Approfondite</h2>

                    <p>
                        Le applicazioni dell'ozono coprono un'ampia varietà di ambienti, strutture e contesti operativi. 
                        Le sezioni elencate di seguito rappresentano alcune delle aree che verranno progressivamente approfondite con contenuti dedicati.
                    </p>

                    <h3>Ambito Residenziale</h3>
                    <ul>
                        <li>Trattamento dell'aria negli ambienti domestici</li>
                        <li>Applicazioni dell'ozono in camere da letto e zone giorno</li>
                        <li>Utilizzo dell'ozono in cucine e ambienti di servizio</li>
                        <li>Applicazioni dell'ozono in spazi privati e abitazioni</li>
                    </ul>

                    <h3>Ambito Commerciale</h3>
                    <ul>
                        <li>Applicazioni dell'ozono in uffici e ambienti lavorativi</li>
                        <li>Utilizzo dell'ozono in ristoranti e attività di ristorazione</li>
                        <li>Applicazioni dell'ozono in strutture ricettive e alberghiere</li>
                        <li>Trattamento degli ambienti in spazi aperti al pubblico</li>
                    </ul>

                    <h3>Ambito Industriale</h3>
                    <ul>
                        <li>Applicazioni dell'ozono nell'industria alimentare</li>
                        <li>Utilizzo dell'ozono in magazzini e aree di stoccaggio</li>
                        <li>Applicazioni dell'ozono in impianti produttivi</li>
                        <li>Trattamento dell'aria e degli ambienti in contesti industriali</li>
                    </ul>
                </section>

                <section>
                    <h2>Ambito e Limiti dei Contenuti</h2>

                    <p>
                        Questa pagina ha lo scopo di offrire una panoramica generale delle principali applicazioni dell'ozono in diversi contesti ambientali e operativi. 
                        I contenuti presentati sono pensati per fornire una visione introduttiva e strutturata delle possibilità offerte dall'ozono.
                    </p>

                    <p>
                        Le informazioni presenti non costituiscono istruzioni tecniche, indicazioni operative o soluzioni specifiche per singoli casi. 
                        Ogni applicazione dell'ozono richiede valutazioni dedicate in base all'ambiente, agli obiettivi e alle condizioni operative.
                    </p>

                    <p>
                        Per approfondimenti tecnici, descrizioni dettagliate delle applicazioni e analisi di casi specifici, saranno disponibili sezioni e pagine dedicate, progettate per fornire informazioni complete e contestualizzate.
                    </p>
                </section>


            </main>

            <footer>
                <p>&copy; 2026 Ozonogroup. Tutti i diritti riservati.</p>
            </footer>

        </body>
        </html>


    '''
    '''
<!-- Placeholder per aree dettagliate future -->
    <section>
      <h2>Aree di Applicazione Dettagliate</h2>
      <ul>
        <li>Strutture dell'industria alimentare</li>
        <li>Ambientazioni per la conservazione a freddo</li>
        <li>Trattamento dell'aria residenziale</li>
        <li>Sistemi di trattamento dell'acqua</li>
      </ul>
    </section>
    '''

    html_filepath = f'{g.WEBSITE_FOLDERPATH}/applicazioni.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)

def gen():
    applications_gen()
    quit()
    # settori_alimentare_lattiero_caseario_gen()
    # settori_alimentare_carni_gen()
    # settori_alimentare_ortofrutta_gen()
    # settori_alimentare_gen()
    # sector_rows = io.csv_read(f'{g.DATABASE_FOLDERPATH}/settori.csv')

    sectors = io.json_read(f'{g.SSOT_FOLDERPATH}/sectors.json')
    for sector in sectors:
        sector_name = sector['name']
        subsectors = sector['subsectors']
        for subsector in subsectors:
            subsector_name = subsector['name']
            item = {
                'sector_name': sector_name,
                'subsector_name': subsector_name,
            }
            sectors_sector_subsector_gen(item)
        item = sector
        sectors_sector_gen(item)
    item = sectors
    sectors_gen(item)

    quit()

    '''
    for sector_row in sector_rows:
        sector_name = sector_row[0]
        settori_settore_gen(sector_name, ['confezionamento', 'trasporti', 'agricolo'])
        sectors_sector_subsector_gen(subsector_name, ['confezionamento', 'trasporti', 'agricolo'])
    quit()
    '''
    

    '''
    settori_settore_gen('agricolo')
    settori_settore_gen('farmaceutico')
    settori_settore_gen('confezionamento')
    settori_settore_gen('trasporto')
    settori_settore_gen('cosmetico')
    settori_settore_gen('chimico')
    settori_settore_gen('tessile')
    '''

    # settori_settore_sottosettore_gen('lattiero-caseario')

    # settori_logistico_gen()
    # settori_horeca_gen()
    # settori_farmaceutico_gen()
    # settori_agroalimentare_gen()
    # settori_sportivo_gen()

    # settori_gen()
    pass
    
    
