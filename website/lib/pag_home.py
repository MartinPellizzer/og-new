import os

from lib import g
from lib import components

def gen():
    with open('styles/tmp/pag-home.css', 'w') as f: f.write('')
    html_hero = f'''
        <section class="home-hero-section">
            <div class="container-xl" style="height: 100%;">
                <div class="home-header">
                    <div class="home-header-menu">
                        <a class="home-header-logo" href="#">Ozonogroup</a>
                        <nav class="home-header-menu-nav">
                            <a href="#">Home</a>
                            <a href="/prodotti.html">Prodotti</a>
                            <a href="#">Contatti</a>
                        </nav>
                    </div>
                    <div>
                        <a class="home-header-button" href="#">Prenota consulenza gratuita</a>
                    </div>
                </div>
                <div class="home-hero-container">
                    <div class="home-hero-title-container">
                        <div style="flex: 2;">
                            <h1 class="home-hero-title">Sanificazione
                                ozono per l'industria alimentare
                            </h1>
                        </div>
                        <div style="flex: 1;"></div>
                    </div>
                    <div class="home-hero-content-container">
                        <div style="flex: 2;"></div>
                        <div style="flex: 1;">
                            <p style="color: #ffffff; font-size: 16px; line-height: 24px; margin-bottom: 24px;">Progettiamo
                                sistemi di sanificazione con ozono per ambienti di produzione alimentari più
                                sicuri e igienici (senza l'uso di sostanze chimiche).</p>
                            <div style="display: flex; gap: 24px;">
                                <a style="color: #111111; background-color: #ffffff; padding: 8px 16px; border-radius: 9999px; border: 1px solid #ffffff;"
                                    href="#">Prenota consulenza</a>
                                <a style="color: #ffffff; padding: 8px 16px; border-radius: 9999px; border: 1px solid #ffffff;"
                                    href="#">Come funziona</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    '''

    html_index = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            {components.html_header_light()}
            {components.html_header_dark()}
            <main>
                {html_hero}
            </main>
            <footer>
            </footer>
        </body>
        </html>
    '''

    html_index_filepath = 'public/index.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)

