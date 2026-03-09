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
                <div class="grid-0000-cards">
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
