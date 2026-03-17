import os

from lib import g
from lib import components

def soluzioni__gen():
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
                        <p>Approfondisci <a href="/soluzioni/acqua/">l'ozonizzazione dell'acqua</a> nei sistemi industriali.</p>
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

    ########################################
    # GRID 0005
    ########################################
    h2 = f'''Impatto delle criticità sui processi produttivi'''
    subordinate = f'''Il mancato controllo delle variabili sopra descritte genera costi occulti significativi.'''
    card_0000_h3 = f''
    card_0000_subordinate = f''
    conseguenze_html = f'''
        <section class="grid-0005">
            <div class="container-xl grid-0005-content-container">
                <h2>{h2}</h2>
                <p class="grid-0005-subordinate">{subordinate}</p>
                
                <div class="grid-5 grid-0005-cards">
                    <div class="grid-0005-card">
                        <h3>Fermi Impianto</h3>
                        <p>Per manutenzione straordinaria e sanificazioni d'emergenza</p>
                    </div>
                    <div class="grid-0005-card">
                        <h3>Costi Chimici</h3>
                        <p>Elevato consumo di reagenti per tentativi di bonifica</p>
                    </div>
                    <div class="grid-0005-card">
                        <h3>Rischi Normativi</h3>
                        <p>Sanzioni per sforamento limiti emissivi o scarichi</p>
                    </div>
                    <div class="grid-0005-card">
                        <h3>Qualità Prodotto</h3>
                        <p>Riduzione della shelf-life e contaminazione crociata</p>
                    </div>
                    <div class="grid-0005-card">
                        <h3>Reputazione</h3>
                        <p>Impatto negativo su clienti e audit di qualità</p>
                    </div>
                </div>
            </div>
        </section>
    '''
    
    ########################################
    # GRID 0007
    ########################################
    h2 = f'''Come interveniamo per risolvere queste problematiche'''
    subordinate = f'''Progettiamo sistemi a ozono su misura integrati nei processi produttivi, dimensionati in base a concentrazione, portata e parametri operativi specifici. Non vendiamo macchine standard, ma risolviamo problemi di processo.'''
    card_0000_h3 = f'01. Analisi Tecnica'
    card_0000_subordinate = f'Rilevamento dati in sito e valutazione delle criticità attuali.'
    card_0001_h3 = f'02. Studio di Fattibilità'
    card_0001_subordinate = f'Calcolo del dosaggio necessario e verifica della compatibilità impiantistica.'
    card_0002_h3 = f'03. Integrazione'
    card_0002_subordinate = f'Installazione del generatore e automazione del processo di ossidazione.'
    soluzioni_html = f'''
        <section class="grid-0006">
            <div class="container-xl grid-0006-content-container">
                <h2>{h2}</h2>
                <p class="grid-0006-subordinate">{subordinate}</p>
                <div class="grid-3 grid-0006-cards">
                    <div class="grid-0006-card">
                        <h3>{card_0000_h3}</h3>
                        <p>{card_0000_subordinate}</p>
                    </div>
                    <div class="grid-0006-card">
                        <h3>{card_0001_h3}</h3>
                        <p>{card_0001_subordinate}</p>
                    </div>
                    <div class="grid-0006-card">
                        <h3>{card_0002_h3}</h3>
                        <p>{card_0002_subordinate}</p>
                    </div>
                </div>
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

    if 0:
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
                            <h3>Fermi Impianto</h3>
                            <p>Per manutenzione straordinaria e sanificazioni d'emergenza</p>
                        </div>
                        <div class="impact-item">
                            <h3>Costi Chimici</h3>
                            <p>Elevato consumo di reagenti per tentativi di bonifica</p>
                        </div>
                        <div class="impact-item">
                            <h3>Rischi Normativi</h3>
                            <p>Sanzioni per sforamento limiti emissivi o scarichi</p>
                        </div>
                        <div class="impact-item">
                            <h3>Qualità Prodotto</h3>
                            <p>Riduzione della shelf-life e contaminazione crociata</p>
                        </div>
                        <div class="impact-item">
                            <h3>Reputazione</h3>
                            <p>Impatto negativo su clienti e audit di qualità</p>
                        </div>
                    </div>
                </div>
            </section>
        '''

    if 0:
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
    
    ########################################
    # CTA 0000
    ########################################
    h2 = f'''Richiedi analisi tecnica personalizzata'''
    subordinate = f'''Valutiamo con te la fattibilità dell'intervento sul tuo impianto.'''
    href = '/contatti.html'
    anchor = 'Richiedi analisi tecnica'
    cta_html = f'''
        <section class="cta-0000">
            <div class="container-xl">
                <h2>{h2}</h2>
                <p class="cta-0000-subordinate">{subordinate}</p>
                <div>
                    <a class="cta-0000-link" href="{href}">{anchor}</a>
                </div>
            </div>
        </section>
    '''

    if 0:
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

def soluzioni__acqua__gen():
    
    light_gray = '#f8f8f8'
    ########################################
    # HERO 0001
    ########################################
    h1 = f'''
        Ozonizzazione dell’Acqua: Principi, Applicazioni e Sistemi Industriali
    '''
    subordinate = f'''
        L’ozonizzazione dell’acqua è un processo di trattamento avanzato che utilizza l’ozono (O₃), un potente agente ossidante, per la disinfezione e la rimozione di contaminanti organici e inorganici. Impiegata nei sistemi industriali a ozono, questa tecnologia consente di eliminare microrganismi, degradare microinquinanti e migliorare le caratteristiche organolettiche dell’acqua attraverso reazioni di ossidazione diretta e indiretta, senza lasciare residui chimici persistenti.
    '''
    href = '/contatti.html'
    anchor = 'Richiedi una consulenza gratuita'
    hero_html = f'''
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
    definizione_html = f'''
        <section class="article-section" style="text-align: center;">
            <div class="container-md">
                <h2>
                    Cos'è l'Ozonizzazione dell'Acqua?
                </h2>
                <p>
                    L’ozonizzazione dell’acqua è un processo di trattamento che utilizza l’ozono (O₃), generato in situ tramite sistemi industriali, come agente ossidante e disinfettante per eliminare microrganismi, degradare contaminanti organici e inorganici e migliorare le caratteristiche chimico-fisiche dell’acqua senza lasciare residui persistenti.
                </p>
            </div>
        </section>
    '''
    ########################################
    row_0_h2 = f'''Proprietà Chimico-Fisiche dell’Ozono'''
    row_0_subordinate = f'''L’ozono (O₃) è una molecola triatomica altamente instabile con un elevato potenziale ossidante, caratterizzata da solubilità limitata in acqua, rapida decomposizione in funzione di pH e temperatura, e capacità di generare specie reattive come i radicali ossidrilici che ne determinano l’efficacia nei processi di trattamento.'''
    row_0_img_src = f'''/immagini/placeholder.jpg'''
    img_height = '400px'
    proprieta_html = f'''
        <section class="col-0000" style="background-color: {light_gray};">
            <div class="container-xl col-0000-content-container">
                <div class="col-0000-row m-flex">
                    <div class="flex-1">
                        <h2>{row_0_h2}</h2>
                        <p>{row_0_subordinate}</p>
                    </div>
                    <div class="flex-1">
                        <table>
                            <tr>
                                <th>Proprietà</th>
                                <th>Valore / Caratteristica</th>
                            </tr>
                            <tr>
                                <td>Potenziale Ossidante</td>
                                <td>2,07 V (molto alto, superiore al cloro)</td>
                            </tr>
                            <tr>
                                <td>Solubilità in Acqua</td>
                                <td>Limitata, circa 0,05 g/100 mL a 20°C</td>
                            </tr>
                            <tr>
                                <td>Emivita in Acqua</td>
                                <td>Da pochi minuti a seconda di temperatura, pH e presenza di contaminanti</td>
                            </tr>
                            <tr>
                                <td>Stabilità</td>
                                <td>Instabile, si decompone rapidamente in ossigeno (O₂)</td>
                            </tr>
                            <tr>
                                <td>Reattività</td>
                                <td>Forma radicali ossidrilici (·OH) durante la decomposizione</td>
                            </tr>
                            <tr>
                                <td>pH di Influenza</td>
                                <td>La decomposizione accelera con pH alcalino</td>
                            </tr>
                            <tr>
                                <td>Temperatura di Influenza</td>
                                <td>La stabilità diminuisce con l’aumento della temperatura</td>
                            </tr>
                        </table>
                    </div>
                <div>
            </div>
        </section>
    '''
    principi_html = f'''
        <section class="article-section">
            <div class="container-md">
            <h2>
                Principi di Funzionamento nei Sistemi di Trattamento
            </h2>
            <p>
                Nei sistemi di trattamento delle acque, l’ozonizzazione funziona attraverso la generazione in situ di ozono, la sua efficace dissoluzione nel fluido e il successivo contatto controllato con i contaminanti, dove agisce come potente ossidante sia direttamente sia tramite la formazione di radicali ossidrilici, permettendo la disinfezione e la degradazione chimica delle sostanze indesiderate.
            </p>
            </div>
        </section>
    '''
    meccanismi_html = f'''
        <section class="article-section" style="background-color: {light_gray};">
            <div class="container-md">
            <h2>
                Meccanismi di Ossidazione e Disinfezione
            </h2>
            <p>
                I meccanismi di ossidazione e disinfezione dell’ozono si basano sulla sua elevata capacità ossidante, che agisce sia direttamente reagendo con composti organici e membrane cellulari dei microrganismi, sia indirettamente attraverso la formazione di radicali ossidrilici altamente reattivi, portando alla degradazione dei contaminanti e all’inattivazione efficace di batteri, virus e protozoi.
            </p>
            </div>
        </section>
    '''
    tipologie_html = f'''
        <section class="article-section">
            <div class="container-md">
            <h2>
                Tipologie di Sistemi Industriali a Ozono
            </h2>
            <p>
                Le tipologie di sistemi industriali a ozono si distinguono in base alla modalità di generazione, configurazione impiantistica, metodo di contatto gas-liquido e scala operativa, includendo impianti batch o continui, sistemi a iniezione diretta o con contattori dedicati, e soluzioni modulari o centralizzate progettate per specifiche applicazioni nel trattamento delle acque.
            </p>
            </div>
        </section>
    '''
    componenti_html = f'''
        <section class="article-section" style="background-color: {light_gray};">
            <div class="container-md">
            <h2>
                Componenti degli Impianti di Ozonizzazione
            </h2>
            <p>
                I componenti degli impianti di ozonizzazione sono l’insieme di dispositivi che permettono la produzione, il trasferimento, il contatto e il controllo dell’ozono nell’acqua, includendo tipicamente il generatore di ozono, i sistemi di alimentazione del gas (aria o ossigeno), gli iniettori o diffusori, i reattori di contatto, i sistemi di distruzione dell’ozono residuo e gli strumenti di monitoraggio e automazione del processo.
            </p>
            </div>
        </section>
    '''
    parametri_html = f'''
        <section class="article-section">
            <div class="container-md">
            <h2>
                Parametri Operativi e di Processo
            </h2>
            <p>
                I parametri operativi e di processo nell’ozonizzazione dell’acqua comprendono la concentrazione di ozono, il tempo di contatto con l’acqua, la portata del flusso, la temperatura e il pH, oltre all’efficienza di trasferimento del gas e alla gestione della domanda chimica dell’acqua, tutti fattori determinanti per garantire una disinfezione efficace e la degradazione dei contaminanti.
            </p>
            </div>
        </section>
    '''
    applicazioni_html = f'''
        <section class="article-section" style="background-color: {light_gray};">
            <div class="container-md">
            <h2>
                Applicazioni nel Trattamento delle Acque
            </h2>
            <p>
                L’ozonizzazione dell’acqua viene impiegata per la disinfezione di acqua potabile, la depurazione di acque reflue industriali e civili, la rimozione di composti organici, pesticidi e microinquinanti, il controllo di odori e sapori, la prevenzione della proliferazione di microrganismi in torri di raffreddamento, piscine e impianti di acquacoltura, e come trattamento preliminare o integrativo nei processi di purificazione avanzata.
            </p>
            </div>
        </section>
    '''
    rimozione_html = f'''
        <section class="article-section">
            <div class="container-md">
            <h2>
                Rimozione dei Contaminanti
            </h2>
            <p>
                L’ozono rimuove efficacemente batteri, virus, protozoi, composti organici, pesticidi, farmaci, metalli e sostanze responsabili di odore, sapore e colore attraverso reazioni di ossidazione diretta e indiretta che degradano i contaminanti in composti meno dannosi o facilmente filtrabili.
            </p>
            </div>
        </section>
    '''
    integrazione_html = f'''
        <section class="article-section" style="background-color: {light_gray};">
            <div class="container-md">
            <h2>
                Integrazione con Altri Processi di Trattamento
            </h2>
            <p>
                L’ozonizzazione dell’acqua si integra con altri processi di trattamento come filtrazione, carbone attivo, raggi UV e clorazione per aumentare l’efficacia complessiva nella rimozione di microrganismi, composti organici, odori e colori, e può essere combinata con processi di ossidazione avanzata (AOP) per degradare contaminanti refrattari e micropollutanti.
            </p>
            </div>
        </section>
    '''
    vantaggi_html = f'''
        <section class="article-section">
            <div class="container-md">
            <h2>
                Vantaggi e Limiti della Tecnologia
            </h2>
            <p>
                L’ozonizzazione dell’acqua offre vantaggi come un’elevata efficacia nella disinfezione, la rimozione di microinquinanti e composti organici, l’assenza di residui chimici persistenti e il miglioramento delle caratteristiche organolettiche, ma presenta limiti legati all’instabilità dell’ozono, ai costi energetici elevati, alla complessità impiantistica e alla possibile formazione di sottoprodotti come i bromati.
            </p>
            </div>
        </section>
    '''
    sicurezza_html = f'''
        <section class="article-section" style="background-color: {light_gray};">
            <div class="container-md">
            <h2>
                Vantaggi e Limiti della Tecnologia
            </h2>
            <p>
                La gestione dell’ozono nei sistemi industriali richiede procedure rigorose per prevenire esposizioni pericolose, comprendendo l’uso di sensori di rilevamento, sistemi di ventilazione, abbattitori di ozono residuo e formazione specifica del personale per garantire livelli di sicurezza conformi agli standard normativi.
            </p>
            </div>
        </section>
    '''
    controllo_html = f'''
        <section class="article-section">
            <div class="container-md">
            <h2>
                Controllo, Monitoraggio e Automazione
            </h2>
            <p>
                Il controllo, il monitoraggio e l’automazione nei sistemi di trattamento dell’acqua con ozono consistono nell’utilizzo di sensori per rilevare la concentrazione di ozono disciolto, il potenziale ossidante (ORP) e i parametri operativi come flusso e pressione, integrati con sistemi di regolazione automatica e PLC per garantire dosaggi precisi, tempi di contatto ottimali e sicurezza operativa continua.
            </p>
            </div>
        </section>
    '''
    normative_html = f'''
        <section class="article-section" style="background-color: {light_gray};">
            <div class="container-md">
            <h2>
                Normative e Standard di Qualità
            </h2>
            <p>
                Le normative e gli standard di qualità per l’ozonizzazione dell’acqua stabiliscono i limiti massimi di concentrazione di ozono residuo, i valori consentiti di sottoprodotti come i bromati, le linee guida per la sicurezza degli operatori e i requisiti di efficacia nella disinfezione, seguendo le direttive europee, le norme nazionali sull’acqua potabile e le raccomandazioni dell’Organizzazione Mondiale della Sanità.
            </p>
            </div>
        </section>
    '''
    efficienza_html = f'''
        <section class="article-section">
            <div class="container-md">
            <h2>
                Efficienza Energetica e Costi Operativi
            </h2>
            <p>
                L’efficienza energetica e i costi operativi di un sistema di ozonizzazione dipendono dalla potenza del generatore di ozono, dalla concentrazione e dalla portata dell’acqua trattata, dal tempo di contatto richiesto, dall’efficienza del trasferimento gas-liquido e dalla manutenzione dei componenti, e rappresentano il principale fattore di valutazione economica per l’adozione industriale della tecnologia.
            </p>
            </div>
        </section>
    '''
    impatti_html = f'''
        <section class="article-section" style="background-color: {light_gray};">
            <div class="container-md">
            <h2>
                Impatti Ambientali e Sostenibilità
            </h2>
            <p>
                L’ozonizzazione dell’acqua riduce significativamente l’uso di prodotti chimici tradizionali come cloro e biossido di cloro, non produce residui persistenti nell’ambiente e consente una disinfezione efficace con un minore impatto energetico, contribuendo a processi industriali più sostenibili e al miglioramento della qualità ambientale delle acque trattate.
            </p>
            </div>
        </section>
    '''
    innovazioni_html = f'''
        <section class="article-section">
            <div class="container-md">
            <h2>
                Innovazioni Tecnologiche e Ricerca
            </h2>
            <p>
                Le innovazioni tecnologiche nel trattamento dell’acqua con ozono includono generatori a corona migliorati, sistemi di dosaggio automatizzati basati su sensori in tempo reale, integrazione con processi di ossidazione avanzata (AOP) e ottimizzazione energetica, mentre la ricerca si concentra sull’efficacia nella rimozione di microinquinanti emergenti, sulla riduzione dei sottoprodotti indesiderati e sull’implementazione di soluzioni intelligenti per il monitoraggio e il controllo industriale.
            </p>
            </div>
        </section>
    '''
    progettazione_html = f'''
        <section class="article-section" style="background-color: {light_gray};">
            <div class="container-md">
            <h2>
                Progettazione e Dimensionamento degli Impianti
            </h2>
            <p>
                La progettazione e il dimensionamento degli impianti di ozonizzazione richiedono la valutazione precisa della portata d’acqua, del carico inquinante, della concentrazione richiesta di ozono, del tempo di contatto necessario per garantire la disinfezione e l’ossidazione dei contaminanti, nonché la scelta dei componenti adeguati come generatori di ozono, iniettori e contattori, in modo da ottimizzare l’efficienza del trasferimento gas-liquido, ridurre i consumi energetici e garantire sicurezza operativa e conformità normativa.
            </p>
            </div>
        </section>
    '''

    main_html = f'''
        {hero_html}
        {definizione_html}
        {proprieta_html}
        {principi_html}
        {meccanismi_html}
        {tipologie_html}
        {componenti_html}
        {parametri_html}
        {applicazioni_html}
        {rimozione_html}
        {integrazione_html}
        {vantaggi_html}
        {sicurezza_html}
        {controllo_html}
        {normative_html}
        {efficienza_html}
        {impatti_html}
        {innovazioni_html}
        {progettazione_html}
    '''
    main_html = main_html.replace('’', "'")
    
    '''
    H1: Ozonizzazione dell’Acqua: Principi, Applicazioni e Sistemi Industriali

    1. Definizione e Concetto di Ozonizzazione
    2. Proprietà Chimico-Fisiche dell’Ozono
    3. Principi di Funzionamento nei Sistemi di Trattamento
    4. Meccanismi di Ossidazione e Disinfezione
    5. Tipologie di Sistemi Industriali a Ozono
    6. Componenti degli Impianti di Ozonizzazione
    7. Parametri Operativi e di Processo
    8. Applicazioni nel Trattamento delle Acque
    9. Rimozione dei Contaminanti
    10. Integrazione con Altri Processi di Trattamento
    11. Vantaggi e Limiti della Tecnologia
    12. Sicurezza e Gestione dell’Ozono
    13. Controllo, Monitoraggio e Automazione
    14. Normative e Standard di Qualità
    15. Efficienza Energetica e Costi Operativi
    16. Impatti Ambientali e Sostenibilità
    17. Innovazioni Tecnologiche e Ricerca
    18. Progettazione e Dimensionamento degli Impianti
    '''

    meta_title = f'''Ozonizzazione dell'Acqua: Principi, Applicazioni e Sistemi Industriali'''
    html = f'''
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="/styles.css">
            <title>{meta_title}</title>
            <meta name="description" content="">
        </head>
        <body>
            {components.header_default()}
            <main>
                {main_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''

    html_folderpath = f'{g.WEBSITE_FOLDERPATH}/soluzioni/acqua'
    os.makedirs(html_folderpath, exist_ok=True)
    html_filepath = f'{html_folderpath}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)

def main():
    soluzioni__gen()
    soluzioni__acqua__gen()
    
    