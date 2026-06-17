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
        </section>
    '''
    return html

def gen():
    ########################################
    # hero
    ########################################
    opacity = 0.3
    hero_html = f'''
        <section 
            style="
        ">
            {components.header_light()}
            <div class="m-flex container-xl" style="flex-direction: column; justify-content: center; gap: 0rem; height: 96vh;">
                <h1 style="font-family: 'Cormorant Garamond', serif; 
                    letter-spacing: -0.02em;
                    font-weight: 500;
                    color: #1a1a1a; font-size: 5rem; margin-bottom: 1rem;
                    text-align: center;
                    margin-bottom: 3rem;
                ">
                    <span style="
                        font-family: 'Cormorant Garamond', sans-serif;
                        font-size: 2rem; 
                        font-weight: 400;
                        letter-spacing: 3px;
                        margin-bottom: 1rem;
                    ">
                    sistemi industriali a ozono:</span>
                    <br>
                    MIGLIORA LA TUA PRODUZIONE AGROALIMENTARE
                </h1>
                <div style="text-align: center;">
                    <a href="/" class="button-black-ghost-2">
                    Prenota Consulenza
                </a>
                </div>
            </div>
        </section>
    '''

    hero_html = f'''
        <section 
            style="
        ">
            {components.header_light()}
            <div class="m-flex container-xl" 
                style="
                    flex-direction: column; 
                    justify-content: center; 
                    gap: 0rem; height: 
                    96vh;
                ">
                <div style="
                    background-color: #000;
                    padding: 2rem 3rem 5rem 3rem;
                ">
                    <h1 style="font-family: 'Cormorant Garamond', serif; 
                        letter-spacing: -0.02em;
                        font-weight: 500;
                        color: #ffffff;
                        font-size: 5rem;
                        text-align: center;
                        margin-bottom: 3rem;
                    ">
                        <span style="
                            font-family: 'Cormorant Garamond', sans-serif;
                            font-size: 2rem; 
                            font-weight: 400;
                            letter-spacing: 3px;
                            margin-bottom: 1rem;
                        ">
                            USA UN SISTEMA INDUSTRIALE A OZONO PER MIGLIORARE LA TUA PRODUZIONE 
                        </span>
                        <br>
                        MIGLIORA LA TUA PRODUZIONE AGROALIMENTARE
                    </h1>
                    <p>
                    </p>
                    <div style="text-align: center;">
                        <a href="/" class="button-white-ghost-2">
                            Prenota Consulenza
                        </a>
                    </div>
                </div>
            </div>
        </section>
    '''

    hero_html = f'''
        <section 
            style="
        ">
            {components.header_light()}
            <div class="m-flex container-xl" style="flex-direction: column; justify-content: center; gap: 0rem; height: 96vh;">
                <h1 style="
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
                ">
                    ACQUISTA UN SISTEMA INDUSTRIALE A OZONO E MIGLIORA LA TUA PRODUZIONE
                </h1>
                <p style="font-family: 'Cormorant Garamond', serif; 
                    letter-spacing: -0.02em;
                    font-weight: 500;
                    color: #1a1a1a; 
                    font-size: 5rem; 
                    margin-bottom: 1rem;
                    line-height: 1.1;
                    text-align: center;
                    margin-bottom: 3rem;
                ">
                    MIGLIORARE IL TUO PROCESSO PRODUTTIVO AGROALIMENTARE NON E' MAI STATO COSI' FACILE.
                </p>
                <div class="m-flex" style="gap: 1rem; margin: 0 auto;">
                    <div style="text-align: center;">
                        <span class="button-black-2" style="display: flex; align-items: center; gap: 0.5rem;">
                            <svg xmlns="http://www.w3.org/2000/svg" height="20" viewBox="0 -960 960 960" width="20" fill="#ffffff">
                                <path
                                    d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm320-280L160-640v400h640v-400L480-440Zm0-80 320-200H160l320 200ZM160-640v-80 480-400Z" />
                            </svg>
                            <span style="text-transform: capitalize;">Email: </span>
                            <span style="text-transform: lowercase;">info@ozonogroup.it</span>
                        </span>
                    </div>
                    <div style="text-align: center;">
                        <span class="button-black-ghost-2" style="display: flex; align-items: center; gap: 0.5rem;">
                            <svg xmlns="http://www.w3.org/2000/svg" height="20" viewBox="0 -960 960 960" width="20" fill="#1a1a1a">
                                <path
                                    d="M798-120q-125 0-247-54.5T329-329Q229-429 174.5-551T120-798q0-18 12-30t30-12h162q14 0 25 9.5t13 22.5l26 140q2 16-1 27t-11 19l-97 98q20 37 47.5 71.5T387-386q31 31 65 57.5t72 48.5l94-94q9-9 23.5-13.5T670-390l138 28q14 4 23 14.5t9 23.5v162q0 18-12 30t-30 12ZM241-600l66-66-17-94h-89q5 41 14 81t26 79Zm358 358q39 17 79.5 27t81.5 13v-88l-94-19-67 67ZM241-600Zm358 358Z" />
                            </svg>
                            <span style="text-transform: capitalize;">Telefono: </span>
                            <span style="text-transform: lowercase;">+39 0423 952833</span>
                        </span>
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
            <title>Contatti | Ozonogroup</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Manrope:wght@300;400;500;600&display=swap" rel="stylesheet">
        </head>
        <body>
            <main>
                {hero_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
                # {about_0000_html}
                # {cta()}
    html_filepath = f'{g.website_folderpath}/contatti.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)
