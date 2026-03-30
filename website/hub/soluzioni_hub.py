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
        <section class="article-section">
            <div class="container-md">
                <h2>
                    Cos'è l'Ozonizzazione dell'Acqua?
                </h2>
                <p>
L’ozonizzazione dell’acqua è un processo di trattamento che utilizza l’ozono (O₃), un gas altamente ossidante composto da tre atomi di ossigeno, per migliorare la qualità dell’acqua attraverso reazioni chimiche di ossidazione e l’inattivazione di microrganismi. 
                </p>
                <p>
Grazie al suo elevato potenziale di ossidazione (circa 2,07 V), l’ozono è in grado di distruggere batteri, virus e altri patogeni e di ossidare numerosi composti organici e inorganici presenti nell’acqua. A differenza della clorazione, che lascia un residuo chimico persistente nell’acqua trattata, l’ozono si decompone rapidamente tornando a ossigeno molecolare, mentre rispetto alla disinfezione con radiazione UV offre anche un’azione chimica di ossidazione dei contaminanti oltre alla sola inattivazione microbiologica. Nei sistemi di trattamento delle acque, l’ozonizzazione viene generalmente impiegata come fase intermedia o avanzata del processo per migliorare la qualità chimica e microbiologica dell’acqua prima delle fasi finali di trattamento. 
                </p>
                <p>
Questa tecnologia può essere applicata a diverse tipologie di acqua, tra cui acqua potabile, acque reflue civili e industriali e acque di processo, con l’obiettivo di ottenere disinfezione efficace, ossidazione dei contaminanti e miglioramento delle caratteristiche sensoriali come odore, colore e sapore.
                </p>
                <dl>
<dt>Ozonizzazione</dt>
<dd>Processo di trattamento dell’acqua che utilizza ozono disciolto come agente ossidante e disinfettante.</dd>

<dt>Ozono (O3)</dt>
<dd>Molecola triatomica di ossigeno con elevato potenziale di ossidazione.</dd>

<dt>Trattamento acqua</dt>
<dd>Applicazione dell’ozono per migliorare qualità microbiologica e chimica dell’acqua.</dd>
</dl>
            </div>
        </section>
    '''

    ########################################
    row_0_h2 = f'''Proprietà Chimico-Fisiche dell’Ozono'''
    row_0_subordinate = f'''
        L’ozono (O₃) è una molecola triatomica altamente instabile con un elevato potenziale ossidante, caratterizzata da solubilità limitata in acqua, rapida decomposizione in funzione di pH e temperatura, e capacità di generare specie reattive come i radicali ossidrilici che ne determinano l’efficacia nei processi di trattamento.
    '''
    row_0_img_src = f'''/immagini/placeholder.jpg'''
    img_height = '400px'
    proprieta_html = f'''
        <section class="col-0000" style="background-color: {light_gray};">
            <div class="container-md">
                        <h2>{row_0_h2}</h2>
                        <p>
L’ozono (O₃) è una molecola triatomica costituita da tre atomi di ossigeno disposti in una struttura angolare instabile, caratterizzata da un elevato potenziale di ossidazione pari a circa 2,07 V, superiore a quello del cloro e quindi particolarmente efficace nei processi di ossidazione chimica in acqua. 
                    </p>
                        <p>
In condizioni standard è un gas di colore blu pallido con una solubilità in acqua moderata ma superiore a quella dell’ossigeno molecolare, con valori tipici di circa 10–13 mg/L a 0 °C e pressione atmosferica, solubilità che diminuisce rapidamente con l’aumento della temperatura. Dal punto di vista della stabilità chimica l’ozono è una specie fortemente instabile e tende a decomporsi spontaneamente tornando a ossigeno molecolare (O₂), con una velocità di decomposizione influenzata da fattori come temperatura, pH e presenza di sostanze catalitiche nell’acqua. In acqua pura a 20 °C il tempo di emivita è generalmente compreso tra 10 e 20 minuti, mentre in aria è molto più breve, spesso inferiore ai 30 minuti, e si riduce ulteriormente all’aumentare della temperatura o in condizioni alcaline, dove la decomposizione è accelerata. 
                    </p>
                        <p>
In fase gassosa l’ozono è relativamente più stabile ma reagisce rapidamente con superfici e contaminanti atmosferici, mentre in fase liquida è più reattivo e soggetto a trasformazioni chimiche rapide dovute alle interazioni con le specie disciolte presenti nell’acqua.
                    </p>
                        <table>
                        <thead>
                            <tr>
                                <th>Proprietà</th>
                                <th>Valore / Caratteristica</th>
                            </tr>
                        </thead>
                        <tbody>

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
                        </tbody>
                        </table>
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
Nei sistemi industriali di trattamento, l’ozonizzazione funziona generando ozono in loco e trasferendolo efficacemente dall’aria o dall’ossigeno all’acqua tramite dispositivi progettati per massimizzare il contatto tra le due fasi. 
</p>
<p>
L’ozono viene prodotto principalmente tramite scarica a corona, dove un campo elettrico ad alta tensione (tipicamente 5–20 kV) dissocia le molecole di ossigeno (O₂) permettendo la formazione di O₃; l’efficienza del processo dipende fortemente dalla qualità del gas di alimentazione, che può essere aria essiccata o ossigeno puro, con quest’ultimo che consente concentrazioni di ozono più elevate e maggiore resa energetica. Il gas ozonizzato viene poi iniettato nell’acqua tramite iniettori Venturi o diffusori, creando microbolle che aumentano la superficie di scambio e migliorano il trasferimento di massa gas-liquido. La miscelazione e il contatto avvengono in appositi contattori (colonne o vasche), dimensionati per garantire un tempo di permanenza sufficiente affinché l’ozono si dissolva e reagisca. 
</p>
<p>
Infine, il gas residuo non disciolto viene separato e convogliato verso sistemi di distruzione, evitando dispersioni e garantendo la sicurezza operativa.
</p>
<p>
La seguente lista elenca le fasi del principio di funzionamento:
</p>
<ol>
<li>Produzione dell’ozono tramite scarica a corona</li>
<li>Preparazione del gas di alimentazione (aria o ossigeno)</li>
<li>Iniezione dell’ozono nel flusso d’acqua</li>
<li>Miscelazione gas-liquido</li>
<li>Contatto nel reattore di ozonizzazione</li>
<li>Separazione del gas residuo</li>
</ol>
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
L’ozonizzazione dell’acqua funziona grazie a due meccanismi principali: l’ossidazione diretta operata dall’ozono molecolare (O₃) e l’ossidazione indiretta mediata dai radicali ossidrilici (•OH), entrambi responsabili della degradazione chimica dei contaminanti e della disinfezione microbiologica. 
                </p>
                <p>
L’ozono molecolare reagisce in modo selettivo con doppi legami, gruppi aromatici e composti contenenti zolfo o azoto, ossidando sostanze organiche complesse e trasformandole in molecole più semplici o biodegradabili, mentre nei sistemi acquosi può decomporsi generando radicali •OH, caratterizzati da un potenziale ossidante superiore e da una reattività non selettiva. Nei confronti dei composti inorganici, l’ozono ossida specie come Fe²⁺ e Mn²⁺ a forme insolubili (Fe³⁺, Mn⁴⁺), facilitandone la successiva rimozione, mentre sul piano microbiologico inattiva batteri, virus e protozoi attraverso l’ossidazione delle membrane cellulari e dei componenti intracellulari, causando perdita di integrità e morte cellulare. La velocità e l’efficacia di queste reazioni dipendono dalla cinetica chimica, influenzata da parametri come concentrazione di ozono, natura dei contaminanti e condizioni del mezzo, con reazioni dirette generalmente più lente ma selettive e reazioni radicaliche estremamente rapide ma meno specifiche. 
                </p>
                <p>
Ad esempio, composti organici come fenoli vengono rapidamente degradati tramite attacco radicalico, mentre microrganismi vengono inattivati in pochi secondi grazie alla distruzione delle membrane e all’ossidazione di proteine ed enzimi vitali.
                </p>
                <p>
                Lista di reazioni chimiche:
                </p>
                <ul>
<li>Ossidazione diretta tramite molecola O3</li>
<li>Formazione di radicali ossidrilici (•OH)</li>
<li>Ossidazione di composti organici</li>
<li>Ossidazione di composti inorganici</li>
<li>Distruzione delle membrane cellulari dei microrganismi</li>
</ul>
            </div>
        </section>
    '''
                # <img class="img-original" src="/immagini/diagramma-principio-trattamento-acqua-ozono.png">
    tipologie_html = f'''
        <section class="article-section">
            <div class="container-md">
            <h2>
                Tipologie di Sistemi Industriali a Ozono
            </h2>
            <p>
Le tipologie di sistemi industriali a ozono si distinguono principalmente in base alla modalità di trattamento del flusso idrico e alla configurazione impiantistica, includendo sistemi a flusso continuo, batch, modulari, centralizzati e skid-mounted, oltre a diverse soluzioni di contatto come inline o in vasca. 
            </p>
            <p>
Nei sistemi a flusso continuo l’acqua viene trattata senza interruzioni con portate costanti, tipicamente da pochi m³/h fino a oltre 10.000 m³/h negli impianti municipali, mentre nei sistemi batch il trattamento avviene in volumi definiti, utile per processi discontinui o serbatoi di accumulo. Gli impianti modulari sono costituiti da unità scalabili installate in parallelo, permettendo un aumento graduale della capacità senza modifiche strutturali rilevanti, mentre gli impianti centralizzati su larga scala concentrano la produzione di ozono in un’unica infrastruttura per servire grandi portate con elevata efficienza operativa. I sistemi skid-mounted integrano tutti i componenti su una piattaforma prefabbricata, riducendo tempi di installazione e complessità in sito, e sono tipicamente utilizzati per portate medio-basse o applicazioni industriali specifiche. 
            </p>
            <p>
Infine, nelle configurazioni inline l’ozono viene iniettato direttamente in linea con tempi di contatto ridotti e controllo dinamico, mentre nei sistemi con vasca di contatto si utilizzano reattori dedicati per garantire tempi di permanenza più lunghi e maggiore uniformità di trattamento.
            </p>
            <table>
<thead>
<tr>
<th>Tipo di sistema</th>
<th>Descrizione</th>
<th>Applicazione tipica</th>
</tr>
</thead>
<tbody>
<tr>
<td>Batch</td>
<td>Trattamento in serbatoio</td>
<td>Processi discontinui</td>
</tr>
<tr>
<td>Flusso continuo</td>
<td>Ozonizzazione inline</td>
<td>Impianti municipali</td>
</tr>
<tr>
<td>Modulare</td>
<td>Unità prefabbricate</td>
<td>Industria</td>
</tr>
</tbody>
</table>
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
Un impianto di ozonizzazione è costituito da una catena di componenti progettati per generare, trasferire e gestire in sicurezza l’ozono fino al suo completo utilizzo e abbattimento. 
            </p>
            <p>
Il generatore di ozono, basato tipicamente su scarica a corona, produce O₃ a partire da ossigeno fornito da sistemi di alimentazione gas (compressori o concentratori di O₂), mentre gli essiccatori d’aria riducono l’umidità sotto valori critici (generalmente < -40 °C punto di rugiada) per garantire efficienza e stabilità del processo. L’ozono viene poi iniettato nell’acqua tramite iniettori Venturi o diffusori, che permettono un trasferimento efficace gas-liquido creando microbolle e aumentando la superficie di contatto. Il contatto tra ozono e acqua avviene in appositi reattori, come colonne o vasche di contatto, progettati per massimizzare la dissoluzione e limitare le perdite di gas. 
            </p>
            <p>
L’ozono non disciolto viene trattato tramite distruttori catalitici o termici prima del rilascio, mentre tutte le tubazioni e i componenti sono realizzati in materiali compatibili (come acciaio inox, PTFE o PVDF) per resistere all’elevato potere ossidante dell’ozono.
            </p>
            <ul>
<li>Generatore di ozono</li>
<li>Compressore o alimentazione gas</li>
<li>Essiccatore dell’aria</li>
<li>Iniettore Venturi</li>
<li>Reattore di contatto</li>
<li>Distruttore di ozono residuo</li>
</ul>
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
I parametri operativi definiscono quanta quantità di ozono viene effettivamente trasferita all’acqua e per quanto tempo rimane disponibile per reagire, determinando direttamente l’efficacia del trattamento. 
            </p>
            <p>
La dose di ozono applicata dipende dalla domanda di ozono dell’acqua, cioè dalla quantità di sostanze ossidabili presenti, e tipicamente varia da 0,5 a 5 mg/L per acque potabili fino a oltre 10 mg/L in acque industriali più contaminate; questa dose è legata alla concentrazione di ozono in ingresso (generalmente 1–10% in peso nel gas) e alla portata dell’acqua, che influisce sul tempo disponibile per il contatto. Il parametro chiave è il valore CT (concentrazione × tempo), che rappresenta l’esposizione complessiva all’ozono e che, ad esempio, per la disinfezione può richiedere valori nell’ordine di 0,5–5 mg·min/L a seconda del microrganismo target. L’efficienza di trasferimento gas-liquido, spesso compresa tra il 70% e il 95% nei sistemi ben progettati, è influenzata da pressione operativa, dimensione delle bolle e qualità dell’acqua in ingresso, inclusi torbidità e presenza di sostanze organiche che consumano ozono. 
            </p>
            <p>
Ad esempio, un’acqua con alta domanda di ozono e alta portata richiederà una dose maggiore e un sistema di contatto più efficiente per mantenere lo stesso livello di trattamento rispetto a un’acqua già parzialmente trattata.
            </p>
            <table>
<thead>
<tr>
<th>Parametro</th>
<th>Unità</th>
<th>Descrizione</th>
</tr>
</thead>
<tbody>
<tr>
<td>Dose di ozono</td>
<td>mg/L</td>
<td>Quantità di ozono applicata</td>
</tr>
<tr>
<td>Tempo di contatto</td>
<td>min</td>
<td>Durata reazione ozono-acqua</td>
</tr>
<tr>
<td>Portata</td>
<td>m³/h</td>
<td>Flusso acqua trattata</td>
</tr>
<tr>
<td>Concentrazione ozono</td>
<td>g/Nm³</td>
<td>Concentrazione nel gas</td>
</tr>
</tbody>
</table>
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
L’ozonizzazione dell’acqua viene applicata in diversi ambiti per migliorare la qualità dell’acqua attraverso disinfezione e ossidazione selettiva dei contaminanti, adattandosi sia a usi civili che industriali. 
            </p>
            <p>
Nel trattamento dell’acqua potabile è impiegata per eliminare microrganismi e composti responsabili di odori e sapori, mentre nelle acque reflue civili consente di ridurre il carico organico residuo e migliorare la qualità dell’effluente prima dello scarico o del riuso. Nelle acque reflue industriali trova applicazione nella degradazione di composti complessi e difficilmente biodegradabili, come coloranti, fenoli o residui farmaceutici, con concentrazioni di ozono tipicamente più elevate rispetto al settore civile. In ambito alimentare e delle bevande viene utilizzata per sanificare acqua di processo e superfici senza lasciare residui, mentre in acquacoltura, piscine e torri di raffreddamento garantisce il controllo microbiologico continuo e la riduzione dei biofilm. 
            </p>
            <p>
Infine, nei sistemi di riutilizzo delle acque, l’ozono rappresenta uno stadio chiave per ottenere standard qualitativi elevati, rendendo l’acqua idonea a impieghi agricoli, industriali o civili non potabili.
            </p>
            <ul>
<li>Acqua potabile</li>
<li>Acque reflue civili</li>
<li>Acque reflue industriali</li>
<li>Industria alimentare</li>
<li>Piscine e centri benessere</li>
<li>Acquacoltura</li>
</ul>
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
L’ozonizzazione rimuove i contaminanti dall’acqua attraverso un’azione combinata di disinfezione e ossidazione chimica ad alto potenziale, capace di inattivare microrganismi e trasformare sostanze indesiderate in composti più semplici o filtrabili. 
            </p>
            <p>
In termini microbiologici, l’ozono garantisce una rapida disinfezione batterica (log removal elevati anche a basse concentrazioni), inattiva virus mediante danneggiamento del materiale genetico ed elimina protozoi resistenti come Giardia e Cryptosporidium grazie all’ossidazione delle membrane cellulari. Dal punto di vista chimico, ossida composti organici complessi (come pesticidi e residui farmaceutici), contribuendo alla rimozione dei microinquinanti emergenti e alla riduzione del carico organico disciolto. Parallelamente, degrada le sostanze responsabili di colore, odori e sapori (ad esempio composti fenolici o geosmina), migliorando le caratteristiche organolettiche dell’acqua. 
            </p>
            <p>
Infine, ossida metalli come ferro e manganese trasformandoli in forme insolubili facilmente separabili tramite filtrazione, rendendo il processo particolarmente efficace nei trattamenti di affinamento delle acque potabili e industriali.
            </p>
            <table>
<thead>
<tr>
<th>Categoria</th>
<th>Esempi</th>
</tr>
</thead>
<tbody>
<tr>
<td>Microrganismi</td>
<td>Batteri, virus, protozoi</td>
</tr>
<tr>
<td>Composti organici</td>
<td>Pesticidi, farmaci</td>
</tr>
<tr>
<td>Metalli</td>
<td>Ferro, manganese</td>
</tr>
<tr>
<td>Parametri estetici</td>
<td>Colore, odori</td>
</tr>
</tbody>
</table>
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
L’ozonizzazione non è normalmente utilizzata come processo isolato, ma viene integrata in sequenze multi-stadio per massimizzare l’efficacia complessiva del trattamento dell’acqua. 
            </p>
            <p>
In pre-ozonizzazione, l’ozono viene applicato a monte per ossidare composti organici complessi, migliorare la biodegradabilità e facilitare le fasi successive come filtrazione su sabbia o membrane, riducendo il fouling e aumentando l’efficienza di rimozione. In post-ozonizzazione, invece, viene utilizzato come fase finale per affinare la qualità dell’acqua, eliminare microinquinanti residui e migliorare le caratteristiche organolettiche prima della distribuzione o riutilizzo. L’integrazione con carbone attivo (GAC o biologico BAC) è particolarmente efficace: l’ozono trasforma composti refrattari in sostanze più facilmente adsorbibili o biodegradabili, creando una sinergia che aumenta la rimozione complessiva dei contaminanti. 
            </p>
            <p>
L’accoppiamento con UV consente di generare radicali ossidrilici altamente reattivi nei processi AOP, mentre le configurazioni multi-stadio combinano queste tecnologie in sequenze ottimizzate in funzione della qualità dell’acqua e degli obiettivi di trattamento.
            </p>
            <ol>
<li>Pre-filtrazione</li>
<li>Ozonizzazione</li>
<li>Filtrazione su carbone attivo</li>
<li>Filtrazione finale</li>
<li>Disinfezione finale</li>
</ol>
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
L’ozonizzazione dell’acqua è una tecnologia altamente efficace perché combina una forte capacità ossidante e un ampio spettro di disinfezione, ma presenta limiti legati alla gestione dell’ozono e alla complessità impiantistica. 
            </p>
            <p>
L’ozono ha un potenziale redox di circa 2,07 V, superiore al cloro, e permette quindi di ossidare rapidamente composti organici e inattivare batteri, virus e protozoi in tempi ridotti, contribuendo anche alla rimozione di odori, sapori e colore migliorando le caratteristiche organolettiche dell’acqua. A differenza dei disinfettanti tradizionali, non lascia residui persistenti perché si decompone in ossigeno, riducendo l’impatto chimico sul sistema trattato. Tuttavia, questa stessa instabilità impone la produzione in loco tramite generatori dedicati, aumentando la complessità e i costi tecnici rispetto a soluzioni più semplici. 
            </p>
            <p>
Inoltre, in presenza di specifici precursori come il bromo, possono formarsi sottoprodotti indesiderati (ad esempio bromati), rendendo necessario un controllo accurato delle condizioni operative e della qualità dell’acqua in ingresso.
            </p>
            <table>
<thead>
<tr>
<th>Vantaggi</th>
<th>Limiti</th>
</tr>
</thead>
<tbody>
<tr>
<td>Elevato potere ossidante</td>
<td>Instabilità dell’ozono</td>
</tr>
<tr>
<td>Nessun residuo chimico</td>
<td>Produzione in loco necessaria</td>
</tr>
<tr>
<td>Ampio spettro di disinfezione</td>
<td>Consumo energetico</td>
</tr>
</tbody>
</table>
            </div>
        </section>
    '''
    sicurezza_html = f'''
        <section class="article-section" style="background-color: {light_gray};">
            <div class="container-md">
            <h2>
                Sicurezza e Gestione dell’Ozono
            </h2>
            <p>
La sicurezza nella gestione dell’ozono nei sistemi di trattamento acqua si basa sul controllo rigoroso dell’esposizione, sulla prevenzione delle perdite e sull’adozione di sistemi tecnici e procedure operative adeguate, poiché l’ozono è un gas altamente ossidante e tossico per l’uomo. 
            </p>
            <p>
A concentrazioni superiori a 0,1 ppm può causare irritazione delle vie respiratorie, mentre i limiti di esposizione professionale tipicamente accettati sono di circa 0,1 ppm per esposizioni prolungate (8 ore) e fino a 0,3 ppm per esposizioni brevi, rendendo necessario un monitoraggio continuo negli ambienti chiusi. Il rischio principale è legato a eventuali perdite dai generatori o dalle linee di iniezione, con possibile accumulo in locali poco ventilati, motivo per cui è essenziale progettare sistemi di ventilazione forzata e installare distruttori di ozono residuo per convertire l’O₃ in ossigeno prima del rilascio in atmosfera. Dal punto di vista operativo, sono indispensabili procedure standard che includano rilevamento automatico delle fughe, allarmi, evacuazione controllata e manutenzione programmata delle apparecchiature. 
            </p>
            <p>
Infine, la formazione degli operatori è critica: il personale deve essere in grado di riconoscere i rischi, interpretare i dati dei sensori e intervenire correttamente in caso di anomalie o emergenze.
            </p>
            <ul>
<li>Monitoraggio delle concentrazioni di ozono</li>
<li>Sistemi di ventilazione</li>
<li>Distruzione dell’ozono residuo</li>
<li>Procedure di emergenza</li>
<li>Formazione degli operatori</li>
</ul>
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
Il controllo, monitoraggio e automazione nei sistemi di ozonizzazione servono a garantire che la concentrazione di ozono sia sempre efficace per il trattamento ma senza superare limiti operativi e di sicurezza, attraverso una gestione continua e in tempo reale del processo. 
            </p>
            <p>
Questo si realizza utilizzando sensori di ozono in aria per rilevare eventuali fughe e proteggere gli operatori, sensori di ozono disciolto per misurare la quantità effettivamente disponibile in acqua e strumenti di misurazione ORP per valutare indirettamente il potenziale ossidante del sistema. I dati raccolti vengono elaborati da sistemi PLC e supervisionati tramite interfacce SCADA, che permettono il controllo automatico della dose di ozono in funzione della qualità dell’acqua e della domanda istantanea. Ad esempio, un aumento del carico organico rilevato dai sensori può attivare automaticamente un incremento della produzione di ozono, mantenendo stabile l’efficienza del trattamento. 
            </p>
            <p>
Inoltre, sistemi di allarme segnalano anomalie o superamenti di soglia, mentre la registrazione continua dei dati consente analisi storiche, ottimizzazione operativa e manutenzione predittiva.
            </p>
            <table>
<thead>
<tr>
<th>Strumento</th>
<th>Funzione</th>
</tr>
</thead>
<tbody>
<tr>
<td>Sensore ozono</td>
<td>Misura concentrazione ozono</td>
</tr>
<tr>
<td>ORP meter</td>
<td>Misura potenziale redox</td>
</tr>
<tr>
<td>PLC</td>
<td>Controllo automatico impianto</td>
</tr>
<tr>
<td>SCADA</td>
<td>Supervisione del sistema</td>
</tr>
</tbody>
</table>
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
Le normative e gli standard di qualità per l’ozonizzazione dell’acqua stabiliscono limiti precisi sia per la concentrazione di ozono residuo sia per i sottoprodotti derivati dal processo, come i bromati, che devono rimanere al di sotto di 10 µg/L secondo le linee guida europee e dell’OMS. 
            </p>
            <p>
In Europa, la Direttiva 98/83/CE sull’acqua potabile definisce requisiti di sicurezza chimica e microbiologica che gli impianti a ozono devono rispettare, mentre le linee guida dell’Organizzazione Mondiale della Sanità forniscono indicazioni aggiuntive sui limiti di esposizione e sui criteri di efficacia. Gli impianti industriali e alimentari devono inoltre ottenere certificazioni specifiche, come ISO 9001 per la gestione della qualità e certificazioni HACCP per il trattamento dell’acqua destinata al contatto con alimenti. I sistemi devono essere progettati per garantire un dosaggio controllato e un monitoraggio continuo, assicurando che l’acqua trattata soddisfi i requisiti chimici e microbiologici richiesti. 
            </p>
            <p>
Ad esempio, un impianto di ozonizzazione per acqua potabile in un comune europeo deve documentare la concentrazione di ozono e i livelli di sottoprodotti almeno quotidianamente per dimostrare la conformità normativa.
            </p>
            <ul>
<li>Direttiva europea acqua potabile</li>
<li>Linee guida OMS</li>
<li>Standard EPA per disinfezione</li>
<li>Limiti per bromati</li>
</ul>
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
L’efficienza energetica e i costi operativi di un sistema di ozonizzazione dipendono principalmente dal consumo elettrico dei generatori di ozono e dall’efficienza con cui l’energia viene convertita in ozono utile per il trattamento dell’acqua.
            </p>
            <p>
Nei generatori industriali a scarica corona moderni il consumo specifico varia tipicamente tra 8 e 15 kWh per kg di ozono prodotto quando si utilizza ossigeno puro come gas di alimentazione, mentre l’efficienza di conversione energetica si colloca generalmente tra il 10% e il 18%, valori che incidono direttamente sui costi operativi (OPEX), costituiti soprattutto da energia elettrica, fornitura di ossigeno e manutenzione ordinaria dei componenti. I costi di investimento iniziale (CAPEX) includono generatori, sistemi di alimentazione gas e apparecchiature di contatto e possono rappresentare una quota significativa del progetto, ma nel ciclo di vita dell’impianto il costo energetico rimane spesso la voce dominante. La manutenzione riguarda principalmente elettrodi, sistemi di raffreddamento, essiccatori e componenti soggetti a usura, con costi annuali generalmente stimati tra il 3% e il 6% del valore dell’impianto. 
            </p>
            <p>
L’ottimizzazione energetica si ottiene migliorando la concentrazione di ozono prodotta, utilizzando ossigeno ad alta purezza e riducendo le perdite di processo, e una corretta analisi costo-beneficio mostra che, nonostante l’investimento iniziale, l’ozono può risultare economicamente competitivo quando consente di ridurre l’uso di reagenti chimici e migliorare l’efficacia complessiva del trattamento.
            </p>
            <table>
<thead>
<tr>
<th>Voce</th>
<th>Descrizione</th>
</tr>
</thead>
<tbody>
<tr>
<td>Consumo energetico</td>
<td>Energia richiesta dai generatori</td>
</tr>
<tr>
<td>Manutenzione</td>
<td>Sostituzione componenti</td>
</tr>
<tr>
<td>Costi operativi</td>
<td>Gestione quotidiana</td>
</tr>
</tbody>
</table>
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
L’ozonizzazione dell’acqua è considerata una tecnologia relativamente sostenibile perché utilizza un ossidante che si decompone rapidamente senza lasciare residui chimici persistenti nell’ambiente. 
            </p>
            <p>
L’ozono (O₃), dopo aver reagito con i contaminanti, si riconverte in ossigeno molecolare (O₂), evitando l’accumulo di sottoprodotti stabili tipici di altri trattamenti e riducendo la necessità di aggiungere ulteriori reagenti chimici per la disinfezione o l’ossidazione. Tuttavia il processo richiede energia elettrica per la generazione dell’ozono, con consumi tipici nell’ordine di 8–15 kWh per kg di ozono prodotto nei generatori industriali a scarica corona, il che implica emissioni indirette di CO₂ legate al mix energetico utilizzato per alimentare l’impianto. Dal punto di vista ambientale, l’efficacia dell’ozono nella degradazione di composti organici complessi e microinquinanti consente di migliorare significativamente la qualità dell’acqua trattata, rendendola più idonea al riutilizzo in applicazioni industriali, agricole o civili. 
            </p>
            <p>
Per questo motivo la tecnologia è spesso adottata nei sistemi avanzati di trattamento e riciclo delle acque, contribuendo alla riduzione dei prelievi da fonti naturali e supportando una gestione più sostenibile delle risorse idriche.
            </p>
            <ul>
<li>Riduzione uso di reagenti chimici</li>
<li>Assenza di residui persistenti</li>
<li>Miglioramento qualità dell’acqua</li>
<li>Supporto al riutilizzo delle acque</li>
</ul>
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
Le innovazioni tecnologiche nel trattamento dell’acqua con ozono si concentrano sull’aumento dell’efficienza di generazione, sul miglioramento del trasferimento gas-liquido e sull’integrazione con sistemi digitali avanzati, con l’obiettivo di ottenere prestazioni più elevate e maggiore affidabilità nei sistemi industriali. 
            </p>
            <p>
Negli ultimi anni sono stati sviluppati generatori a scarica a corona ad alta frequenza con alimentazione elettronica ottimizzata, capaci di produrre concentrazioni di ozono superiori a 12–16% in peso quando alimentati con ossigeno puro, riducendo il consumo energetico specifico fino a circa 7–10 kWh per kg di ozono prodotto rispetto ai sistemi più tradizionali. Parallelamente, la ricerca si è concentrata sull’ottimizzazione del trasferimento dell’ozono in acqua tramite diffusori micro-nanobubble, iniettori ad alta efficienza e contattori progettati con modellazione CFD, che permettono di aumentare la superficie di contatto e quindi la dissoluzione dell’ozono nel liquido. Un altro ambito di sviluppo è l’integrazione con tecnologie digitali come sensori intelligenti, piattaforme IoT e analisi dati in tempo reale, che consentono il monitoraggio continuo delle prestazioni dell’impianto e la regolazione automatica dei parametri operativi per massimizzare l’efficienza del processo. 
            </p>
            <p>
Inoltre, la ricerca sta espandendo l’uso dell’ozono nei processi di ossidazione avanzata (AOP) combinandolo con UV o perossido di idrogeno per generare radicali ossidrilici altamente reattivi, mentre nuovi materiali resistenti all’ozono, come polimeri fluorurati e acciai speciali, stanno migliorando la durata dei componenti e rendendo possibile l’applicazione della tecnologia in settori emergenti come la rimozione di microinquinanti farmaceutici e il trattamento avanzato delle acque industriali.
            </p>
            <ul>
<li>Generatori ad alta efficienza</li>
<li>Sistemi AOP avanzati</li>
<li>Integrazione IoT negli impianti</li>
<li>Materiali resistenti all’ozono</li>
</ul>
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
La progettazione e il dimensionamento di un impianto di ozonizzazione consistono nel definire la capacità del sistema in modo che la quantità di ozono prodotta e trasferita all’acqua sia sufficiente a raggiungere gli obiettivi di trattamento richiesti dalle condizioni operative reali. 
            </p>
            <p>
Il processo inizia con l’analisi delle esigenze di trattamento e con la caratterizzazione dell’acqua in ingresso, valutando parametri come carico organico, presenza di composti ossidabili, torbidità, ferro, manganese e concentrazione di microinquinanti, dati che permettono di stimare la domanda di ozono espressa tipicamente in mg O₃/L; ad esempio, acque potabili superficiali possono richiedere 0,5–2 mg/L, mentre acque industriali o reflue possono superare 5–10 mg/L. Sulla base della portata idraulica e della domanda di ozono si dimensionano i generatori, che nei sistemi industriali producono normalmente da poche decine di grammi fino a diversi chilogrammi di ozono all’ora tramite scarica a corona alimentata da aria essiccata o ossigeno puro, e si dimensionano i contattori gas-liquido affinché garantiscano un tempo di contatto adeguato e un’elevata efficienza di trasferimento. La scelta dei materiali e dei componenti deve considerare la forte capacità ossidante dell’ozono, utilizzando acciai inox specifici, PTFE, PVDF o vetro per evitare degradazioni e perdite di prestazioni nel tempo. 
            </p>
            <p>
Infine si definiscono il layout impiantistico e l’integrazione nel sistema esistente, prevedendo configurazioni modulari e scalabili che permettano di aumentare la capacità del trattamento o adattarlo a variazioni di portata senza modifiche strutturali rilevanti all’impianto.
            </p>
            <ul>
<li>Analisi della qualità dell’acqua</li>
<li>Calcolo della domanda di ozono</li>
<li>Dimensionamento generatori</li>
<li>Progettazione del reattore di contatto</li>
<li>Definizione layout impiantistico</li>
</ul>
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
    
    