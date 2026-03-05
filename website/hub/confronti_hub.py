import os

from lib import g
from lib import components

def main():
    hero_html = f'''
        <section style="padding-top: 4rem; padding-bottom: 4rem; background-color: #f9f9f9;">
            <div class="container-xl m-flex" style="gap: 3rem; align-items: center;">
                <div class="flex-1">
                    <h1 style="margin-bottom: 1rem;
                        font-size: 2.5rem; line-height: 1.2;
                        color: #0056b3;
                    ">
                        Confronto tra tecnologie per il trattamento industriale di aria, acqua e superfici
                    </h1>
                    <p style="margin-bottom: 2rem;">
                        La scelta della tecnologia di trattamento dipende da parametri operativi, contaminanti presenti e integrazione nel processo produttivo. Non esiste una soluzione universale, ma la scelta più efficiente.
                    </p>
                    <a href="#" class="button-blue">
                        Scopri le applicazioni industriali 
                    </a>
                </div>
                <div class="flex-1">
                    <img src="/immagini/tecnologia-featured.jpg">
                </div>
            </div>
        </section>
    '''
    
    card_p_size = '0.9rem'
    how_html = f'''
        <section style="padding-top: 4rem; padding-bottom: 4rem;">
            <div class="container-xl" style="text-align: center;">
                <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">
                    Come scegliere la tecnologia di trattamento più adatta
                </h2>
                <p style="margin-bottom: 2rem;">
                    La selezione di un impianto di sanificazione o ossidazione richiede un'analisi ingegneristica. Ecco i fattori critici che determinano la scelta:
                </p>
                <div class="grid-5" style="gap: 1rem;">
                    <div style="background-color: #f9f9f9; padding: 2rem;">
                        <p style="font-size: {card_p_size}; font-weight: bold;">Tipo contaminanti</p>
                    </div>
                    <div style="background-color: #f9f9f9; padding: 2rem;">
                        <p style="font-size: {card_p_size}; font-weight: bold;">Concentrazione</p>
                    </div>
                    <div style="background-color: #f9f9f9; padding: 2rem;">
                        <p style="font-size: {card_p_size}; font-weight: bold;">Portata del processo</p>
                    </div>
                    <div style="background-color: #f9f9f9; padding: 2rem;">
                        <p style="font-size: {card_p_size}; font-weight: bold;">Vincoli impiantistici</p>
                    </div>
                    <div style="background-color: #f9f9f9; padding: 2rem;">
                        <p style="font-size: {card_p_size}; font-weight: bold;">Costi operativi (OPEX)</p>
                    </div>
                </div>
            </div>
        </section>
    '''
    
    vs_html = f'''
        <section class="confronti-vs" style="padding-top: 4rem; padding-bottom: 4rem; background-color: #f9f9f9;">
            <div class="container-xl" style="">
                <h2 style="font-size: 1.5rem; margin-bottom: 1rem; text-align: center;">
                    Analisi Comparativa delle Tecnologie
                </h2>
                <p style="margin-bottom: 2rem; text-align: center;">
                    Schede tecniche di confronto per supportare la decisione d'acquisto.
                </p>
                <div class="grid-2" style="gap: 1rem;">
                    <div>
                        <h3 style="font-size: 1.5rem; padding: 1rem; background: #0056b3; color: #fff;">
                            Ozono vs Cloro
                        </h3>
                        <div style="padding: 2rem; background-color: #fff;">
                            <p style="margin-bottom: 1rem;">
                                Applicazioni: Trattamento acqua, disinfezione potabile, piscine.
                            </p>
                            <table style="
                                border-collapse: collapse; text-align: left; font-size: 0.9rem;
                                width: 100%;
                            ">
                                <thead>
                                    <tr>
                                        <th>Parametro</th>
                                        <th>Ozono</th>
                                        <th>Cloro</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>Residui chimici</td>
                                        <td>Nessuno</td>
                                        <td>Presenti (Trialometani)</td>
                                    </tr>
                                    <tr>
                                        <td>Velocità ossidazione</td>
                                        <td>Molto Alta</td>
                                        <td>Media</td>
                                    </tr>
                                    <tr>
                                        <td>Sicurezza stoccaggio</td>
                                        <td>Alta (On-site)</td>
                                        <td>Critica</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div>
                        <h3 style="font-size: 1.5rem; padding: 1rem; background: #0056b3; color: #fff;">
                            Ozono vs UV
                        </h3>
                        <div style="padding: 2rem; background-color: #fff;">
                            <p style="margin-bottom: 1rem;">
                                Applicazioni: Disinfezione acqua, trattamento aria, superfici.
                            </p>
                            <table style="
                                border-collapse: collapse; text-align: left; font-size: 0.9rem;
                                width: 100%;
                            ">
                                <thead>
                                    <tr>
                                        <th>Parametro</th>
                                        <th>Ozono</th>
                                        <th>UV</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>Efficacia microbiologica</td>
                                        <td>Azione residua</td>
                                        <td>Istantanea (senza residuo)</td>
                                    </tr>
                                    <tr>
                                        <td>Costi operativi</td>
                                        <td>Medio-Bassi (Elettricità)</td>
                                        <td>Medio-Alti (Sostituzione lampade)</td>
                                    </tr>
                                    <tr>
                                        <td>Integrazione</td>
                                        <td>Flessibile (Gas/Liq)</td>
                                        <td>Richiede trasparenza mezzo</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div>
                        <h3 style="font-size: 1.5rem; padding: 1rem; background: #0056b3; color: #fff;">
                            Ozono vs Biofiltri
                        </h3>
                        <div style="padding: 2rem; background-color: #fff;">
                            <p style="margin-bottom: 1rem;">
                                Applicazioni: Abbattimento odori, trattamento VOC, depurazione aria.
                            </p>
                            <table style="
                                border-collapse: collapse; text-align: left; font-size: 0.9rem;
                                width: 100%;
                            ">
                                <thead>
                                    <tr>
                                        <th>Parametro</th>
                                        <th>Ozono</th>
                                        <th>Biofiltri</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>Spazio impianto</td>
                                        <td>Compatto</td>
                                        <td>Elevato</td>
                                    </tr>
                                    <tr>
                                        <td>Manutenzione</td>
                                        <td>Minima</td>
                                        <td>Complessa (controllo umidità/batteri)</td>
                                    </tr>
                                    <tr>
                                        <td>Efficienza picchi</td>
                                        <td>Immediata</td>
                                        <td>Lenta (shock tossici)</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div>
                        <h3 style="font-size: 1.5rem; padding: 1rem; background: #0056b3; color: #fff;">
                            Ozono vs Perossido (H2O2)
                        </h3>
                        <div style="padding: 2rem; background-color: #fff;">
                            <p style="margin-bottom: 1rem;">
                                Applicazioni: Ossidazione avanzata (AOP), contaminanti organici.
                            </p>
                            <table style="
                                border-collapse: collapse; text-align: left; font-size: 0.9rem;
                                width: 100%;
                            ">
                                <thead>
                                    <tr>
                                        <th>Parametro</th>
                                        <th>Ozono</th>
                                        <th>Perossido</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>Residui finali</td>
                                        <td>Ossigeno</td>
                                        <td>Acqua + Ossigeno</td>
                                    </tr>
                                    <tr>
                                        <td>Sicurezza</td>
                                        <td>Alta</td>
                                        <td>Manipolazione chimica</td>
                                    </tr>
                                    <tr>
                                        <td>Velocità reazione</td>
                                        <td>Alta</td>
                                        <td>Media (dipende da catalizzatore)</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    '''

    fattori_html = f'''
        <section style="padding-top: 4rem; padding-bottom: 4rem;">
            <div class="container-xl" style="">
                <h2 style="font-size: 1.5rem; margin-bottom: 1rem; text-align: center;">
                    Fattori che determinano la scelta della tecnologia
                </h2>
                <p style="margin-bottom: 2rem; text-align: center;">
                    Un approccio ingegneristico per massimizzare il ROI dell'impianto.
                </p>
                <div class="grid-3" style="gap: 1rem;">
                    <div style="padding: 2rem; border-left: 4px solid #00a8cc;">
                        <h3 style="color: #0056b3; font-size: 1.125rem;">Tipo di contaminante</h3>
                        <p>Identificare se il target è organico, inorganico o microbiologico è il primo passo. L'ozono eccelle nell'ossidazione organica e nella disinfezione.</p>
                    </div>
                    <div style="padding: 2rem; border-left: 4px solid #00a8cc;">
                        <h3 style="color: #0056b3; font-size: 1.125rem;">
Concentrazione del carico
                        </h3>
                        <p>
Alti carichi inquinanti potrebbero richiedere pre-trattamenti o dosaggi specifici di ozono per evitare saturazione.
                        </p>
                    </div>
                    <div style="padding: 2rem; border-left: 4px solid #00a8cc;">
                        <h3 style="color: #0056b3; font-size: 1.125rem;">
Portata del processo
                        </h3>
                        <p>
Il dimensionamento del generatore di ozono o dell'unità UV deve essere proporzionale al flusso (m³/h o m³/giorno).
                        </p>
                    </div>
                    <div style="padding: 2rem; border-left: 4px solid #00a8cc;">
                        <h3 style="color: #0056b3; font-size: 1.125rem;">
Integrazione impiantistica
                        </h3>
                        <p>
Valutare lo spazio disponibile, la presenza di aria compressa e la facilità di automazione nel PLC di bordo macchina.
                        </p>
                    </div>
                    <div style="padding: 2rem; border-left: 4px solid #00a8cc;">
                        <h3 style="color: #0056b3; font-size: 1.125rem;">
Costi operativi (OPEX)
                        </h3>
                        <p>
Confrontare il costo dell'elettricità per produrre ozono rispetto all'acquisto continuo di reagenti chimici o sostituzione filtri.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    '''
    
    competitori_html = f'''
        <section style="padding-top: 4rem; padding-bottom: 4rem;">
            <div class="container-xl" style="padding: 2rem; background-color: #fff8f8; border: 1px solid #ffcccc;">
                <h2 style="color: #c0392b; font-size: 1.5rem; margin-bottom: 1rem;">
                    Quando altre tecnologie possono essere più adatte
                </h2>
                <p style="margin-bottom: 1rem;">
                    Per garantire la massima trasparenza tecnica, segnaliamo i casi in cui l'ozono non è la prima scelta:
                </p>
                <ul style="margin-left: 2rem;">
                    <li><strong>Contaminanti non ossidabili:</strong>Alcuni metalli pesanti o sali inorganici specifici richiedono precipitazione o scambio ionico.</li>
                    <li><strong>Processi con umidità critica non controllabile:</strong>In ambienti dove l'umidità relativa supera costantemente l'85% senza deumidificazione, l'efficacia dell'ozono gassoso può variare.</li>
                    <li><strong>Esigenze di trattamento continuo specifico:</strong>In alcuni casi di filtrazione meccanica pura, l'ozono non sostituisce la rimozione fisica dei solidi sospesi.</li>
                </ul>
            </div>
        </section>
    '''
    
    soluzioni_html = f'''
        <section style="padding-top: 4rem; padding-bottom: 4rem; background-color: #0056b3;">
            <div class="container-xl" style="padding: 2rem; text-align: center;">
                <h2 style="color: #fff; text-align: center; font-size: 1.5rem; margin-bottom: 1rem;">
                    Applicazioni dei sistemi a ozono nei processi industriali
                </h2>
                <p style="color: #fff; margin-bottom: 2rem; text-align: center;">
                    Una volta definita la tecnologia, scopri come integriamo i generatori di ozono nelle linee di produzione. 
                </p>
                <a href="#" class="button-white-ghost">
                    Vai alle Soluzioni Industriali  
                </a>
            </div>
        </section>
    '''

    cta_html = f'''
        <section class="final-cta">
            <div class="container-xl">
                <h2 style="font-size: 2rem; margin-bottom: 1rem;">
                    Valutazione tecnica della soluzione più adatta
                </h2>
                <p style="margin-bottom: 20px;">
                    La scelta della tecnologia richiede un'analisi preliminare delle condizioni operative e dei parametri di processo. I nostri ingegneri sono a disposizione per confrontare le opzioni per il tuo impianto. 
                 </p>
                <a href="/contatti.html" class="button-blue" style="text-decoration: none;">
                Richiedi consulenza tecnica
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
            <title>Confronto tra tecnologie per il trattamento industriale di aria, acqua e superfici</title>
            <meta name="description" content="">
        </head>
        <body>
            {components.header_default()}
            <main>
                {hero_html}
                {how_html}
                {vs_html}
                {fattori_html}
                {competitori_html}
                {soluzioni_html}
                {cta_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_folderpath = f'{g.WEBSITE_FOLDERPATH}/confronti/'
    os.makedirs(html_folderpath, exist_ok=True)
    html_filepath = f'{html_folderpath}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)
