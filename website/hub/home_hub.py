from lib import g
from lib import components

from data import settori_data

def gen():
    section_py = '8rem'
    opacity = 0.66
    hero_old = f'''
        <section style="
                background: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), url('/immagini/home/generatore-ozono-industriale-impianto.jpg');
                background-size: cover;
                background-position: center;
                padding-top: 8rem;
                padding-bottom: 8rem;
        ">
            <div class="container-xl" style="display: flex;">
                <div style="flex: 3;">
                    <h1 style="color: #ffffff; font-size: 4rem; line-height: 1; font-weight: bold; text-align: left; margin-bottom: 1rem;">
                        Produciamo generatori di ozono industriali ad alta efficienza
                    </h1>
                    <p style="color: #ffffff; font-size: 1.25rem; line-height: 1.4; text-align: left; margin-bottom: 2rem;">
                      <strong>I generatori di ozono industriali</strong> sono sistemi progettati e prodotti internamente
                      per il trattamento delle acque e la sanitizzazione industriale,
                      garantendo controllo preciso dell’ozono, affidabilità operativa
                      e conformità alle normative di sicurezza.
                    </p>
                    <a class="button-square-default-accent"> 
                        <span>Prenota Consulenza Gratuita</span>
                    </a>
                </div>
                <div style="flex: 2;">
                </div>
            </div>
        </section>      
    '''

    hero_1 = f'''
        <section style="
                background: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), url('/immagini/home/generatore-ozono-industriale-impianto.jpg');
                background-size: cover;
                background-position: center;
                height: 60vh;
        ">
            <div class="container-xl" style="display: flex; align-items: center; height: 100%;">
                <div style="flex: 3;">
                    <h1 style="color: #ffffff; font-size: 4rem; line-height: 1; text-align: left; margin-bottom: 1rem;">
                        Generatori di ozono industriali per la sanificazione efficace di impianti e ambienti
                    </h1>
                    <p style="color: #ffffff; font-size: 1.25rem; line-height: 1.4; text-align: left; margin-bottom: 2rem;">
                      Ozonogroup progetta e produce sistemi a ozono per la sanificazione industriale, garantendo sicurezza, efficienza e conformità alle normative.conformità alle normative di sicurezza.
                    </p>
                    <a class="button-square-default-accent"> 
                        <span>Richiedi una consulenza gratuita</span>
                    </a>
                </div>
                <div style="flex: 1;">
                </div>
            </div>
        </section>      
    '''

    hero_2 = f'''
        <section class="container-xl" style="margin-top: 5rem;">
            <div style="display: flex; gap: 3rem;">
                <div style="flex: 3;">
                    <h1 style="color: #111111; font-size: 4rem; line-height: 1; font-weight: normal; text-align: left; margin-bottom: 1rem;">
                        Produciamo generatori di ozono industriali ad alta efficienza
                    </h1>
                    <p style="color: #111111; font-size: 1.125rem; line-height: 1.4; text-align: left; margin-bottom: 2rem;">
                        <strong>I generatori di ozono industriali</strong> sono sistemi progettati e prodotti ad-hoc
                        per il trattamento delle acque e la sanitizzazione industriale,
                        garantendo controllo preciso dell’ozono, affidabilità operativa
                        e conformità alle normative di sicurezza.
                    </p>
                    <div>
                        <a class="button-invert" href="/contatti.html">
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M680-80v-120H560v-80h120v-120h80v120h120v80H760v120h-80Zm-480-80q-33 0-56.5-23.5T120-240v-480q0-33 23.5-56.5T200-800h40v-80h80v80h240v-80h80v80h40q33 0 56.5 23.5T760-720v244q-20-3-40-3t-40 3v-84H200v320h280q0 20 3 40t11 40H200Zm0-480h480v-80H200v80Zm0 0v-80 80Z"/></svg>
                            <span>Prenota Consulenza Gratuita</span>
                        </a>
                    </div>
                </div>
                <div style="flex: 2">
                    <img src="/immagini/home/generatore-ozono-industriale-impianto.jpg" alt="Generatore di ozono industriale installato in un impianto per il trattamento delle acque">
                </div>
            </div>
        </section>      
    '''

    # settori
    settori_1 = f'''
        <section style="padding-top: 6rem;">
            <div class="container-xl">
                <h2 style="margin-bottom: 1rem;">
                    Applicazioni industriali dei nostri sistemi
                </h2>
                <p style="margin-bttom: 3rem;">
I sistemi a ozono industriali di Ozonogroup trovano applicazione in molteplici settori, garantendo sanificazione efficace, sicurezza e piena conformità alle normative. Scopri come le nostre soluzioni possono supportare il tuo settore industriale, riducendo rischi di contaminazione e migliorando l’igiene degli impianti.
                </p>
                <div class="grid-4" style="padding-top: 3rem; row-gap: 3rem;">
                    <div>
                        <h3 style="margin-bottom: 1rem;">
                            Alimentare
                        </h3>
                        <img src="/immagini/home/alimentare.jpg" style="margin-bottom: 1rem;">
                        <p>
                            Sanificazione industriale alimentare con generatori di ozono. Igiene completa, sicurezza HACCP e protezione di linee produttive e impianti.
                        </p>
                    </div>
                    <div>
                        <h3 style="margin-bottom: 1rem;">
                            Farmaceutico
                        </h3>
                        <img src="/immagini/home/farmaceutico.jpg" style="margin-bottom: 1rem;">
                        <p>
                            Ozono industriale per impianti farmaceutici. Controllo contaminazioni, igiene rigorosa e piena conformità agli standard GMP.
                        </p>
                    </div>
                    <div>
                        <h3 style="margin-bottom: 1rem;">
                            Confezionamento
                        </h3>
                        <img src="/immagini/home/packaging.jpg" style="margin-bottom: 1rem;">
                        <p>
                            Generatori di ozono per linee di packaging industriale. Igiene e sicurezza in ogni fase della produzione e del confezionamento.
                        </p>
                    </div>
                    <div>
                        <h3 style="margin-bottom: 1rem;">
                            Trasporti
                        </h3>
                        <img src="/immagini/home/trasporti.jpg" style="margin-bottom: 1rem;">
                        <p>
                            Sanificazione industriale di magazzini e centri logistici. Protezione della merce e riduzione contaminazioni senza fermare le operazioni.
                        </p>
                    </div>
                    <div>
                        <h3 style="margin-bottom: 1rem;">
                            Cosmetico
                        </h3>
                        <img src="/immagini/home/cosmetico.jpg" style="margin-bottom: 1rem;">
                        <p>
                            Ozono industriale per impianti cosmetici. Controllo contaminazioni e igiene completa durante la produzione e lo stoccaggio.
                        </p>
                    </div>
                    <div>
                        <h3 style="margin-bottom: 1rem;">
                            Chimico
                        </h3>
                        <img src="/immagini/home/chimico.jpg" style="margin-bottom: 1rem;">
                        <p>
                            Sanificazione industriale in impianti chimici. Riduzione di contaminazioni e protezione dei macchinari e dell’ambiente di lavoro.
                        </p>
                    </div>
                    <div>
                        <h3 style="margin-bottom: 1rem;">
                            Agricolo
                        </h3>
                        <img src="/immagini/home/agricolo.jpg" style="margin-bottom: 1rem;">
                        <p>
                            Sanificazione di impianti agroindustriali e serre. Protezione da muffe, batteri e contaminazioni biologiche durante la produzione.
                        </p>
                    </div>
                    <div>
                        <h3 style="margin-bottom: 1rem;">
                            Tessile
                        </h3>
                        <img src="/immagini/home/tessile.jpg" style="margin-bottom: 1rem;">
                        <p>
                            Ozono industriale per linee tessili. Sanificazione di macchinari e ambienti, riducendo contaminazioni e odori durante la produzione.
                        </p>
                    </div>
                </div>
            </div>
        </ection>
    '''

    ########################################
    # servizi
    ########################################
    servizi_data = [
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M480-120q-117 0-198.5-81.5T200-400q0-100 61.5-176.5T420-674q-26-5-50-14.5T327-717q-28-29-37.5-67t-9.5-78v-18q86-2 148 56.5T489-680q14-43 39.5-80t57.5-69q9-9 21-9t21 9q9 9 9 21t-9 21q-25 25-45 54t-34 61q94 24 152.5 99.5T760-400q0 117-81.5 198.5T480-120Zm0-60q92 0 156-64t64-156q0-92-64-156t-156-64q-92 0-156 64t-64 156q0 92 64 156t156 64Zm0-220Z"/></svg>''',
            'title': f'''Sanificazione Prodotti''',
            'description': f'''Sanifichiamo prodotti, materie prime e imballaggi con ozono per eliminare cariche microbiche e prolungarne la sicurezza e la conservabilità.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M251-160q-88 0-149.5-61.5T40-371q0-78 50-137t127-71q20-97 94-158.5T482-799q112 0 189 81.5T748-522v24q72-2 122 46.5T920-329q0 69-50 119t-119 50H251Zm0-60h500q45 0 77-32t32-77q0-45-32-77t-77-32h-63v-84q0-91-61-154t-149-63q-88 0-149.5 63T267-522h-19q-62 0-105 43.5T100-371q0 63 44 107t107 44Zm229-260Z"/></svg>''',
            'title': f'''Sanificazione Aria''',
            'description': f'''Neutralizziamo virus, batteri e odori negli impianti di ventilazione con ozono, migliorando la qualità dell'aria e la sicurezza dei tuoi ambienti.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M176-120q-19-4-35.5-20.5T120-176l664-664q21 5 36 20.5t21 35.5L176-120Zm-56-252v-112l356-356h112L120-372Zm0-308v-80q0-33 23.5-56.5T200-840h80L120-680Zm560 560 160-160v80q0 33-23.5 56.5T760-120h-80Zm-308 0 468-468v112L484-120H372Z"/></svg>''',
            'title': f'''Sanificazione Superfici''',
            'description': f'''Trattiamo pavimenti, attrezzature e linee produttive con ozono per eliminare residui biologici e ridurre il rischio di contaminazioni.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
    ]
    servizi_cards = []
    for item in servizi_data:
        servizi_cards.append(f'''
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
    servizi_cards = ''.join(servizi_cards)
    servizi = f'''
        <section class="container-xl" style="padding-top: {section_py}; padding-bottom: {section_py};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                        Servizi di sanificazione industriale con ozono
                    </h2>
                </div>
                <div style="flex: 1; display: flex; justify-content: end;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/servizi.html">
                            <span>Vedi Servizi</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                    <div>
                </div>
            </div>
        </ection>
    '''


    ########################################
    # servizi
    ########################################
    servizi_data = [
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M480-120q-117 0-198.5-81.5T200-400q0-100 61.5-176.5T420-674q-26-5-50-14.5T327-717q-28-29-37.5-67t-9.5-78v-18q86-2 148 56.5T489-680q14-43 39.5-80t57.5-69q9-9 21-9t21 9q9 9 9 21t-9 21q-25 25-45 54t-34 61q94 24 152.5 99.5T760-400q0 117-81.5 198.5T480-120Zm0-60q92 0 156-64t64-156q0-92-64-156t-156-64q-92 0-156 64t-64 156q0 92 64 156t156 64Zm0-220Z"/></svg>''',
            'title': f'''Sanificazione Prodotti''',
            'description': f'''Sanifichiamo prodotti, materie prime e imballaggi con ozono per eliminare cariche microbiche e prolungarne la sicurezza e la conservabilità.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M251-160q-88 0-149.5-61.5T40-371q0-78 50-137t127-71q20-97 94-158.5T482-799q112 0 189 81.5T748-522v24q72-2 122 46.5T920-329q0 69-50 119t-119 50H251Zm0-60h500q45 0 77-32t32-77q0-45-32-77t-77-32h-63v-84q0-91-61-154t-149-63q-88 0-149.5 63T267-522h-19q-62 0-105 43.5T100-371q0 63 44 107t107 44Zm229-260Z"/></svg>''',
            'title': f'''Sanificazione Aria''',
            'description': f'''Neutralizziamo virus, batteri e odori negli impianti di ventilazione con ozono, migliorando la qualità dell'aria e la sicurezza dei tuoi ambienti.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M176-120q-19-4-35.5-20.5T120-176l664-664q21 5 36 20.5t21 35.5L176-120Zm-56-252v-112l356-356h112L120-372Zm0-308v-80q0-33 23.5-56.5T200-840h80L120-680Zm560 560 160-160v80q0 33-23.5 56.5T760-120h-80Zm-308 0 468-468v112L484-120H372Z"/></svg>''',
            'title': f'''Sanificazione Superfici''',
            'description': f'''Trattiamo pavimenti, attrezzature e linee produttive con ozono per eliminare residui biologici e ridurre il rischio di contaminazioni.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
    ]
    servizi_cards = []
    for item in servizi_data:
        servizi_cards.append(f'''
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
    servizi_cards = ''.join(servizi_cards)
    servizi = f'''
        <section class="container-xl" style="padding-top: {section_py}; padding-bottom: {section_py};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                        Servizi di sanificazione industriale con ozono
                    </h2>
                </div>
                <div style="flex: 1; display: flex; justify-content: end;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/servizi.html">
                            <span>Vedi Servizi</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                    <div>
                </div>
            </div>
        </ection>
    '''


    ########################################
    # servizi
    ########################################
    servizi_data = [
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M480-120q-117 0-198.5-81.5T200-400q0-100 61.5-176.5T420-674q-26-5-50-14.5T327-717q-28-29-37.5-67t-9.5-78v-18q86-2 148 56.5T489-680q14-43 39.5-80t57.5-69q9-9 21-9t21 9q9 9 9 21t-9 21q-25 25-45 54t-34 61q94 24 152.5 99.5T760-400q0 117-81.5 198.5T480-120Zm0-60q92 0 156-64t64-156q0-92-64-156t-156-64q-92 0-156 64t-64 156q0 92 64 156t156 64Zm0-220Z"/></svg>''',
            'title': f'''Sanificazione Prodotti''',
            'description': f'''Sanifichiamo prodotti, materie prime e imballaggi con ozono per eliminare cariche microbiche e prolungarne la sicurezza e la conservabilità.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M251-160q-88 0-149.5-61.5T40-371q0-78 50-137t127-71q20-97 94-158.5T482-799q112 0 189 81.5T748-522v24q72-2 122 46.5T920-329q0 69-50 119t-119 50H251Zm0-60h500q45 0 77-32t32-77q0-45-32-77t-77-32h-63v-84q0-91-61-154t-149-63q-88 0-149.5 63T267-522h-19q-62 0-105 43.5T100-371q0 63 44 107t107 44Zm229-260Z"/></svg>''',
            'title': f'''Sanificazione Aria''',
            'description': f'''Neutralizziamo virus, batteri e odori negli impianti di ventilazione con ozono, migliorando la qualità dell'aria e la sicurezza dei tuoi ambienti.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M176-120q-19-4-35.5-20.5T120-176l664-664q21 5 36 20.5t21 35.5L176-120Zm-56-252v-112l356-356h112L120-372Zm0-308v-80q0-33 23.5-56.5T200-840h80L120-680Zm560 560 160-160v80q0 33-23.5 56.5T760-120h-80Zm-308 0 468-468v112L484-120H372Z"/></svg>''',
            'title': f'''Sanificazione Superfici''',
            'description': f'''Trattiamo pavimenti, attrezzature e linee produttive con ozono per eliminare residui biologici e ridurre il rischio di contaminazioni.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
    ]
    servizi_cards = []
    for item in servizi_data:
        servizi_cards.append(f'''
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
    servizi_cards = ''.join(servizi_cards)
    servizi = f'''
        <section class="container-xl" style="padding-top: {section_py}; padding-bottom: {section_py};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                        Servizi di sanificazione industriale con ozono
                    </h2>
                </div>
                <div style="flex: 1; display: flex; justify-content: end;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/servizi.html">
                            <span>Vedi Servizi</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                    <div>
                </div>
            </div>
        </ection>
    '''


    ########################################
    # servizi
    ########################################
    servizi_data = [
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M480-120q-117 0-198.5-81.5T200-400q0-100 61.5-176.5T420-674q-26-5-50-14.5T327-717q-28-29-37.5-67t-9.5-78v-18q86-2 148 56.5T489-680q14-43 39.5-80t57.5-69q9-9 21-9t21 9q9 9 9 21t-9 21q-25 25-45 54t-34 61q94 24 152.5 99.5T760-400q0 117-81.5 198.5T480-120Zm0-60q92 0 156-64t64-156q0-92-64-156t-156-64q-92 0-156 64t-64 156q0 92 64 156t156 64Zm0-220Z"/></svg>''',
            'title': f'''Sanificazione Prodotti''',
            'description': f'''Sanifichiamo prodotti, materie prime e imballaggi con ozono per eliminare cariche microbiche e prolungarne la sicurezza e la conservabilità.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M251-160q-88 0-149.5-61.5T40-371q0-78 50-137t127-71q20-97 94-158.5T482-799q112 0 189 81.5T748-522v24q72-2 122 46.5T920-329q0 69-50 119t-119 50H251Zm0-60h500q45 0 77-32t32-77q0-45-32-77t-77-32h-63v-84q0-91-61-154t-149-63q-88 0-149.5 63T267-522h-19q-62 0-105 43.5T100-371q0 63 44 107t107 44Zm229-260Z"/></svg>''',
            'title': f'''Sanificazione Aria''',
            'description': f'''Neutralizziamo virus, batteri e odori negli impianti di ventilazione con ozono, migliorando la qualità dell'aria e la sicurezza dei tuoi ambienti.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M176-120q-19-4-35.5-20.5T120-176l664-664q21 5 36 20.5t21 35.5L176-120Zm-56-252v-112l356-356h112L120-372Zm0-308v-80q0-33 23.5-56.5T200-840h80L120-680Zm560 560 160-160v80q0 33-23.5 56.5T760-120h-80Zm-308 0 468-468v112L484-120H372Z"/></svg>''',
            'title': f'''Sanificazione Superfici''',
            'description': f'''Trattiamo pavimenti, attrezzature e linee produttive con ozono per eliminare residui biologici e ridurre il rischio di contaminazioni.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
    ]
    servizi_cards = []
    for item in servizi_data:
        servizi_cards.append(f'''
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
    servizi_cards = ''.join(servizi_cards)
    servizi = f'''
        <section class="container-xl" style="padding-top: {section_py}; padding-bottom: {section_py};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                        Servizi di sanificazione industriale con ozono
                    </h2>
                </div>
                <div style="flex: 1; display: flex; justify-content: end;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/servizi.html">
                            <span>Vedi Servizi</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                    <div>
                </div>
            </div>
        </ection>
    '''


    ########################################
    # servizi
    ########################################
    servizi_data = [
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M480-120q-117 0-198.5-81.5T200-400q0-100 61.5-176.5T420-674q-26-5-50-14.5T327-717q-28-29-37.5-67t-9.5-78v-18q86-2 148 56.5T489-680q14-43 39.5-80t57.5-69q9-9 21-9t21 9q9 9 9 21t-9 21q-25 25-45 54t-34 61q94 24 152.5 99.5T760-400q0 117-81.5 198.5T480-120Zm0-60q92 0 156-64t64-156q0-92-64-156t-156-64q-92 0-156 64t-64 156q0 92 64 156t156 64Zm0-220Z"/></svg>''',
            'title': f'''Sanificazione Prodotti''',
            'description': f'''Sanifichiamo prodotti, materie prime e imballaggi con ozono per eliminare cariche microbiche e prolungarne la sicurezza e la conservabilità.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M251-160q-88 0-149.5-61.5T40-371q0-78 50-137t127-71q20-97 94-158.5T482-799q112 0 189 81.5T748-522v24q72-2 122 46.5T920-329q0 69-50 119t-119 50H251Zm0-60h500q45 0 77-32t32-77q0-45-32-77t-77-32h-63v-84q0-91-61-154t-149-63q-88 0-149.5 63T267-522h-19q-62 0-105 43.5T100-371q0 63 44 107t107 44Zm229-260Z"/></svg>''',
            'title': f'''Sanificazione Aria''',
            'description': f'''Neutralizziamo virus, batteri e odori negli impianti di ventilazione con ozono, migliorando la qualità dell'aria e la sicurezza dei tuoi ambienti.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M176-120q-19-4-35.5-20.5T120-176l664-664q21 5 36 20.5t21 35.5L176-120Zm-56-252v-112l356-356h112L120-372Zm0-308v-80q0-33 23.5-56.5T200-840h80L120-680Zm560 560 160-160v80q0 33-23.5 56.5T760-120h-80Zm-308 0 468-468v112L484-120H372Z"/></svg>''',
            'title': f'''Sanificazione Superfici''',
            'description': f'''Trattiamo pavimenti, attrezzature e linee produttive con ozono per eliminare residui biologici e ridurre il rischio di contaminazioni.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
    ]
    servizi_cards = []
    for item in servizi_data:
        servizi_cards.append(f'''
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
    servizi_cards = ''.join(servizi_cards)
    servizi = f'''
        <section class="container-xl" style="padding-top: {section_py}; padding-bottom: {section_py};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                        Servizi di sanificazione industriale con ozono
                    </h2>
                </div>
                <div style="flex: 1; display: flex; justify-content: end;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/servizi.html">
                            <span>Vedi Servizi</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                    <div>
                </div>
            </div>
        </ection>
    '''


    ########################################
    # servizi
    ########################################
    servizi_data = [
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M480-120q-117 0-198.5-81.5T200-400q0-100 61.5-176.5T420-674q-26-5-50-14.5T327-717q-28-29-37.5-67t-9.5-78v-18q86-2 148 56.5T489-680q14-43 39.5-80t57.5-69q9-9 21-9t21 9q9 9 9 21t-9 21q-25 25-45 54t-34 61q94 24 152.5 99.5T760-400q0 117-81.5 198.5T480-120Zm0-60q92 0 156-64t64-156q0-92-64-156t-156-64q-92 0-156 64t-64 156q0 92 64 156t156 64Zm0-220Z"/></svg>''',
            'title': f'''Sanificazione Prodotti''',
            'description': f'''Sanifichiamo prodotti, materie prime e imballaggi con ozono per eliminare cariche microbiche e prolungarne la sicurezza e la conservabilità.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M251-160q-88 0-149.5-61.5T40-371q0-78 50-137t127-71q20-97 94-158.5T482-799q112 0 189 81.5T748-522v24q72-2 122 46.5T920-329q0 69-50 119t-119 50H251Zm0-60h500q45 0 77-32t32-77q0-45-32-77t-77-32h-63v-84q0-91-61-154t-149-63q-88 0-149.5 63T267-522h-19q-62 0-105 43.5T100-371q0 63 44 107t107 44Zm229-260Z"/></svg>''',
            'title': f'''Sanificazione Aria''',
            'description': f'''Neutralizziamo virus, batteri e odori negli impianti di ventilazione con ozono, migliorando la qualità dell'aria e la sicurezza dei tuoi ambienti.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M176-120q-19-4-35.5-20.5T120-176l664-664q21 5 36 20.5t21 35.5L176-120Zm-56-252v-112l356-356h112L120-372Zm0-308v-80q0-33 23.5-56.5T200-840h80L120-680Zm560 560 160-160v80q0 33-23.5 56.5T760-120h-80Zm-308 0 468-468v112L484-120H372Z"/></svg>''',
            'title': f'''Sanificazione Superfici''',
            'description': f'''Trattiamo pavimenti, attrezzature e linee produttive con ozono per eliminare residui biologici e ridurre il rischio di contaminazioni.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
    ]
    servizi_cards = []
    for item in servizi_data:
        servizi_cards.append(f'''
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
    servizi_cards = ''.join(servizi_cards)
    servizi = f'''
        <section class="container-xl" style="padding-top: {section_py}; padding-bottom: {section_py};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                        Servizi di sanificazione industriale con ozono
                    </h2>
                </div>
                <div style="flex: 1; display: flex; justify-content: end;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/servizi.html">
                            <span>Vedi Servizi</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                    <div>
                </div>
            </div>
        </ection>
    '''


    ########################################
    # servizi
    ########################################
    servizi_data = [
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M480-120q-117 0-198.5-81.5T200-400q0-100 61.5-176.5T420-674q-26-5-50-14.5T327-717q-28-29-37.5-67t-9.5-78v-18q86-2 148 56.5T489-680q14-43 39.5-80t57.5-69q9-9 21-9t21 9q9 9 9 21t-9 21q-25 25-45 54t-34 61q94 24 152.5 99.5T760-400q0 117-81.5 198.5T480-120Zm0-60q92 0 156-64t64-156q0-92-64-156t-156-64q-92 0-156 64t-64 156q0 92 64 156t156 64Zm0-220Z"/></svg>''',
            'title': f'''Sanificazione Prodotti''',
            'description': f'''Sanifichiamo prodotti, materie prime e imballaggi con ozono per eliminare cariche microbiche e prolungarne la sicurezza e la conservabilità.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M251-160q-88 0-149.5-61.5T40-371q0-78 50-137t127-71q20-97 94-158.5T482-799q112 0 189 81.5T748-522v24q72-2 122 46.5T920-329q0 69-50 119t-119 50H251Zm0-60h500q45 0 77-32t32-77q0-45-32-77t-77-32h-63v-84q0-91-61-154t-149-63q-88 0-149.5 63T267-522h-19q-62 0-105 43.5T100-371q0 63 44 107t107 44Zm229-260Z"/></svg>''',
            'title': f'''Sanificazione Aria''',
            'description': f'''Neutralizziamo virus, batteri e odori negli impianti di ventilazione con ozono, migliorando la qualità dell'aria e la sicurezza dei tuoi ambienti.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M176-120q-19-4-35.5-20.5T120-176l664-664q21 5 36 20.5t21 35.5L176-120Zm-56-252v-112l356-356h112L120-372Zm0-308v-80q0-33 23.5-56.5T200-840h80L120-680Zm560 560 160-160v80q0 33-23.5 56.5T760-120h-80Zm-308 0 468-468v112L484-120H372Z"/></svg>''',
            'title': f'''Sanificazione Superfici''',
            'description': f'''Trattiamo pavimenti, attrezzature e linee produttive con ozono per eliminare residui biologici e ridurre il rischio di contaminazioni.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
    ]
    servizi_cards = []
    for item in servizi_data:
        servizi_cards.append(f'''
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
    servizi_cards = ''.join(servizi_cards)
    servizi = f'''
        <section class="container-xl" style="padding-top: {section_py}; padding-bottom: {section_py};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                        Servizi di sanificazione industriale con ozono
                    </h2>
                </div>
                <div style="flex: 1; display: flex; justify-content: end;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/servizi.html">
                            <span>Vedi Servizi</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                </div>
            </div>
        </ection>
    '''


    ########################################
    # servizi
    ########################################
    servizi_data = [
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M480-120q-117 0-198.5-81.5T200-400q0-100 61.5-176.5T420-674q-26-5-50-14.5T327-717q-28-29-37.5-67t-9.5-78v-18q86-2 148 56.5T489-680q14-43 39.5-80t57.5-69q9-9 21-9t21 9q9 9 9 21t-9 21q-25 25-45 54t-34 61q94 24 152.5 99.5T760-400q0 117-81.5 198.5T480-120Zm0-60q92 0 156-64t64-156q0-92-64-156t-156-64q-92 0-156 64t-64 156q0 92 64 156t156 64Zm0-220Z"/></svg>''',
            'title': f'''Sanificazione Prodotti''',
            'description': f'''Sanifichiamo prodotti, materie prime e imballaggi con ozono per eliminare cariche microbiche e prolungarne la sicurezza e la conservabilità.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M251-160q-88 0-149.5-61.5T40-371q0-78 50-137t127-71q20-97 94-158.5T482-799q112 0 189 81.5T748-522v24q72-2 122 46.5T920-329q0 69-50 119t-119 50H251Zm0-60h500q45 0 77-32t32-77q0-45-32-77t-77-32h-63v-84q0-91-61-154t-149-63q-88 0-149.5 63T267-522h-19q-62 0-105 43.5T100-371q0 63 44 107t107 44Zm229-260Z"/></svg>''',
            'title': f'''Sanificazione Aria''',
            'description': f'''Neutralizziamo virus, batteri e odori negli impianti di ventilazione con ozono, migliorando la qualità dell'aria e la sicurezza dei tuoi ambienti.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M176-120q-19-4-35.5-20.5T120-176l664-664q21 5 36 20.5t21 35.5L176-120Zm-56-252v-112l356-356h112L120-372Zm0-308v-80q0-33 23.5-56.5T200-840h80L120-680Zm560 560 160-160v80q0 33-23.5 56.5T760-120h-80Zm-308 0 468-468v112L484-120H372Z"/></svg>''',
            'title': f'''Sanificazione Superfici''',
            'description': f'''Trattiamo pavimenti, attrezzature e linee produttive con ozono per eliminare residui biologici e ridurre il rischio di contaminazioni.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
    ]
    servizi_cards = []
    for item in servizi_data:
        servizi_cards.append(f'''
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
    servizi_cards = ''.join(servizi_cards)
    servizi = f'''
        <section class="container-xl" style="padding-top: {section_py}; padding-bottom: {section_py};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                        Servizi di sanificazione industriale con ozono
                    </h2>
                </div>
                <div style="flex: 1; display: flex; justify-content: end;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/servizi.html">
                            <span>Vedi Servizi</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                </div>
            </div>
            <div class="grid-3" style="column-gap: 3rem; row-gap: 0;">
                {servizi_cards}
            <div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    ########################################
    # prodotti
    ########################################
    prodotti_data = [
        {
            'icon': f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M80-80v-481l280-119v80l200-81v121h320v480H80Zm60-60h680v-359.8H500V-592l-200 80v-79l-160 71v380Zm310-100h60v-160h-60v160Zm-160 0h60v-160h-60v160Zm320 0h60v-160h-60v160Zm270-320H700l40-320h100l40 320ZM140-140h680-680Z"/></svg>
            ''',
            'title': f'''Generatori di Ozono Industriali''',
            'description': f'''Sistemi ad alte portate per impianti produttivi e aree di grandi dimensioni. Integrabili con linee di sanificazione automatizzate.''',
            'link_href': f'''/prodotti.html''',
            'link_anchor': f'''Scopri i modelli industriali''',
        },
        {
            'icon': f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M140-180h120v-320h440v320h120v-460L480-776 140-640v460Zm-60 60v-560l400-160 400 160v560H640v-320H320v320H80Zm290 0v-60h60v60h-60Zm80-120v-60h60v60h-60Zm80 120v-60h60v60h-60ZM260-500h440-440Z"/></svg>           
            ''',
            'title': f'''Generatori di Ozono Portatili''',
            'description': f'''Dispositivi compatti per sanificazioni rapide di ambienti, veicoli e camere di stoccaggio. Facili da trasportare, potenti e certificati.''',
            'link_href': f'''/prodotti.html''',
            'link_anchor': f'''Scopri i modelli portatili''',
        },
        {
            'icon': f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M320-80q-66 0-113-47t-47-113v-400q0-66 47-113t113-47h50v-80h60v80h100v-80h60v80h50q66 0 113 47t47 113v400q0 66-47 113T640-80H320Zm0-60h320q42 0 71-29t29-71v-400q0-42-29-71t-71-29H320q-42 0-71 29t-29 71v400q0 42 29 71t71 29Zm0-440h320v-60H320v60Zm160 315q33 0 56.5-23.5T560-344q0-26-15-45t-65-76q-50 58-65 76.5T400-344q0 32 23.5 55.5T480-265ZM220-740v600-600Z"/></svg>            
            ''',
            'title': f'''Accessori e Sistemi di Controllo''',
            'description': f'''Centraline di monitoraggio, sensori di concentrazione e sistemi di sicurezza per la gestione dell'ozono in ambiente industriale.''',
            'link_href': f'''/prodotti.html''',
            'link_anchor': f'''Scopri gli accessori''',
        },
    ]
    prodotti_cards = []
    for item in prodotti_data:
        prodotti_cards.append(f'''
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
    prodotti_cards = ''.join(prodotti_cards)
    prodotti = f'''
        <section class="container-xl" style="padding-top: {section_py}; padding-bottom: {section_py};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                        I nostri generatori di ozono professionali per la sanificazione industriale                   
                    </h2>
                </div>
                <div style="flex: 1; display: flex; justify-content: end;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/prodotti.html">
                            <span>Vedi Prodotti</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                </div>
            </div>
            <div class="grid-3" style="column-gap: 3rem; row-gap: 0;">
                {prodotti_cards}
            <div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''

    ########################################
    # servizi
    ########################################
    servizi_data = [
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M480-120q-117 0-198.5-81.5T200-400q0-100 61.5-176.5T420-674q-26-5-50-14.5T327-717q-28-29-37.5-67t-9.5-78v-18q86-2 148 56.5T489-680q14-43 39.5-80t57.5-69q9-9 21-9t21 9q9 9 9 21t-9 21q-25 25-45 54t-34 61q94 24 152.5 99.5T760-400q0 117-81.5 198.5T480-120Zm0-60q92 0 156-64t64-156q0-92-64-156t-156-64q-92 0-156 64t-64 156q0 92 64 156t156 64Zm0-220Z"/></svg>''',
            'title': f'''Sanificazione Prodotti''',
            'description': f'''Sanifichiamo prodotti, materie prime e imballaggi con ozono per eliminare cariche microbiche e prolungarne la sicurezza e la conservabilità.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M251-160q-88 0-149.5-61.5T40-371q0-78 50-137t127-71q20-97 94-158.5T482-799q112 0 189 81.5T748-522v24q72-2 122 46.5T920-329q0 69-50 119t-119 50H251Zm0-60h500q45 0 77-32t32-77q0-45-32-77t-77-32h-63v-84q0-91-61-154t-149-63q-88 0-149.5 63T267-522h-19q-62 0-105 43.5T100-371q0 63 44 107t107 44Zm229-260Z"/></svg>''',
            'title': f'''Sanificazione Aria''',
            'description': f'''Neutralizziamo virus, batteri e odori negli impianti di ventilazione con ozono, migliorando la qualità dell'aria e la sicurezza dei tuoi ambienti.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M176-120q-19-4-35.5-20.5T120-176l664-664q21 5 36 20.5t21 35.5L176-120Zm-56-252v-112l356-356h112L120-372Zm0-308v-80q0-33 23.5-56.5T200-840h80L120-680Zm560 560 160-160v80q0 33-23.5 56.5T760-120h-80Zm-308 0 468-468v112L484-120H372Z"/></svg>''',
            'title': f'''Sanificazione Superfici''',
            'description': f'''Trattiamo pavimenti, attrezzature e linee produttive con ozono per eliminare residui biologici e ridurre il rischio di contaminazioni.''',
            'link_href': f'''/servizi.html''',
            'link_anchor': f'''Scopri Servizio''',
        },
    ]
    servizi_cards = []
    for item in servizi_data:
        servizi_cards.append(f'''
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
    servizi_cards = ''.join(servizi_cards)
    servizi = f'''
        <section class="container-xl" style="padding-top: {section_py}; padding-bottom: {section_py};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                        Servizi di sanificazione industriale con ozono
                    </h2>
                </div>
                <div style="flex: 1; display: flex; justify-content: end;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/servizi.html">
                            <span>Vedi Servizi</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                </div>
            </div>
            <div class="grid-3" style="column-gap: 3rem; row-gap: 0;">
                {servizi_cards}
            <div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    ########################################
    # prodotti
    ########################################
    prodotti_data = [
        {
            'icon': f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M80-80v-481l280-119v80l200-81v121h320v480H80Zm60-60h680v-359.8H500V-592l-200 80v-79l-160 71v380Zm310-100h60v-160h-60v160Zm-160 0h60v-160h-60v160Zm320 0h60v-160h-60v160Zm270-320H700l40-320h100l40 320ZM140-140h680-680Z"/></svg>
            ''',
            'title': f'''Generatori di Ozono Industriali''',
            'description': f'''Sistemi ad alte portate per impianti produttivi e aree di grandi dimensioni. Integrabili con linee di sanificazione automatizzate.''',
            'link_href': f'''/prodotti.html''',
            'link_anchor': f'''Scopri i modelli industriali''',
        },
        {
            'icon': f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M140-180h120v-320h440v320h120v-460L480-776 140-640v460Zm-60 60v-560l400-160 400 160v560H640v-320H320v320H80Zm290 0v-60h60v60h-60Zm80-120v-60h60v60h-60Zm80 120v-60h60v60h-60ZM260-500h440-440Z"/></svg>           
            ''',
            'title': f'''Generatori di Ozono Portatili''',
            'description': f'''Dispositivi compatti per sanificazioni rapide di ambienti, veicoli e camere di stoccaggio. Facili da trasportare, potenti e certificati.''',
            'link_href': f'''/prodotti.html''',
            'link_anchor': f'''Scopri i modelli portatili''',
        },
        {
            'icon': f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M320-80q-66 0-113-47t-47-113v-400q0-66 47-113t113-47h50v-80h60v80h100v-80h60v80h50q66 0 113 47t47 113v400q0 66-47 113T640-80H320Zm0-60h320q42 0 71-29t29-71v-400q0-42-29-71t-71-29H320q-42 0-71 29t-29 71v400q0 42 29 71t71 29Zm0-440h320v-60H320v60Zm160 315q33 0 56.5-23.5T560-344q0-26-15-45t-65-76q-50 58-65 76.5T400-344q0 32 23.5 55.5T480-265ZM220-740v600-600Z"/></svg>            
            ''',
            'title': f'''Accessori e Sistemi di Controllo''',
            'description': f'''Centraline di monitoraggio, sensori di concentrazione e sistemi di sicurezza per la gestione dell'ozono in ambiente industriale.''',
            'link_href': f'''/prodotti.html''',
            'link_anchor': f'''Scopri gli accessori''',
        },
    ]
    prodotti_cards = []
    for item in prodotti_data:
        prodotti_cards.append(f'''
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
    prodotti_cards = ''.join(prodotti_cards)
    prodotti = f'''
        <section class="container-xl" style="padding-top: {section_py}; padding-bottom: {section_py};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                        I nostri generatori di ozono professionali per la sanificazione industriale                   
                    </h2>
                </div>
                <div style="flex: 1; display: flex; justify-content: end;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/prodotti.html">
                            <span>Vedi Prodotti</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                </div>
            </div>
            <div class="grid-3" style="column-gap: 3rem; row-gap: 0;">
                {prodotti_cards}
            <div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''

    ########################################
    # settori
    ########################################
    settori_cards = []
    for item_i, item in enumerate(settori_data.data):
        settore_card = f'''
            <div>
                <img style="margin-bottom: 1rem; border-radius: 1rem; height: 15rem; object-fit: cover;" src="{item['image_src']}">
                
                <h3 style="color: #222222; font-size: 1.25rem; line-height: 1.2; font-weight: bold; margin-bottom: 1rem;">
                    {item['title']}
                </h3>
                
                <p style="color: #555555; margin-bottom: 1rem;">
                    {item['description']}
                </p>
                
                <p>
                    <a style="color: #555555;" href="{item['href']}">Scopri settore</a>
                </p>
            </div>
        '''
        settori_cards.append(settore_card)
    settori_cards = ''.join(settori_cards)
    section_pb = '5rem'
    settori = f'''
        <section class="container-xl" style="padding-top: {section_py}; padding-bottom: {section_pb};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                        Soluzioni su misura per ogni settore
                    </h2>
                </div>
                <div style="flex: 1; display: flex; justify-content: end;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/settori.html">
                            <span>Vedi Settori</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                </div>
            </div>
            <div class="grid-3" style="column-gap: 3rem; row-gap: 3rem;">
                {settori_cards}
            <div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''

    ########################################
    # ozono
    ########################################    
    ozono_data = [
        {
            'href': '''/ozono/chimica.html''',
            'image_src': '/immagini/ozono-chimica.jpg',
            'category': 'CHIMICA',
            'title': '''Chimica dell'ozono: reazioni, meccanismi e implicazioni atmosferiche''',
            'description': '''La molecola di ozono, O₃, presenta una struttura piegata con un angolo di circa 117°, dovuto all'ibridazione sp² degli atomi di ossigeno...''',
            'date': '''6 Ottobre 2025''',
            'datetime': '''2025-10-06''',
        },
        {
            'href': '''/ozono/ambiente.html''',
            'image_src': '/immagini/ozono-ambiente.jpg',
            'category': 'AMBIENTE',
            'title': '''Ozono nell'ambiente: cos'è, dove si trova e quali sono i suoi effetti sull'atmosfera''',
            'description': '''L'ozono è una delle molecole più affascinanti e controverse dell'atmosfera terrestre. Può essere allo stesso tempo un prezioso alleato contro i raggi ultravioletti e un pericoloso inquinante se presente nei bassi strati dell'aria.''',
            'date': '''6 Ottobre 2025''',
            'datetime': '''2025-10-06''',
        },
        {
            'href': '''/ozono/sanificazione.html''',
            'image_src': '/immagini/ozono-sanificazione.jpg',
            'category': 'SANIFICAZIONE',
            'title': '''Sanificazione a ozono: la soluzione naturale per igiene, sicurezza e benessere''',
            'description': '''La sanificazione a ozono sta diventando una delle soluzioni più efficaci ed ecologiche per garantire la pulizia, la disinfezione e l'igiene di ambienti domestici, professionali e agricoli.''',
            'date': '''6 Ottobre 2025''',
            'datetime': '''2025-10-06''',
        },
        {
            'href': '''/ozono/terapia.html''',
            'image_src': '/immagini/ozono-terapia.jpg',
            'category': 'OZONOTERAPIA',
            'title': '''Ozonoterapia: applicazioni, meccanismi e prospettive della terapia con ozono''',
            'description': '''Negli ultimi anni l'ozonoterapia ha guadagnato un ruolo crescente all'interno della medicina rigenerativa e funzionale.''',
            'date': '''6 Ottobre 2025''',
            'datetime': '''2025-10-06''',
        },
        {
            'href': '''/ozono/sanificazione/applicazioni/caseificio.html''',
            'image_src': '/immagini/ozono-sanificazione-applicazioni-caseificio.jpg',
            'category': 'SANIFICAZIONE',
            'title': '''Sanificazione con ozono nei caseifici: guida pratica per caseifici italiani''',
            'description': '''Nei caseifici italiani, la sanificazione rappresenta un passaggio fondamentale per garantire la qualità dei prodotti e la sicurezza alimentare.''',
            'date': '''6 Ottobre 2025''',
            'datetime': '''2025-10-06''',
        },
    ]
    ozono_card_featured_index = 2
    ozono_cards_small = []
    for item_i, item in enumerate(ozono_data):
        if item_i == ozono_card_featured_index: continue
        ozono_card_small = f'''
            <div style="display: flex; gap: 3rem; margin-bottom: 2rem;">
                <div style="flex: 5;">
                    <h3 style="color: #222222; font-size: 1.5rem; line-height: 1.2; font-weight: bold; margin-bottom: 1rem;">
                        {item['title']}
                    </h3>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span>{item['date']}</span>
                        <span>{item['category'].capitalize()}</span>
                        <div style="display: inline-block;">
                            <a style="color: #222222; display: flex; gap: 0.5rem; align-items: center;" href="{item['href']}">
                                <span>Leggi Articolo</span>
                                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                            </a>
                        </div>
                    </div>
                </div>
                <div style="flex: 2;">
                    <img style="border-radius: 1rem; height: 10rem; object-fit: cover;" src="{item['image_src']}">
                </div>
            </div>
        '''
        if item_i != len(ozono_data)-1:
            ozono_card_small += f'''<div style="background-color: #ededed; height: 1px; margin-bottom: 2rem;"></div>'''
        ozono_cards_small.append(ozono_card_small)
    ozono_cards_small = ''.join(ozono_cards_small)
    ozono = f'''
        <section class="container-xl" style="padding-top: {section_py}; padding-bottom: {section_py};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                        Guida all'Ozono
                    </h2>
                </div>
                <div style="flex: 1; display: flex; justify-content: end;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/ozono.html">
                            <span>Vedi Articoli</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                </div>
            </div>
            <div class="grid-2" style="column-gap: 4rem; row-gap: 0;">
                <div>
                    <h3 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 2rem;">
                        {ozono_data[ozono_card_featured_index]['title']}
                    </h3> 
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem;">
                        <span>{ozono_data[ozono_card_featured_index]['date']}</span>
                        <span>Sanificazione</span>
                        <div style="display: inline-block;">
                            <a class="button-default-2" href="{ozono_data[ozono_card_featured_index]['href']}">
                                <span>Leggi Articolo</span>
                                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                            </a>
                        </div>
                    </div>
                    <img style="border-radius: 1rem; height: 40rem; object-fit: cover;" src="{ozono_data[ozono_card_featured_index]['image_src']}">
                </div>
                <div>
                    {ozono_cards_small}
                <div>
            <div>
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
                {hero_1}
                {settori_1}
                {servizi}
                {prodotti}
                {settori}
                {ozono}
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
    html_filepath = f'{g.WEBSITE_FOLDERPATH}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)
