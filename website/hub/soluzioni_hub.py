import os

from lib import g
from lib import components

def main():

    '''
    '''
    background_color = 'rgba(0, 0, 0, 0.5)'
    background_color = 'rgba(0, 30, 60, 0.8)'
    color = f'#fff'
    hero_html = f'''
        <div class="" style="
                background: linear-gradient({background_color}, {background_color}), 
                url('/immagini/soluzioni.jpg');
                background-size: cover;
                background-position: center;
                padding-top: 8.0rem;
                padding-bottom: 8.0rem;
        ">
            <div class="container-lg" style="text-align: center;">
                <h1 style="font-size: 2.5rem; color: {color}; margin-bottom: 2rem;">
                    Soluzioni a ozono per problematiche industriali legate ad aria, acqua e impianti
                </h1>
                <p class="container-md" style="font-size: 1.1rem; color: {color}; margin-bottom: 2rem;">
                    Analizziamo criticità operative nei processi produttivi e progettiamo sistemi a ozono su misura per la loro risoluzione.
                </p>
                <a href="#contact" class="btn" style="text-decoration: none;">Richiedi analisi tecnica</a>
            </div>
        </div>
    '''
    
    ########################################
    # HERO 0001
    ########################################
    h1 = f'Sistemi industriali a ozono su misura per processi produttivi'
    subordinate = f'Progettiamo, realizziamo e integriamo impianti a ozono personalizzati per risolvere problematiche tecniche in ambito industriale.'
    href = '/contatti.html'
    anchor = 'Richiedi una consulenza gratuita'
    hero_0001_html = f'''
        <section class="hero-0001"
            style="background-image: linear-gradient(rgba(0, 30, 60, 0.8), rgba(0, 30, 60, 0.8)), 
            url('/immagini/soluzioni.jpg');
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
    row_0_h2 = f'''Purificazione dell'aria con ozono per eliminare odori, batteri e contaminanti'''
    row_0_subordinate = f'''Per purificare l'aria, i sistemi ad ozono ossidano odori, microrganismi e composti organici volatili presenti negli ambienti o nei condotti HVAC.'''
    row_0_img_src = f'''/immagini/soluzioni-aria.jpg'''
    row_1_h2 = f'''Trattamento dell'acqua con ozono per disinfezione e ossidazione avanzata'''
    row_1_subordinate = f'''Per trattare l'acqua, l'ozono viene dissolto nel flusso idrico per ossidare contaminanti organici, eliminare microrganismi e migliorare qualità, colore e odore dell'acqua.'''
    row_1_img_src = f'''/immagini/soluzioni-acqua.jpg'''
    row_2_h2 = f'''Sanificazione delle superfici con ozono per eliminare microrganismi e residui biologici'''
    row_2_subordinate = f'''Per sanificare le superfici, l'ozono viene diffuso negli ambienti o in camere di trattamento per inattivare batteri, virus, muffe e biofilm su materiali e attrezzature.'''
    row_2_img_src = f'''/immagini/soluzioni-superfici.jpg'''
    # subordinate = f'''Progettiamo e realizziamo impianti a ozono per applicazioni industriali specifiche, adattando ogni soluzione ai processi produttivi del settore di riferimento.'''
    img_height = '400px'
    problemi_html = f'''
        <section class="grid-0004">
            <div class="container-xl grid-0004-content-container">
                <article class="grid-0004-row m-flex">
                    <div class="flex-1">
                        <h2>{row_0_h2}</h2>
                        <p>{row_0_subordinate}</p>
                        <ul style="margin-left: 2rem; margin-bottom: 1rem;">
                            <li style="margin-bottom: 0.8rem;">Odori persistenti in ambienti produttivi</li>
                            <li style="margin-bottom: 0.8rem;">Emissioni VOC non controllate</li>
                            <li style="margin-bottom: 0.8rem;">Non conformità alle normative ambientali</li>
                            <li style="margin-bottom: 0.8rem;">Accumulo contaminanti nei condotti</li>
                            <li style="margin-bottom: 0.8rem;">Carica microbica in ambienti chiusi</li>
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
                            <li style="margin-bottom: 0.8rem;">Elevato COD/BOD negli scarichi</li>
                            <li style="margin-bottom: 0.8rem;">Presenza di contaminanti ossidabili</li>
                            <li style="margin-bottom: 0.8rem;">Biofilm in circuiti chiusi</li>
                            <li style="margin-bottom: 0.8rem;">Non conformità allo scarico</li>
                            <li style="margin-bottom: 0.8rem;">Disinfezione inefficace post-trattamento</li>
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
                            <li style="margin-bottom: 0.8rem;">Biofilm persistente sulle superfici</li>
                            <li style="margin-bottom: 0.8rem;">Contaminazione microbiologica ricorrente</li>
                            <li style="margin-bottom: 0.8rem;">Serbatoi e tubazioni difficili da trattare</li>
                            <li style="margin-bottom: 0.8rem;">Linee produttive complesse</li>
                            <li style="margin-bottom: 0.8rem;">Rischi per sicurezza alimentare (HACCP)</li>
                        </ul>
                    </div>
                    <div class="flex-1">
                        <img src="{row_2_img_src}">
                    </div>
                </article>
            </div>
        </section>
    '''

    if 0:
        gap = f'4rem'
        margin_bottom = gap
        # <a href="#">→ Approfondisci le soluzioni per il trattamento aria</a>
        # <a href="#">→ Approfondisci trattamento acque industriali</a>
        # <a href="#">→ Approfondisci sanificazione impianti</a>
        problemi_html = f'''
        <section class="problems-section">
            <div class="container">
                <div class="problems-grid">
                    
                    <!-- A. ARIA -->
                    <article class="container-xl m-flex" style="align-items: center; gap: {gap}; margin-bottom: {margin_bottom}; margin-top: 8.0rem;">
                        <div class="flex-1">
                            <h2 style="font-size: 2rem; margin-bottom: 1.5rem;">
                                Criticità nella gestione dell'aria di processo
                            </h2>
                            <ul style="margin-left: 2rem; margin-bottom: 1rem;">
                                <li style="margin-bottom: 0.8rem;">Odori persistenti in ambienti produttivi</li>
                                <li style="margin-bottom: 0.8rem;">Emissioni VOC non controllate</li>
                                <li style="margin-bottom: 0.8rem;">Non conformità alle normative ambientali</li>
                                <li style="margin-bottom: 0.8rem;">Accumulo contaminanti nei condotti</li>
                                <li style="margin-bottom: 0.8rem;">Carica microbica in ambienti chiusi</li>
                            </ul>
                            <div style="background-color: #f0f4f8; padding: 1rem; color: #555; font-size: 0.9rem;">
                                <p>
                                <strong>Causa Tecnica:</strong> L'inefficienza dei sistemi di ricirbo e filtrazione standard permette la persistenza di composti organici volatili e la proliferazione batterica, saturando rapidamente i filtri a carboni attivi.
                                </p>
                            </div>
                        </div>
                        <div class="flex-1">
                            <img src="/immagini/soluzioni-aria.jpg">
                        </div>
                    </article>

                    <!-- B. ACQUA -->
                    <article class="container-xl m-flex m-row-reverse" style="align-items: center; gap: {gap}; margin-bottom: {margin_bottom};">
                        <div class="flex-1">
                            <h2 style="font-size: 2rem; margin-bottom: 1rem;">
                                Criticità nel trattamento delle acque industriali
                            </h2>
                            <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                                <li style="margin-bottom: 0.8rem;">Elevato COD/BOD negli scarichi</li>
                                <li style="margin-bottom: 0.8rem;">Presenza di contaminanti ossidabili</li>
                                <li style="margin-bottom: 0.8rem;">Biofilm in circuiti chiusi</li>
                                <li style="margin-bottom: 0.8rem;">Non conformità allo scarico</li>
                                <li style="margin-bottom: 0.8rem;">Disinfezione inefficace post-trattamento</li>
                            </ul>
                            <div style="background-color: #f0f4f8; padding: 1rem; color: #555; font-size: 0.9rem;">
                                <p>
                                <strong>Causa Tecnica:</strong> L'uso di ossidanti chimici tradizionali (cloro) spesso non abbatte completamente il carico organico e favorisce la formazione di sottoprodotti tossici, senza rimuovere efficacemente il biofilm.
                                </p>
                            </div>
                        </div>
                        <div class="flex-1">
                            <img src="/immagini/soluzioni-acqua.jpg">
                        </div>
                    </article>

                    <!-- C. IMPIANTI -->
                    <article class="container-xl m-flex" style="align-items: center; gap: {gap}; margin-bottom: 8.0rem;">
                        <div class="flex-1">
                            <h2 style="font-size: 2rem; margin-bottom: 1rem;">
                                Criticità nella sanificazione di impianti industriali
                            </h2>
                            <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                                <li style="margin-bottom: 0.8rem;">Biofilm persistente sulle superfici</li>
                                <li style="margin-bottom: 0.8rem;">Contaminazione microbiologica ricorrente</li>
                                <li style="margin-bottom: 0.8rem;">Serbatoi e tubazioni difficili da trattare</li>
                                <li style="margin-bottom: 0.8rem;">Linee produttive complesse</li>
                                <li style="margin-bottom: 0.8rem;">Rischi per sicurezza alimentare (HACCP)</li>
                            </ul>
                            <div style="background-color: #f0f4f8; padding: 1rem; color: #555; font-size: 0.9rem;">
                                <p>
                                <strong>Causa Tecnica:</strong> Le procedure di CIP (Cleaning In Place) standard spesso lasciano residui organici che agiscono da substrato per la rigenerazione batterica, rendendo necessari fermi macchina frequenti.
                                </p>
                            </div>
                        </div>
                        <div class="flex-1">
                            <img src="/immagini/soluzioni-superfici.jpg">
                        </div>
                    </article>

                </div>
            </div>
        </section>
        '''

    conseguenze_html = '''
        <section class="impact-section">
            <div class="container-xl">
                <h2 style="font-size: 2rem; margin-bottom: 1rem;">
                    Impatto delle criticità sui processi produttivi
                </h2>
                <p style="color: #fff;">
                    Il mancato controllo delle variabili sopra descritte genera costi occulti significativi.
                </p>
                
                <div class="impact-grid">
                    <div class="impact-item">
                        <strong>Fermi Impianto</strong>
                        <span>Per manutenzione straordinaria e sanificazioni d'emergenza</span>
                    </div>
                    <div class="impact-item">
                        <strong>Costi Chimici</strong>
                        <span>Elevato consumo di reagenti per tentativi di bonifica</span>
                    </div>
                    <div class="impact-item">
                        <strong>Rischi Normativi</strong>
                        <span>Sanzioni per sforamento limiti emissivi o scarichi</span>
                    </div>
                    <div class="impact-item">
                        <strong>Qualità Prodotto</strong>
                        <span>Riduzione della shelf-life e contaminazione crociata</span>
                    </div>
                    <div class="impact-item">
                        <strong>Reputazione</strong>
                        <span>Impatto negativo su clienti e audit di qualità</span>
                    </div>
                </div>
            </div>
        </section>
    '''

    '''
                <div style="text-align: center; margin-top: 30px;">
                    <a href="#">→ Scopri il nostro metodo</a>
                </div>
    '''
    soluzioni_html = f'''
        <section class="solution-section">
            <div class="container-xl">
                <div class="solution-intro">
                    <h2 style="font-size: 2rem; margin-bottom: 1rem;">Come interveniamo per risolvere queste problematiche</h2>
                    <p>Progettiamo sistemi a ozono su misura integrati nei processi produttivi, dimensionati in base a concentrazione, portata e parametri operativi specifici. Non vendiamo macchine standard, ma risolviamo problemi di processo.</p>
                </div>

                <div class="solution-steps">
                    <div class="step">
                        <h3>01. Analisi Tecnica</h3>
                        <p>Rilevamento dati in sito e valutazione delle criticità attuali.</p>
                    </div>
                    <div class="step">
                        <h3>02. Studio di Fattibilità</h3>
                        <p>Calcolo del dosaggio necessario e verifica della compatibilità impiantistica.</p>
                    </div>
                    <div class="step">
                        <h3>03. Integrazione</h3>
                        <p>Installazione del generatore e automazione del processo di ossidazione.</p>
                    </div>
                </div>
            </div>
        </section>
    '''

    cta_html = f'''
        <section class="final-cta">
            <div class="container-xl">
                <h2 style="font-size: 2rem; margin-bottom: 1rem;">Richiedi analisi tecnica personalizzata</h2>
                <p style="margin-bottom: 20px;">Valutiamo insieme la fattibilità dell'intervento sul tuo impianto.</p>
                <a href="#" class="btn1" style="text-decoration: none;">Richiedi analisi tecnica</a>
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
            <title>Soluzioni a ozono per problematiche industriali | Ozonogroup</title>
            <meta name="description" content="">
        </head>
        <body>
            {components.header_default()}
            <main>
                {hero_0001_html}
                {problemi_html}
                {conseguenze_html}
                {soluzioni_html}
                {cta_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_folderpath = f'{g.WEBSITE_FOLDERPATH}/soluzioni'
    os.makedirs(html_folderpath, exist_ok=True)
    html_filepath = f'{html_folderpath}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)
