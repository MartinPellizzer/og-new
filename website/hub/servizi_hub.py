from lib import g
from lib import components

servizi_sanificazione_ambientale_data = [
    {
        'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M550.03-275q18.97 0 36.97-7.5t32-21.5l35-35-35-35-35 35q-6.79 7.09-15.84 10.05-9.05 2.95-18.11 2.95-9.05 0-18.14-2.95-9.09-2.96-15.91-10.05l-37.27-37.27Q465-390 446.97-397q-18.02-7-37-7-18.97 0-36.97 7t-32 21l-35 35 35 35 35-35q6.79-7.09 15.84-10.05 9.05-2.95 18.11-2.95 9.05 0 18.14 2.95 9.09 2.96 15.91 10.05l37.27 37.27Q495-290 513.03-282.5q18.02 7.5 37 7.5Zm0-120q18.97 0 36.97-7.5t32-21.5l35-35-35-35-35 35q-6.79 7.09-15.84 10.05-9.05 2.95-18.11 2.95-9.05 0-18.14-2.95-9.09-2.96-15.91-10.05l-37.27-37.27Q465-510 446.97-517q-18.02-7-37-7-18.97 0-36.97 7t-32 21l-35 35 35 35 35-35q6.79-7.09 15.84-10.05 9.05-2.95 18.11-2.95 9.05 0 18.14 2.95 9.09 2.96 15.91 10.05l37.27 37.27Q495-410 513.03-402.5q18.02 7.5 37 7.5Zm0-120q18.97 0 36.97-7.5t32-21.5l35-35-35-35-35 35q-6.79 7.09-15.84 10.05-9.05 2.95-18.11 2.95-9.05 0-18.14-2.95-9.09-2.96-15.91-10.05l-37.27-37.27Q465-630 446.97-637q-18.02-7-37-7-18.97 0-36.97 7t-32 21l-35 35 35 35 35-35q7-6 16-9.5t18-3.5q9 0 18.09 2.95 9.09 2.96 15.91 10.05l37.27 37.27Q495-530 513.03-522.5q18.02 7.5 37 7.5ZM160-160v-480l320-240 320 240v480H160Zm60-60h520v-394L480-803 220-614v394Zm260-292Z"/></svg>''',
        'title': f'''Sanificazione ambienti industriali''',
        'description': f'''Trattamenti completi di spazi produttivi, laboratori, magazzini.''',
        'link_href': f'''#''',
        'link_anchor': f'''Maggiori info''',
    },
    {
        'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M161-120q-18-8-26-17.5T120-165l678-675q15 5 26.5 16.5T840-796L161-120Zm-41-278v-86l356-356h86L120-398Zm0-320v-62q0-24 18-42t42-18h62L120-718Zm598 598 122-122v62q0 24-18 42t-42 18h-62Zm-320 0 442-442v86L484-120h-86Z"/></svg>''',
        'title': f'''Sanificazione superfici e attrezzature''',
        'description': f'''Applicazioni mirate su macchinari, banchi, utensili, piani di lavoro.''',
        'link_href': f'''#''',
        'link_anchor': f'''Maggiori info''',
    },
    {
        'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M480.24-260Q572-260 636-324.24q64-64.23 64-156Q700-572 635.76-636q-64.23-64-156-64Q388-700 324-635.76q-64 64.23-64 156Q260-388 324.24-324q64.23 64 156 64Zm-.24-60q-29 0-56-10.5T375-360h210q-22 19-49 29.5T480-320Zm-138-80q-8-14-13-29t-7-31h316q-2 16-7 31t-13 29H342Zm-20-100q2-16 7-31t13-29h276q8 14 13 29t7 31H322Zm53-100q22-19 49-29.5t56-10.5q29 0 56 10.5t49 29.5H375ZM180-120q-24.75 0-42.37-17.63Q120-155.25 120-180v-600q0-24.75 17.63-42.38Q155.25-840 180-840h600q24.75 0 42.38 17.62Q840-804.75 840-780v600q0 24.75-17.62 42.37Q804.75-120 780-120H180Zm0-60h600v-600H180v600Zm0-600v600-600Z"/></svg>''',
        'title': f'''Sanificazione aria e impianti HVAC''',
        'description': f'''Interventi su condotte, filtri, ventilazione e climatizzazione.''',
        'link_href': f'''#''',
        'link_anchor': f'''Maggiori info''',
    },
    {
        'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M309-650v-118h60v118h-60Zm0 361v-196h60v196h-60ZM220-80q-24.75 0-42.37-17.63Q160-115.25 160-140v-680q0-24.75 17.63-42.38Q195.25-880 220-880h520q24.75 0 42.38 17.62Q800-844.75 800-820v680q0 24.75-17.62 42.37Q764.75-80 740-80H220Zm0-60h520v-398H220v398Zm0-458h520v-222H220v222Z"/></svg>''',
        'title': f'''Sanificazione celle frigorifere e ambienti a temperatura controllata''',
        'description': f'''Eliminazione di muffe e batteri in aree refrigerate.''',
        'link_href': f'''#''',
        'link_anchor': f'''Maggiori info''',
    },
    {
        'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M224.12-161q-49.12 0-83.62-34.42Q106-229.83 106-279H40v-461q0-24 18-42t42-18h579v167h105l136 181v173h-71q0 49.17-34.38 83.58Q780.24-161 731.12-161t-83.62-34.42Q613-229.83 613-279H342q0 49-34.38 83.5t-83.5 34.5Zm-.12-60q24 0 41-17t17-41q0-24-17-41t-41-17q-24 0-41 17t-17 41q0 24 17 41t41 17ZM100-339h22q17-27 43.04-43t58-16q31.96 0 58.46 16.5T325-339h294v-401H100v401Zm631 118q24 0 41-17t17-41q0-24-17-41t-41-17q-24 0-41 17t-17 41q0 24 17 41t41 17Zm-52-204h186L754-573h-75v148ZM360-529Z"/></svg>''',
        'title': f'''Sanificazione veicoli industriali e mezzi di trasporto''',
        'description': f'''Per logistica, food delivery, flotte aziendali.''',
        'link_href': f'''#''',
        'link_anchor': f'''Maggiori info''',
    },
]

def gen_old():
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
                        Servizi professionali di sanificazione con ozono per ambienti industriali
                    </h2>
                    <p style="color: #1f1f1f;">                        
                        Soluzioni su misura per aria, superfici e impianti, studiate per garantire igiene, sicurezza e conformità normativa in ogni settore.
                    </p>
                </div>
                {hero_button}
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # servizi
    ########################################
    cards = []
    for item in servizi_sanificazione_ambientale_data:
        cards.append(f'''
            <div>
                <div style="display: inline-block; margin-bottom: 2rem; border: 1px solid #f2f2f2; border-radius: 2rem; padding: 2rem;">
                    { item['icon'] }
                </div>
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
    servizi_sanificazione_ambientale = f'''
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
            <div style="flex: 2;">
                <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                    Servizi di sanificazione ambientale
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
    servizi_monitoraggio_controllo_data = [
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M320-80q-66 0-113-47t-47-113v-400q0-66 47-113t113-47h50v-80h60v80h100v-80h60v80h50q66 0 113 47t47 113v400q0 66-47 113T640-80H320Zm0-60h320q42 0 71-29t29-71v-400q0-42-29-71t-71-29H320q-42 0-71 29t-29 71v400q0 42 29 71t71 29Zm0-440h320v-60H320v60Zm160 315q33 0 56.5-23.5T560-344q0-26-15-45t-65-76q-50 58-65 76.5T400-344q0 32 23.5 55.5T480-265ZM220-740v600-600Z"/></svg>''',
            'title': f'''Monitoraggio qualità dell'aria e superfici''',
            'description': f'''Sensori e campionamenti periodici.''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in servizi_monitoraggio_controllo_data:
        cards.append(f'''
            <div>
                <div style="display: inline-block; margin-bottom: 2rem; border: 1px solid #f2f2f2; border-radius: 2rem; padding: 2rem;">
                    { item['icon'] }
                </div>
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
    servizi_monitoraggio_controllo = f'''
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
            <div style="flex: 2;">
                <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                    Servizi di monitoraggio e controllo
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
    servizi_manutenzione_supporto_data = [
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M705-128 447-388q-23 8-46 13t-47 5q-97.08 0-165.04-67.67Q121-505.33 121-602q0-31 8.16-60.39T152-718l145 145 92-86-149-149q25.91-15.16 54.96-23.58Q324-840 354-840q99.17 0 168.58 69.42Q592-701.17 592-602q0 24-5 47t-13 46l259 258q11 10.96 11 26.48T833-198l-76 70q-10.7 11-25.85 11Q716-117 705-128Zm28-57 40-40-273-273q16-21 24-49.5t8-54.5q0-75-55.5-127T350-782l102 104q9 9 8.5 21.5T451-635L318-510q-9.27 8-21.64 8-12.36 0-20.36-8l-98-97q3 77 54.67 127T354-430q25 0 53-8t49-24l277 277ZM476-484Z"/></svg>''',
            'title': f'''Manutenzione programmata impianti ad ozono''',
            'description': f'''Controlli e sostituzione componenti periodici.''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        # {
        #     'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M320-80q-66 0-113-47t-47-113v-400q0-66 47-113t113-47h50v-80h60v80h100v-80h60v80h50q66 0 113 47t47 113v400q0 66-47 113T640-80H320Zm0-60h320q42 0 71-29t29-71v-400q0-42-29-71t-71-29H320q-42 0-71 29t-29 71v400q0 42 29 71t71 29Zm0-440h320v-60H320v60Zm160 315q33 0 56.5-23.5T560-344q0-26-15-45t-65-76q-50 58-65 76.5T400-344q0 32 23.5 55.5T480-265ZM220-740v600-600Z"/></svg>''',
        #     'title': f'''Taratura e revisione generatori ad ozono''',
        #     'description': f'''Calibrazione strumenti e controllo resa.''',
        #     'link_href': f'''#''',
        #     'link_anchor': f'''Maggiori info''',
        # },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M240-399h313v-60H240v60Zm0-130h480v-60H240v60Zm0-130h480v-60H240v60ZM80-80v-740q0-24 18-42t42-18h680q24 0 42 18t18 42v520q0 24-18 42t-42 18H240L80-80Zm134-220h606v-520H140v600l74-80Zm-74 0v-520 520Z"/></svg>''',
            'title': f'''Assistenza tecnica e pronto intervento''',
            'description': f'''Supporto post-vendita per guasti e anomalie.''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in servizi_manutenzione_supporto_data:
        cards.append(f'''
            <div>
                <div style="display: inline-block; margin-bottom: 2rem; border: 1px solid #f2f2f2; border-radius: 2rem; padding: 2rem;">
                    { item['icon'] }
                </div>
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
    servizi_manutenzione_supporto = f'''
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
            <div style="flex: 2;">
                <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                    Servizi di manutenzione e supporto tecnico
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
    servizi = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            {servizi_sanificazione_ambientale}
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            {servizi_monitoraggio_controllo}
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            {servizi_manutenzione_supporto}
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
                {servizi}
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
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_filepath = f'{g.website_folderpath}/servizi.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)

def gen():
    hero = f'''
        <h1>
            Sistemi Industriali a Ozono per l'Industria Agroalimentare
        </h1>
    '''
    style_small = f'''
        font-family: 'Cormorant Garamond', serif;
        font-family: 'Manrope', sans-serif;
        font-weight: 500;
        color: #1a1a1a;
        font-size: 5rem;
        margin-bottom: 1rem;
        text-align: center;
        margin-bottom: 3rem;
        font-size: 1.125rem;
        font-weight: 400;
        letter-spacing: 4px;
        margin-bottom: 2rem;
        line-height: 1.3;
    '''
    style_big = f'''
        font-family: 'Cormorant Garamond', serif;
        letter-spacing: -0.02em;
        font-weight: 500;
        color: #1a1a1a;
        font-size: 5rem;
        margin-bottom: 1rem;
        line-height: 1.1;
        text-align: center;
        margin-bottom: 3rem;
    '''
    hero_html = f'''
        <section 
            style="
        ">
            {components.header_light()}
            <div class="m-flex container-xl" style="flex-direction: column; justify-content: center; gap: 0rem; height: 96vh;">
                <h1 style="{style_big}">
                    SISTEMI INDUSTRIALI A OZONO PERSONALIZZATI</br>
                    <span style="{style_small}">
                        PER AZIENDE AGROALIMENTARI CHE VOGLIONO MIGLIORARE IL LORO PROCESSO PRODUTTIVO
                    </span>
                </h1>
            </div>
        </section>
    '''
    opacity = 0.4
    hero_0001_html = f'''
        <section 
            style="
            background-image: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), url('/immagini/home/uva-0000.png');   
            background-image: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), url('https://images.unsplash.com/photo-1543257580-7269da773bf5?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');   
            background-position: center; 
            background-size: cover;
        ">
            {components.header_transparent()}
            <div class="m-flex container-xl" style="flex-direction: column; justify-content: center; gap: 0rem; height: 96vh;">
                <h1 style="color: #fff; text-align: center;">
                    <span style="display: inline-block; margin-bottom: 1rem;">
SISTEMI INDUSTRIALI A OZONO PERSONALIZZATI
                    <span>
                    <span class="sup-h" style="display: inline-block; color: #fff;">
per aziende agroalimentari che vogliono migliorare il loro processo produttivo
                    </span>
                </h1>
            </div>
        </section>
    '''

    img_src = f'''
        https://images.unsplash.com/photo-1584056866693-1f9d42e9feb6?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
    '''
    intro_html = f'''
        <section class="s s-bg">
            <div class="container-xl">
                <div class="m-flex" style="gap: 5rem;">
                    <div style="flex: 1;">
                        <h2 style="text-transform: uppercase;">
Riduci le contaminazioni e aumenta la sicurezza alimentare con sistemi industriali a ozono progettati per la tua produzione
                        </h2>
                        <p>
Le contaminazioni microbiologiche rappresentano una delle principali minacce per le aziende agroalimentari. Un singolo problema lungo il processo produttivo può compromettere la qualità del prodotto, ridurne la shelf life e generare costi significativi legati a scarti, richiami o fermi produttivi.
                        </p>
                        <p>
I sistemi industriali a ozono offrono una soluzione efficace per migliorare l'igiene dei processi, ridurre la carica microbiologica e contribuire a elevare gli standard di sicurezza alimentare.
                        </p>
                        <p>
Con oltre 20 anni di esperienza nel settore agroalimentare, progettiamo e realizziamo impianti a ozono personalizzati in base alle esigenze operative, produttive e normative della tua azienda.
                        </p>
                    </div>
                    <div style="flex: 1;">
                        <img src="{img_src}">
                    </div>
                </div>
            </div>
        </section>
    '''

    servizi_0000_html = f'''
        <section class="s">
            <div class="container-xl">
                <h2 class="sup-h">
i nostri sevizi
                </h2>
                <div class="grid-2-0000">
                    <div>
                        <h3 style="text-transform: uppercase;">
                            Analisi
                        </h3>
                        <p>
Valutiamo il tuo processo produttivo, le criticità esistenti e le opportunità di integrazione della tecnologia a ozono. L'obiettivo è determinare se l'applicazione è tecnicamente ed economicamente vantaggiosa e individuare la soluzione più efficace per il tuo contesto produttivo.
                        </p>
                    </div>
                    <div>
                        <h3 style="text-transform: uppercase;">
Progettazione
                        </h3>
                        <p>
Ogni impianto viene progettato sulla base delle caratteristiche specifiche della tua produzione. Dimensioniamo il sistema in funzione dei volumi, delle modalità operative, degli obiettivi di sanificazione e delle esigenze di integrazione con gli impianti esistenti.
                        </p>
                    </div>
                    <div>
                        <h3 style="text-transform: uppercase;">
Installazione
                        </h3>
                        <p>
Seguiamo tutte le fasi di installazione e collaudo per garantire il corretto funzionamento del sistema e la piena integrazione nei processi produttivi.
                        </p>
                    </div>
                    <div>
                        <h3 style="text-transform: uppercase;">
Assistenza
                        </h3>
                        <p>
Manteniamo il sistema efficiente nel tempo attraverso interventi programmati, controlli periodici e supporto tecnico specializzato.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    '''
    img_src = f'https://images.unsplash.com/photo-1581091226507-ca552def2daf?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    processo_0000_html = f'''
        <section class="s s-bg">
            <div class="container-xl">
                <div class="m-flex" style="gap: 5rem;">
                    <div style="flex: 1;">
                        <img src="{img_src}">
                    </div>
                    <div style="flex: 1;">
                        <h2 class="sup-h">
come funziona il processo
                        </h2>
                        <h3 style="text-transform: uppercase;">
1. Chiamata Conoscitiva
                        </h3>
                        <p>
Analizziamo le esigenze della tua azienda e gli obiettivi che desideri raggiungere.
                        </p>
                        <h3 style="text-transform: uppercase;">
2. Sopralluogo Tecnico
                        </h3>
                        <p>
Raccogliamo tutte le informazioni necessarie sul processo produttivo, sugli impianti esistenti e sulle criticità da risolvere.
                        </p>
                        <h3 style="text-transform: uppercase;">
3. Valutazione di Fattibilità
                        </h3>
                        <p>
Verifichiamo la compatibilità della tecnologia a ozono con la tua applicazione e definiamo il potenziale beneficio operativo.
                        </p>
                        <h3 style="text-transform: uppercase;">
4. Progettazione del Sistema
                        </h3>
                        <p>
Sviluppiamo una soluzione su misura ottimizzata per la tua realtà produttiva.
                        </p>
                        <h3 style="text-transform: uppercase;">
5. Installazione e Collaudo
                        </h3>
                        <p>
Installiamo il sistema e ne verifichiamo le prestazioni attraverso test e controlli operativi.
                        </p>
                        <h3 style="text-transform: uppercase;">
6. Supporto Continuativo
                        </h3>
                        <p>
Forniamo assistenza tecnica e manutenzione programmata per garantire risultati costanti nel tempo.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    '''

    style_text = f'''
        style="
            font-family: 'Manrope', sans-serif;
            font-size: 1rem;
            color: #1a1a1a;
        "
    '''
    opacity = 0.3
    for_who_0000_html = f'''
        <section 
            class="s"
            style="
                background-image: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), url('https://images.unsplash.com/photo-1533077162801-86490c593afb?q=80&w=1074&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');   
                background-position: center; 
                background-size: cover;
                display: flex;
                align-items: center;
            ">
            <div 
                class="
                    grid-2
                    container-xl
                " 
                style="
                    gap: 5rem;
                "
            >
                <div 
                    style="
                        background-color: #ffffff;
                        padding: 3rem;
                    "
                >
                    <h2 style="text-transform: uppercase;">
Per Chi è Indicato
                    </h2>
                        <p
                            style="
                                font-family: 'Manrope', sans-serif;
                                font-size: 1rem;
                                color: #1a1a1a;
                                margin-bottom: 1rem;
                            "
                        >
                            I nostri sistemi industriali a ozono sono particolarmente adatti per aziende agroalimentari che desiderano:
                        </p>
                        <ul 
                            style="
                                margin-left: 1.5rem;
                                display: flex;
                                flex-direction: column;
                                gap: 0.5rem;
                            "
                        >
                            <li {style_text}>
                                Ridurre il rischio di contaminazioni
                            </li>
                            <li {style_text}>
                                Migliorare la sicurezza alimentare
                            </li>
                            <li {style_text}>
                                Aumentare la shelf life dei prodotti
                            </li>
                            <li {style_text}>
                                Ottimizzare i processi produttivi
                            </li>
                            <li {style_text}>
                                Integrare tecnologie innovative nei processi
                            </li>
                            <li {style_text}>
                                Affidarsi a un partner specializzato nel settore agroalimentare
                            </li>
                        </ul>
                </div>
                <div 
                    style="
                        background-color: #ffffff;
                        padding: 3rem;
                    "
                >
                    <h2 style="text-transform: uppercase;">
                        Non è il servizio ottimale per te se
                    </h2>
                        <ul 
                            style="
                                margin-left: 1.5rem;
                                display: flex;
                                flex-direction: column;
                                gap: 0.5rem;
                            "
                        >
                            <li {style_text}>
                                Sei un privato
                            </li>
                            <li {style_text}>
                                Cerchi soluzioni standard, quindi non idonee per l'utilizzo industriale
                            </li>
                            <li {style_text}>
                                Non hai la possibilità di integrare nuove tecnologie nei tuoi processi produttivi
                            </li>
                            <li {style_text}>
                                Stai cercando semplicemente un fornitore di apparecchiature senza supporto tecnico e consulenziale
                            </li>
                        </ul>
                </div>
            </div>
        </section>
    '''
    why_us_0000_html = f'''
        <section class="s">
            <div class="container-xl">
                <h2 class="sup-h">
perché scegliere noi
                </h2>
                <div class="grid-2-0000">
                    <div>
                        <h3 style="text-transform: uppercase;">
                            Oltre 20 Anni di Esperienza
                        </h3>
                        <p>
Da oltre due decenni supportiamo aziende agroalimentari nell'implementazione di soluzioni basate sull'ozono.
                        </p>
                    </div>
                    <div>
                        <h3 style="text-transform: uppercase;">
Specializzazione nel Settore Alimentare
                        </h3>
                        <p>
Conosciamo le problematiche specifiche dell'industria alimentare e progettiamo soluzioni pensate per rispondere alle sue esigenze operative.
                        </p>
                    </div>
                    <div>
                        <h3 style="text-transform: uppercase;">
                            Soluzioni Su Misura
                        </h3>
                        <p>
Ogni sistema viene progettato sulla base della tua applicazione, dei tuoi processi e dei risultati che desideri ottenere.
                        </p>
                    </div>
                    <div>
                        <h3 style="text-transform: uppercase;">
                            Supporto Completo
                        </h3>
                        <p>
Ti accompagniamo dalla valutazione iniziale fino alla manutenzione programmata dell'impianto.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    '''
    cta_0000_html = f'''
        <section class="s s-bg">
            <div class="container-xl">
                <div class="grid-2-0000">
                    <div style="flex: 1;">
                        <h2 style="text-transform: uppercase;">
                            Prenota una Chiamata Conoscitiva
                        </h2>
                        <div>
                            <a href="/contatti.html" class="button-black-ghost-2">
                                PRENOTA
                            </a>
                        </div>
                    </div>
                    <div style="flex: 1;">
                        <p>
Scopri se un sistema industriale a ozono può aiutare la tua azienda a ridurre le contaminazioni, migliorare la sicurezza alimentare e aumentare la shelf life dei tuoi prodotti.                        </p>
                        <p>
Durante la chiamata analizzeremo la tua applicazione, valuteremo le opportunità di integrazione della tecnologia e ti forniremo un primo orientamento tecnico senza impegno.
                        </p>
                        <p>
Prenota ora una chiamata conoscitiva e scopri la soluzione più adatta alla tua realtà produttiva.
                        </p>
                    </div>
                </div>
            </div>
        </section>
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
            <link rel="stylesheet" href="/styles.css">
            <title>Servizi | Ozonogroup</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Manrope:wght@300;400;500;600&display=swap" rel="stylesheet">
        </head>
        <body>
            <main>
                {hero_0001_html}
                {intro_html}
                {servizi_0000_html}
                {processo_0000_html}
                {for_who_0000_html}
                {why_us_0000_html}
                {cta_0000_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_filepath = f'{g.website_folderpath}/servizi.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)
