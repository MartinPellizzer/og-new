import os
import shutil

from lib import g
from lib import components

def main():
    shutil.copy2(f'templates/styles.css', f'{g.TEMPLATES_FOLDERPATH}/styles.css')

    ########################################
    # HERO 0000
    ########################################
    _id = f'HERO 0000'
    h1 = f'Sistemi industriali a ozono su misura per processi produttivi'
    subordinate = f'Progettiamo, realizziamo e integriamo impianti a ozono personalizzati per risolvere problematiche tecniche in ambito industriale.'
    href = '#'
    anchor = 'Richiedi una consulenza gratuita'
    hero_0000_html = f'''
        <p>{_id}</p>
        <section class="hero-0000">
            <div class="hero-0000-content-container">
                <h1 class="container-lg">{h1}</h1>
                <p class="container-md">{subordinate}</p>
                <div class="hero-0000-link">
                    <a href="{href}">{anchor}</a>
                </div>
            </div>
        </section>
    '''
    
    ########################################
    # HERO 0001
    ########################################
    _id = f'HERO 0001'
    h1 = f'Sistemi industriali a ozono su misura per processi produttivi'
    subordinate = f'Progettiamo, realizziamo e integriamo impianti a ozono personalizzati per risolvere problematiche tecniche in ambito industriale.'
    href = '#'
    anchor = 'Richiedi una consulenza gratuita'
    hero_0001_html = f'''
        <span style="color: #111; background-color: #ffff00;">{_id}</span>
        <section class="hero-0001">
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
    # GRID 0000
    ########################################
    _id = f'GRID 0000'
    h2 = f'''Applicazioni industriali dell'ozono'''
    subordinate = f'''L'ozono viene utilizzato in ambito industriale per disinfettare, ossidare, deodorare e trattare fluidi e ambienti produttivi.'''
    img_height = '400px'
    grid_0000_html = f'''
        <span style="color: #111; background-color: #ffff00;">{_id}</span>
        <section class="grid-0000 ">
            <div class="grid-0000-content-container">
                <h2>{h2}</h2>
                <p class="grid-0000-supplementary">{subordinate}</p>
                <div class="grid-0000-cards grid-4">
                    <article>
                        <img src="/immagini/placeholder.jpg" alt="" width="200" height="400">
                        <h3>Trattamento acque industriali</h3>
                        <p>Progettiamo impianti di ozonizzazione per ossidare contaminanti, eliminare batteri e migliorare la qualità delle acque di processo e reflue.</p>
                    </article>
                    <article>
                        <img src="/immagini/placeholder.jpg" alt="" width="200" height="400">
                        <h3>Sanificazione ambienti e superfici</h3>
                        <p>Utilizziamo generatori di ozono industriali per eliminare microrganismi, muffe, virus e biofilm da ambienti produttivi e superfici operative.</p>
                    </article>
                    <article>
                        <img src="/immagini/placeholder.jpg" alt="" width="200" height="400">
                        <h3>Abbattimento odori industriali</h3>
                        <p>Implementiamo soluzioni a ozono per decomporre composti organici volatili (VOC) e neutralizzare odori persistenti in impianti industriali.</p>
                    </article>
                    <article>
                        <img src="/immagini/placeholder.jpg" alt="" width="200" height="400">
                        <h3>Settore alimentare e agroindustriale</h3>
                        <p>Progettiamo sistemi a ozono per la sicurezza alimentare, la sanificazione delle linee produttive e il trattamento delle acque di lavaggio.</p>
                    </article>
                </div>
            </div>
        </section>
    '''

    ########################################
    # GRID 0001
    ########################################
    _id = f'GRID 0001'
    h2 = f'''Perché scegliere l'ozono nei processi industriali?'''
    subordinate = f'''L'ozono è un ossidante naturale con elevato potere disinfettante che elimina batteri, virus, muffe e composti organici senza lasciare residui chimici.'''
    img_height = '400px'
    grid_0001_html = f'''
        <span style="color: #111; background-color: #ffff00;">{_id}</span>
        <section class="grid-0001">
            <div class="container-xl">
                <h2 style="color: #ffffff;">{h2}</h2>
                <p>{subordinate}</p>
                <ul class="grid-4">
                    <li>
                        <svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#1f1f1f"><path d="M172-120q-42 0-59.5-39t11.5-71l248-280v-270h-52q-13 0-21.5-8.5T290-810q0-13 8.5-21.5T320-840h320q13 0 21.5 8.5T670-810q0 13-8.5 21.5T640-780h-52v270l248 280q29 32 11.5 71T788-120H172Zm70-90h476L558-395H402L242-210Zm-82 30h640L528-488v-292h-96v292L160-180Zm320-300Z"/></svg>
                        Riduce l'uso di prodotti chimici nei processi industriali
                    </li>
                    <li>
                        <svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#1f1f1f"><path d="M600-90q-12 0-21-9t-9-21v-41q-28-3-53-13t-47-27l-39 39q-9 8-21.5 8.5T388-162q-9-9-9-21.5t9-21.5l40-39q-5-7-9.5-14.5T410-274l-31-62-51 51q-9 8-21.5 8.5T285-285q-9-9-9-21t9-21l51-52-62-31q-7-4-13.5-7.5T248-426l-35 35q-9 8-21.5 8.5T170-391q-9-9-9-21t9-21l34-34q-17-22-28.5-48T161-570h-41q-12 0-21-9t-9-21q0-13 9-21.5t21-8.5h43q5-24 14.5-46t23.5-41l-34-34q-9-9-9-21t9-21q9-9 21-9t21 9l34 34q19-14 41-23.5t46-14.5v-43q0-13 9-21.5t21-8.5q13 0 21.5 8.5T390-840v41q29 3 55 14.5t49 29.5l34-34q9-9 21.5-9t21.5 9q9 9 9 21t-9 21l-36 36 8 12q4 6 7 13l30 60 48-49q9-9 21.5-9t21.5 9q9 9 9 21.5t-9 21.5l-50 49 65 33 16 10 16 10 39-39q9-9 21-9t21 9q9 9 9 21.5t-9 21.5l-39 38q16 21 26 46t13 52h41q13 0 21.5 8.5T870-360q0 12-8.5 21t-21.5 9h-43q-5 24-14 46t-23 41l32 32q9 9 9 21.5t-9 21.5q-9 8-21.5 8.5T749-168l-32-33q-19 14-41 23.5T630-163v43q0 12-8.5 21T600-90Zm-6-130q69 0 112-51.5T738-389q-6-35-26.5-63T659-496l-66-34q-20-11-36-27t-27-36l-34-66q-19-38-53.5-59.5T366-740q-69 0-112 51.5T222-571q6 35 26.5 63t52.5 44l66 33q20 11 36.5 27.5T431-367l33 66q19 38 53.5 59.5T594-220ZM380-540q25 0 42.5-17.5T440-600q0-25-17.5-42.5T380-660q-25 0-42.5 17.5T320-600q0 25 17.5 42.5T380-540Zm235.5 235.5Q630-319 630-340t-14.5-35.5Q601-390 580-390t-35.5 14.5Q530-361 530-340t14.5 35.5Q559-290 580-290t35.5-14.5ZM480-480Z"/></svg>
                        Elimina microrganismi e biofilm da superfici e attrezzature
                    </li>
                    <li>
                        <svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#1f1f1f"><path d="M80-200v-100h610v100H80Zm655 0v-100h50v100h-50Zm95 0v-100h50v100h-50Zm-95-145v-56q0-42-24.5-66T651-491h-71q-54 0-90.5-41.5T453-628q0-54 36.5-90.5T580-755v50q-35 0-56 21t-21 56q0 35 21 61t56 26h71q54 0 94 37t40 91v68h-50Zm95 0v-100q0-75-50-123t-125-48v-50q34 0 55.5-24t21.5-58q0-34-21.5-58T655-830v-50q54 0 90.5 39t36.5 93q0 33-12.5 57T737-650q58 20 100.5 75T880-445v100h-50Z"/></svg>
                        Decompone odori e composti organici volatili (VOC)
                    </li>
                    <li>
                        <svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#1f1f1f"><path d="M213-175q-43.59-45-68.3-104Q120-338 120-400q0-73 25.5-133.5T222-645q35-35 87-59t122.5-37.5Q502-755 591-758.5t198 3.5q8 108 5.5 197.5t-16 160.75q-13.5 71.25-38 124.56Q716-218.87 680-183q-51 51-110 77T444-80q-69 0-126.5-23.5T213-175Zm103 0q25 17 58 26t69.92 9Q497-140 547-162t91-64q27-27 46-70.5t31-103Q727-459 731-534t0-165q-94-2-168.5 2.5T431-680q-57 12-98 30.5T266-604q-42 43-64 91t-22 98q0 48 20.5 100.5T251-230q53-98 127-176t157-123q-87 75-141 162.5T316-175Zm0 0Zm0 0Z"/></svg>
                        Si riconverte in ossigeno senza generare sottoprodotti tossici
                    </li>
                </ul>
            </div>
        </section>
    '''

    ########################################
    # GRID 0002
    ########################################
    _id = f'GRID 0002'
    h2 = f'''Settori industriali in cui operiamo'''
    subordinate = f'''Progettiamo e realizziamo impianti a ozono per applicazioni industriali specifiche, adattando ogni soluzione ai processi produttivi del settore di riferimento.'''
    img_height = '400px'
    grid_0002_html = f'''
        <span style="color: #111; background-color: #ffff00;">{_id}</span>
        <section class="grid-0002">
            <div class="container-xl">
                <h2>{h2}</h2>
                <p class="grid-0002-supplementary">{subordinate}</p>
                <div class="grid-0002-cards grid-3">
                    <article>
                        <img src="/immagini/placeholder.jpg" alt="" width="200" height="400">
                        <h3>Industria alimentare</h3>
                        <p>Sistemi di ozonizzazione per sanificazione ambienti, trattamento acque di processo e controllo microbiologico nelle linee produttive alimentari.</p>
                    </article>
                    <article>
                        <img src="/immagini/placeholder.jpg" alt="" width="200" height="400">
                        <h3>Impianti di depurazione</h3>
                        <p>Impianti a ozono per ossidazione avanzata, riduzione COD e abbattimento odori negli impianti di trattamento acque reflue.</p>
                    </article>
                    <article>
                        <img src="/immagini/placeholder.jpg" alt="" width="200" height="400">
                        <h3>Caseifici</h3>
                        <p>Soluzioni a ozono per sanificazione celle di stagionatura, ambienti produttivi e trattamento acque nei processi lattiero-caseari.</p>
                    </article>
                    <article>
                        <img src="/immagini/placeholder.jpg" alt="" width="200" height="400">
                        <h3>Macelli</h3>
                        <p>Sistemi di ozonizzazione per controllo carica batterica, eliminazione odori e igienizzazione ambienti di lavorazione carni.</p>
                    </article>
                    <article>
                        <img src="/immagini/placeholder.jpg" alt="" width="200" height="400">
                        <h3>Aziende agricole</h3>
                        <p>Impianti a ozono per trattamento acqua irrigazione, sanificazione serre e riduzione patogeni nelle coltivazioni.</p>
                    </article>
                    <article>
                        <img src="/immagini/placeholder.jpg" alt="" width="200" height="400">
                        <h3>Impianti chimici</h3>
                        <p>Soluzioni di ossidazione con ozono per processi chimici industriali, abbattimento composti organici volatili e trattamento reflui.</p>
                    </article>
                </div>
            </div>
        </section>
    '''

    ########################################
    # GRID 0003
    ########################################
    _id = f'GRID 0003'
    h2 = f'''Dati tecnici misurabili dei nostri impianti a ozono industriali'''
    subordinate = f'''I nostri generatori di ozono industriali sono progettati con parametri tecnici verificabili e prestazioni misurabili in contesti produttivi reali.'''
    img_height = '400px'
    grid_0003_html = f'''
        <span style="color: #111; background-color: #ffff00;">{_id}</span>
        <section class="grid-0003">
            <div class="container-xl">
                <h2>{h2}</h2>
                <p>{subordinate}</p>
                <ul class="grid-3">
                    <li><span>0 - 100 g/h</span>Produzione ozono nominale</li>
                    <li><span>0,1 ppm</span>Sensori ozono ambientale di sicurezza<strong></strong></li>
                    <li><span>0 - 10 ppm</span>Monitoraggio continuo concentrazione</li>
                </ul>
            </div>
        </section>
    '''
    

   ########################################
    # GRID 0004
    ########################################
    row_0_h2 = f'''Purificazione dell'aria con ozono per eliminare odori, batteri e contaminanti'''
    row_0_subordinate = f'''Per purificare l'aria, i sistemi ad ozono ossidano odori, microrganismi e composti organici volatili presenti negli ambienti o nei condotti HVAC.'''
    row_0_img_src = f'''/immagini/placeholder.jpg'''
    row_1_h2 = f'''Trattamento dell'acqua con ozono per disinfezione e ossidazione avanzata'''
    row_1_subordinate = f'''Per trattare l'acqua, l'ozono viene dissolto nel flusso idrico per ossidare contaminanti organici, eliminare microrganismi e migliorare qualità, colore e odore dell'acqua.'''
    row_1_img_src = f'''/immagini/placeholder.jpg'''
    row_2_h2 = f'''Sanificazione delle superfici con ozono per eliminare microrganismi e residui biologici'''
    row_2_subordinate = f'''Per sanificare le superfici, l'ozono viene diffuso negli ambienti o in camere di trattamento per inattivare batteri, virus, muffe e biofilm su materiali e attrezzature.'''
    row_2_img_src = f'''/immagini/placeholder.jpg'''
    # subordinate = f'''Progettiamo e realizziamo impianti a ozono per applicazioni industriali specifiche, adattando ogni soluzione ai processi produttivi del settore di riferimento.'''
    img_height = '400px'
    grid_0004_html = f'''
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

    '''
   
    '''

    ########################################
    # FAQ 0000
    ########################################
    _id = f'FAQ 0000'
    h2 = f'''Domande frequenti sugli impianti a ozono industriali'''
    subordinate = f''' Risposte tecniche e rapide sulle applicazioni industriali dell'ozono.'''
    img_height = '400px'
    faq_0000_html = f'''
        <span style="color: #111; background-color: #ffff00;">{_id}</span>
        <section class="faq-0000">
            <div class="container-xl">
                <h2>{h2}</h2>
                <p class="faq-0000-supplementary">{subordinate}</p>
            </div>
            <div class="container-md">
                <div class="faq-0000-card">
                    <h3>Cos'è un generatore di ozono industriale?</h3>
                    <p>Un generatore di ozono industriale è un dispositivo che produce ozono (O₃) a concentrazioni controllate per sanificare ambienti, trattare acque e ossidare contaminanti in ambito produttivo. Funziona tramite scarica a corona o tecnologia UV.</p>
                </div>
                <div class="faq-0000-card">
                    <h3>L'ozono è sicuro negli ambienti di lavoro?</h3>
                    <p>L'ozono è sicuro se utilizzato con sistemi di controllo, sensori ambientali e nel rispetto dei limiti di esposizione previsti dalle normative vigenti. Gli impianti industriali prevedono monitoraggio automatico e gestione dei livelli residui.</p>
                </div>
                <div class="faq-0000-card">
                    <h3>Qual'è la differenza tra ozono e cloro?</h3>
                    <p>L'ozono è un ossidante più potente del cloro e non lascia residui chimici, poiché si riconverte in ossigeno. Il cloro, invece, può generare sottoprodotti chimici e richiede gestione dei residui.</p>
                </div>
                <div class="faq-0000-card">
                    <h3>Quanto costa un impianto a ozono?</h3>
                    <p>Il costo di un impianto a ozono varia in base a portata, concentrazione richiesta, automazione e settore applicativo. Gli impianti industriali partono da alcune migliaia di euro fino a sistemi su misura di fascia superiore.</p>
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
            <title></title>
            <meta name="description" content="">
        </head>
        <body>
            <main>
            {hero_0001_html}
            {grid_0000_html}
            {grid_0001_html}
            {grid_0002_html}
            {grid_0003_html}
            {faq_0000_html}
            {grid_0004_html}
            </main>
        </body>
        </html>
    '''
    html_folderpath = f'{g.TEMPLATES_FOLDERPATH}'
    os.makedirs(html_folderpath, exist_ok=True)
    html_filepath = f'{html_folderpath}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)
