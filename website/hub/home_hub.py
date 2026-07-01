
from lib import g
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
                    <span class="sup-h" style="color: #ffffff;">
                    sistemi industriali a ozono:</span>
                    <br>
                    MIGLIORA LA TUA PRODUZIONE AGROALIMENTARE
                </h1>
                <div style="text-align: center;">
                    <a href="/" class="button-white-ghost-2">
                    Prenota Consulenza
                </a>
                </div>
            </div>
        </section>
    '''


    img_src = f'https://images.unsplash.com/photo-1515150144380-bca9f1650ed9?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    img_src = 'https://images.unsplash.com/photo-1591268315196-2c9b815d71cd?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    img_src = 'https://images.unsplash.com/photo-1518994603110-1912b3272afd?q=80&w=848&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    what_0000_html = f'''
        <section class="s">
            <div class="container-xl">
                <div class="m-flex" style="gap: 5rem;">
                    <div style="flex: 1;">
                        <p class="sup-h">
meno sprechi, maggior profitto
                        </p>
                        <h2>
UN NUOVO SISTEMA PER SANIFICARE I TUOI PRODOTTI IN MODO RAPIDO ED ECOLOGICO
                        </h2>
                        <p>
Se la tua produzione è a rischio a causa di contaminazioni microbiologiche (come batteri, muffe o lieviti), devi sapere che non sei il solo. Purtroppo, questo è un problema fin troppo diffuso nel settore agroalimentare.
                        </p>
                        <p>
Infatti, queste contaminazioni si trovano in gran numero nell'aria dei locali di stoccaggio dei prodotti, sulle superfici di lavorazione e persino nell'acqua di lavaggio che usi durante il tuo processo produttivo. 
Da qui deriva la perdita di qualità del tuo prodotto, la riduzione della sua shelf life o addirittura l'obbligo di scartare il prodotto stesso prima di poterlo immettere nel mercato.
                        </p>
                        <p>
Se ti trovi in questa situazione, un rimedio pratico è l'ozono.
                        </p>
                        <p>
I sistemi industriali a ozono ti permettono di ridurre microbi e altri agenti patogeni in modo rapido ed ecologico.
Come noto, l'ozono è una delle molecole con il più alto potere ossidante esistente (maggiore del cloro) e per questo disinfetta velocemente. In aggiunta, non lascia residui chimici sui prodotti, quindi aiuta a ridurre (o eliminare completamente) l'uso di sostanze chimiche come disinfettanti clorati, composti quaternari d'ammonio, altri biocidi chimici.
                        </p>
                    </div>
                    <div style="flex: 1;">
                        <img src="{img_src}">
                    </div>
                </div>
            </div>
        </section>
    '''

    about_0000_html = f'''
        <section class="s s-bg">
            <div class="container-xl">
                <div class="m-flex" style="gap: 5rem;">
                    <div style="flex: 1;">
                        <h2>
LA NOSTRA AZIENDA
                        </h2>
                        <p class="sup-h">
sviluppiamo tecnologia a ozono per l'industria agroalimentare
                        </p>
                        <div>
                            <a href="/contatti.html" class="button-black-ghost-2">
                                CONTATTACI
                            </a>
                        </div>
                    </div>
                    <div style="flex: 1;">
                        <p>
Ozonogroup progetta sistemi industriali a ozono da oltre 20 anni, concentrandosi sul settore agroalimentare. Per questo motivo conosciamo bene i problemi di contaminazione che aziende come caseifici, salumifici e birrifici (per citarne alcuni) sono costrette ad affrontare giorno per giorno durante le fasi di lavorazione dei prodotti alimentari.
                        </p>
                        <p>
Infatti, ci siamo specializzati nella realizzazione di attrezzature in grado di risolvere questi tuoi problemi in modo preciso e automatizzato. Puoi usare i nostri sistemi per produrre ozono ad alta purezza e a basso consumo energetico. nonche' di monitorare l'andamento del trattamento. In questo modo, con pochi test, sarai in grato di trovare la formula esatta per risolvere queste tue problematiche (o prevenirle). Perche siamo convinti che debba essere il sistema a ozono ad addattarsi al cliente, non viceversa.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    '''

    offer_0000_html = f'''
        <section class="s">
            <div class="container-xl">
                <h2 class="sup-h">
cosa facciamo
                </h2>
                <div class="grid-3-0000">
                    <div style="flex: 1;">
                        <h3>
ANALISI FATTIBILITÀ
                        </h3>
                        <p>
Non sai se l'ozono è la soluzione migliore per te? Abbiamo lavorato nel campo dell'ozono per 20+ anni e ci siamo imbattuti in molte situazioni in cui l'ozono non era la soluzione migliore, quindi siamo in grado di stimare se questa tecnologia fa al caso tuo o no. In questo modo, puoi evitare che la tua azienda faccia investimenti non vantaggiosi.
                        </p>
                    </div>
                    <div style="flex: 1;">
                        <h3>
SISTEMA PERSONALIZZATO
                        </h3>
                        <p>
Se dopo una prima analisi di fattibilità riteniamo che l'ozono è la soluzione ottimale per te, svilupperemo il sistema a ozono ideale per la tua specifica applicazione. Questo sistema verrà progettato per essere facilmente integrato nel tuo processo produttivo e per darti un ritorno di investimento positivo nel modo più immediato possiblile.
                        </p>
                    </div>
                    <div style="flex: 1;">
                        <h3>
INSTALLAZIONE E MANUTENZIONE
                        </h3>
                        <p>
Una volta sviluppato il sistema ad-hoc per la tua applicazione, veniamo personalmente a consegnartelo, ad aiutarti con l'installazione e a fare il collaudo. Infine, valutiamo con te un piano di manutenzione programmata per assicurarti che il tuo nuovo sistema sia sempre funzionante e performante.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    '''


    cta_0000_html = f'''
        <section style="
                height: 100vh;
                background-image: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), url('                        https://images.unsplash.com/photo-1637181156153-bedd1098f8c1?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D.jpg');   
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
                <h2 class="sup-h" style="text-align: center;">
comincia a migliorare la tua produzione agroalimentare
                </h2>
                <p class="t-h-md" style="text-align: center;">
CONTATTACI E DESCRIVICI LA TUA SITUAZIONE. VALUTEREMO CON TE SE L'OZONO È LA SOLUZIONE MIGLIORE.
                </p>
                <div class="m-flex" style="gap: 1rem; margin: 0 auto;">
                    <div style="text-align: center;">
                        <a href="/contatti.html" class="button-black-2" style="display: flex; align-items: center; gap: 0.5rem;">
                            LAVORIAMO ASSIEME
                        </a>
                    </div>
                </div>
            </div>
        </section>
    '''
                # margin-top: 8rem;

   
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
            <main class="home" id="contenuto-principale">
                {hero_0001_html}
                {what_0000_html}
                {about_0000_html}
                {offer_0000_html}
                {cta_0000_html}
            </main>
            <!-- =======================================
                 FOOTER
                 Include company info, legal, sitemap, social links
            ======================================== -->
            {components.footer_dark()}
        </body>
        </html>
    '''
    
    html_filepath = f'{g.WEBSITE_FOLDERPATH}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)

