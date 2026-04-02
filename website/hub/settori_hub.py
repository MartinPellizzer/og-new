import os

from lib import g
from lib import components

def main():

    ########################################
    # HERO 0001
    ########################################
    h1 = f'Applicazioni dei sistemi a ozono nei principali settori industriali'
    subordinate = f'Analizziamo criticità operative nei processi produttivi e progettiamo sistemi a ozono su misura per la loro risoluzione.'
    href = '/contatti.html'
    anchor = 'Richiedi una consulenza gratuita'
    hero_html = f'''
        <section class="hero-0001"
            style="background-image: linear-gradient(rgba(0, 30, 60, 0.8), rgba(0, 30, 60, 0.8)), 
            url('/immagini/settori.jpg');
        ">
            <div class="hero-0001-content-container">
                <h1 class="container-lg">{h1}</h1>
                <p class="container-md">{subordinate}</p>
                <div class="hero-0001-link">
                    <a href="{href}">{anchor}</a>
                </div>
            </div>
        </section>
    '''

    ########################################
    # GRID 0004
    ########################################
    row_0_h2 = f'''Industria Alimentare: sanificazione, conservazione e sicurezza microbiologica con ozono'''
    row_0_subordinate = f'''L'ozono elimina batteri, virus e muffe su acqua, superfici e ambienti, migliorando shelf-life e sicurezza alimentare senza residui chimici.'''
    row_0_img_src = f'''/immagini/settori-alimentare.jpg'''
    row_1_h2 = f'''Industria Chimica: ossidazione avanzata e trattamento di acque e emissioni'''
    row_1_subordinate = f'''L'ozono ossida composti organici e inorganici, riducendo contaminanti, odori e carichi inquinanti nei processi chimici industriali.'''
    row_1_img_src = f'''/immagini/settori-chimica.jpg'''
    row_2_h2 = f'''Industria Farmaceutica: sterilizzazione e controllo contaminazioni in ambienti critici'''
    row_2_subordinate = f'''L'ozono garantisce abbattimento microbiologico in cleanroom, impianti e acque di processo, supportando standard GMP e validazione.'''
    row_2_img_src = f'''/immagini/settori-farmaceutica.jpg'''
    row_3_h2 = f'''Settore Rifiuti: abbattimento odori e trattamento percolati con ozono'''
    row_3_subordinate = f'''L'ozono neutralizza composti odorigeni e degrada sostanze organiche nei percolati, migliorando gestione e impatto ambientale.'''
    row_3_img_src = f'''/immagini/settori-rifiuti.jpg'''
    row_4_h2 = f'''Manifatturiero & Logistica: sanificazione ambientale e controllo qualità nei processi'''
    row_4_subordinate = f'''Llozono riduce cariche microbiologiche e odori in stabilimenti e magazzini, ottimizzando condizioni igieniche e conservazione dei prodotti.'''
    row_4_img_src = f'''/immagini/settori-logistica.jpg'''
    # subordinate = f'''Progettiamo e realizziamo impianti a ozono per applicazioni industriali specifiche, adattando ogni soluzione ai processi produttivi del settore di riferimento.'''
    img_height = '400px'
    settori_html = f'''
        <section class="grid-0004">
            <div class="container-xl grid-0004-content-container">
                <article class="grid-0004-row m-flex">
                    <div class="flex-1">
                        <h2>{row_0_h2}</h2>
                        <p>{row_0_subordinate}</p>
                        <ul style="margin-left: 2rem; margin-bottom: 1rem;">
                            <li style="margin-bottom: 0.8rem;">Contaminazione microbiologica ambientale</li>
                            <li style="margin-bottom: 0.8rem;">Odori nei reparti produttivi</li>
                            <li style="margin-bottom: 0.8rem;">Sanificazione linee e serbatoi</li>
                            <li style="margin-bottom: 0.8rem;">Rischi per sicurezza alimentare</li>
                            <li style="margin-bottom: 0.8rem;">Gestione acque di processo</li>
                        </ul>
                    </div>
                    <div class="flex-1">
                        <img src="{row_0_img_src}">
                    </div>
                </article>
                <article class="grid-0004-row m-flex m-row-reverse">
                    <div class="flex-1">
                        <h2>{row_1_h2}</h2>
                        <p>{row_1_subordinate}</p>
                        <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                            <li style="margin-bottom: 0.8rem;">Emissioni VOC (Composti Organici Volatili)</li>
                            <li style="margin-bottom: 0.8rem;">Trattamento gas ossidabili</li>
                            <li style="margin-bottom: 0.8rem;">Odori persistenti e complessi</li>
                            <li style="margin-bottom: 0.8rem;">Normative ambientali stringenti</li>
                            <li style="margin-bottom: 0.8rem;">Trattamento aria di processo</li>
                        </ul>
                    </div>
                    <div class="flex-1">
                        <img src="{row_1_img_src}">
                    </div>
                </article>
                <article class="grid-0004-row m-flex">
                    <div class="flex-1">
                        <h2>{row_2_h2}</h2>
                        <p>{row_2_subordinate}</p>
                        <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                            <li style="margin-bottom: 0.8rem;">Controllo rigoroso carica microbica</li>
                            <li style="margin-bottom: 0.8rem;">Gestione ambienti controllati (Clean Rooms)</li>
                            <li style="margin-bottom: 0.8rem;">Disinfezione impianti e superfici</li>
                            <li style="margin-bottom: 0.8rem;">Rischio contaminazione crociata</li>
                    </div>
                    <div class="flex-1">
                        <img src="{row_2_img_src}">
                    </div>
                </article>
                <article class="grid-0004-row m-flex m-row-reverse">
                    <div class="flex-1">
                        <h2>{row_3_h2}</h2>
                        <p>{row_3_subordinate}</p>
                        <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                            <li style="margin-bottom: 0.8rem;">Emissioni odorigene intense</li>
                            <li style="margin-bottom: 0.8rem;">Presenza di bioaerosol pericolosi</li>
                            <li style="margin-bottom: 0.8rem;">Trattamento aria capannoni</li>
                            <li style="margin-bottom: 0.8rem;">Impatto ambientale sul territorio</li>
                        </ul>
                    </div>
                    <div class="flex-1">
                        <img src="{row_3_img_src}">
                    </div>
                </article>
                <article class="grid-0004-row m-flex">
                    <div class="flex-1">
                        <h2>{row_4_h2}</h2>
                        <p>{row_4_subordinate}</p>
                        <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                            <li style="margin-bottom: 0.8rem;">Aria stagnante in grandi volumi</li>
                            <li style="margin-bottom: 0.8rem;">Odori da materiali stoccati</li>
                            <li style="margin-bottom: 0.8rem;">Contaminazioni in ambienti chiusi</li>
                            <li style="margin-bottom: 0.8rem;">Benessere operatori</li>
                    </div>
                    <div class="flex-1">
                        <img src="{row_4_img_src}">
                    </div>
                </article>
            </div>
        </section>
    '''

    '''
        <a href="/soluzioni/trattamento-aria/" class="app-item">
            <h4>Trattamento aria ambienti produttivi</h4>
            <span class="btn-outline" style="font-size:0.8rem; padding: 5px 10px; margin-top:5px;">Scopri di
                più</span>
        </a>
        <a href="/soluzioni/disinfezione-acqua/" class="app-item">
            <h4>Disinfezione acqua di processo</h4>
            <span class="btn-outline" style="font-size:0.8rem; padding: 5px 10px; margin-top:5px;">Scopri di
                più</span>
        </a>
        <a href="/soluzioni/sanificazione-impianti/" class="app-item">
            <h4>Sanificazione impianti e linee</h4>
            <span class="btn-outline" style="font-size:0.8rem; padding: 5px 10px; margin-top:5px;">Scopri di
                più</span>
        </a>
        <a href="/soluzioni/ossidazione/" class="app-item">
            <h4>Ossidazione contaminanti</h4>
            <span class="btn-outline" style="font-size:0.8rem; padding: 5px 10px; margin-top:5px;">Scopri di
                più</span>
        </a>
    '''
    applicazioni_html = f'''
        <section class="applications-bridge">
            <div class="container-xl">
                <h2 style="font-size: 2rem; margin-bottom: 1.5rem;">
                    Applicazioni dei sistemi a ozono nei diversi contesti
                </h2>
                <p>Dalle problematiche analizzate derivano soluzioni mirate.</p>

                <div class="app-grid">
                    <div class="app-item">
                        <h4>Trattamento aria ambienti produttivi</h4>
                    </div>
                    <div class="app-item">
                        <h4>Disinfezione acqua di processo</h4>
                    </div>
                    <div class="app-item">
                        <h4>Sanificazione impianti e linee</h4>
                    </div>
                    <div class="app-item">
                        <h4>Ossidazione contaminanti</h4>
                    </div>
                </div>
            </div>
        </section>
    '''

    '''
    Scopri il nostro metodo di lavoro → 
    '''
    metodo_html = f'''
        <section style="padding-top: 5rem; padding-bottom: 5rem;">
            <div class="container-lg">
                <h2 style="font-size: 2rem; margin-bottom: 1.5rem; text-align: center;">
                    Perché l'analisi preliminare è fondamentale
                </h2>
                <p class="container-md" style="text-align: center;">
                    Ogni settore richiede un'analisi preliminare specifica per valutare fattibilità, dimensionamento corretto e integrazione sicura del sistema a ozono nel tuo ciclo produttivo esistente.
                </p>
            </div>
        </section>
    '''
    metodo_html = f''
    
    cta_html = f'''
        <section class="final-cta">
            <div class="container-xl">
                <h2 style="font-size: 2rem; margin-bottom: 1rem;">Richiedi analisi tecnica personalizzata</h2>
                <p style="margin-bottom: 20px;">Valutiamo insieme la fattibilità dell'intervento sul tuo impianto.</p>
                <a href="/contatti.html" class="button-blue" style="text-decoration: none;">
                    Richiedi analisi tecnica
                </a>
            </div>
        </section>
    '''

    html = f'''
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="/styles.css">
            <title>Settori industriali per sistemi a ozono</title>
            <meta name="description" content="">
        </head>
        <body>
            {components.header_default()}
            <main>
                {hero_html}
                {settori_html}
                {applicazioni_html}
                {metodo_html}
                {cta_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_folderpath = f'{g.WEBSITE_FOLDERPATH}/settori'
    os.makedirs(html_folderpath, exist_ok=True)
    html_filepath = f'{html_folderpath}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)
