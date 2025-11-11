from lib import g
from lib import components

def cta():
    html = f'''
        <section class="container-xl" style="margin-top: 6rem; margin-bottom: 6rem;">
            <div style="display: flex; align-items: center; gap: 3rem; margin-bottom: 2rem;">
                <h2 style="color: {g.color_black_pearl}; font-size: 1.25rem; font-weight: normal;">Contattaci</h2>
                <div style="display: flex; align-items: center; gap: 1.5rem;">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="{g.color_black_pearl}">
                            <path
                                d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm320-280L160-640v400h640v-400L480-440Zm0-80 320-200H160l320 200ZM160-640v-80 480-400Z" />
                        </svg>
                        <span>Email: info@ozonogroup.it</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="{g.color_black_pearl}">
                            <path
                                d="M798-120q-125 0-247-54.5T329-329Q229-429 174.5-551T120-798q0-18 12-30t30-12h162q14 0 25 9.5t13 22.5l26 140q2 16-1 27t-11 19l-97 98q20 37 47.5 71.5T387-386q31 31 65 57.5t72 48.5l94-94q9-9 23.5-13.5T670-390l138 28q14 4 23 14.5t9 23.5v162q0 18-12 30t-30 12ZM241-600l66-66-17-94h-89q5 41 14 81t26 79Zm358 358q39 17 79.5 27t81.5 13v-88l-94-19-67 67ZM241-600Zm358 358Z" />
                        </svg>
                        <span>Telefono: +39 0423 952833</span>
                    </div>
                </div>
            </div>
            <div style="">
                <div style="display: inline-block;">
                    <a class="button-default-3" href="/contatti.html">
                        <span>Prenota Consulenza Gratuita</span>
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#ffffff"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                    </a>
                </div>
            </div>
        </section>
    '''
    return html

def gen():
    section_hero_py = '5rem'
    section_py = '8rem'
    
    hero_button = f'''
        <div style="flex: 1; display: flex; justify-content: end; margin-top: 0.25rem;">
            <div style="display: inline-block;">
                <a class="button-default-1" href="/contatti.html">
                    <span>Prenota Consulenza Gratuita</span>
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                </a>
            </div>
        </div>
    '''
    ########################################
    # hero
    ########################################
    hero = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_hero_py};">
            <div style="display: flex; justify-content: space-between; center;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
                        Generatori e sistemi professionali ad ozono per l'industria
                    </h2>
                    <p style="color: #1f1f1f;">                        
                        Progettiamo e forniamo soluzioni affidabili per la sanificazione di ambienti, superfici e impianti produttivi.
                    </p>
                </div>
                {hero_button}
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # prodotti
    ########################################
    prodotti_piccoli_data = [
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-mini.png''',
            'title': f'''Mini''',
            'description': f'''Generatore compatto e disponibile in diversi modelli, progettato per purificare l'aria in ambienti di dimensioni contenute.''',
            'link_href': f'''/documenti/mini-o3-scheda-tecnica.pdf''',
            'link_anchor': f'''Scheda Tecnica''',
        },
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-nymphea.png''',
            'title': f'''Nymphea''',
            'description': f'''Generatore pratico e funzionale, progettato specificamente per il trattamento dell'acqua in contesti domestici e di piccola scala.''',
            'link_href': f'''/documenti/nymphaea-h2o-scheda-tecnica.pdf''',
            'link_anchor': f'''Scheda Tecnica''',
        },
    ]
    cards = []
    for item in prodotti_piccoli_data:
        cards.append(f'''
            <div> 
                <img src="{ item['image_url'] }" style="height: 10rem; object-fit: contain; margin-bottom: 1rem;">
                <h3 style="color: #222222; font-size: 1.5rem; line-height: 1.25; font-weight: bold; margin-bottom: 1rem;">
                    { item['title'] }
                </h3> 
                <p style="color: #555555; margin-bottom: 2rem;">
                    { item['description'] }                    
                </p>
                <div style="flex: 1; display: flex;;">
                    <div style="display: inline-block;">
                        <a class="button-default-2" href="{ item['link_href'] }">
                            <span>{ item['link_anchor'] }</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M360-460h40v-80h40q17 0 28.5-11.5T480-580v-40q0-17-11.5-28.5T440-660h-80v200Zm40-120v-40h40v40h-40Zm120 120h80q17 0 28.5-11.5T640-500v-120q0-17-11.5-28.5T600-660h-80v200Zm40-40v-120h40v120h-40Zm120 40h40v-80h40v-40h-40v-40h40v-40h-80v200ZM320-240q-33 0-56.5-23.5T240-320v-480q0-33 23.5-56.5T320-880h480q33 0 56.5 23.5T880-800v480q0 33-23.5 56.5T800-240H320Zm0-80h480v-480H320v480ZM160-80q-33 0-56.5-23.5T80-160v-560h80v560h560v80H160Zm160-720v480-480Z"/></svg>
                        </a>
                    </div>
                </div>
            </div>
        ''')
    cards = ''.join(cards)
    prodotti_piccoli = f'''
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
            <div style="flex: 2;">
                <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                    Generatori di piccole dimensioni
                </h2>
            </div>
            <div style="flex: 1; display: flex; justify-content: end;">
                
            </div>
        </div>
        <div class="grid-3" style="column-gap: 3rem; row-gap: 3rem;">
            {cards}
        </div>
    '''

    ########################################
    prodotti_medi_data = [
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-bigpower.png''',
            'title': f'''Bigpower''',
            'description': f'''Generatore di media potenza è disponibile in più configurazioni e garantisce un'efficace sanificazione dell'aria.''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-lympha.png''',
            'title': f'''Lympha''',
            'description': f'''Generatore di media potenza progettato per il trattamento dell'acqua in sistemi di media grandezza.''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in prodotti_medi_data:
        cards.append(f'''
            <div> 
                <img src="{ item['image_url'] }" style="height: 15rem; object-fit: contain; margin-bottom: 1rem;">
                <h3 style="color: #222222; font-size: 1.5rem; line-height: 1.25; font-weight: bold; margin-bottom: 1rem;">
                    { item['title'] }
                </h3> 
                <p style="color: #555555; margin-bottom: 2rem;">
                    { item['description'] }                    
                </p>
                <p>
                    <a style="color: #555555;" href="{ item['link_href'] }">{ item['link_anchor'] }</a>
                </p>
            </div>
        ''')
    cards = ''.join(cards)
    prodotti_medi = f'''
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
            <div style="flex: 2;">
                <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                    Generatori di medie dimensioni
                </h2>
            </div>
            <div style="flex: 1; display: flex; justify-content: end;">
                
            </div>
        </div>
        <div class="grid-3" style="column-gap: 3rem; row-gap: 3rem;">
            {cards}
        </div>
    '''
    ########################################

    ########################################
    prodotti_grandi_data = [
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-greenozone.png''',
            'title': f'''Greenozone''',
            'description': f'''Generatore ad alta capacità progettato per trattare grandi volumi d'aria in ambienti industriali.''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-hydor.png''',
            'title': f'''Hydor''',
            'description': f'''Generatore potente e altamente affidabile, specifico per il trattamento dell'acqua in impianti di grandi dimensioni.''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-delta.png''',
            'title': f'''Delta''',
            'description': f'''Generatore di ultima generazione, dotato di schermo touch per un controllo avanzato dei parametri.''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in prodotti_grandi_data:
        cards.append(f'''
            <div> 
                <img src="{ item['image_url'] }" style="height: 20rem; object-fit: contain; margin-bottom: 1rem;">
                <h3 style="color: #222222; font-size: 1.5rem; line-height: 1.25; font-weight: bold; margin-bottom: 1rem;">
                    { item['title'] }
                </h3> 
                <p style="color: #555555; margin-bottom: 2rem;">
                    { item['description'] }                    
                </p>
                <p>
                    <a style="color: #555555;" href="{ item['link_href'] }">{ item['link_anchor'] }</a>
                </p>
            </div>
        ''')
    cards = ''.join(cards)
    prodotti_grandi = f'''
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
            <div style="flex: 2;">
                <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                    Generatori di grandi dimensioni
                </h2>
            </div>
            <div style="flex: 1; display: flex; justify-content: end;">
                
            </div>
        </div>
        <div class="grid-3" style="column-gap: 3rem; row-gap: 3rem;">
            {cards}
        </div>
    '''
    ########################################

    prodotti = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            {prodotti_piccoli}
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            {prodotti_medi}
        </section>
        <div style="background-color: #ededed; height: 1px;"></div> 
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            {prodotti_grandi}
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''

    ########################################
    # html
    ########################################
    html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/style.css">
        </head>
        <body>
            {components.header_light()}
            <main>
                {hero}
                {prodotti}
                {cta()}
            </main>
                
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_filepath = f'{g.website_folderpath}/prodotti.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)
