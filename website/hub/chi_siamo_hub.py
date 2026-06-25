from lib import g
from lib import components

def gen():    

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
        text-transform: uppercase;
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
        text-transform: uppercase;
    '''

    opacity = 0.5
    hero_0000_html = f'''
        <section 
            style="
            background-image: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), url('https://images.unsplash.com/photo-1528582654826-585a71fcf7f4?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');   
            background-position: center; 
            background-size: cover;
        ">
            {components.header_transparent()}
            <div class="m-flex container-xl" style="flex-direction: column; justify-content: center; gap: 0rem; height: 96vh;">
                <h1 style="{style_big} color: #fff;">
                    <span style="{style_small} color: #fff;">
                        Chi cerca una soluzione a ozono non ha bisogno di una macchina...
                    </span></br>
                    Ha bisogno di un risultato.
                </h1>
            </div>
        </section>
        
        <section style="padding-top: 8rem; padding-bottom: 8rem; background-color: #f4f6f8;">
            <div class="container-xl">
                <p class="container-lg"
                    style="
                    font-family: 'Manrope', sans-serif;
                    font-size: 1rem;
                    color: #1a1a1a;
                    margin-bottom: 1rem;
                ">
Ridurre le contaminazioni, migliorare il processo produttivo e aumentare la sicurezza alimentare richiede molto più che acquistare un generatore di ozono da catalogo. Richiede una soluzione progettata per la specifica applicazione, supportata da esperienza e costruita per funzionare nel mondo reale.
                </p>
            </div>
        </section>
        <section style="padding-top: 8rem; padding-bottom: 8rem;">
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
            <title>Chi Siamo | Ozonogroup</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Manrope:wght@300;400;500;600&display=swap" rel="stylesheet">
        </head>
        <body>
            <main>
                {hero_0000_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_filepath = f'{g.website_folderpath}/chi-siamo.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)
