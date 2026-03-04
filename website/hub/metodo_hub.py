import os

from lib import g
from lib import components

def main():
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
                    Metodo di progettazione e integrazione dei sistemi industriali a ozono                </h1>
                <p class="container-md" style="font-size: 1.1rem; color: {color}; margin-bottom: 2rem;">
                    Ogni impianto viene sviluppato su misura attraverso analisi tecnica preliminare, studio di fattibilità e integrazione impiantistica controllata.                
                </p>
                <a href="/contatti.html" class="button-blue" style="text-decoration: none;">Richiedi una consulenza tecnica</a>
            </div>
        </div>
    '''

    gap = f'4rem'
    margin_bottom = gap
    # <a href="#">Analisi settore alimentare →</a>
    img_height = '500px'
    step_1_html = f'''
        <div class="container-xl m-flex" style="">
            <div class="flex-1" style="border-right: 4px solid #00a8e8;">
                <div class="method-step-card">
                    <span style="
                        font-size: 0.9rem;
                        font-weight: 700;
                        color: #00a8e8;
                        text-transform: uppercase;
                        letter-spacing: 1px;
                        margin-bottom: 0.5rem;
                        display: block;
                    ">
                        Passo 1
                    </span>
                    <h3 style="font-size: 1.25rem; margin-bottom: 1.5rem;">
                        Analisi tecnica preliminare
                    </h3>
                    <ul style="margin-left: 2rem; margin-bottom: 1rem;">
                        <li style="margin-bottom: 0.8rem;">Raccolta dati di processo</li>
                        <li style="margin-bottom: 0.8rem;">Identificazione criticità</li>
                        <li style="margin-bottom: 0.8rem;">Definizione parametri operativi</li>
                        <li style="margin-bottom: 0.8rem;">Analisi vincoli impiantistici</li>
                    </ul>
                </div>
            </div>
            <div class="flex-1">
            </div>
        </div>
    '''
    step_2_html = f'''
        <div class="container-xl m-flex" style="">
            <div class="flex-1">
            </div>
            <div class="flex-1" style="border-left: 4px solid #00a8e8;">
                <div class="method-step-card">
                    <span style="
                        font-size: 0.9rem;
                        font-weight: 700;
                        color: #00a8e8;
                        text-transform: uppercase;
                        letter-spacing: 1px;
                        margin-bottom: 0.5rem;
                        display: block;
                    ">
                        Passo 2
                    </span>
                    <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">
                        Sopralluogo industriale
                    </h3>
                    <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                        <li style="margin-bottom: 0.8rem;">Verifica condizioni reali</li>
                        <li style="margin-bottom: 0.8rem;">Misurazioni ambientali in loco</li>
                        <li style="margin-bottom: 0.8rem;">Odori persistenti e complessi</li>
                        <li style="margin-bottom: 0.8rem;">Analisi spazi e layout impianto</li>
                        <li style="margin-bottom: 0.8rem;">Valutazione integrazione fisica</li>
                    </ul>
                </div>
            </div>
        </div>
    '''
    step_3_html = f'''
        <div class="container-xl m-flex" style="">
            <div class="flex-1" style="border-right: 4px solid #00a8e8;">
                <div class="method-step-card">
                    <span style="
                        font-size: 0.9rem;
                        font-weight: 700;
                        color: #00a8e8;
                        text-transform: uppercase;
                        letter-spacing: 1px;
                        margin-bottom: 0.5rem;
                        display: block;
                    ">
                        Passo 3
                    </span>
                    <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">
                        Studio di fattibilità
                    </h3>
                    <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                        <li style="margin-bottom: 0.8rem;">Calcolo concentrazione necessaria</li>
                        <li style="margin-bottom: 0.8rem;">Dimensionamento generatore</li>
                        <li style="margin-bottom: 0.8rem;">Analisi sicurezza (HSE)</li>
                        <li style="margin-bottom: 0.8rem;">Valutazione ROI preliminare</li>
                    </ul>
                </div>
            </div>
            <div class="flex-1">
            </div>
        </div>
    '''
    step_4_html = f'''
        <div class="container-xl m-flex" style="">
            <div class="flex-1">
            </div>
            <div class="flex-1" style="border-left: 4px solid #00a8e8;">
                <div class="method-step-card">
                    <span style="
                        font-size: 0.9rem;
                        font-weight: 700;
                        color: #00a8e8;
                        text-transform: uppercase;
                        letter-spacing: 1px;
                        margin-bottom: 0.5rem;
                        display: block;
                    ">
                        Passo 4
                    </span>
                    <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">
                        Progettazione su misura
                    </h3>
                    <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                        <li style="margin-bottom: 0.8rem;">Definizione configurazione impiantistica</li>
                        <li style="margin-bottom: 0.8rem;">Integrazione con linee esistenti</li>
                        <li style="margin-bottom: 0.8rem;">Automazione e gestione PLC</li>
                        <li style="margin-bottom: 0.8rem;">Ingegnerizzazione sistemi di sicurezza</li>
                    </ul>
                </div>
            </div>
        </div>
    '''
    step_5_html = f'''
        <div class="container-xl m-flex" style="">
            <div class="flex-1" style="border-right: 4px solid #00a8e8;">
                <div class="method-step-card">
                    <span style="
                        font-size: 0.9rem;
                        font-weight: 700;
                        color: #00a8e8;
                        text-transform: uppercase;
                        letter-spacing: 1px;
                        margin-bottom: 0.5rem;
                        display: block;
                    ">
                        Passo 5
                    </span>
                    <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">
                        Costruzione e assemblaggio
                    </h3>
                    <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                        <li style="margin-bottom: 0.8rem;">Produzione sistema in stabilimento</li>
                        <li style="margin-bottom: 0.8rem;">Test preliminari di banco</li>
                        <li style="margin-bottom: 0.8rem;">Controllo qualità rigoroso</li>
                    </ul>
                </div>
            </div>
            <div class="flex-1">
            </div>
        </div>
    '''
    step_6_html = f'''
        <div class="container-xl m-flex" style="">
            <div class="flex-1">
            </div>
            <div class="flex-1" style="border-left: 4px solid #00a8e8;">
                <div class="method-step-card">
                    <span style="
                        font-size: 0.9rem;
                        font-weight: 700;
                        color: #00a8e8;
                        text-transform: uppercase;
                        letter-spacing: 1px;
                        margin-bottom: 0.5rem;
                        display: block;
                    ">
                        Passo 6
                    </span>
                    <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">
                        Installazione e collaudo
                    </h3>
                    <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                        <li style="margin-bottom: 0.8rem;">Messa in funzione in sito</li>
                        <li style="margin-bottom: 0.8rem;">Taratura parametri operativi</li>
                        <li style="margin-bottom: 0.8rem;">Verifica performance finali</li>
                        <li style="margin-bottom: 0.8rem;">Formazione tecnica del personale</li>
                    </ul>
                </div>
            </div>
        </div>
    '''

    metodo_html = f'''
        <section class="problems-section" style="margin-top: 5rem; margin-bottom: 5rem;">
            <div class="container-xl">
                <h2 style="font-size: 2rem; margin-bottom: 1rem; text-align: center;">Richiedi analisi tecnica personalizzata</h2>
                <p style="margin-bottom: 20px; text-align: center;">
                Valutiamo insieme la fattibilità dell'intervento sul tuo impianto.</p>
                
                <div>
                    {step_1_html}
                    {step_2_html}
                    {step_3_html}
                    {step_4_html}
                    {step_5_html}
                    {step_6_html}
                </div>
            </div>
        </section>
    '''

    controllo_html = f'''
        <section class="" style="background-color : #f9f9f9; padding-top: 4rem; padding-bottom: 4rem;">
            <div class="container-xl">
                <h2 style="font-size: 2rem; margin-bottom: 3rem; text-align: center;">
                    Controllo dei parametri e sicurezza operativa
                </h2>
                <div class="grid-3" style="gap: 2rem;">
                    <div style="background-color: #fff; padding: 2rem; border-left: 4px solid #2c3e50;">
                        <h3 style="font-size: 1.25rem; line-height: 1.4;">
                        Monitoraggio Continuo
                        </h3>
                        <p>
                        Controllo costante della concentrazione di ozono tramite sensori ambientali di precisione per garantire l'efficacia del trattamento.
                        </p>
                    </div>
                    <div style="background-color: #fff; padding: 2rem; border-left: 4px solid #2c3e50;">
                        <h3 style="font-size: 1.25rem; line-height: 1.4;">
                        Sicurezza e Interblocchi
                        </h3>
                        <p>
                        Controllo costante della concentrazione di ozono tramite sensori ambientali di precisione per garantire l'efficacia del trattamento.
                        </p>
                    </div>
                    <div style="background-color: #fff; padding: 2rem; border-left: 4px solid #2c3e50;">
                        <h3 style="font-size: 1.25rem; line-height: 1.4;">
                        Conformità Normativa
                        </h3>
                        <p>
                        Controllo costante della concentrazione di ozono tramite sensori ambientali di precisione per garantire l'efficacia del trattamento.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    '''

    assistenza_html = f'''
        <section class="" style="padding-top: 4rem; padding-bottom: 4rem;">
            <div class="container-xl">
                <h2 style="font-size: 2rem; margin-bottom: 1rem; text-align: center;">
Assistenza tecnica e manutenzione programmata
                </h2>
                <p style="margin-bottom: 20px; text-align: center;">
                Il nostro impegno non termina con l'installazione. Garantiamo continuità operativa attraverso un servizio strutturato.
                </p>
                <div class="m-flex" style="gap: 4rem; justify-content: center;">
                    <div style="flex-1">
                        <div style="margin-bottom: 1rem;"><span style="color: green; font-weight: bold;">✔</span> Monitoraggio prestazioni</div>
                        <div style="margin-bottom: 1rem;"><span style="color: green; font-weight: bold;">✔</span> Sostituzione componenti</div>
                        <div><span style="color: green; font-weight: bold;">✔</span> Aggiornamento impianto</div>
                    </div>
                    <div style="flex-1">
                        <div style="margin-bottom: 1rem;"><span style="color: green; font-weight: bold;">✔</span> Interventi programmati</div>
                        <div><span style="color: green; font-weight: bold;">✔</span> Supporto remoto</div>
                    </div>
                </div>
            </div>
        </section>
    '''
    
    custom_html = f'''
        <section class="" style="background-color: #f9f9f9; padding-top: 4rem; padding-bottom: 4rem;">
            <div class="container-xl">
                <h2 style="font-size: 2rem; margin-bottom: 1rem; text-align: center;">
Perché un sistema su misura è diverso da una soluzione standard?
                </h2>
                <p style="margin-bottom: 20px; text-align: center;">
Non vendiamo semplici generatori, ma sistemi integrati nel tuo processo produttivo.
                </p>
                
                <div style="display: flex; justify-content: center;">
                    <table style="width: 100%; max-width: 800px; margin: 30px auto;
                        border-collapse: collapse; background: white; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
                        text-align: left;
                    ">
                        <thead>
                            <tr>
                                <th style="background-color: #2c3e50; color: white;">Caratteristica</th>
                                <th style="background-color: #2c3e50; color: white;">Soluzione Standard</th>
                                <th style="background-color: #2c3e50; color: white;">Il Nostro Metodo</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Progettazione</td>
                                <td>Configurazione fissa</td>
                                <td>Adattata al layout e processo</td>
                            </tr>
                            <tr>
                                <td>Integrazione</td>
                                <td>Limitata o assente</td>
                                <td>Completa con PLC e linee esistenti</td>
                            </tr>
                            <tr>
                                <td>Sicurezza</td>
                                <td>Generica</td>
                                <td>Specifiche per il sito</td>
                            </tr>
                            <tr>
                                <td>Efficienza</td>
                                <td>Stimata</td>
                                <td>Calcolata e verificata</td>
                            </tr>
                        </tbody>
                    </table>
                <div>
            </div>
        </section>
    '''
    
    cta_html = f'''
        <section class="final-cta">
            <div class="container-xl">
                <h2 style="font-size: 2rem; margin-bottom: 1rem;">
                Ogni progetto parte da un'analisi tecnica.
                </h2>
                <p style="margin-bottom: 20px;">
                Verifica la fattibilità del tuo impianto con i nostri ingegneri.
                </p>
                <a href="/contatti.html" class="button-blue" style="text-decoration: none;">
                Richiedi sopralluogo
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
            <title>Metodo di Progettazione dei Sistemi Industriali a Ozono</title>
            <meta name="description" content="">
        </head>
        <body>
            {components.header_default()}
            <main>
                {hero_html}
                {metodo_html}
                {controllo_html}
                {assistenza_html}
                {custom_html}
                {cta_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_folderpath = f'{g.WEBSITE_FOLDERPATH}/metodo'
    os.makedirs(html_folderpath, exist_ok=True)
    html_filepath = f'{html_folderpath}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)
