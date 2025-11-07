from lib import g
from lib import components

def gen():
    section_hero_py = '5rem'
    section_py = '8rem'
    
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
                <div style="flex: 1; display: flex; justify-content: end; margin-top: 0.25rem;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/servizi.html">
                            <span>Richiedi Preventivo</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                </div>
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # servizi
    ########################################
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

    servizi = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            {servizi_sanificazione_ambientale}
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            {servizi_monitoraggio_controllo}
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
                <div style="background-color: #ededed; height: 1px;"></div>
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
                            <a class="button-default-3" href="/ozono.html">
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
