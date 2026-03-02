import os

from lib import g
from lib import components

def main():
    background_color = 'rgba(0, 0, 0, 0.5)'
    background_color = 'rgba(0, 30, 60, 0.8)'
    color = f'#fff'
    h1 = 'Applicazioni dei sistemi a ozono nei principali settori industriali'
    subordinate = f'Analizziamo criticità operative nei processi produttivi e progettiamo sistemi a ozono su misura per la loro risoluzione.'
    anchor = 'Richiedi consulenza tecnica per il tuo settore'
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
                    {h1}
                </h1>
                <p class="container-md" style="font-size: 1.1rem; color: {color}; margin-bottom: 2rem;">
                    {subordinate}
                </p>
                <a href="#contact" class="button-blue" style="">
                    {anchor}
                </a>
            </div>
        </div>
    '''

    gap = f'4rem'
    margin_bottom = gap
    # <a href="#">Analisi settore alimentare →</a>
    img_height = '500px'
    settori_html = f'''
        <section class="problems-section">
            <div class="container">
                <div>
                    <article class="container-xl m-flex" style="align-items: center; gap: {gap}; margin-bottom: {margin_bottom}; margin-top: 8.0rem;">
                        <div class="flex-1">
                            <h2 style="font-size: 2rem; margin-bottom: 1.5rem;">
                                Industria Alimentare
                            </h2>
                            <ul style="margin-left: 2rem; margin-bottom: 1rem;">
                                <li style="margin-bottom: 0.8rem;">Contaminazione microbiologica ambientale</li>
                                <li style="margin-bottom: 0.8rem;">Odori nei reparti produttivi</li>
                                <li style="margin-bottom: 0.8rem;">Sanificazione linee e serbatoi</li>
                                <li style="margin-bottom: 0.8rem;">Rischi per sicurezza alimentare</li>
                                <li style="margin-bottom: 0.8rem;">Gestione acque di processo</li>
                            </ul>
                            <div style="background-color: #f0f4f8; padding: 1rem; color: #555; font-size: 0.9rem;">
                                <p>
                                <strong>Contesto:</strong> Gestione complessa di umidità elevata, carichi organici variabili e necessità di operare in ambienti chiusi senza interrompere la produzione. 
                                </p>
                            </div>
                        </div>
                        <div class="flex-1">
                            <img src="/immagini/home-settori-industria-alimentare.jpg" style="height: {img_height}; object-fit: cover;">
                        </div>
                    </article>
                    <article class="container-xl m-flex m-row-reverse" style="align-items: center; gap: {gap}; margin-bottom: {margin_bottom};">
                        <div class="flex-1">
                            <h2 style="font-size: 2rem; margin-bottom: 1rem;">
                                Industria Chimica
                            </h2>
                            <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                                <li style="margin-bottom: 0.8rem;">Emissioni VOC (Composti Organici Volatili)</li>
                                <li style="margin-bottom: 0.8rem;">Trattamento gas ossidabili</li>
                                <li style="margin-bottom: 0.8rem;">Odori persistenti e complessi</li>
                                <li style="margin-bottom: 0.8rem;">Normative ambientali stringenti</li>
                                <li style="margin-bottom: 0.8rem;">Trattamento aria di processo</li>
                            </ul>
                            <div style="background-color: #f0f4f8; padding: 1rem; color: #555; font-size: 0.9rem;">
                                <p>
                                <strong>Contesto:</strong> Necessità di abbattimento chimico preciso e conformità ai limiti di emissione in atmosfera sempre più severi. 
                                </p>
                            </div>
                        </div>
                        <div class="flex-1">
                            <img src="/immagini/home-settori-chimica.jpg" style="height: {img_height}; object-fit: cover;">
                        </div>
                    </article>
                    <article class="container-xl m-flex" style="align-items: center; gap: {gap}; margin-bottom: {margin_bottom};">
                        <div class="flex-1">
                            <h2 style="font-size: 2rem; margin-bottom: 1rem;">
                                Industria Farmaceutica
                            </h2>
                            <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                                <li style="margin-bottom: 0.8rem;">Controllo rigoroso carica microbica</li>
                                <li style="margin-bottom: 0.8rem;">Gestione ambienti controllati (Clean Rooms)</li>
                                <li style="margin-bottom: 0.8rem;">Disinfezione impianti e superfici</li>
                                <li style="margin-bottom: 0.8rem;">Rischio contaminazione crociata</li>
                            </ul>
                            <div style="background-color: #f0f4f8; padding: 1rem; color: #555; font-size: 0.9rem;">
                                <p>
                                <strong>Contesto:</strong> Priorità assoluta alla sterilità e alla validazione dei processi di disinfezione secondo standard GMP. 
                                </p>
                            </div>
                        </div>
                        <div class="flex-1">
                            <img src="/immagini/settori-farmaceutico.jpg" style="height: {img_height}; object-fit: cover;">
                        </div>
                    </article>
                    <article class="container-xl m-flex m-row-reverse" style="align-items: center; gap: {gap}; margin-bottom: {margin_bottom};">
                        <div class="flex-1">
                            <h2 style="font-size: 2rem; margin-bottom: 1rem;">
                                Settore Rifiuti
                            </h2>
                            <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                                <li style="margin-bottom: 0.8rem;">Emissioni odorigene intense</li>
                                <li style="margin-bottom: 0.8rem;">Presenza di bioaerosol pericolosi</li>
                                <li style="margin-bottom: 0.8rem;">Trattamento aria capannoni</li>
                                <li style="margin-bottom: 0.8rem;">Impatto ambientale sul territorio</li>
                            </ul>
                            <div style="background-color: #f0f4f8; padding: 1rem; color: #555; font-size: 0.9rem;">
                                <p>
                                <strong>Contesto:</strong> Gestione di flussi d'aria massivi con carichi inquinanti intermittenti e variabili. 
                                </p>
                            </div>
                        </div>
                        <div class="flex-1">
                            <img src="/immagini/soluzioni-acqua.jpg" style="height: {img_height}; object-fit: cover;">
                        </div>
                    </article>
                    <article class="container-xl m-flex" style="align-items: center; gap: {gap}; margin-bottom: 8.0rem;">
                        <div class="flex-1">
                            <h2 style="font-size: 2rem; margin-bottom: 1rem;">
                                Manifatturiero & Logistica
                            </h2>
                            <ul style="margin-left: 2rem; margin-bottom: 1.5rem;">
                                <li style="margin-bottom: 0.8rem;">Aria stagnante in grandi volumi</li>
                                <li style="margin-bottom: 0.8rem;">Odori da materiali stoccati</li>
                                <li style="margin-bottom: 0.8rem;">Contaminazioni in ambienti chiusi</li>
                                <li style="margin-bottom: 0.8rem;">Benessere operatori</li>
                            </ul>
                            <div style="background-color: #f0f4f8; padding: 1rem; color: #555; font-size: 0.9rem;">
                                <p>
                                <strong>Contesto:</strong> Necessità di ricambio e sanificazione dell'aria in spazi molto ampi con costi energetici contenuti. 
                                </p>
                            </div>
                        </div>
                        <div class="flex-1">
                            <img src="/immagini/home-ambienti.jpg" style="height: {img_height}; object-fit: cover;">
                        </div>
                    </article>
                </div>
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
