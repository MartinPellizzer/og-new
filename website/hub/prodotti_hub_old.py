def products_gen_old():
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
            'link_href': f'''/documenti/big-power-iv-scheda-tecnica.pdf''',
            'link_anchor': f'''Scheda Tecnica''',
        },
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-lympha.png''',
            'title': f'''Lympha''',
            'description': f'''Generatore di media potenza progettato per il trattamento dell'acqua in sistemi di media grandezza.''',
            'link_href': f'''/documenti/lympha-h2o-scheda-tecnica.pdf''',
            'link_anchor': f'''Scheda Tecnica''',
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
            'link_href': f'''/documenti/greenozone-scheda-tecnica.pdf''',
            'link_anchor': f'''Scheda Tecnica''',
        },
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-hydor.png''',
            'title': f'''Hydor''',
            'description': f'''Generatore potente e altamente affidabile, specifico per il trattamento dell'acqua in impianti di grandi dimensioni.''',
            'link_href': f'''/documenti/hydor-h2o-scheda-tecnica.pdf''',
            'link_anchor': f'''Scheda Tecnica''',
        },
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-delta.png''',
            'title': f'''Delta''',
            'description': f'''Generatore di ultima generazione, dotato di schermo touch per un controllo avanzato dei parametri.''',
            'link_href': f'''/documenti/delta-scheda-tecnica.pdf''',
            'link_anchor': f'''Scheda Tecnica''',
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
prodotti_tutti_data = [
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-mini.png''',
            'title': f'''Mini''',
            'description': f'''Generatore compatto e disponibile in diversi modelli, progettato per purificare l'aria in ambienti di dimensioni contenute.''',
            'link_href': f'''/documenti/mini-o3-scheda-tecnica.pdf''',
            'link_anchor': f'''Scheda Tecnica''',
            'type': f'''Aria'''.title(),
            'price': f'''€2,700''',
        },
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-nymphea.png''',
            'title': f'''Nymphea''',
            'description': f'''Generatore pratico e funzionale, progettato specificamente per il trattamento dell'acqua in contesti domestici e di piccola scala.''',
            'link_href': f'''/documenti/nymphaea-h2o-scheda-tecnica.pdf''',
            'link_anchor': f'''Scheda Tecnica''',
            'type': f'''Acqua'''.title(),
            'price': f'''€1,600''',
        },
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-bigpower.png''',
            'title': f'''Bigpower''',
            'description': f'''Generatore di media potenza è disponibile in più configurazioni e garantisce un'efficace sanificazione dell'aria.''',
            'link_href': f'''/documenti/big-power-iv-scheda-tecnica.pdf''',
            'link_anchor': f'''Scheda Tecnica''',
            'type': f'''Aria'''.title(),
            'price': f'''€2,700''',
        },
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-lympha.png''',
            'title': f'''Lympha''',
            'description': f'''Generatore di media potenza progettato per il trattamento dell'acqua in sistemi di media grandezza.''',
            'link_href': f'''/documenti/lympha-h2o-scheda-tecnica.pdf''',
            'link_anchor': f'''Scheda Tecnica''',
            'type': f'''Acqua'''.title(),
            'price': f'''€2,700''',
        },
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-greenozone.png''',
            'title': f'''Greenozone''',
            'description': f'''Generatore ad alta capacità progettato per trattare grandi volumi d'aria in ambienti industriali.''',
            'link_href': f'''/documenti/greenozone-scheda-tecnica.pdf''',
            'link_anchor': f'''Scheda Tecnica''',
            'type': f'''Aria'''.title(),
            'price': f'''€2,700''',
        },
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-hydor.png''',
            'title': f'''Hydor''',
            'description': f'''Generatore potente e altamente affidabile, specifico per il trattamento dell'acqua in impianti di grandi dimensioni.''',
            'link_href': f'''/documenti/hydor-h2o-scheda-tecnica.pdf''',
            'link_anchor': f'''Scheda Tecnica''',
            'type': f'''Acqua'''.title(),
            'price': f'''€2,700''',
        },
        {
            'image_url': f'''/immagini/ozonogroup-ozonizzatore-delta.png''',
            'title': f'''Delta''',
            'description': f'''Generatore di ultima generazione, dotato di schermo touch per un controllo avanzato dei parametri.''',
            'link_href': f'''/documenti/delta-scheda-tecnica.pdf''',
            'link_anchor': f'''Scheda Tecnica''',
            'type': f'''Aria'''.title(),
            'price': f'''€2,700''',
        },
    ]