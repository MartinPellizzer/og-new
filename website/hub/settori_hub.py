
from lib import g
from lib import io
from lib import components

from data import settori_data

def gen():
    ########################################
    # HERO 0001
    ########################################
    opacity = 0.3
    hero_0001_html = f'''
        <section 
            style="
            background-image: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), url('/immagini/home/uva-0000.png');   
            background-position: center; 
            background-size: cover;
        ">
            {components.header_transparent()}
            <div class="m-flex container-xl" style="flex-direction: column; justify-content: center; gap: 0rem; height: 96vh;">
                <h1 style="color: #fff; text-align: center;">
                    SETTORI DI UTILIZZO DELL'OZONO
                </h1>
                <div style="text-align: center;">
                    <a href="/" class="button-white-ghost-2">
                    Prenota Consulenza
                </a>
                </div>
            </div>
        </section>
    '''

    sectors_cards_html = f''
    sectors_data = io.csv_to_dict('C:\ozonogroup\data\ssot\dataset\manual\settori.csv', delimiter='\\')
    print(sectors_data)
    quit()
    sectors_0000_html = f'''
        <section>
            <div class="container-xl grid-4">
                {sectors_cards_html}
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
            <title>Sistemi Industriali a Ozono | Ozonogroup</title>
            <meta name="description" content="Tecnologie e sistemi a ozono per applicazioni industriali, commerciali e civili. Progettazione, applicazioni e guida tecnica sull'ozono.">
        </head>
        <body>
            <main>
                {hero_0001_html}
            </main>
            <!-- =======================================
                 FOOTER
                 Include company info, legal, sitemap, social links
            ======================================== -->
            {components.footer_dark()}
        </body>
        </html>
    '''

    html_filepath = f'{g.WEBSITE_FOLDERPATH}/settori.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)
    print(html)

