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

    '''

    img_src = 'https://images.unsplash.com/photo-1509622905150-fa66d3906e09?q=80&w=735&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    i_get_you_0000_html = f'''
        <section style="margin-top: 8rem; padding-bottom: 8rem;">
            <div class="container-xl">
                <div class="m-flex" style="gap: 5rem;">
                    <div style="flex: 1;">
                        <h2 style="
                            font-family: 'Cormorant Garamond', serif; 
                            letter-spacing: -0.02em;
                            font-weight: 500;
                            color: #1a1a1a; 
                            font-size: 3em; 
                            margin-bottom: 3rem;
                            padding: 0 1rem;
                            text-transform: uppercase;
                        ">
Comprendiamo il problema perché lo vediamo ogni giorno
                        </h2>
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Molte aziende agroalimentari arrivano da noi dopo aver già provato altre soluzioni.
                        </p>
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Spesso hanno acquistato un generatore di ozono online con la speranza di risolvere rapidamente il problema. Ma senza un corretto dimensionamento, senza una strategia di utilizzo e senza supporto tecnico, i risultati raramente sono quelli attesi.
                        </p>
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Il problema non è l'ozono.
                        </p>
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Il problema è pensare che una tecnologia, da sola, sia una soluzione.
                        </p>
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Quando i risultati non arrivano, le aziende sono costrette a tornare a metodi alternativi: prodotti chimici che comportano costi, gestione e rischi aggiuntivi, oppure sistemi ad alta richiesta energetica come acqua calda e vapore.
                        </p>
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Noi crediamo che esista un modo migliore.
                        </p>
                    </div>
                    <div style="flex: 1;">
                        <img src="{img_src}">
                    </div>
                </div>
            </div>
        </section>
    '''
    
    img_src = 'https://images.unsplash.com/photo-1780078474389-120262d71903?q=80&w=713&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    why_0000_html = f'''
        <section style="padding-bottom: 8rem;">
            <div class="container-xl">
                <div class="m-flex" style="gap: 5rem;">
                    <div style="flex: 1;">
                        <img src="{img_src}">
                    </div>
                    <div style="flex: 1;">
                        <h2 style="
                            font-family: 'Cormorant Garamond', serif; 
                            letter-spacing: -0.02em;
                            font-weight: 500;
                            color: #1a1a1a; 
                            font-size: 3em; 
                            margin-bottom: 3rem;
                            padding: 0 1rem;
                            text-transform: uppercase;
                        ">
Perché è nata Ozonogroup
                        </h2>
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Ozonogroup nasce da una constatazione semplice: nel settore agroalimentare non esistono problemi standard e, di conseguenza, non esistono soluzioni standard.
                        </p>
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Nel corso degli anni abbiamo visto troppe aziende investire in apparecchiature inadatte alla loro applicazione, con aspettative elevate e risultati deludenti.
                        </p>
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Per questo abbiamo scelto un approccio diverso.
                        </p>
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Invece di vendere semplicemente generatori di ozono, analizziamo il processo produttivo, individuiamo la causa del problema e progettiamo una soluzione specifica per l'impianto, il prodotto e gli obiettivi del cliente.
                        </p>
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
L'obiettivo non è installare una macchina.
                        </p>
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
L'obiettivo è ottenere il risultato desiderato nel modo più efficace, sicuro ed efficiente possibile.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    '''

    opacity = 0.1
    social_proof_0000_html = f'''
        <section style="
                height: 100vh;
                background-image: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), url('/immagini/unsplash/agri-0000.jpg');   
                background-image: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), url('https://images.unsplash.com/photo-1560493676-04071c5f467b?q=80&w=1074&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D.jpg');   
                background-image: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), url('https://images.unsplash.com/photo-1483871788521-4f224a86e166?q=80&w=1331&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D.jpg');   
                background-image: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), url('https://images.unsplash.com/photo-1515276427842-f85802d514a2?q=80&w=1476&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');   
                background-position: center; 
                background-size: cover;
                display: flex;
                align-items: center;
            ">
            <div class="
                m-flex container-xl
            " 
                style="
                    flex-direction: column; 
                    justify-content: center; 
                    gap: 0rem; 
                    background-color: #ffffff;
                    padding: 3rem;
                ">
                <h2
                class="container-md" 
                style="font-family: 'Cormorant Garamond', serif; 
                    letter-spacing: -0.02em;
                    font-weight: 500;
                    color: #1a1a1a; 
                    font-size: 5rem; 
                    font-size: 3em; 
                    margin-bottom: 1rem;
                    line-height: 1.1;
                    text-align: center;
                    margin-bottom: 3rem;
                    text-transform: uppercase;
                ">
20 anni di esperienza al servizio dell'industria agroalimentare
                </h2>
                
                        <p class="container-md"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                            text-align: center;
                        ">
Da oltre 20 anni lavoriamo nel settore dell'ozono industriale con una specializzazione precisa: le applicazioni agroalimentari.
                        </p>
                        <p class="container-md"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                            text-align: center;
                        ">
Questa esperienza ci permette di comprendere rapidamente le problematiche produttive, valutare la fattibilità tecnica degli interventi e sviluppare sistemi personalizzati e automatizzati che si integrano con i processi esistenti.
                        </p>
                        <p class="container-md"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                            text-align: center;
                        ">
Ogni progetto viene sviluppato partendo dalle reali esigenze operative dell'azienda, evitando soluzioni sovradimensionate, inefficaci o difficili da gestire.
                        </p>
                        <p class="container-md"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                            text-align: center;
                        ">
Per noi la tecnologia è uno strumento.
                        </p>
                        <p class="container-md"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                            text-align: center;
                        ">
La soluzione è il progetto.
                        </p>
            </div>
        </section>
    '''

    qualities_0000_html = f'''
        <section 
            style="
                min-height: 50vh;
                padding-top: 8rem; 
                padding-bottom: 8rem; 
            "
        >
            <div class="container-xl">
                <h2 style="
                    font-family: 'Cormorant Garamond', serif; 
                    letter-spacing: 3px;
                    font-weight: 400;
                    color: #1a1a1a; 
                    margin-bottom: 1rem;
                    font-size: 1.5rem; 
                    padding: 0 1rem;
                ">
                come lavoriamo
                </h2>
                <div class="m-flex" style="gap: 2rem;">
                    <div style="flex: 1; padding: 0 1rem;">
                        <h3 style="
                            font-family: 'Cormorant Garamond', serif; 
                            letter-spacing: -0.02em;
                            font-weight: 500;
                            color: #1a1a1a; 
                            font-size: 2.5em; 
                            margin-bottom: 1rem;
                            text-transform: uppercase;
                        ">
                            Competenti
                        </h3>
                        <p
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 3rem;
                        ">
Conosciamo le dinamiche del settore agroalimentare e sappiamo come applicare l'ozono in modo efficace e misurabile.
                        </p>
                    </div>
                    <div style="flex: 1; padding: 0 1rem;">
                        <h3 style="
                            font-family: 'Cormorant Garamond', serif; 
                            letter-spacing: -0.02em;
                            font-weight: 500;
                            color: #1a1a1a; 
                            font-size: 2.5em; 
                            margin-bottom: 1rem;
                            text-transform: uppercase;
                        ">
                            Pratici
                        </h3>
                        <p
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 3rem;
                        ">
Cerchiamo soluzioni che funzionino davvero nell'operatività quotidiana, non solo sulla carta.
                        </p>
                    </div>
                    <div style="flex: 1; padding: 0 1rem;">
                        <h3 style="
                            font-family: 'Cormorant Garamond', serif; 
                            letter-spacing: -0.02em;
                            font-weight: 500;
                            color: #1a1a1a; 
                            font-size: 2.5em; 
                            margin-bottom: 1rem;
                            text-transform: uppercase;
                        ">
                            Affidabili
                        </h3>
                        <p
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Seguiamo il cliente dall'analisi iniziale alla messa in servizio, fornendo supporto tecnico e accompagnamento durante tutto il percorso.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    '''

    cta_0000_html = f'''
        <section 
            style="
                min-height: 50vh;
                padding-top: 8rem; 
                padding-bottom: 8rem; 
                background-color: #f8f9fa;
            "
        >
            <div class="container-xl">
                <div class="m-flex" style="gap: 5rem;">
                    <div style="flex: 1; padding: 0 1rem;">
                        <h2 style="
                            font-family: 'Cormorant Garamond', serif; 
                            letter-spacing: -0.02em;
                            font-weight: 500;
                            color: #1a1a1a; 
                            font-size: 3em; 
                            margin-bottom: 1rem;
                            text-transform: uppercase;
                        ">
Parliamo del tuo caso specifico
                        </h2>
                        <div>
                            <a href="/contatti.html" class="button-black-ghost-2">
                                PRENOTA
                            </a>
                        </div>
                    </div>
                    <div style="flex: 1;">
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Ogni impianto, ogni processo e ogni problema di contaminazione presenta caratteristiche diverse.
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Per questo il primo passo non è proporre una soluzione standard, ma comprendere la situazione e valutare quale approccio possa generare il miglior risultato.
                        </p>
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Prenota una chiamata conoscitiva con il team Ozonogroup.
                        </p>
                        <p class="container-lg"
                            style="
                            font-family: 'Manrope', sans-serif;
                            font-size: 1rem;
                            color: #1a1a1a;
                            margin-bottom: 1rem;
                        ">
Analizzeremo il tuo caso, risponderemo alle tue domande e ti aiuteremo a capire se l'ozono può rappresentare la soluzione più efficace per la tua applicazione.
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
            <title>Chi Siamo | Ozonogroup</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Manrope:wght@300;400;500;600&display=swap" rel="stylesheet">
        </head>
        <body>
            <main>
                {hero_0000_html}
                {i_get_you_0000_html}
                {why_0000_html}
                {social_proof_0000_html}
                {qualities_0000_html}
                {cta_0000_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_filepath = f'{g.website_folderpath}/chi-siamo.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)
