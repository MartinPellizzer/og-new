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

    hero_html = f'''
        <section class="hero">
            <div class="container-xl-raw hero-layout">
                <div class="hero-content">
                    <h1>
                        Tecnologie a ozono per aria, acqua e superfici
                    </h1>
                    <p>
                        Progettiamo e realizziamo sistemi a ozono sicuri, controllati e affidabili,
                        adatti a diversi ambiti applicativi, dall’industriale al residenziale.
                    </p>
                    <nav>
                        <ul>
                            <li>
                                <a href="/applicazioni.html">
                                    Esplora le applicazioni
                                </a>
                            </li>
                            <li>
                                <a href="/guida-ozono/">
                                    Guida all’ozono
                                </a>
                            </li>
                        </ul>
                    </nav>
                </div>
                <div class="hero-visual">
                    <figure>
                        <img
                            src="/immagini/sistema-ozono-industriale.jpg"
                            alt="Sistema a ozono per trattamento di aria e acqua in ambiente industriale">
                    </figure>
                </div>
            </div>
        </section>
    '''

    icon_color = '#1558B0'
    icon_width = '64px'
    icon_height = icon_width
    authority_html = f'''
        <section class="authority">
            <div class="container-xl authority-content">
                <h2>Competenza tecnica sull'ozono</h2>
                <p>I nostri sistemi a ozono sono sviluppati secondo rigorosi standard tecnici e di sicurezza, garantendo prestazioni affidabili e conformità alle normative di settore.</p>
                <ul>
                    <li>
<svg xmlns="http://www.w3.org/2000/svg" height="{icon_height}" viewBox="0 -960 960 960" width="{icon_width}" fill="{icon_color}"><path d="M80-570v-170q0-24 18-42t42-18h680q24 0 42 18t18 42v170h-60v-170H140v170H80Zm60 410q-24 0-42-18t-18-42v-170h60v170h680v-170h60v170q0 24-18 42t-42 18H140Zm259.81-130q8.19 0 15.79-4t11.4-12l133-266 53 106q3.75 8 11.25 12t15.75 4h240v-60H659l-72-143q-3.72-8.25-11.17-11.63-7.45-3.37-15.64-3.37-8.19 0-15.79 3.37-7.6 3.38-11.4 11.63L400-388l-53-106q-3.75-8-11.25-12T320-510H80v60h221l72 144q3.72 8 11.17 12 7.45 4 15.64 4ZM480-480Z"/></svg>
                        Monitoraggio e controllo continuo dei sistemi in funzione
                    </li>
                    <li>
<svg xmlns="http://www.w3.org/2000/svg" height="{icon_height}" viewBox="0 -960 960 960" width="{icon_width}" fill="{icon_color}"><path d="M705-128 447-388q-23 8-46 13t-47 5q-97.08 0-165.04-67.67Q121-505.33 121-602q0-31 8.16-60.39T152-718l145 145 92-86-149-149q25.91-15.16 54.96-23.58Q324-840 354-840q99.17 0 168.58 69.42Q592-701.17 592-602q0 24-5 47t-13 46l259 258q11 10.96 11 26.48T833-198l-76 70q-10.7 11-25.85 11Q716-117 705-128Zm28-57 40-40-273-273q16-21 24-49.5t8-54.5q0-75-55.5-127T350-782l102 104q9 9 8.5 21.5T451-635L318-510q-9.27 8-21.64 8-12.36 0-20.36-8l-98-97q3 77 54.67 127T354-430q25 0 53-8t49-24l277 277ZM476-484Z"/></svg>
                        Soluzioni progettate su misura per specifiche esigenze applicative
                    </li>
                    <li>
<svg xmlns="http://www.w3.org/2000/svg" height="{icon_height}" viewBox="0 -960 960 960" width="{icon_width}" fill="{icon_color}"><path d="m296-334 122-122 80 80 152-151v77h60v-180H530v60h77L498-461l-80-80-164 165 42 42ZM180-120q-24 0-42-18t-18-42v-600q0-24 18-42t42-18h600q24 0 42 18t18 42v600q0 24-18 42t-42 18H180Zm0-60h600v-600H180v600Zm0-600v600-600Z"/></svg>
                        Supporto tecnico specializzato per ogni fase operativa
                    </li>
                </ul>
            </div>
        </section>
    '''

    applications_html = f'''
        <section class="applications">
            <div class="applications-content container-xl">
                <h2>
                    Ambiti di applicazione dell’ozono
                </h2>
                <p>
                    Le applicazioni dell’ozono variano in base al contesto d’uso.
                    Esplora i principali ambiti applicativi per soluzioni residenziali,
                    commerciali e industriali.
                </p>
                <div class="applications-cards">
                    <a href="/applicazioni.html#residenziali" class="applicazione-card">
                        <h3>Applicazioni residenziali</h3>
                        <p>
                            Utilizzo dell’ozono in ambienti domestici per il trattamento
                            di aria, acqua e superfici, nel rispetto della sicurezza.
                        </p>
                    </a>
                    <a href="/applicazioni.html#commerciali" class="applicazione-card">
                        <h3>Applicazioni commerciali</h3>
                        <p>
                            Soluzioni a ozono per attività commerciali, strutture ricettive,
                            uffici e spazi aperti al pubblico.
                        </p>
                    </a>
                    <a href="/applicazioni.html#industriali" class="applicazione-card">
                        <h3>Applicazioni industriali</h3>
                        <p>
                            Impiego dell’ozono in processi industriali, impianti complessi
                            e ambienti produttivi regolamentati.
                        </p>
                    </a>
                </div>
                <nav>
                    <a href="/applicazioni.html">
                        Vai alla pagina Applicazioni
                    </a>
                </nav>
            </div>
        </section>
    '''

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
                    <a href="/guida-ozono/chimica-proprieta" class="guida-tile">
                        <h3>Chimica e proprietà dell’ozono</h3>
                        <p>Fondamenti chimici e caratteristiche principali dell’ozono.</p>
                    </a>
                    <a href="/guida-ozono/sicurezza-normative" class="guida-tile">
                        <h3>Sicurezza e normative</h3>
                        <p>Regole, standard e precauzioni per un utilizzo sicuro.</p>
                    </a>
                    <a href="/guida-ozono/applicazioni-industriali" class="guida-tile">
                        <h3>Applicazioni industriali e commerciali</h3>
                        <p>Esempi concreti di utilizzo nei diversi contesti operativi.</p>
                    </a>
                    <a href="/guida-ozono/miti-limiti-pratiche" class="guida-tile">
                        <h3>Miti, limiti e buone pratiche</h3>
                        <p>Approfondimenti su convinzioni errate e buone pratiche operative.</p>
                    </a>
                </div>
                <nav>
                    <a href="/guida-ozono/">
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
            <main id="contenuto-principale">
                {hero_html}
                {authority_html}
                {applications_html}
                {products_html}
                {services_html}
                {guide_html}
                {trust_html}
                {contacts_html}
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

