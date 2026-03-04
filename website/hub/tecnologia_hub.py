import os

from lib import g
from lib import components

def main():
    hero_html = f'''
        <section style="padding-top: 5rem; padding-bottom: 5rem;">
            <div class="container-xl m-flex" style="gap: 3rem; align-items: center;">
                <div class="flex-1">
                    <h1 style="margin-bottom: 1rem;
                        font-size: 2.5rem; line-height: 1.2;
                    ">
                        Tecnologia a ozono per applicazioni industriali
                    </h1>
                    <p style="margin-bottom: 2rem;">
                        La generazione e l'integrazione dell'ozono in ambito industriale richiedono controllo preciso di concentrazione, portata, sicurezza e automazione. 
                    </p>
                    <a href="#" class="button-blue">
                        Scopri le applicazioni industriali → 
                    </a>
                </div>
                <div class="flex-1">
                    <img src="/immagini/tecnologia-featured.jpg">
                </div>
            </div>
        </section>
    '''

    generazione_html = f'''
        <section style="padding-top: 5rem; padding-bottom: 5rem;">
            <div class="container-xl m-flex" style="gap: 3rem;">
                <div style="flex: 2;">
                    <h2 style="margin-bottom: 1rem;
                        font-size: 2rem; line-height: 1.3;
                    ">
                        Generazione dell'ozono in ambito industriale
                    </h2>
                    <p style="margin-bottom: 1rem;">
                        Il principio fisico alla base della generazione industriale di ozono è la <strong>Scarica a Corona (Corona Discharge)</strong> o, più specificamente, la Scarica Dielettrica a Barriera (DBD). Questo processo comporta l'applicazione di un campo elettrico ad alta tensione tra due elettrodi separati da un dielettrico e un gap dove scorre il gas da trattare (ossigeno o aria secca). 
                    </p>
                    <p style="margin-bottom: 3rem;">
                        L'energia elettrica ad alta frequenza dissocia le molecole di ossigeno (O₂) in atomi singoli (O), che si ricombinano immediatamente formando ozono (O₃). La stabilità di questo processo dipende criticamente dalla purezza del gas di alimentazione e dalla gestione termica della cella. 
                    </p>
                    <h3 style="margin-bottom: 1rem;
                        font-size: 1.25rem; line-height: 1.5;
                    ">
                        Fattori Critici di Processo
                    </h3>
                    <ul style="margin-left: 1.5rem;
                        display: flex; flex-direction: column; gap: 1rem;
                    ">
                        <li><strong>Alta Tensione & Frequenza:</strong> Determinano l'efficienza di conversione energetica. 
                        </li>
                        <li><strong>Umidità Residua:</strong> Deve essere mantenuta sotto -60°C punto di rugiada per evitare la formazione di acido nitrico e corrosione.
                        </li>
                        <li><strong>Temperatura del Gas:</strong> Il raffreddamento è essenziale; temperature elevate favoriscono la decomposizione dell'ozono.
                        </li>
                    </ul>
                </div>
                <div style="flex: 1;">
                    <div style="background: #f9f9f9; padding: 1rem; border: 1px solid #e0e0e0;">
                        <h4 style="font-size: 0.8rem; margin-bottom: 0.5rem;">PARAMETRI FISICI</h4>
                        <p style="font-size: 0.9rem; margin-bottom: 0.5rem;">Gas Feed: O₂ (90-93%) o Aria</p>
                        <p style="font-size: 0.9rem; margin-bottom: 0.5rem;">Tensione: 5kV - 20kV AC</p>
                        <p style="font-size: 0.9rem; margin-bottom: 0.5rem;">Frequenza: 50Hz - 2000Hz</p>
                        <p style="font-size: 0.9rem; margin-bottom: 0.5rem;">Gap Dielettrico: 1.5mm - 3.0mm</p>
                    </div>
                </div>
            </div>
        </section>
    '''
    
    parametri_html = f'''
        <section class="tecnologia-parametri" style="padding-top: 5rem; padding-bottom: 5rem;">
            <div class="container-xl">
                <h2 style="margin-bottom: 1rem;
                    font-size: 2rem; line-height: 1.3;
                ">
                    Parametri critici per il corretto funzionamento
                </h2>
                <p style="margin-bottom: 1rem;">
                    L'efficienza di un impianto a ozono non è definita solo dalla potenza installata (kW), ma dall'interazione tra concentrazione prodotta e portata di gas. La seguente tabella illustra le variabili operative fondamentali per la progettazione. 
                </p>
                <table style="width: 100%; border-collapse: collapse; 
                    text-align: left; font-size: 0.9rem; color: #333;
                ">
                    <thead>
                        <tr>
                            <th style="background-color: #f9f9f9; text-transform: uppercase; font-size: 0.9rem; font-weight: 400;">Parametro</th>
                            <th style="background-color: #f9f9f9; text-transform: uppercase; font-size: 0.9rem; font-weight: 400;">Unità di Misura</th>
                            <th style="background-color: #f9f9f9; text-transform: uppercase; font-size: 0.9rem; font-weight: 400;">Impatto su Efficienza e Processo</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Concentrazione</strong></td>
                            <td>g/Nm³ (o % in peso)</td>
                            <td>Determina la velocità di ossidazione. Concentrazioni elevate (>10% da O₂) riducono i volumi di gas da trattare.</td>
                        </tr>
                        <tr>
                            <td><strong>Portata (Flow Rate)</strong></td>
                            <td>Nm³/h</td>
                            <td>Definisce la capacità di distribuzione dell'ozono nel fluido o nell'ambiente target.</td>
                        </tr>
                        <tr>
                            <td><strong>Tempo di Contatto</strong></td>
                            <td>minuti (Ct Value)</td>
                            <td>Prodotto tra Concentrazione (C) e Tempo (t). Cruciale per garantire l'inattivazione microbiologica o l'ossidazione chimica.</td>
                        </tr>
                        <tr>
                            <td><strong>Umidità Relativa</strong></td>
                            <td>% RH / Punto di Rugiada</td>
                            <td>L'umidità nel gas di alimentazione riduce drasticamente la produzione di ozono e genera sottoprodotti acidi corrosivi.</td>
                        </tr>
                        <tr>
                            <td><strong>Temperatura Gas</strong></td>
                            <td>°C</td>
                            <td>Ogni aumento di temperatura riduce la stabilità dell'ozono. Il raffreddamento dell'acqua di scambio è mandatorio.</td>
                        </tr>
                    </tbody>
                </table>
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
            <title>Tecnologia a Ozono Industriale: Principi e Automazione</title>
            <meta name="description" content="">
        </head>
        <body>
            {components.header_default()}
            <main>
                {hero_html}
                {generazione_html}
                {parametri_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_folderpath = f'{g.WEBSITE_FOLDERPATH}/tecnologia'
    os.makedirs(html_folderpath, exist_ok=True)
    html_filepath = f'{html_folderpath}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)
