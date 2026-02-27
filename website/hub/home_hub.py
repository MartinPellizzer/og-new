from lib import g
from lib import components

from data import settori_data

def gen():
    section_py = '8rem'
    opacity = 0.66
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
                      Ozonogroup progetta e produce sistemi a ozono per la sanificazione industriale, garantendo sicurezza, efficienza e conformità alle normative di sicurezza.
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
                        garantendo controllo preciso dell'ozono, affidabilità operativa
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
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                    <div style="flex: 2;">
                        <p style="margin-bttom: 3rem;">
        I sistemi a ozono industriali di Ozonogroup trovano applicazione in molteplici settori, garantendo sanificazione efficace, sicurezza e piena conformità alle normative. Scopri come le nostre soluzioni possono supportare il tuo settore industriale, riducendo rischi di contaminazione e migliorando l'igiene degli impianti.
                        </p>
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
                <div class="grid-4" style="padding-top: 3rem; row-gap: 3rem;">
                    <div>
                        <a href="/settori/alimentare.html" style="text-decoration: none;">
                            <h3 style="margin-bottom: 1rem;">
                                Alimentare
                            </h3>
                            <img src="/immagini/home/alimentare.jpg" style="margin-bottom: 1rem;">
                            <p>
                                Sanificazione industriale alimentare con generatori di ozono. Igiene completa, sicurezza HACCP e protezione di linee produttive e impianti.
                            </p>
                        </a>
                    </div>
                    <div>
                        <a href="/settori/farmaceutico.html" style="text-decoration: none;">
                            <h3 style="margin-bottom: 1rem;">
                                Farmaceutico
                            </h3>
                            <img src="/immagini/home/farmaceutico.jpg" style="margin-bottom: 1rem;">
                            <p>
                                Ozono industriale per impianti farmaceutici. Controllo contaminazioni, igiene rigorosa e piena conformità agli standard GMP.
                            </p>
                        </a>
                    </div>
                    <div>
                        <a href="/settori/confezionamento.html" style="text-decoration: none;">
                            <h3 style="margin-bottom: 1rem;">
                                Confezionamento
                            </h3>
                            <img src="/immagini/home/confezionamento.jpg" style="margin-bottom: 1rem;">
                            <p>
                                Generatori di ozono per linee di packaging industriale. Igiene e sicurezza in ogni fase della produzione e del confezionamento.
                            </p>
                        </a>
                    </div>
                    <div>
                        <a href="/settori/trasporto.html" style="text-decoration: none;">
                            <h3 style="margin-bottom: 1rem;">
                                Trasporto
                            </h3>
                            <img src="/immagini/home/trasporti.jpg" style="margin-bottom: 1rem;">
                            <p>
                                Sanificazione industriale di magazzini e centri logistici. Protezione della merce e riduzione contaminazioni senza fermare le operazioni.
                            </p>
                        </a>
                    </div>
                    <div>
                        <a href="/settori/cosmetico.html" style="text-decoration: none;">
                            <h3 style="margin-bottom: 1rem;">
                                Cosmetico
                            </h3>
                            <img src="/immagini/home/cosmetico.jpg" style="margin-bottom: 1rem;">
                            <p>
                                Ozono industriale per impianti cosmetici. Controllo contaminazioni e igiene completa durante la produzione e lo stoccaggio.
                            </p>
                        </a>
                    </div>
                    <div>
                        <a href="/settori/chimico.html" style="text-decoration: none;">
                            <h3 style="margin-bottom: 1rem;">
                                Chimico
                            </h3>
                            <img src="/immagini/home/chimico.jpg" style="margin-bottom: 1rem;">
                            <p>
                                Sanificazione industriale in impianti chimici. Riduzione di contaminazioni e protezione dei macchinari e dell'ambiente di lavoro.
                            </p>
                        </a>
                    </div>
                    <div>
                        <a href="/settori/agricolo.html" style="text-decoration: none;">
                            <h3 style="margin-bottom: 1rem;">
                                Agricolo
                            </h3>
                            <img src="/immagini/home/agricolo.jpg" style="margin-bottom: 1rem;">
                            <p>
                                Sanificazione di impianti agroindustriali e serre. Protezione da muffe, batteri e contaminazioni biologiche durante la produzione.
                            </p>
                        </a>
                    </div>
                    <div>
                        <a href="/settori/tessile.html" style="text-decoration: none;">
                            <h3 style="margin-bottom: 1rem;">
                                Tessile
                            </h3>
                            <img src="/immagini/home/tessile.jpg" style="margin-bottom: 1rem;">
                            <p>
                                Ozono industriale per linee tessili. Sanificazione di macchinari e ambienti, riducendo contaminazioni e odori durante la produzione.
                            </p>
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

    if 1:
        h1 = f'Tecnologia di Ozonizzazione Industriale per Trattamento Acqua, Aria e Superfici'
        subordinate = f'Progettiamo e realizziamo impianti a ozono per applicazioni industriali, alimentari e ambientali con soluzioni su misura e automatizzate.'
        hero_html = f'''
            <section class="hero" style="
                    background: linear-gradient(rgba(0, 30, 60, 0.8), rgba(0, 30, 60, 0.8)), url('/immagini/home/generatore-ozono-industriale-impianto.jpg');
                    background-size: cover;
                    background-position: center;
                    height: 80vh;
            ">
                <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;">
                    <div class="container-lg">
                        <h1>
                            {h1}
                        </h1>
                        <p class="container-md" style="color: #ffffff; font-size: 1.25rem; line-height: 1.4; text-align: center; margin-bottom: 2rem;">
                            {subordinate}
                        </p>
                        <div style="display: flex; justify-content: center;">
                            <a href="/contatti.html" style="background-color: #0056b3; padding: 12px 16px; color: #ffffff; text-decoration: none;"> 
                                Richiedi una consulenza gratuita
                            </a>
                        </div>
                    </div>
                    <div class="container-md">
                    </div>
                </div>
            </section>      
        '''

    h2 = f'Applicazioni industriali dell’ozono'
    subordinate = f'L’ozono viene utilizzato in ambito industriale per disinfettare, ossidare, deodorare e trattare fluidi e ambienti produttivi.'
    img_height = '400px'
    applications_html = f'''
        <section class="applications">
            <div class="applications-content container-xl">
                <h2>
                    {h2}
                </h2>
                <p style="text-align: center; max-width: 80ch; margin: 0 auto 3rem auto;">
                    {subordinate}
                </p>
                <div class="applications-cards grid-3">
                    <article>
                        <a href="#" 
                        title="Trattamento acque industriali con ozono">
                            <figure>
                                <img 
                                    src="/immagini/home-water.jpg" 
                                    alt="Impianto di trattamento acque industriali con sistema di ozonizzazione"
                                    loading="lazy"
                                    width="600"
                                    height="400"
                                    style="height: {img_height}; object-fit: cover; object-position: center; margin-bottom: 1rem;"
                                >
                            </figure>
                            <h3>Trattamento acque industriali</h3>
                        </a>
                        <p>
                            Progettiamo impianti di ozonizzazione per ossidare contaminanti, eliminare batteri
                            e migliorare la qualità delle acque di processo e reflue.
                        </p>
                    </article>
                    <article>
                        <a href="#" 
                        title="Sanificazione ambienti e superfici con ozono">
                            <figure>
                                <img 
                                    src="/immagini/home-ambienti.jpg" 
                                    alt="Sanificazione di ambiente industriale mediante generatore di ozono"
                                    loading="lazy"
                                    width="600"
                                    height="400"
                                    style="height: {img_height}; object-fit: cover; object-position: center; margin-bottom: 1rem;"
                                >
                            </figure>
                            <h3>Sanificazione ambienti e superfici</h3>
                        </a>
                        <p>
                            Utilizziamo generatori di ozono industriali per eliminare microrganismi,
                            muffe, virus e biofilm da ambienti produttivi e superfici operative.
                        </p>
                    </article>
                    <article>
                        <a href="#" title="Abbattimento odori industriali con ozono">
                            <figure>
                                <img 
                                    src="/immagini/home-odori.jpg" 
                                    alt="Sistema di abbattimento odori industriali con tecnologia a ozono"
                                    loading="lazy"
                                    width="600"
                                    height="400"
                                    style="height: {img_height}; object-fit: cover; object-position: center; margin-bottom: 1rem;"
                                >
                            </figure>
                            <h3>Abbattimento odori industriali</h3>
                        </a>
                        <p>
                            Implementiamo soluzioni a ozono per decomporre composti organici volatili (VOC)
                            e neutralizzare odori persistenti in impianti industriali.
                        </p>
                    </article>
                    <article>
                        <a href="#" title="Soluzioni a ozono per il settore alimentare e agroindustriale">
                            <figure>
                                <img 
                                    src="/immagini/home-alimenti.jpg" 
                                    alt="Applicazione di ozono nel settore alimentare e agroindustriale"
                                    loading="lazy"
                                    width="600"
                                    height="400"
                                    style="height: {img_height}; object-fit: cover; object-position: center; margin-bottom: 1rem;"
                                >
                            </figure>
                            <h3>Settore alimentare e agroindustriale</h3>
                        </a>
                        <p>
                            Progettiamo sistemi a ozono per la sicurezza alimentare,
                            la sanificazione delle linee produttive e il trattamento delle acque di lavaggio.
                        </p>
                    </article>

                </div>
            </div>
        </section>
    '''

    h2 = f'Perché scegliere l’ozono nei processi industriali?'
    subordinate = f'L’ozono è un ossidante naturale con elevato potere disinfettante che elimina batteri, virus, muffe e composti organici senza lasciare residui chimici.'
    img_height = '400px'
    benefits_html = f'''
        <section class="benefits" style="
            background: linear-gradient(rgba(0, 30, 60, 0.8), rgba(0, 30, 60, 0.8)), 
            url('/immagini/home-benefici.jpg');
            background-size: cover;
            background-position: center;
            padding-top: 6rem;
            padding-bottom: 6rem;
        ">
            <div class="container-xl">
                <h2 style="color: #ffffff;">
                    {h2}
                </h2>
                <p style="color: #ffffff; text-align: center; max-width: 80ch; margin: 0 auto 3rem auto;">
                    {subordinate}
                </p>
            </div>
            <div class="container-xl">
                <ul class="grid-4" style="list-style: none; gap: 2rem;">
                    <li>
                        <svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#1f1f1f"><path d="M172-120q-42 0-59.5-39t11.5-71l248-280v-270h-52q-13 0-21.5-8.5T290-810q0-13 8.5-21.5T320-840h320q13 0 21.5 8.5T670-810q0 13-8.5 21.5T640-780h-52v270l248 280q29 32 11.5 71T788-120H172Zm70-90h476L558-395H402L242-210Zm-82 30h640L528-488v-292h-96v292L160-180Zm320-300Z"/></svg>
                        Riduce l’uso di prodotti chimici nei processi industriali
                    </li>
                    <li>
                        <svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#1f1f1f"><path d="M600-90q-12 0-21-9t-9-21v-41q-28-3-53-13t-47-27l-39 39q-9 8-21.5 8.5T388-162q-9-9-9-21.5t9-21.5l40-39q-5-7-9.5-14.5T410-274l-31-62-51 51q-9 8-21.5 8.5T285-285q-9-9-9-21t9-21l51-52-62-31q-7-4-13.5-7.5T248-426l-35 35q-9 8-21.5 8.5T170-391q-9-9-9-21t9-21l34-34q-17-22-28.5-48T161-570h-41q-12 0-21-9t-9-21q0-13 9-21.5t21-8.5h43q5-24 14.5-46t23.5-41l-34-34q-9-9-9-21t9-21q9-9 21-9t21 9l34 34q19-14 41-23.5t46-14.5v-43q0-13 9-21.5t21-8.5q13 0 21.5 8.5T390-840v41q29 3 55 14.5t49 29.5l34-34q9-9 21.5-9t21.5 9q9 9 9 21t-9 21l-36 36 8 12q4 6 7 13l30 60 48-49q9-9 21.5-9t21.5 9q9 9 9 21.5t-9 21.5l-50 49 65 33 16 10 16 10 39-39q9-9 21-9t21 9q9 9 9 21.5t-9 21.5l-39 38q16 21 26 46t13 52h41q13 0 21.5 8.5T870-360q0 12-8.5 21t-21.5 9h-43q-5 24-14 46t-23 41l32 32q9 9 9 21.5t-9 21.5q-9 8-21.5 8.5T749-168l-32-33q-19 14-41 23.5T630-163v43q0 12-8.5 21T600-90Zm-6-130q69 0 112-51.5T738-389q-6-35-26.5-63T659-496l-66-34q-20-11-36-27t-27-36l-34-66q-19-38-53.5-59.5T366-740q-69 0-112 51.5T222-571q6 35 26.5 63t52.5 44l66 33q20 11 36.5 27.5T431-367l33 66q19 38 53.5 59.5T594-220ZM380-540q25 0 42.5-17.5T440-600q0-25-17.5-42.5T380-660q-25 0-42.5 17.5T320-600q0 25 17.5 42.5T380-540Zm235.5 235.5Q630-319 630-340t-14.5-35.5Q601-390 580-390t-35.5 14.5Q530-361 530-340t14.5 35.5Q559-290 580-290t35.5-14.5ZM480-480Z"/></svg>
                        Elimina microrganismi e biofilm da superfici e attrezzature
                    </li>
                    <li>
                        <svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#1f1f1f"><path d="M80-200v-100h610v100H80Zm655 0v-100h50v100h-50Zm95 0v-100h50v100h-50Zm-95-145v-56q0-42-24.5-66T651-491h-71q-54 0-90.5-41.5T453-628q0-54 36.5-90.5T580-755v50q-35 0-56 21t-21 56q0 35 21 61t56 26h71q54 0 94 37t40 91v68h-50Zm95 0v-100q0-75-50-123t-125-48v-50q34 0 55.5-24t21.5-58q0-34-21.5-58T655-830v-50q54 0 90.5 39t36.5 93q0 33-12.5 57T737-650q58 20 100.5 75T880-445v100h-50Z"/></svg>
                        Decompone odori e composti organici volatili (VOC)
                    </li>
                    <li>
                        <svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#1f1f1f"><path d="M213-175q-43.59-45-68.3-104Q120-338 120-400q0-73 25.5-133.5T222-645q35-35 87-59t122.5-37.5Q502-755 591-758.5t198 3.5q8 108 5.5 197.5t-16 160.75q-13.5 71.25-38 124.56Q716-218.87 680-183q-51 51-110 77T444-80q-69 0-126.5-23.5T213-175Zm103 0q25 17 58 26t69.92 9Q497-140 547-162t91-64q27-27 46-70.5t31-103Q727-459 731-534t0-165q-94-2-168.5 2.5T431-680q-57 12-98 30.5T266-604q-42 43-64 91t-22 98q0 48 20.5 100.5T251-230q53-98 127-176t157-123q-87 75-141 162.5T316-175Zm0 0Zm0 0Z"/></svg>
                        Si riconverte in ossigeno senza generare sottoprodotti tossici
                    </li>
                </ul>
            </div>
        </section>
    '''

    h2 = f'Settori industriali in cui operiamo'
    subordinate = f'Progettiamo e realizziamo impianti a ozono per applicazioni industriali specifiche, adattando ogni soluzione ai processi produttivi del settore di riferimento.'
    img_height = '240px'
    sectors_html = f'''
        <section class="sectors" style="
            padding-top: 6rem;
            padding-bottom: 6rem;
        ">
            <div class="container-xl">
                <h2 style="">
                    {h2}
                </h2>
                <p style="text-align: center; max-width: 80ch; margin: 0 auto 3rem auto;">
                    {subordinate}
                </p>
                <div class="sectors-cards grid-3" style="gap: 2rem;">
                    <article>
                        <a href="#" title="Impianti a ozono per industria alimentare">
                            <figure>
                                <img 
                                    src="/immagini/home-settori-industria-alimentare.jpg" 
                                    alt=""
                                    loading="lazy"
                                    width="600"
                                    height="400"
                                    style="height: {img_height}; object-fit: cover; object-position: center; margin-bottom: 1rem;"
                                >
                            </figure>
                            <h3>Industria alimentare</h3>
                        </a>
                        <p>
                            Sistemi di ozonizzazione per sanificazione ambienti, trattamento acque di processo e controllo microbiologico nelle linee produttive alimentari.
                        </p>
                    </article>

                    <article>
          <a href="#" title="Ozono per impianti di depurazione">
                            <figure>
                                <img 
                                    src="/immagini/home-settori-acque-reflue.jpg" 
                                    alt=""
                                    loading="lazy"
                                    width="600"
                                    height="400"
                                    style="height: {img_height}; object-fit: cover; object-position: center; margin-bottom: 1rem;"
                                >
                            </figure>
                            <h3>Impianti di depurazione</h3>
                        </a>
                        <p>
Impianti a ozono per ossidazione avanzata, riduzione COD e abbattimento 
          odori negli impianti di trattamento acque reflue.                        </p>
                    </article>

                    <article>
          <a href="#" title="Ozono per caseifici">
                            <figure>
                                <img 
                                    src="/immagini/home-settori-caseifici.jpg" 
                                    alt=""
                                    loading="lazy"
                                    width="600"
                                    height="400"
                                    style="height: {img_height}; object-fit: cover; object-position: center; margin-bottom: 1rem;"
                                >
                            </figure>
                            <h3>Caseifici</h3>
                        </a>
                        <p>
Soluzioni a ozono per sanificazione celle di stagionatura, ambienti produttivi 
          e trattamento acque nei processi lattiero-caseari.                      </p>
                    </article>

                    <article>
<a href="#" title="Ozono per macelli industriali">                            <figure>
                                <img 
                                    src="/immagini/home-settori-macelli.jpg" 
                                    alt=""
                                    loading="lazy"
                                    width="600"
                                    height="400"
                                    style="height: {img_height}; object-fit: cover; object-position: center; margin-bottom: 1rem;"
                                >
                            </figure>
                            <h3>Macelli</h3>
                        </a>
                        <p>
Sistemi di ozonizzazione per controllo carica batterica, eliminazione odori 
          e igienizzazione ambienti di lavorazione carni.     
                        </p>
                    </article>

                    <article>
<a href="#" title="Ozono per aziende agricole">                                <img 
                                    src="/immagini/home-settori-agricoltura.jpg" 
                                    alt=""
                                    loading="lazy"
                                    width="600"
                                    height="400"
                                    style="height: {img_height}; object-fit: cover; object-position: center; margin-bottom: 1rem;"
                                >
                            </figure>
                            <h3>Aziende agricole</h3>
                        </a>
                        <p>
Impianti a ozono per trattamento acqua irrigazione, sanificazione serre 
          e riduzione patogeni nelle coltivazioni.
                        </p>
                    </article>

                    <article>
<a href="#" title="Ozono per impianti chimici">                                <img 
                                    src="/immagini/home-settori-chimica.jpg" 
                                    alt=""
                                    loading="lazy"
                                    width="600"
                                    height="400"
                                    style="height: {img_height}; object-fit: cover; object-position: center; margin-bottom: 1rem;"
                                >
                            </figure>
                            <h3>Aziende agricole</h3>
                        </a>
                        <p>
Soluzioni di ossidazione con ozono per processi chimici industriali, 
          abbattimento composti organici volatili e trattamento reflui.                  </p>
                    </article>


                </div>
            </div>
        </section>
    '''

    h2 = f'Dati tecnici misurabili dei nostri impianti a ozono industriali'
    subordinate = f'I nostri generatori di ozono industriali sono progettati con parametri tecnici verificabili e prestazioni misurabili in contesti produttivi reali.'
    img_height = '400px'
    authority_html = f'''
        <section class="benefits" style="
            background: linear-gradient(rgba(0, 30, 60, 0.8), rgba(0, 30, 60, 0.8)), 
            url('/immagini/home-dati-tecnici.jpg');
            background-size: cover;
            background-position: center;
            padding-top: 6rem;
            padding-bottom: 6rem;
        ">
            <div class="container-xl">
                <h2 style="color: #ffffff;">
                    {h2}
                </h2>
                <p style="color: #ffffff; text-align: center; max-width: 80ch; margin: 0 auto 3rem auto;">
                    {subordinate}
                </p>
            </div>
            <div class="container-xl">
                <ul class="benefits grid-3" style="gap: 2rem; list-style: none;">
                    <li><span>0 - 100 g/h</span>Produzione ozono nominale</li>
                    <li><span>0,1 ppm</span>Sensori ozono ambientale di sicurezza<strong></strong></li>                    </li>
                    <li><span>0 - 10 ppm</span>Monitoraggio continuo concentrazione</li>
                </ul>
            </div>
        </section>
    '''


    ozone_html = f'''
        <section class="ozone">
            <div class="ozone_content container-xl">
              <h2>
                Cos’è l’ozono e come funziona
              </h2>
              <p>
                L’ozono è un gas instabile composto da tre atomi di ossigeno, utilizzato come agente ossidante naturale. 
                Ha applicazioni in trattamento dell’aria, depurazione dell’acqua e sanificazione di superfici, quando 
                impiegato correttamente secondo parametri tecnici e sicurezza normativa.
              </p>
              <p>
                Scopri i principi chimici, i limiti e le modalità di utilizzo corrette nella nostra 
                <a href="/ozono.html" title="Guida completa all’ozono">Guida completa all’ozono</a>.
              </p>
            </div>
        </section>
    '''

    icon_color = '#1558B0'
    icon_width = '64px'
    icon_height = icon_width
#     authority_html = f'''
#         <section class="authority">
#             <div class="container-xl authority-content">
#                 <h2>Competenza tecnica sull'ozono</h2>
#                 <p>I nostri sistemi a ozono sono sviluppati secondo rigorosi standard tecnici e di sicurezza, garantendo prestazioni affidabili e conformità alle normative di settore.</p>
#                 <ul>
#                     <li>
# <svg xmlns="http://www.w3.org/2000/svg" height="{icon_height}" viewBox="0 -960 960 960" width="{icon_width}" fill="{icon_color}"><path d="M80-570v-170q0-24 18-42t42-18h680q24 0 42 18t18 42v170h-60v-170H140v170H80Zm60 410q-24 0-42-18t-18-42v-170h60v170h680v-170h60v170q0 24-18 42t-42 18H140Zm259.81-130q8.19 0 15.79-4t11.4-12l133-266 53 106q3.75 8 11.25 12t15.75 4h240v-60H659l-72-143q-3.72-8.25-11.17-11.63-7.45-3.37-15.64-3.37-8.19 0-15.79 3.37-7.6 3.38-11.4 11.63L400-388l-53-106q-3.75-8-11.25-12T320-510H80v60h221l72 144q3.72 8 11.17 12 7.45 4 15.64 4ZM480-480Z"/></svg>
#                         Monitoraggio e controllo continuo dei sistemi in funzione
#                     </li>
#                     <li>
# <svg xmlns="http://www.w3.org/2000/svg" height="{icon_height}" viewBox="0 -960 960 960" width="{icon_width}" fill="{icon_color}"><path d="M705-128 447-388q-23 8-46 13t-47 5q-97.08 0-165.04-67.67Q121-505.33 121-602q0-31 8.16-60.39T152-718l145 145 92-86-149-149q25.91-15.16 54.96-23.58Q324-840 354-840q99.17 0 168.58 69.42Q592-701.17 592-602q0 24-5 47t-13 46l259 258q11 10.96 11 26.48T833-198l-76 70q-10.7 11-25.85 11Q716-117 705-128Zm28-57 40-40-273-273q16-21 24-49.5t8-54.5q0-75-55.5-127T350-782l102 104q9 9 8.5 21.5T451-635L318-510q-9.27 8-21.64 8-12.36 0-20.36-8l-98-97q3 77 54.67 127T354-430q25 0 53-8t49-24l277 277ZM476-484Z"/></svg>
#                         Soluzioni progettate su misura per specifiche esigenze applicative
#                     </li>
#                     <li>
# <svg xmlns="http://www.w3.org/2000/svg" height="{icon_height}" viewBox="0 -960 960 960" width="{icon_width}" fill="{icon_color}"><path d="m296-334 122-122 80 80 152-151v77h60v-180H530v60h77L498-461l-80-80-164 165 42 42ZM180-120q-24 0-42-18t-18-42v-600q0-24 18-42t42-18h600q24 0 42 18t18 42v600q0 24-18 42t-42 18H180Zm0-60h600v-600H180v600Zm0-600v600-600Z"/></svg>
#                         Supporto tecnico specializzato per ogni fase operativa
#                     </li>
#                 </ul>
#             </div>
#         </section>
#     '''

    

    products_html = f'''
        <section class="products">
            <div class="products-content container-xl">
                <h2>
                    Generatori e sistemi a ozono
                </h2>
                <p>
                    La nostra offerta comprende generatori e sistemi a ozono progettati
                    per diversi contesti applicativi, con soluzioni scalabili, sicure
                    e controllate.
                </p>
                <div class="products-list">
                    <a href="/prodotti.html#generatori" class="prodotto-item">
                        <h3>Generatori di ozono</h3>
                        <p>
                            Unità progettate per la produzione controllata di ozono,
                            adatte a impianti civili, commerciali e industriali.
                        </p>
                    </a>
                    <a href="/prodotti.html#acqua" class="prodotto-item">
                        <h3>Sistemi per trattamento acqua</h3>
                        <p>
                            Soluzioni dedicate al trattamento e alla depurazione dell’acqua
                            in applicazioni civili e industriali.
                        </p>
                    </a>
                    <a href="/prodotti.html#integrati" class="prodotto-item">
                        <h3>Soluzioni integrate</h3>
                        <p>
                            Sistemi a ozono progettati per l’integrazione in impianti
                            complessi e processi industriali.
                        </p>
                    </a>
                    <a href="/prodotti.html#compatti" class="prodotto-item">
                        <h3>Unità compatte e civili</h3>
                        <p>
                            Dispositivi compatti per applicazioni residenziali o commerciali,
                            con particolare attenzione alla sicurezza operativa.
                        </p>
                    </a>
                </div>
                <nav>
                    <a href="/prodotti.html">
                        Scopri tutti i prodotti
                    </a>
                </nav>
            </div>
        </section>
    '''

    services_html = f'''
        <section class="services">
            <div class="services-content container-xl">
                <h2>
                    Servizi di progettazione e supporto
                </h2>
                <p>
                    Accompagniamo i sistemi a ozono lungo l’intero ciclo di vita,
                    dalla progettazione iniziale alla manutenzione operativa,
                    garantendo continuità, sicurezza e prestazioni controllate.
                </p>
                <div class="services-line"></div>
                <div class="services-timeline">
                    <div class="service-step">
                        <h3>Progettazione</h3>
                        <p>
                            Analisi tecnica e progettazione di sistemi a ozono
                            in base alle specifiche applicative e normative.
                        </p>
                    </div>
                    <div class="service-step">
                        <h3>Integrazione</h3>
                        <p>
                            Integrazione dei sistemi a ozono in impianti esistenti
                            o di nuova realizzazione.
                        </p>
                    </div>
                    <div class="service-step">
                        <h3>Avviamento e collaudo</h3>
                        <p>
                            Messa in servizio, test operativi e verifica delle
                            prestazioni in condizioni reali.
                        </p>
                    </div>
                    <div class="service-step">
                        <h3>Assistenza e manutenzione</h3>
                        <p>
                            Supporto tecnico continuo, manutenzione programmata
                            e consulenza operativa.
                        </p>
                    </div>
                </div>
                <nav>
                    <a href="/servizi.html">
                        Approfondisci i servizi
                    </a>
                </nav>
            </div>
        </section>
    '''

    guide_html = f'''
        <section class="guide">
            <div class="container-xl">
                <h2>
                    Guida completa all’ozono
                </h2>
                <p>
                    Approfondisci i principi dell’ozono, le applicazioni sicure e le migliori pratiche operative
                    per impieghi industriali, commerciali e civili. Un percorso completo per comprendere
                    tecnologia, sicurezza e buone prassi.
                </p>
                <div class="guide-cards">
                    <a href="/ozono.html" class="guida-tile">
                        <h3>Chimica e proprietà dell’ozono</h3>
                        <p>Fondamenti chimici e caratteristiche principali dell’ozono.</p>
                    </a>
                    <a href="/ozono.html" class="guida-tile">
                        <h3>Sicurezza e normative</h3>
                        <p>Regole, standard e precauzioni per un utilizzo sicuro.</p>
                    </a>
                    <a href="/ozono.html" class="guida-tile">
                        <h3>Applicazioni industriali e commerciali</h3>
                        <p>Esempi concreti di utilizzo nei diversi contesti operativi.</p>
                    </a>
                    <a href="/ozono.html" class="guida-tile">
                        <h3>Miti, limiti e buone pratiche</h3>
                        <p>Approfondimenti su convinzioni errate e buone pratiche operative.</p>
                    </a>
                </div>
                <nav>
                    <a href="/ozono.html">
                        Consulta la guida completa
                    </a>
                </nav>
            </div>
        </section>
    '''

    icon_color = '#1558B0'
    icon_width = '64px'
    icon_height = icon_width
    trust_html = f'''
        <section class="trust">
            <div class="container-xl">
                <h2 id="trust-title">Affidabilità per applicazioni professionali</h2>
                <div class="trust-items">
                    <div class="trust-item">
<svg xmlns="http://www.w3.org/2000/svg" height="{icon_height}" viewBox="0 -960 960 960" width="{icon_width}" fill="{icon_color}"><path d="m363-310 117-71 117 71-31-133 104-90-137-11-53-126-53 126-137 11 104 90-31 133ZM481-29 346-160H160v-186L26-480l134-134v-186h186l135-134 133 134h186v186l134 134-134 134v186H614L481-29Zm0-84 107.92-107H740v-151l109-109-109-109v-151H589L481-849 371-740H220v151L111-480l109 109v151h150l111 107Zm0-368Z"/></svg>
                        <h3>Esperienza consolidata</h3>
                        <p>Oltre 20 anni nella progettazione e realizzazione di sistemi a ozono</p>
                    </div>
                    <div class="trust-item">
<svg xmlns="http://www.w3.org/2000/svg" height="{icon_height}" viewBox="0 -960 960 960" width="{icon_width}" fill="{icon_color}"><path d="M480-450q-45 0-77.5-32.5T370-560q0-45 32.5-77.5T480-670q45 0 77.5 32.5T590-560q0 45-32.5 77.5T480-450ZM244-40v-304q-45-47-64.5-103T160-560q0-136 92-228t228-92q136 0 228 92t92 228q0 57-19.5 113T716-344v304l-236-79-236 79Zm236-260q109 0 184.5-75.5T740-560q0-109-75.5-184.5T480-820q-109 0-184.5 75.5T220-560q0 109 75.5 184.5T480-300ZM304-124l176-55 176 55v-171q-40 29-86 42t-90 13q-44 0-90-13t-86-42v171Zm176-86Z"/></svg>
                        <h3>Certificazioni e standard</h3>
                        <p>Conformità a standard internazionali di sicurezza e qualità</p>
                    </div>
                    <div class="trust-item">
<svg xmlns="http://www.w3.org/2000/svg" height="{icon_height}" viewBox="0 -960 960 960" width="{icon_width}" fill="{icon_color}"><path d="M0-240v-53q0-38.57 41.5-62.78Q83-380 150.38-380q12.16 0 23.39.5t22.23 2.15q-8 17.35-12 35.17-4 17.81-4 37.18v65H0Zm240 0v-65q0-32 17.5-58.5T307-410q32-20 76.5-30t96.5-10q53 0 97.5 10t76.5 30q32 20 49 46.5t17 58.5v65H240Zm540 0v-65q0-19.86-3.5-37.43T765-377.27q11-1.73 22.17-2.23 11.17-.5 22.83-.5 67.5 0 108.75 23.77T960-293v53H780Zm-480-60h360v-6q0-37-50.5-60.5T480-390q-79 0-129.5 23.5T300-305v5ZM149.57-410q-28.57 0-49.07-20.56Q80-451.13 80-480q0-29 20.56-49.5Q121.13-550 150-550q29 0 49.5 20.5t20.5 49.93q0 28.57-20.5 49.07T149.57-410Zm660 0q-28.57 0-49.07-20.56Q740-451.13 740-480q0-29 20.56-49.5Q781.13-550 810-550q29 0 49.5 20.5t20.5 49.93q0 28.57-20.5 49.07T809.57-410ZM480-480q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T600-600q0 50-34.5 85T480-480Zm.35-60Q506-540 523-557.35t17-43Q540-626 522.85-643t-42.5-17q-25.35 0-42.85 17.15t-17.5 42.5q0 25.35 17.35 42.85t43 17.5ZM480-300Zm0-300Z"/></svg>
                        <h3>Collaborazioni professionali</h3>
                        <p>Progetti realizzati con aziende leader e operatori specializzati</p>
                    </div>
                    <div class="trust-item">
<svg xmlns="http://www.w3.org/2000/svg" height="{icon_height}" viewBox="0 -960 960 960" width="{icon_width}" fill="{icon_color}"><path d="m357-513 90-90-75-75-48 48-42-42 48-48-75-74-90 90 192 191Zm346 348 90-91-75-75-48 48-42-42 48-48-74-74-90 90 191 192Zm8-615 70 70-70-70ZM276-120H120v-156l194-194L80-704l174-176 236 235 178-178q9-9 20-13t22-4q11 0 22 4t20 13l71 71q9 9 13 20t4 22q0 11-4 22t-13 20L645-490l235 235L705-81 471-315 276-120Zm-96-60h70l393-394-70-70-393 394v70Zm428-429-35-35 70 70-35-35Z"/></svg>
                        <h3>Progetti industriali completati</h3>
                        <p>Soluzioni implementate con successo in contesti civili, commerciali e industriali</p>
                    </div>
                </div>
            </div>
        </section>
    '''

    contacts_html = f'''
        <section class="contacts">
            <div class="container-xl">
                <h2>
                    Contatto tecnico
                </h2>
                <p>
                    Per valutare soluzioni personalizzate o approfondire le applicazioni dei nostri sistemi a ozono,
                    il nostro team tecnico è disponibile per consulenze e supporto dedicato.
                </p>
                <nav>
                    <a href="/contatti.html">
                        Contattaci
                    </a>
                </nav>
            </div>
        </section>
    '''

    problems_html = f'''
        <section class="problems">
          <div class="container-xl">
            <h2>
              Problemi che l’ozono può contribuire a risolvere
            </h2>
            <p>
              L’ozono viene impiegato come tecnologia di supporto
              nella gestione di specifiche problematiche ambientali e di processo.
              L’efficacia dipende dal contesto, dalla progettazione e dall’utilizzo corretto.
            </p>
            <ul>
              <li>
                <h3>Problemi di qualità dell’aria</h3>
                <p>
                  Contaminazione microbica, odori persistenti e composti ossidabili
                  in ambienti chiusi e industriali.
                </p>
                <a href="/problemi/aria.html">
                  <!-- Approfondisci i problemi legati all’aria -->
                </a>
              </li>
              <li>
                <h3>Problemi di trattamento dell’acqua</h3>
                <p>
                  Presenza di microrganismi, carichi organici e contaminanti
                  in acqua potabile, di processo o reflua.
                </p>
                <a href="/problemi/acqua.html">
                  <!-- Approfondisci i problemi legati all’acqua -->
                </a>
              </li>
              <li>
                <h3>Problemi su superfici e processi</h3>
                <p>
                  Controllo microbiologico, sanificazione e gestione dell’igiene
                  in superfici, impianti e cicli produttivi.
                </p>
                <a href="/problemi/superfici-processi.html">
                  <!-- Approfondisci i problemi di superfici e processi -->
                </a>
              </li>
              <li>
                <h3>Problemi complessi e ambienti regolamentati</h3>
                <p>
                  Applicazioni in contesti industriali avanzati,
                  con vincoli normativi e requisiti di sicurezza elevati.
                </p>
                <a href="/problemi/ambienti-regolamentati.html">
                  <!-- Approfondisci i contesti regolamentati -->
                </a>
              </li>
            </ul>
          </div>
        </section>
    '''

                # {authority_html}

    design_html = f'''
        <section class="design">
          <div class="container-xl">
              <h2>
                Progettazione di sistemi a ozono
              </h2>

              <p>
                Un sistema a ozono efficace non dipende dal generatore,
                ma dalla progettazione complessiva del processo.
                Parametri operativi, sicurezza, controllo e normativa
                determinano il successo o il fallimento dell’applicazione.
              </p>

              <ul>
                <li>Analisi del contesto applicativo</li>
                <li>Definizione dei parametri di processo</li>
                <li>Gestione della sicurezza e dei rischi</li>
                <li>Monitoraggio e controllo operativo</li>
                <li>Conformità normativa e validazione</li>
              </ul>

            </div>
        </section>
    '''
    # TODO
    '''
              <p>
                <a href="/progettazione-sistemi-ozono.html">
                  Approfondisci la progettazione dei sistemi a ozono
                </a>
              </p>
    '''

    technologies_html = f'''
        <section class="technologies">
          <div class="container-xl">
              <h2>
                Tecnologie a ozono
              </h2>
              <p>
                Le tecnologie a ozono si differenziano in base alla modalità di generazione
                e al contesto di applicazione. Ogni sistema richiede soluzioni progettate
                in funzione del mezzo trattato e delle condizioni operative.
              </p>
              <ul>
                <li>
                  <h3>
                      Generazione dell’ozono
                  </h3>
                  <p>
                    Sistemi per la produzione controllata di ozono,
                    progettati in base a portata, concentrazione e continuità operativa.
                  </p>
                </li>
                <li>
                  <h3>
                      Trattamento dell’aria
                  </h3>
                  <p>
                    Tecnologie per la sanificazione, deodorazione
                    e trattamento dell’aria in ambienti civili e industriali.
                  </p>
                </li>
                <li>
                  <h3>
                      Trattamento dell’acqua
                  </h3>
                  <p>
                    Sistemi a ozono per il trattamento, la depurazione
                    e il controllo microbiologico dell’acqua.
                  </p>
                </li>
                <li>
                  <h3>
                      Sistemi integrati
                  </h3>
                  <p>
                    Soluzioni a ozono integrate in impianti complessi
                    e processi industriali regolamentati.
                  </p>
                </li>
              </ul>
              <nav>
                <a href="/prodotti.html">
                  Esplora tutte le tecnologie a ozono
                </a>
              </nav>
          <div>
        </section>
    '''

    services_html = f'''
        <section class="services">
            <div class="container-xl">
              <h2>
                Servizi tecnici per sistemi a ozono
              </h2>
              <p>
                L’ozono è una tecnologia che richiede progettazione, controllo
                e gestione nel tempo. I nostri servizi garantiscono che ogni sistema
                funzioni in modo sicuro, conforme ed efficace nel suo contesto reale.
              </p>
              <ul>
                <li>
                  <strong>Consulenza tecnica</strong> per la valutazione di problemi
                  risolvibili con l’ozono
                </li>
                <li>
                  <strong>Progettazione dei sistemi</strong> in base a parametri,
                  normative e condizioni operative
                </li>
                <li>
                  <strong>Integrazione e avviamento</strong> in impianti nuovi o esistenti
                </li>
                <li>
                  <strong>Assistenza e manutenzione</strong> per garantire continuità
                  e sicurezza nel tempo
                </li>
              </ul>
              <p>
                <a href="/servizi.html">
                  Approfondisci i servizi tecnici
                </a>
              </p>
            </div>
        </section>
    '''

    guide_html = f'''
        <section class="guide">
            <div class="container-xl">
                <h2>
                  Guida all’ozono: conoscenza, sicurezza e applicazioni
                </h2>
                <p>
                  La guida all’ozono di Ozonogroup è un hub tecnico dedicato
                  alla comprensione completa dell’ozono come tecnologia.
                  Include fondamenti scientifici, criteri di sicurezza,
                  normative e applicazioni reali.
                </p>
                <ul>
                  <li>
                      Fondamenti dell’ozono
                  </li>
                  <li>
                      Sicurezza e normative
                  </li>
                  <li>
                      Progettazione dei sistemi a ozono
                  </li>
                  <li>
                      Applicazioni tecniche dell’ozono
                  </li>
                  <li>
                      Limiti, rischi e buone pratiche
                  </li>
                </ul>
                <nav>
                    <p>
                      <a href="/ozono.html">
                        Accedi all’hub completo sulla tecnologia dell’ozono
                      </a>
                    </p>
                </nav>
            </div>
        </section>
    '''

    trust_html = '''
        <section class="trust">
            <div class="container-xl">
              <h2>
                Affidabilità tecnica e continuità operativa
              </h2>
              <p>
                L’utilizzo dell’ozono richiede competenza, controllo e responsabilità.
                La nostra affidabilità si basa su esperienza documentata, conformità
                normativa e progetti reali in contesti complessi.
              </p>
              <ul>
                <li>
                  <strong>Esperienza consolidata</strong><br>
                  Progettazione e applicazione di sistemi a ozono da oltre 20 anni.
                </li>
                <li>
                  <strong>Standard e normative</strong><br>
                  Sistemi progettati secondo standard tecnici e requisiti di sicurezza.
                </li>
                <li>
                  <strong>Progetti verificabili</strong><br>
                  Implementazioni in ambiti civili, commerciali e industriali.
                </li>
                <li>
                  <strong>Collaborazioni qualificate</strong><br>
                  Attività svolte con operatori, aziende e tecnici specializzati.
                </li>
              </ul>
            </div>
        </section>
    '''
    # TODO
    '''
          <nav>
            <ul>
              <li><a href="/chi-siamo.html">Profilo e competenze</a></li>
              <li><a href="/progetti.html">Progetti e casi applicativi</a></li>
              <li><a href="/certificazioni.html">Certificazioni e conformità</a></li>
            </ul>
          </nav>
    '''

    margin_bottom = f'2rem;'
    faq_html = f'''
        <section class="faq" itemscope itemtype="https://schema.org/FAQPage">
            <div class="container-xl"">
                <h2>
                    Domande frequenti sugli impianti a ozono industriali
                </h2>
                <p style="text-align: center; max-width: 80ch; margin: 0 auto 3rem auto;">
                    Risposte tecniche e rapide sulle applicazioni industriali dell’ozono.
                </p>
            </div>
            <div class="container-md"">
                <!-- FAQ 1 -->
                <div class="card" style="margin-bottom: {margin_bottom}" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                    <h3 itemprop="name">Cos’è un generatore di ozono industriale?</h3>
                    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                    <p itemprop="text">
                        Un generatore di ozono industriale è un dispositivo che produce ozono (O₃) a concentrazioni controllate per sanificare ambienti, trattare acque e ossidare contaminanti in ambito produttivo. Funziona tramite scarica a corona o tecnologia UV.
                    </p>
                    </div>
                </div>

                <!-- FAQ 2 -->
                <div class="card" style="margin-bottom: {margin_bottom}" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                    <h3 itemprop="name">L’ozono è sicuro negli ambienti di lavoro?</h3>
                    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                    <p itemprop="text">
                        L’ozono è sicuro se utilizzato con sistemi di controllo, sensori ambientali e nel rispetto dei limiti di esposizione previsti dalle normative vigenti. Gli impianti industriali prevedono monitoraggio automatico e gestione dei livelli residui.
                    </p>
                    </div>
                </div>

                <!-- FAQ 3 -->
                <div class="card" style="margin-bottom: {margin_bottom}" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                    <h3 itemprop="name">Qual è la differenza tra ozono e cloro?</h3>
                    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                    <p itemprop="text">
                        L’ozono è un ossidante più potente del cloro e non lascia residui chimici, poiché si riconverte in ossigeno. Il cloro, invece, può generare sottoprodotti chimici e richiede gestione dei residui.
                    </p>
                    </div>
                </div>

                <!-- FAQ 4 -->
                <div class="card" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                    <h3 itemprop="name">Quanto costa un impianto a ozono?</h3>
                    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                    <p itemprop="text">
                        Il costo di un impianto a ozono varia in base a portata, concentrazione richiesta, automazione e settore applicativo. Gli impianti industriali partono da alcune migliaia di euro fino a sistemi su misura di fascia superiore.
                    </p>
                    </div>
                </div>
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
            <title>Tecnologie a ozono per aria, acqua e superfici</title>
            <meta name="description" content="Tecnologie e sistemi a ozono per applicazioni industriali, commerciali e civili. Progettazione, applicazioni e guida tecnica sull'ozono.">
        </head>
        <body>
            {components.header_default()}
            <main class="home" id="contenuto-principale">
                {hero_html}
                {applications_html}
                {benefits_html}
                {sectors_html}
                {authority_html}
                {faq_html}
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

