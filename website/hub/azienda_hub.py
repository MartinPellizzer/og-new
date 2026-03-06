import os

from lib import g
from lib import components

def main():
    section_margin = '8rem'
    hero_html = f'''
        <section style="padding-top: {section_margin}; padding-bottom: {section_margin}; background-color: #f9f9f9;">
            <div class="container-xl m-flex" style="gap: 5rem; align-items: center;">
                <div class="flex-1">
                    <h1 style="margin-bottom: 1rem;
                        font-size: 2.5rem; line-height: 1.2;
                        color: #0056b3;
                    ">
                        Azienda specializzata nello sviluppo di sistemi industriali a ozono
                    </h1>
                    <p style="margin-bottom: 2rem;">
                        Progettiamo e realizziamo soluzioni su misura per il trattamento di aria, acqua e impianti industriali attraverso tecnologia a ozono integrata nei processi produttivi.
                    </p>
                    <a href="#" class="button-blue">
                        Scopri il nostro metodo di lavoro 
                    </a>
                </div>
                <div class="flex-1">
                    <img src="/immagini/tecnologia-featured.jpg">
                </div>
            </div>
        </section>
    '''
    
    who_html = f'''
        <section style="padding-top: {section_margin}; padding-bottom: {section_margin};">
            <div class="container-xl m-flex" style="gap: 5rem; align-items: center;">
                <div class="flex-1">
                    <img src="/immagini/tecnologia-featured.jpg">
                </div>
                <div class="flex-1">
                    <h2 style="margin-bottom: 1rem;
                        font-size: 1.5rem; line-height: 1.2;
                        color: #0056b3;
                    ">
                        Chi siamo
                    </h2>
                    <p style="margin-bottom: 1rem;">
                        Siamo uno studio tecnico ingegneristico nato con una missione precisa: portare la tecnologia dell'ozono dall'ambito teorico alla pratica industriale complessa.
                    </p>
                    <p style="margin-bottom: 1rem;">
                        A differenza dei rivenditori di prodotti standard, noi non vendiamo "scatole chiuse". Progettiamo sistemi su misura, analizzando la chimica e la fisica del processo specifico del cliente.
                    </p>
                    <ul style="margin-left: 2rem;">
                        <li style="margin-bottom: 0.5rem;"><strong>Focus B2B:</strong> Ci rivolgiamo esclusivamente all'industria.</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Ingegnerizzazione:</strong> Ogni componente è dimensionato per lo scopo.</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Indipendenza:</strong> Non siamo vincolati a un singolo produttore di generatori.</li>
                    </ul>
                </div>
            </div>
        </section>
    '''
    
    competenza_html = f'''
        <section style="padding-top: {section_margin}; padding-bottom: {section_margin}; background-color: #f9f9f9;">
            <div class="container-xl" style="display: flex; flex-direction: column; align-items: center;">
                <h2 style="margin-bottom: 1rem;
                    font-size: 1.5rem; line-height: 1.2;
                    color: #0056b3;
                    text-align: center;
                ">
                    Competenze ingegneristiche e tecniche
                </h2>
                <p style="
                    margin-bottom: 3rem;
                    text-align: center;
                ">
                    Il nostro valore aggiunto risiede nella capacità di tradurre i requisiti di processo in specifiche tecniche impiantistiche.
                </p>
                <div class="grid-4" style="gap: 2rem; margin-bottom: 3rem;">
                    <div style="background-color: #fff; padding: 2rem;">
                        <h3 style="font-size: 1.125rem;">Progettazione Impiantistica</h3>
                        <ul style="margin-left: 1rem;">
                            <li style="margin-bottom: 0.5rem; font-size: 0.9rem;">Dimensionamento sistemi ozono</li>
                            <li style="margin-bottom: 0.5rem; font-size: 0.9rem;">Integrazione con impianti esistenti</li>
                            <li style="margin-bottom: 0.5rem; font-size: 0.9rem;">Studio dei flussi e dosaggi</li>
                        </ul>
                    </div>
                    <div style="background-color: #fff; padding: 2rem;">
                        <h3 style="font-size: 1.125rem;">Automazione e Controllo</h3>
                        <ul style="margin-left: 1rem;">
                            <li style="margin-bottom: 0.5rem; font-size: 0.9rem;">Integrazione PLC e SCADA</li>
                            <li style="margin-bottom: 0.5rem; font-size: 0.9rem;">Monitoraggio parametri operativi</li>
                            <li style="margin-bottom: 0.5rem; font-size: 0.9rem;">Gestione allarmi e sicurezza</li>
                        </ul>
                    </div>
                    <div style="background-color: #fff; padding: 2rem;">
                        <h3 style="font-size: 1.125rem;">Sicurezza e Normative</h3>
                        <ul style="margin-left: 1rem;">
                            <li style="margin-bottom: 0.5rem; font-size: 0.9rem;">Valutazione rischio ozono</li>
                            <li style="margin-bottom: 0.5rem; font-size: 0.9rem;">Progettazione sistemi di abbattimento</li>
                            <li style="margin-bottom: 0.5rem; font-size: 0.9rem;">Conformità CE e direttive ATEX</li>
                        </ul>
                    </div>
                    <div style="background-color: #fff; padding: 2rem;">
                        <h3 style="font-size: 1.125rem;">Integrazione di Processo</h3>
                        <ul style="margin-left: 1rem;">
                            <li style="margin-bottom: 0.5rem; font-size: 0.9rem;">Adattamento ai flussi produttivi</li>
                            <li style="margin-bottom: 0.5rem; font-size: 0.9rem;">Ottimizzazione prestazioni energetiche</li>
                            <li style="margin-bottom: 0.5rem; font-size: 0.9rem;">Minimizzazione sottoprodotti</li>
                        </ul>
                    </div>
                </div>
                <a href="#" class="button-blue" style="">
                    Approfondisci la tecnologia
                </a>
            </div>
        </section>
    '''

    esperienza_html = f'''
        <section style="padding-top: {section_margin}; padding-bottom: {section_margin};">
            <div class="container-xl" style="display: flex; flex-direction: column; align-items: center;">
                <h2 style="margin-bottom: 1rem;
                    font-size: 1.5rem; line-height: 1.2;
                    color: #0056b3;
                    text-align: center;
                ">
                    Esperienza nei diversi settori industriali
                </h2>
                <p style="
                    margin-bottom: 3rem;
                    text-align: center;
                ">
                    La nostra tecnologia è stata applicata con successo in ambienti critici e regolamentati.
                </p>
                <div class="grid-3" style="width: 100%; gap: 1rem; margin-bottom: 3rem; background-color: #0056b3;
                    text-align: center;
                ">
                    <div style="padding: 2rem;">
                        <p style="font-size: 3rem; line-height: 1; color: #fff;">15+ <br>
                        <span style="font-size: 1.0rem; color: #fff; text-transform: uppercase;">
                        Anni Esperienza
                        </span></p>
                    </div>
                    <div style="padding: 2rem;">
                        <p style="font-size: 3rem; line-height: 1; color: #fff;">
                        5 
                        <br>
                        <span style="font-size: 1.0rem; color: #fff; text-transform: uppercase;">
                        Paesi Serviti (EU) 
                        </span></p>
                    </div>
                    <div style="padding: 2rem;">
                        <p style="font-size: 3rem; line-height: 1; color: #fff;">
                        8 
                        <br>
                        <span style="font-size: 1.0rem; color: #fff; text-transform: uppercase;">
                        Settori Serviti
                        </span></p>
                    </div>
                </div>
                <div class="grid-5" style="gap: 1rem; margin-bottom: 3rem;">
                    <div style="background-color: #f9f9f9; padding: 2rem;">
                        <h3 style="font-size: 1rem;">Settore Alimentare</h3>
                        <p>
                            Sanificazione acque e ambienti
                        </p>
                    </div>
                    <div style="background-color: #f9f9f9; padding: 2rem;">
                        <h3 style="font-size: 1rem;">Settore Chimico</h3>
                        <p>
                            Ossidazione avanzata
                        </p>
                    </div>
                    <div style="background-color: #f9f9f9; padding: 2rem;">
                        <h3 style="font-size: 1rem;">Settore Farmaceutico</h3>
                        <p>
                            Water for Injection (WFI)
                        </p>
                    </div>
                    <div style="background-color: #f9f9f9; padding: 2rem;">
                        <h3 style="font-size: 1rem;">Trattamento Rifiuti</h3>
                        <p>
                            Deodorizzazione e trattamento percolati
                        </p>
                    </div>
                    <div style="background-color: #f9f9f9; padding: 2rem;">
                        <h3 style="font-size: 1rem;">Manufatturiero</h3>
                        <p>
                            Trattamento superfici e aria
                        </p>
                    </div>
                </div>
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
            <title>Chi Siamo - Specialisti in Tecnologie a Ozono Industriali</title>
            <meta name="description" content="">
        </head>
        <body>
            {components.header_default()}
            <main>
                {hero_html}
                {who_html}
                {competenza_html}
                {esperienza_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_folderpath = f'{g.WEBSITE_FOLDERPATH}/azienda/'
    os.makedirs(html_folderpath, exist_ok=True)
    html_filepath = f'{html_folderpath}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)
