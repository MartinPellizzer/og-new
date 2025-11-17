import os

from lib import g
from lib import components

from data import settori_data

section_hero_py = '5rem'
section_py = '8rem'

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
            <div style="">
                <div style="display: inline-block;">
                    <a class="button-default-3" href="/contatti.html">
                        <span>Prenota Consulenza Gratuita</span>
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#ffffff"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                    </a>
                </div>
            </div>
        </section>
    '''
    return html


hero_button = f'''
    <div style="flex: 1; display: flex; justify-content: end; margin-top: 0.25rem;">
        <div style="display: inline-block;">
            <a class="button-default-1" href="/contatti.html">
                <span>Prenota Consulenza Gratuita</span>
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
            </a>
        </div>
    </div>
'''

def settori_alimentare_gen():
    data = settori_data.data[0]
    page_slug = data['page_slug']
    ########################################
    # hero
    ########################################
    html_hero = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_hero_py};">
            <div style="display: flex; justify-content: space-between; center;">
                <div style="flex: 2;">
                    <h1 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
                        Sanificazione ad ozono per l'industria alimentare
                    </h1>
                    <p style="color: #1f1f1f;">                        
                        Soluzioni per la sicurezza alimentare e la conformità HACCP.
                    </p>
                </div>
                {hero_button}
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # problemi
    ########################################
    problemi_data = [
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M600-90q-12 0-21-9t-9-21v-41q-28-3-53.02-12.91Q491.97-183.82 470-201l-39 39q-9.07 8.25-21.53 8.62Q397-153 388-162.05q-9-9.06-9-21.5 0-12.45 9-21.45l40-39q-4.67-6.88-9.33-14.44Q414-266 410-274l-31-62-51 51q-9.27 8.25-21.64 8.62Q294-276 285-285t-9-21q0-12 9-21l51-52-62-31q-7-4-13.5-7.5T248-426l-35 35q-9.07 8.25-21.53 8.62Q179-382 170-391q-9-9-9-21t9-21l34-34q-17-22-28.5-48T161-570h-41q-12 0-21-9t-9-21.5q0-12.5 9-21t21-8.5h43.2q4.8-24 14.3-46t23.5-41l-34-34q-9-9-9-21t9-21q9-9 21-9t21 9l34 34q19-14 41-23.5t46-14.3V-840q0-12.75 9-21.38 9-8.62 21.5-8.62t21 8.62q8.5 8.63 8.5 21.38v41q29 3 55.01 14.53Q471.02-772.94 494-755l34-34q9.07-9 21.53-9 12.47 0 21.47 9 9 9 9 21t-9 21l-36 36q4 6 7.93 11.85 3.93 5.84 7.07 13.15l30 60 48-49q9.07-9 21.53-9 12.47 0 21.47 9.05 9 9.06 9 21.5 0 12.45-9 21.45l-50 49 65 33 16 10 16 10 39-39q9-9 21-9t21 9.05q9 9.06 9 21.5 0 12.45-9 21.45l-39 38q16 21 26 46t13 52h41q12.75 0 21.38 8.62Q870-372.75 870-360q0 12-8.62 21-8.63 9-21.38 9h-43.2q-4.8 24-13.8 46t-23 41l32 32q9 9.07 9 21.53 0 12.47-9.05 21.47-9.06 8.25-21.5 8.62Q758-159 749-168l-32-33q-19 14-41 23.5t-46 14.3v43.2q0 12-8.62 21-8.63 9-21.38 9Zm-6-130q69 0 112-51.5T738-389q-5.87-35-26.44-63Q691-480 659-496l-66-34q-19.93-10.53-35.97-26.77Q541-573 530-593l-34-66q-19-38-53.69-59.5Q407.63-740 366-740q-69 0-112 51.5T222-571q5.88 35 26.44 63Q269-480 301-464l66 33q20.32 10.78 36.66 27.39Q420-387 431-367l33 66q19 38 53.69 59.5T594-220ZM380-540q25 0 42.5-17.5T440-600q0-25-17.5-42.5T380-660q-25 0-42.5 17.5T320-600q0 25 17.5 42.5T380-540Zm200 250q21 0 35.5-14.5T630-340q0-21-14.5-35.5T580-390q-21 0-35.5 14.5T530-340q0 21 14.5 35.5T580-290ZM480-480Z"/></svg>''',
            'title': f'''Rischio di contaminazioni microbiologiche''',
            'description': f'''Batteri, muffe e lieviti possono proliferare su superfici e impianti, anche dopo una sanificazione tradizionale.
Le aree umide e le linee di produzione continue rendono difficile un controllo costante della carica microbica.''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M166-120v-94h127L187-576q-32-15-50-40.5T119-684q0-47 34.5-81.5T235-800q44 0 73 23.5t39 62.5h146v-59q0-12 9-21t21-9q11 0 18.5 8.5T549-775l75-72q8-8 20.5-10.5T670-854l158 76q9 5 12.5 14t-1.5 19q-5 10-14.5 12t-18.5-3l-155-75-98 99v52l98 103 155-76q10-5 19-2.5t14 12.5q5 10 1.5 20T827-588l-153 72q-14 7-27 6.5T624-520l-75-72q0 14-7.5 21t-18.5 7q-12 0-21-9t-9-21v-60H345q0 12-6.5 24.5T323-609l205 395h158v94H166Zm69-508q24 0 40-16t16-40q0-24-16-40t-40-16q-24 0-40 16t-16 40q0 24 16 40t40 16Zm124 414h102L272-581q-3 2-10 4t-11 3l108 360Zm102 0Z"/></svg>''',
            'title': f'''Difficoltà di sanificare macchinari e superfici complesse''',
            'description': f'''I macchinari alimentari, con componenti in acciaio e plastiche a contatto diretto con il cibo, richiedono trattamenti efficaci ma delicati.
Le soluzioni chimiche possono lasciare residui, corrodere materiali o richiedere lunghi tempi di risciacquo.''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M225-80q-43.75 0-74.37-30.63Q120-141.25 120-185v-135h120v-560h600v695q0 43.75-30.62 74.37Q778.75-80 735-80H225Zm509.91-60Q754-140 767-152.94q13-12.94 13-32.06v-635H300v500h390v135q0 19.12 12.91 32.06 12.91 12.94 32 12.94ZM360-640v-60h360v60H360Zm0 120v-60h360v60H360ZM224-140h406v-120H180v75q0 19.12 13 32.06Q206-140 224-140Zm0 0h-44 450-406Z"/></svg>''',
            'title': f'''Conformità alle normative HACCP e controlli ASL''',
            'description': f'''Il mantenimento dei livelli di igiene previsti dal sistema HACCP è obbligatorio e soggetto a verifiche periodiche da parte delle autorità sanitarie.
Ogni deviazione può comportare sanzioni, fermi di produzione o perdita di certificazioni.''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M172-120q-41.78 0-59.39-39T124-230l248-280v-270h-52q-12.75 0-21.37-8.68-8.63-8.67-8.63-21.5 0-12.82 8.63-21.32 8.62-8.5 21.37-8.5h320q12.75 0 21.38 8.68 8.62 8.67 8.62 21.5 0 12.82-8.62 21.32-8.63 8.5-21.38 8.5h-52v270l248 280q29 32 11.39 71T788-120H172Zm70-90h476L558-395H402L242-210Zm-82 30h640L528-488v-292h-96v292L160-180Zm320-300Z"/></svg>''',
            'title': f'''Residui chimici e sicurezza alimentare''',
            'description': f'''Molti disinfettanti tradizionali lasciano residui potenzialmente nocivi o alterano l'odore e il sapore degli alimenti.
Le aziende cercano soluzioni naturali e certificate che garantiscano sicurezza e sostenibilità.''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M592-302 450-444v-196h60v171l124 124-42 43ZM450-730v-90h60v90h-60Zm280 280v-60h90v60h-90ZM450-140v-90h60v90h-60ZM140-450v-60h90v60h-90ZM480.27-80q-82.74 0-155.5-31.5Q252-143 197.5-197.5t-86-127.34Q80-397.68 80-480.5t31.5-155.66Q143-709 197.5-763t127.34-85.5Q397.68-880 480.5-880t155.66 31.5Q709-817 763-763t85.5 127Q880-563 880-480.27q0 82.74-31.5 155.5Q817-252 763-197.68q-54 54.31-127 86Q563-80 480.27-80Zm.23-60Q622-140 721-239.5t99-241Q820-622 721.19-721T480-820q-141 0-240.5 98.81T140-480q0 141 99.5 240.5t241 99.5Zm-.5-340Z"/></svg>''',
            'title': f'''Continuità produttiva e tempi di fermo''',
            'description': f'''I processi di pulizia non devono interferire con la produttività.
Ogni ora di fermo linea è un costo: servono sistemi di sanificazione rapidi, automatizzabili e senza risciacquo.''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M213-175q-43.59-45-68.3-104Q120-338 120-400q0-73 25.5-133.5T222-645q35-35 87-59t122.5-37.5Q502-755 591-758.5t198 3.5q8 108 5.5 197.5t-16 160.75q-13.5 71.25-38 124.56Q716-218.87 680-183q-51 51-110 77T444-80q-69 0-126.5-23.5T213-175Zm103 0q25 17 58 26t69.92 9Q497-140 547-162t91-64q27-27 46-70.5t31-103Q727-459 731-534t0-165q-94-2-168.5 2.5T431-680q-57 12-98 30.5T266-604q-42 43-64 91t-22 98q0 48 20.5 100.5T251-230q53-98 127-176t157-123q-87 75-141 162.5T316-175Zm0 0Zm0 0Z"/></svg>''',
            'title': f'''Sostenibilità e riduzione dell'impatto ambientale''',
            'description': f'''Le aziende del food si orientano sempre più verso protocolli a basso impatto, riducendo l'uso di acqua e chimici aggressivi.
Le soluzioni devono essere efficaci e al tempo stesso rispettose dell'ambiente e del consumatore.''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in problemi_data:
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
            </div>
        ''')
                # <p>
                #     <a style="color: #555555;" href="{ item['link_href'] }">{ item['link_anchor'] }</a>
                # </p>
    cards = ''.join(cards)
    html_problemi = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            <div class="container-md" style="margin-bottom: 5rem;">
                <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
                    Le sfide igieniche del settore alimentare
                </h2>
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
In ambienti di lavorazione alimentare, l'igiene non è solo una questione di qualità, ma di legge.
                </p>    
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
Ogni giorno, operatori e responsabili della sicurezza si confrontano con la necessità di mantenere superfici, impianti e ambienti liberi da contaminazioni, rispettando al tempo stesso rigidi protocolli HACCP e tempi produttivi sempre più serrati.
                </p>    
                <p style="color: #1f1f1f;">    
Un errore minimo può compromettere la sicurezza del prodotto, la reputazione dell'azienda e la conformità alle normative.
                </p>    
            </div>
            <div class="grid-2" style="column-gap: 8rem; row-gap: 3rem; margin-bottom: 8rem;">
                {cards}
            </div>
            <div class="container-md">
                <p style="color: #1f1f1f; margin-bottom: 1rem">    
                Queste sfide rendono necessario un cambio di paradigma nei metodi di igienizzazione:
serve una tecnologia in grado di eliminare i microrganismi in profondità, senza residui, compatibile con i materiali e i ritmi produttivi del settore.
                </p>
                <p style="color: #1f1f1f;">    
È qui che l'ozono rappresenta una soluzione concreta, naturale e certificata.
                </p>
            </div>
        </section> 
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # soluzioni
    ########################################
    html_soluzioni = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            <div class="container-md" style="margin-bottom: 5rem;">
                <h2 style="color: #1f1f1f; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
                    Come l'ozono risolve le criticità dell'igiene alimentare
                </h2>
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
L'ozono rappresenta una delle tecnologie più efficaci e sostenibili per la sanificazione nel settore alimentare.
                </p>
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
È un gas naturale con un elevato potere ossidante, capace di eliminare batteri, virus, muffe e odori in pochi minuti, senza lasciare alcun residuo chimico.
                </p>
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
Grazie alla sua versatilità, può essere utilizzato per il trattamento di aria, superfici, celle frigorifere e impianti di produzione, riducendo tempi di fermo e garantendo una sanificazione uniforme anche nei punti più difficili da raggiungere.
                </p>
            </div>
            <div class="container-md">
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
                    Eliminazione totale di batteri, muffe e virus
                </h3>
                <p style="color: #1f1f1f; margin-bottom: 3rem;">
                    L'ozono ossida la membrana cellulare dei microrganismi, distruggendoli in modo irreversibile.
                    È efficace contro oltre 99,9% di batteri, spore e muffe, anche in aree difficili da trattare con metodi tradizionali.
                </p>
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
                    Trattamento profondo senza danneggiare materiali
                </h3>
                <p style="color: #1f1f1f; margin-bottom: 3rem;">
                    Essendo un gas, penetra in ogni fessura, cavità e componente dei macchinari.
                    Non corrode l'acciaio inox né lascia residui, rendendolo ideale per nastri trasportatori, utensili e impianti complessi.
                </p>
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
Conformità alle normative HACCP e ISO
                </h3>
                <p style="color: #1f1f1f; margin-bottom: 3rem;">
L'ozono è riconosciuto come agente sanificante naturale dal Ministero della Salute (prot. n. 24482 del 31/07/1996) e conforme ai protocolli HACCP.
L'adozione di sistemi ad ozono supporta la certificazione dei processi e la tracciabilità delle attività di sanificazione.
                </p>
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
Nessun residuo chimico
                </h3>
                <p style="color: #1f1f1f; margin-bottom: 3rem;">
Dopo il trattamento, l'ozono si riconverte in ossigeno, senza rilasciare sostanze chimiche o alterare gli alimenti.
È perfetto per ambienti di produzione, stoccaggio e confezionamento dove è richiesta purezza assoluta.
                </p>
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
Sanificazione rapida e automatizzabile
                </h3>
                <p style="color: #1f1f1f; margin-bottom: 3rem;">
I generatori di ozono possono essere integrati nei cicli produttivi o nei sistemi HVAC, permettendo la sanificazione automatica tra un turno e l'altro, con tempi di inattività minimi.
                </p>
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
Soluzione sostenibile e a basso impatto ambientale
                </h3>
                <p style="color: #1f1f1f; margin-bottom: 5rem;">
Nessun consumo di acqua o detergenti chimici, solo aria e corrente elettrica.
Riduce gli sprechi, migliora la sicurezza dei lavoratori e contribuisce agli obiettivi ESG e di sostenibilità aziendale.
                </p>
                <p style="color: #1f1f1f;">
Grazie alla sua efficacia e sicurezza, la sanificazione ad ozono è oggi una tecnologia chiave per l'industria alimentare moderna.
La nostra azienda progetta e applica protocolli su misura per ogni realtà produttiva, combinando esperienza tecnica e sistemi certificati.
                </p>
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # servizi
    ########################################
    servizi_data = [
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="m229-496-6-49q-20-5-37.5-14.5T154-583l-44 18-30-49 37-35q-5-20-5-39t5-39l-37-35 30-49 44 18q14-14 31.5-23.5T223-831l6-49h60l6 49q20 5 37.5 14.5T364-793l44-18 30 49-38 35q5 19 5 38.5t-5 39.5l38 35-30 49-44-18q-14 15-31.5 24T295-545l-6 49h-60Zm30-100q38 0 65-27t27-65q0-38-27-65t-65-27q-38 0-65 27t-27 65q0 38 27 65t65 27ZM644-40l-14-57q-27-7-51.5-21T536-154l-54 17-38-65 42-38q-8-26-8-54t8-54l-42-37 38-65 54 15q19-21 43-35.5t51-20.5l14-57h75l14 57q29 4 52.5 19t42.5 37l54-15 38 65-42 37q8 26 8 54t-8 54l42 38-38 66-54-18q-18 23-42.5 36.5T733-97l-14 57h-75Zm38-115q58 0 98.5-40.5T821-294q0-58-40.5-98.5T682-433q-58 0-98.5 40.5T543-294q0 58 40.5 98.5T682-155Z"/></svg>
            ''',
            'title': f'''Sanificazione ambienti produttivi''',
            'description': f'''
            Eliminazione di batteri, muffe e odori in aree di lavorazione, confezionamento e stoccaggio.
I trattamenti ad ozono assicurano una disinfezione uniforme e completa, anche nei punti più difficili da raggiungere.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M480.24-260Q572-260 636-324.24q64-64.23 64-156Q700-572 635.76-636q-64.23-64-156-64Q388-700 324-635.76q-64 64.23-64 156Q260-388 324.24-324q64.23 64 156 64Zm-.24-60q-29 0-56-10.5T375-360h210q-22 19-49 29.5T480-320Zm-138-80q-8-14-13-29t-7-31h316q-2 16-7 31t-13 29H342Zm-20-100q2-16 7-31t13-29h276q8 14 13 29t7 31H322Zm53-100q22-19 49-29.5t56-10.5q29 0 56 10.5t49 29.5H375ZM180-120q-24.75 0-42.37-17.63Q120-155.25 120-180v-600q0-24.75 17.63-42.38Q155.25-840 180-840h600q24.75 0 42.38 17.62Q840-804.75 840-780v600q0 24.75-17.62 42.37Q804.75-120 780-120H180Zm0-60h600v-600H180v600Zm0-600v600-600Z"/></svg>
            ''',
            'title': f'''Trattamento aria e impianti HVAC''',
            'description': f'''
            Purificazione dell'aria e sanificazione dei canali di ventilazione per ridurre la carica microbica aerotrasportata.
L'ozono agisce direttamente nei condotti, migliorando la qualità dell'aria e prevenendo ricontaminazioni.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M309-650v-118h60v118h-60Zm0 361v-196h60v196h-60ZM220-80q-24.75 0-42.37-17.63Q160-115.25 160-140v-680q0-24.75 17.63-42.38Q195.25-880 220-880h520q24.75 0 42.38 17.62Q800-844.75 800-820v680q0 24.75-17.62 42.37Q764.75-80 740-80H220Zm0-60h520v-398H220v398Zm0-458h520v-222H220v222Z"/></svg>
            ''',
            'title': f'''Sanificazione di celle frigorifere e magazzini refrigerati''',
            'description': f'''
            Trattamento regolare di celle e ambienti a bassa temperatura, dove muffe e batteri possono proliferare nonostante il freddo.
L'ozono agisce anche a basse temperature, senza compromettere gli alimenti.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M201-120q-50 0-85-35t-35-85q0-50 35-85t85-35h560q50 0 85 35t35 85q0 50-35 85t-85 35H201Zm0-60h560q25.5 0 42.75-17.25T821-240q0-25.5-17.25-42.75T761-300H201q-25.5 0-42.75 17.25T141-240q0 25.5 17.25 42.75T201-180Zm190-260q-12.75 0-21.37-8.63Q361-457.25 361-470v-340q0-12.75 8.63-21.38Q378.25-840 391-840h340q12.75 0 21.38 8.62Q761-822.75 761-810v340q0 12.75-8.62 21.37Q743.75-440 731-440H391Zm30-60h280v-280H421v280ZM79-530v-60h221v60H79Zm401-120h162v-60H480v60Zm-319 0h147v-60H161v60Zm260 150v-280 280Z"/></svg>
            ''',
            'title': f'''Trattamento macchinari e nastri trasportatori''',
            'description': f'''
            Protocollo di sanificazione senza acqua né detergenti chimici, ideale per macchine di produzione e linee automatizzate.
Riduce i tempi di fermo e preserva le superfici metalliche.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M80-590v-190q0-24 18-42t42-18h680q24 0 42 18t18 42v190h-60v-190H140v190H80Zm60 350q-24 0-42-18t-18-42v-230h60v230h680v-230h60v230q0 24-18 42t-42 18H140ZM40-120v-60h880v60H40Zm440-420ZM80-530v-60h240q8.16 0 15.58 4T347-574l55 112 131-231q4-8 11.5-11.5t15.62-3.5q8.12 0 15.5 3.5Q583-701 587-693l50.55 103H880v60H619q-8.25 0-15.75-4T592-546l-34-69-131 229q-3.72 8-11.17 12-7.45 4-15.64 4-8.19 0-15.69-4T373-386l-72-144H80Z"/></svg>
            ''',
            'title': f'''Monitoraggio e verifiche post-trattamento''',
            'description': f'''
            Controlli periodici e report certificati sulla carica microbica residua.
Ogni intervento viene documentato secondo gli standard HACCP e ISO, garantendo tracciabilità totale.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M743-631q-26 26-58 38.5T619-580q-34 0-66-12.5T495-631l-75-75q-17-17-37.5-25t-42.5-8q-22 0-42.5 8T260-706l-68 68-43-43 68-68q26-26 58-38.5t65-12.5q33 0 64.5 12.5T462-749l75 75q17 17 37.5 25.5T618-640q23 0 44-8.5t38-25.5l68-68 43 43-68 68Zm0 210q-26 26-58 38.5T619-370q-34 0-66-12.5T495-421l-75-75q-17-17-37.5-25t-42.5-8q-22 0-42.5 8T260-496l-68 68-43-42 68-69q26-26 58-38.5t65-12.5q33 0 64.5 12.5T462-539l75 75q17 17 38 25.5t44 8.5q23 0 43.5-8.5T700-464l68-68 43 43-68 68Zm-1 210q-26 26-57.5 38.5T619-160q-34 0-66-12.5T495-211l-76-75q-17-17-37.5-25t-42.5-8q-22 0-42.5 8T259-286l-68 68-42-42 68-69q26-26 57.5-38.5T339-380q33 0 65 12.5t58 38.5l75 75q17 17 38 25.5t44 8.5q23 0 43.5-8.5T700-254l68-68 42 43-68 68Z"/></svg>
            ''',
            'title': f'''Deodorizzazione e trattamento odori''',
            'description': f'''
            Rimozione di odori organici da ambienti, celle e aree di lavorazione senza mascherarli.
L'ozono neutralizza le molecole odorose, migliorando il comfort e la percezione di pulizia.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in servizi_data:
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
            </div>
        ''')
    cards = ''.join(cards)
    html_servizi = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            <div class="container-md" style="margin-bottom: 5rem;">
                <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
                    Servizi principali per l'industria alimentare
                </h2>
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
In ambienti di lavorazione alimentare, l'igiene non è solo una questione di qualità, ma di legge.
                </p>    
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
Ogni giorno, operatori e responsabili della sicurezza si confrontano con la necessità di mantenere superfici, impianti e ambienti liberi da contaminazioni, rispettando al tempo stesso rigidi protocolli HACCP e tempi produttivi sempre più serrati.
                </p>    
                <p style="color: #1f1f1f;">    
Un errore minimo può compromettere la sicurezza del prodotto, la reputazione dell'azienda e la conformità alle normative.
                </p>    
            </div>
            <div class="grid-3" style="column-gap: 5rem; row-gap: 3rem; margin-bottom: 8rem;">
                {cards}
            </div>
            <div class="container-md">
                <p style="color: #1f1f1f;">    
Ogni servizio è progettato per adattarsi al tuo processo produttivo, nel rispetto delle normative e dei ritmi aziendali.
Scopri nel dettaglio come operiamo e quali risultati abbiamo ottenuto nel tuo settore.
                </p>
            </div>
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
                {html_hero}
                {html_problemi}
                {html_soluzioni}
                {html_servizi}
                {cta()}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    try: os.makedirs(f'{g.website_folderpath}/settori')
    except: pass
    html_filepath = f'{g.website_folderpath}/settori/{page_slug}.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)

def settori_alimentare_lattiero_caseario_gen():
    data = {
        'page_slug': '''alimentare/lattiero-caseario''',
        'href': '''/settori/alimentare.html''',
        'image_src': '/immagini/settori-industria-alimentare.jpg',
        'category': '',
        'title': '''Sanificazione Caseifici: aree critiche, problemi e soluzioni per l'industria lattiero-casearia''',
        'description': '''
La sanificazione nei caseifici è fondamentale per garantire la sicurezza alimentare, prevenire contaminazioni e preservare la qualità dei prodotti lattiero-caseari. Ogni area di produzione ha rischi specifici, dal latte crudo alla stagionatura dei formaggi, e richiede procedure mirate e tecnologie avanzate come l'ozono, la nebulizzazione o i sistemi CIP (Clean-In-Place).
        ''',
        'date': '''6 Ottobre 2025''',
        'datetime': '''2025-10-06''',
    }
    page_slug = data['page_slug']
    ########################################
    # hero
    ########################################
    html_hero = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_hero_py};">
            <div style="display: flex; justify-content: space-between; center;">
                <div style="flex: 2;">
                    <h1 style="color: #1f1f1f; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
Sanificazione ozono per il settore lattiero-caseario
                    </h1>
                    <p style="color: #1f1f1f;">                        
La sanificazione nei caseifici è fondamentale per garantire la sicurezza alimentare, prevenire contaminazioni e preservare la qualità dei prodotti lattiero-caseari. Ogni area di produzione ha rischi specifici, dal latte crudo alla stagionatura dei formaggi, e richiede procedure mirate e tecnologie avanzate come l'ozono, la nebulizzazione o i sistemi CIP (Clean-In-Place).
                    </p>
                </div>
                {hero_button}
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # area
    ########################################
    data = [
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M646-80q-100 0-167-67t-67-167q0-100 67-167t167-67q100 0 167 67t67 167q0 100-67 167T646-80Zm0-60q72 0 123-51t51-123q0-72-51-123t-123-51q-72 0-123 51t-51 123q0 72 51 123t123 51Zm-506-20q-24 0-42-18t-18-42v-330q0-13 1.5-21t6.5-19l92-200h-22q-15 0-24.5-9.5T124-824v-22q0-15 9.5-24.5T158-880h261q15 0 24.5 9.5T453-846v22q0 15-9.5 24.5T419-790h-22l96 222q-12 6-25 15t-24 18L329-790h-82L140-559v339h224q3 15 10 31t15 29H140Zm506-438q-36 0-60-24t-24-60q0-36 24-60t60-24v168q0-36 24-60t60-24q36 0 60 24t24 60H646Z"/></svg>
            ''',
            'title': f'''Ricezione e stoccaggio del latte crudo''',
            'description': f'''
Questa fase è il primo punto critico: la sanificazione qui previene l'introduzione di patogeni nell'intera linea produttiva.
            ''',
            'punti_critici': [
'serbatoi di raccolta', 'tubazioni', 'pompe', 'valvole'
            ],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M220-400q0 63 28.5 118.5T328-189q-4-12-6-24.5t-2-24.5q0-32 12-60t35-51l113-111 113 111q23 23 35 51t12 60q0 12-2 24.5t-6 24.5q51-37 79.5-92.5T740-400q0-54-23-105.5T651-600q-21 15-44 23.5t-46 8.5q-61 0-101-41.5T420-714v-20q-46 33-83 73t-63 83.5q-26 43.5-40 89T220-400Zm260 24-71 70q-14 14-21.5 31t-7.5 37q0 41 29 69.5t71 28.5q42 0 71-28.5t29-69.5q0-20-7.5-37T551-306l-71-70Zm0-464v132q0 34 23.5 57t57.5 23q18 0 33.5-7.5T622-658l18-22q74 42 117 117t43 163q0 134-93 227T480-80q-134 0-227-93t-93-227q0-128 86-246.5T480-840Z"/></svg>
            ''',
            'title': f'''
Pastorizzazione e trattamento termico
            ''',
            'description': f'''
La pastorizzazione riduce il carico microbico, ma le superfici e le tubazioni richiedono sanificazioni mirate per evitare ricontaminazioni.
            ''',
            'punti_critici': ['pastorizzatori', 'serbatoi di accumulo', 'tubazioni', 'valvole'],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M584.88-120Q539-120 507-152.12q-32-32.12-32-78T507.12-308q32.12-32 78-32T663-307.88q32 32.12 32 78T662.88-152q-32.12 32-78 32Zm-.06-60q21.18 0 35.68-14.32 14.5-14.33 14.5-35.5 0-21.18-14.32-35.68-14.33-14.5-35.5-14.5-21.18 0-35.68 14.32-14.5 14.33-14.5 35.5 0 21.18 14.32 35.68 14.33 14.5 35.5 14.5Zm80.12-230Q575-410 512.5-472.56 450-535.13 450-625.06q0-89.94 62.56-152.44 62.57-62.5 152.5-62.5 89.94 0 152.44 62.56 62.5 62.57 62.5 152.5 0 89.94-62.56 152.44-62.57 62.5-152.5 62.5Zm-.17-60Q730-470 775-514.77q45-44.78 45-110Q820-690 775.23-735q-44.78-45-110-45Q600-780 555-735.23q-45 44.78-45 110Q510-560 554.77-515q44.78 45 110 45ZM275-237q-65 0-110-45t-45-110q0-65 45-110t110-45q65 0 110 45t45 110q0 65-45 110t-110 45Zm-.13-60Q314-297 342-324.87q28-27.86 28-67Q370-431 342.13-459q-27.86-28-67-28Q236-487 208-459.13q-28 27.86-28 67Q180-353 207.87-325q27.86 28 67 28ZM585-230Zm80-395ZM275-392Z"/></svg>
            ''',
            'title': f'''
Coagulazione e lavorazione della cagliata
            ''',
            'description': f'''
Nelle vasche e sulle attrezzature di lavorazione la pulizia meccanica è fondamentale per rimuovere residui organici che favoriscono muffe e batteri.
            ''',
            'punti_critici': ['vasche di coagulazione', 'coltelli', 'nastri trasportatori'],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M160-410v-70h640v70H160Zm0-121v-60h640v60H160ZM449-80v-158l-77 76-42-42 149-148 147 148-42 42-75-76v158h-60Zm30-568L331-796l42-42 75 76v-158h60v158l77-76 42 42-148 148Z"/></svg>
            ''',
            'title': f'''
Pressatura e formatura
            ''',
            'description': f'''
Stampi, presse e superfici di lavoro sono punti di contatto diretto con il prodotto e richiedono sanificazioni tra un ciclo e l'altro.
            ''',
            'punti_critici': ['presse per formaggi', 'stampi', 'tavoli di lavoro'],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M480-80q-137 0-228.5-94T160-408h60q0 115 74 191.5T480-140q112 0 186-76.5T740-408h60q0 140-91.5 234T480-80ZM199.82-490q-12.82 0-21.32-8.68-8.5-8.67-8.5-21.5 0-12.82 8.68-21.32 8.67-8.5 21.5-8.5 12.82 0 21.32 8.68 8.5 8.67 8.5 21.5 0 12.82-8.68 21.32-8.67 8.5-21.5 8.5Zm180 0q-12.82 0-21.32-8.68-8.5-8.67-8.5-21.5 0-12.82 8.68-21.32 8.67-8.5 21.5-8.5 12.82 0 21.32 8.68 8.5 8.67 8.5 21.5 0 12.82-8.68 21.32-8.67 8.5-21.5 8.5Zm200 0q-12.82 0-21.32-8.68-8.5-8.67-8.5-21.5 0-12.82 8.68-21.32 8.67-8.5 21.5-8.5 12.82 0 21.32 8.68 8.5 8.67 8.5 21.5 0 12.82-8.68 21.32-8.67 8.5-21.5 8.5Zm180 0q-12.82 0-21.32-8.68-8.5-8.67-8.5-21.5 0-12.82 8.68-21.32 8.67-8.5 21.5-8.5 12.82 0 21.32 8.68 8.5 8.67 8.5 21.5 0 12.82-8.68 21.32-8.67 8.5-21.5 8.5Zm-470-110q-12.82 0-21.32-8.68-8.5-8.67-8.5-21.5 0-12.82 8.68-21.32 8.67-8.5 21.5-8.5 12.82 0 21.32 8.68 8.5 8.67 8.5 21.5 0 12.82-8.68 21.32-8.67 8.5-21.5 8.5Zm380 0q-12.82 0-21.32-8.68-8.5-8.67-8.5-21.5 0-12.82 8.68-21.32 8.67-8.5 21.5-8.5 12.82 0 21.32 8.68 8.5 8.67 8.5 21.5 0 12.82-8.68 21.32-8.67 8.5-21.5 8.5Zm-190-10q-12.82 0-21.32-8.68-8.5-8.67-8.5-21.5 0-12.82 8.68-21.32 8.67-8.5 21.5-8.5 12.82 0 21.32 8.68 8.5 8.67 8.5 21.5 0 12.82-8.68 21.32-8.67 8.5-21.5 8.5Zm-100-100q-12.82 0-21.32-8.68-8.5-8.67-8.5-21.5 0-12.82 8.68-21.32 8.67-8.5 21.5-8.5 12.82 0 21.32 8.68 8.5 8.67 8.5 21.5 0 12.82-8.68 21.32-8.67 8.5-21.5 8.5Zm200 0q-12.82 0-21.32-8.68-8.5-8.67-8.5-21.5 0-12.82 8.68-21.32 8.67-8.5 21.5-8.5 12.82 0 21.32 8.68 8.5 8.67 8.5 21.5 0 12.82-8.68 21.32-8.67 8.5-21.5 8.5Zm-100-100q-12.82 0-21.32-8.68-8.5-8.67-8.5-21.5 0-12.82 8.68-21.32 8.67-8.5 21.5-8.5 12.82 0 21.32 8.68 8.5 8.67 8.5 21.5 0 12.82-8.68 21.32-8.67 8.5-21.5 8.5Zm.18 402Z"/></svg>
            ''',
            'title': f'''
Salatura
            ''',
            'description': f'''
I bagni di salamoia e le vasche possono diventare serbatoi di contaminanti se non gestiti e sanificati correttamente.
            ''',
            'punti_critici': ['bagni salamoia', 'vasche', 'tavoli di applicazione sale'],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M620-530q-21 0-35.5-14.5T570-580q0-13 4.5-24t12-21.5q7.5-10.5 16.5-20t17-19.5q8 10 17 19.5t16.5 20q7.5 10.5 12 21.5t4.5 24q0 21-14.5 35.5T620-530Zm170-132q-21 0-35.5-14.5T740-712q0-13 4.5-24t12-21.5q7.5-10.5 16.5-20t17-19.5q8 10 17 19.5t16.5 20q7.5 10.5 12 21.5t4.5 24q0 21-14.5 35.5T790-662Zm0 262q-21 0-35.5-14.5T740-450q0-13 4.5-24t12-21.5q7.5-10.5 16.5-20t17-19.5q8 10 17 19.5t16.5 20q7.5 10.5 12 21.5t4.5 24q0 21-14.5 35.5T790-400ZM336-121q-76 0-129-53t-53-129q0-48 24-90.5t66-68.5v-286q0-38 27-65t65-27q38 0 65 27t27 65v286q42 26 66 68.5t24 90.5q0 76-53 129t-129 53ZM214-303h244q0-40-19-71.5T388-420l-20-9v-319q0-14-9-23t-23-9q-14 0-23 9t-9 23v319l-20 9q-32 14-51 46t-19 71Z"/></svg>
            ''',
            'title': f'''
Stagionatura e maturazione
            ''',
            'description': f'''
Le celle e gli scaffali di stagionatura richiedono un controllo rigoroso di umidità e aria perché sono le aree più sensibili alla formazione di muffe.
            ''',
            'punti_critici': ['celle frigorifere', 'scaffali', 'sistemi di umidificazione'],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M450-154v-309L180-619v309l270 156Zm60 0 270-156v-310L510-463v309Zm-60 69L150-258q-14-8-22-22t-8-30v-340q0-16 8-30t22-22l300-173q14-8 30-8t30 8l300 173q14 8 22 22t8 30v340q0 16-8 30t-22 22L510-85q-14 8-30 8t-30-8Zm194-525 102-59-266-154-102 59 266 154Zm-164 96 104-61-267-154-104 60 267 155Z"/></svg>
            ''',
            'title': f'''
Confezionamento e packaging
            ''',
            'description': f'''
Il confezionamento è il punto finale prima che il prodotto entri nel mercato: la sanificazione qui tutela la shelf-life e la sicurezza del consumatore.
            ''',
            'punti_critici': ['linee di confezionamento', 'nastri trasportatori', 'tavoli di imballaggi'],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M140-180h120v-320h440v320h120v-460L480-776 140-640v460Zm-60 60v-560l400-160 400 160v560H640v-320H320v320H80Zm290 0v-60h60v60h-60Zm80-120v-60h60v60h-60Zm80 120v-60h60v60h-60ZM260-500h440-440Z"/></svg>
            ''',
            'title': f'''
Magazzino e stoccaggio prodotti finiti
            ''',
            'description': f'''
Lo stoccaggio richiede sanificazioni per evitare contaminazioni da movimentazione e per preservare i prodotti fino alla distribuzione.
            ''',
            'punti_critici': ['celle frigorifere', 'scaffalature', 'carrelli e pallet'],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M200-120v-60h208v-104h-15q-81 0-137-56t-56-137q0-61 35-111t92-70q4-40 35-65t72-22l-21-59 41-14.56L440-856l66-24 14 37 40-14 113 295-43 15 14 37-64 23-14-37-43 16-25-68q-15 17-35.5 24.5t-43.83 6.5Q393-546 371-561t-35-38q-35 17-55.5 49.97Q260-516.07 260-477q0 55.42 38.79 94.21Q337.58-344 393-344h347v60H508v104h252v60H200Zm356-452 53-19-80-206-53 19 80 206Zm-130.18-23q21.18 0 35.68-14.32 14.5-14.33 14.5-35.5 0-21.18-14.32-35.68-14.33-14.5-35.5-14.5-21.18 0-35.68 14.32-14.5 14.33-14.5 35.5 0 21.18 14.32 35.68 14.33 14.5 35.5 14.5ZM556-572Zm-130-75Zm2 0Z"/></svg>
            ''',
            'title': f'''
Laboratori di controllo qualità
            ''',
            'description': f'''
I laboratori devono ridurre al minimo le contaminazioni incrociate per garantire risultati di analisi affidabili.
            ''',
            'punti_critici': ['strumenti analitici', 'tavoli di lavoro', 'microscopi', 'cappe di protezione'],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M212-80v-300h-50v-228q0-29 21.5-50.5t50.24-21.5h104.52q28.74 0 50.24 21.5Q410-637 410-608v228h-50v300H212Zm74.08-654q-30.08 0-51.58-21.42t-21.5-51.5q0-30.08 21.42-51.58t51.5-21.5q30.08 0 51.58 21.42t21.5 51.5q0 30.08-21.42 51.58t-51.5 21.5ZM630-80v-240H526l86-311q7.22-23.59 26.61-36.3Q658-680 684-680t45.39 12.7Q748.78-654.59 756-631l86 311H738v240H630Zm54.08-654q-30.08 0-51.58-21.42t-21.5-51.5q0-30.08 21.42-51.58t51.5-21.5q30.08 0 51.58 21.42t21.5 51.5q0 30.08-21.42 51.58t-51.5 21.5Z"/></svg>
            ''',
            'title': f'''
Aree comuni e servizi
            ''',
            'description': f'''
Pavimenti, corridoi, spogliatoi e servizi igienici sono punti di diffusione possibile di contaminanti che possono raggiungere l'area produttiva.
            ''',
            'punti_critici': ['pavimenti', 'corridoi', 'spogliatoi', 'bagni', 'zone di movimentazione carrelli'],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in data:
        punti_critici = '\n'.join([f'<li style="margin-bottom: 0.5rem;">{x.capitalize()}</li>' for x in item['punti_critici']])
        cards.append(f'''
            <div>
                <div style="display: inline-block; margin-bottom: 2rem; border: 1px solid #f2f2f2; border-radius: 2rem; padding: 2rem;">
                    { item['icon'] }
                </div>
                <h3 style="color: #1f1f1f; font-size: 1.5rem; line-height: 1.25; font-weight: bold; margin-bottom: 1rem;">
                    { item['title'] }
                </h3> 
                <p style="color: #555555; margin-bottom: 2rem;">
                    { item['description'] }                    
                </p>
                <p style="color: #555555; margin-bottom: 0.675rem; font-size: 0.675rem;">
                    PUNTI CRITICI
                </p>
                <ul style="list-style-type: none;">
                    {punti_critici}
                </ul>
            </div>
        ''')
    cards = ''.join(cards)
    html_aree = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            <div style="margin-bottom: 5rem;">
                <h2 style="color: #1f1f1f; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
                    Aree
                </h2>
            </div>
            <div class="grid-3" style="column-gap: 8rem; row-gap: 3rem; margin-bottom: 0;">
                {cards}
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''

    ########################################
    # problemi
    ########################################
    data = [
        {
            'icon': f'''
{g.GRASS_48_BLUE_SVG}
            ''',
            'title': f'''
Muffe
            ''',
            'description': f'''
Le muffe sono tra i contaminanti più frequenti nei caseifici, soprattutto nelle aree ad alta umidità e contatto prolungato con le forme.
            ''',
            'aree_critiche': [
'stagionatura', 'pressatura', 'bagni salamoia',
            ],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.BACTERIA_48_BLUE_SVG}
            ''',
            'title': f'''
Contaminazione crociata
            ''',
            'description': f'''
I batteri patogeni rappresentano un rischio critico per sicurezza alimentare e conformità normativa, richiedendo interventi rigorosi e continuativi.
            ''',
            'aree_critiche': ['latte crudo', 'pastorizzatori', 'linee di confezionamento'],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.CONTAMINATION_48_BLUE_SVG}
            ''',
            'title': f'''
Contaminazione crociata
            ''',
            'description': f'''
È uno dei problemi più insidiosi, perché può diffondersi rapidamente attraverso superfici, utensili, ambienti e movimenti del personale.
            ''',
            'aree_critiche': ['cagliata', 'stagionatura', 'magazzino'],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.SMOKE_48_BLUE_SVG}
            ''',
            'title': f'''
Odori e qualità dell'aria
            ''',
            'description': f'''
La qualità dell'aria influisce sia sul prodotto che sul comfort degli operatori e può indicare la presenza di batteri, muffe o VOC.
            ''',
            'aree_critiche': ['stagionatura', 'linee di confezionamento'],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.LAYERS_48_BLUE_SVG}
            ''',
            'title': f'''
Biofilm e residui organici
            ''',
            'description': f'''
I biofilm sono tra i problemi più difficili da eliminare e richiedono protocolli specifici e verifiche regolari, poiché resistono ai normali detergenti.
            ''',
            'aree_critiche': ['tubazioni', 'vasche', 'superfici di contatto'],
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in data:
        aree_critiche = '\n'.join([f'<li style="margin-bottom: 0.5rem;">{x.capitalize()}</li>' for x in item['aree_critiche']])
        cards.append(f'''
            <div>
                <div style="display: inline-block; margin-bottom: 2rem; border: 1px solid #f2f2f2; border-radius: 2rem; padding: 2rem;">
                    { item['icon'] }
                </div>
                <h3 style="color: #1f1f1f; font-size: 1.5rem; line-height: 1.25; font-weight: bold; margin-bottom: 1rem;">
                    { item['title'] }
                </h3> 
                <p style="color: #555555; margin-bottom: 2rem;">
                    { item['description'] }                    
                </p>
                <p style="color: #555555; margin-bottom: 0.675rem; font-size: 0.675rem;">
                    AREE CRITICHE
                </p>
                <ul style="list-style-type: none;">
                    {aree_critiche}
                </ul>
            </div>
        ''')
    cards = ''.join(cards)
    html_problemi = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            <div style="margin-bottom: 5rem;">
                <h2 style="color: #1f1f1f; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
                    Problemi
                </h2>
            </div>
            <div class="grid-3" style="column-gap: 8rem; row-gap: 3rem; margin-bottom: 0;">
                {cards}
            </div>
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
                {html_hero}
                {html_aree}
                {html_problemi}
                {cta()}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    try: os.makedirs(f'{g.website_folderpath}/settori')
    except: pass
    try: os.makedirs(f'{g.website_folderpath}/settori/alimentare')
    except: pass
    html_filepath = f'{g.website_folderpath}/settori/{page_slug}.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)

def settori_logistico_gen():
    data = settori_data.data[1]
    page_slug = data['page_slug']
    ########################################
    # hero
    ########################################
    html_hero = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_hero_py};">
            <div style="display: flex; justify-content: space-between; center;">
                <div style="flex: 2;">
                    <h1 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
Sanificazione ad ozono per logistica e magazzini
                    </h1>
                    <p style="color: #1f1f1f;">                        
Ambienti di stoccaggio, mezzi di trasporto e aree di transito sicure, igienizzate e prive di odori, con protocolli certificati e senza residui chimici.
                    </p>
                </div>
                {hero_button}
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # problemi
    ########################################
    problemi_data = [
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M600-90q-12 0-21-9t-9-21v-41q-28-3-53.02-12.91Q491.97-183.82 470-201l-39 39q-9.07 8.25-21.53 8.62Q397-153 388-162.05q-9-9.06-9-21.5 0-12.45 9-21.45l40-39q-4.67-6.88-9.33-14.44Q414-266 410-274l-31-62-51 51q-9.27 8.25-21.64 8.62Q294-276 285-285t-9-21q0-12 9-21l51-52-62-31q-7-4-13.5-7.5T248-426l-35 35q-9.07 8.25-21.53 8.62Q179-382 170-391q-9-9-9-21t9-21l34-34q-17-22-28.5-48T161-570h-41q-12 0-21-9t-9-21.5q0-12.5 9-21t21-8.5h43.2q4.8-24 14.3-46t23.5-41l-34-34q-9-9-9-21t9-21q9-9 21-9t21 9l34 34q19-14 41-23.5t46-14.3V-840q0-12.75 9-21.38 9-8.62 21.5-8.62t21 8.62q8.5 8.63 8.5 21.38v41q29 3 55.01 14.53Q471.02-772.94 494-755l34-34q9.07-9 21.53-9 12.47 0 21.47 9 9 9 9 21t-9 21l-36 36q4 6 7.93 11.85 3.93 5.84 7.07 13.15l30 60 48-49q9.07-9 21.53-9 12.47 0 21.47 9.05 9 9.06 9 21.5 0 12.45-9 21.45l-50 49 65 33 16 10 16 10 39-39q9-9 21-9t21 9.05q9 9.06 9 21.5 0 12.45-9 21.45l-39 38q16 21 26 46t13 52h41q12.75 0 21.38 8.62Q870-372.75 870-360q0 12-8.62 21-8.63 9-21.38 9h-43.2q-4.8 24-13.8 46t-23 41l32 32q9 9.07 9 21.53 0 12.47-9.05 21.47-9.06 8.25-21.5 8.62Q758-159 749-168l-32-33q-19 14-41 23.5t-46 14.3v43.2q0 12-8.62 21-8.63 9-21.38 9Zm-6-130q69 0 112-51.5T738-389q-5.87-35-26.44-63Q691-480 659-496l-66-34q-19.93-10.53-35.97-26.77Q541-573 530-593l-34-66q-19-38-53.69-59.5Q407.63-740 366-740q-69 0-112 51.5T222-571q5.88 35 26.44 63Q269-480 301-464l66 33q20.32 10.78 36.66 27.39Q420-387 431-367l33 66q19 38 53.69 59.5T594-220ZM380-540q25 0 42.5-17.5T440-600q0-25-17.5-42.5T380-660q-25 0-42.5 17.5T320-600q0 25 17.5 42.5T380-540Zm200 250q21 0 35.5-14.5T630-340q0-21-14.5-35.5T580-390q-21 0-35.5 14.5T530-340q0 21 14.5 35.5T580-290ZM480-480Z"/></svg>
            ''',
            'title': f'''
Rischio di contaminazione delle merci e delle superfici
            ''',
            'description': f'''
Pallet, scaffalature e superfici di contatto accumulano microrganismi, polveri e residui organici che possono contaminare le merci, specialmente nel settore alimentare e farmaceutico.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M224.12-161q-49.12 0-83.62-34.42Q106-229.83 106-279H40v-461q0-24 18-42t42-18h579v167h105l136 181v173h-71q0 49.17-34.38 83.58Q780.24-161 731.12-161t-83.62-34.42Q613-229.83 613-279H342q0 49-34.38 83.5t-83.5 34.5Zm-.12-60q24 0 41-17t17-41q0-24-17-41t-41-17q-24 0-41 17t-17 41q0 24 17 41t41 17ZM100-339h22q17-27 43.04-43t58-16q31.96 0 58.46 16.5T325-339h294v-401H100v401Zm631 118q24 0 41-17t17-41q0-24-17-41t-41-17q-24 0-41 17t-17 41q0 24 17 41t41 17Zm-52-204h186L754-573h-75v148ZM360-529Z"/></svg>
            ''',
            'title': f'''
Mezzi di trasporto difficili da sanificare
            ''',
            'description': f'''
Camion, furgoni refrigerati e container richiedono protocolli di igienizzazione rapidi ed efficaci, capaci di eliminare batteri e odori tra un carico e l'altro, senza dover usare detergenti aggressivi.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M140-180h120v-320h440v320h120v-460L480-776 140-640v460Zm-60 60v-560l400-160 400 160v560H640v-320H320v320H80Zm290 0v-60h60v60h-60Zm80-120v-60h60v60h-60Zm80 120v-60h60v60h-60ZM260-500h440-440Z"/></svg>
            ''',
            'title': f'''
Scarsa qualità dell'aria nei magazzini chiusi
            ''',
            'description': f'''
Le particelle sospese, i residui organici e gli odori si accumulano facilmente in ambienti ampi e scarsamente ventilati, creando condizioni insalubri per gli operatori e le merci.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M161-120q-18-8-26-17.5T120-165l678-675q15 5 26.5 16.5T840-796L161-120Zm-41-278v-86l356-356h86L120-398Zm0-320v-62q0-24 18-42t42-18h62L120-718Zm598 598 122-122v62q0 24-18 42t-42 18h-62Zm-320 0 442-442v86L484-120h-86Z"/></svg>
            ''',
            'title': f'''
Ampiezza e complessità degli spazi
            ''',
            'description': f'''
I magazzini industriali hanno volumi elevati, aree di difficile accesso e superfici eterogenee.
Le soluzioni tradizionali richiedono tempo, manodopera e spesso non raggiungono una copertura uniforme.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M592-302 450-444v-196h60v171l124 124-42 43ZM450-730v-90h60v90h-60Zm280 280v-60h90v60h-90ZM450-140v-90h60v90h-60ZM140-450v-60h90v60h-90ZM480.27-80q-82.74 0-155.5-31.5Q252-143 197.5-197.5t-86-127.34Q80-397.68 80-480.5t31.5-155.66Q143-709 197.5-763t127.34-85.5Q397.68-880 480.5-880t155.66 31.5Q709-817 763-763t85.5 127Q880-563 880-480.27q0 82.74-31.5 155.5Q817-252 763-197.68q-54 54.31-127 86Q563-80 480.27-80Zm.23-60Q622-140 721-239.5t99-241Q820-622 721.19-721T480-820q-141 0-240.5 98.81T140-480q0 141 99.5 240.5t241 99.5Zm-.5-340Z"/></svg>
            ''',
            'title': f'''
Necessità di operare senza interrompere le attività
            ''',
            'description': f'''
Le imprese logistiche non possono permettersi lunghi fermi per la sanificazione: servono sistemi rapidi, automatizzati e senza tempi di asciugatura o risciacquo.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in problemi_data:
        cards.append(f'''
            <div>
                <div style="display: inline-block; margin-bottom: 2rem; border: 1px solid #f2f2f2; border-radius: 2rem; padding: 2rem;">
                    { item['icon'] }
                </div>
                <h3 style="color: #1f1f1f; font-size: 1.5rem; line-height: 1.25; font-weight: bold; margin-bottom: 1rem;">
                    { item['title'] }
                </h3> 
                <p style="color: #555555; margin-bottom: 2rem;">
                    { item['description'] }                    
                </p>
            </div>
        ''')
                # <p>
                #     <a style="color: #555555;" href="{ item['link_href'] }">{ item['link_anchor'] }</a>
                # </p>
    cards = ''.join(cards)
    html_problemi = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            <div class="container-md" style="margin-bottom: 5rem;">
                <h2 style="color: #1f1f1f; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
Le criticità igieniche in logistica e magazzini
                </h2>
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
Nel settore logistico, la pulizia e la sicurezza degli ambienti non sono solo un requisito estetico, ma una condizione indispensabile per la salvaguardia della merce, la prevenzione delle contaminazioni e la tutela del personale.
I magazzini, i centri di smistamento e i mezzi di trasporto rappresentano spazi ad alta rotazione, dove il rischio di proliferazione microbica e contaminazione crociata è costante.
                </p>     
            </div>
            <div class="grid-3" style="column-gap: 8rem; row-gap: 3rem;">
                {cards}
            </div>
        </section> 
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # soluzioni
    ########################################
    html_soluzioni = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            <div class="container-md" style="margin-bottom: 5rem;">
                <h2 style="color: #1f1f1f; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
L'ozono: la risposta naturale alle esigenze della logistica moderna
                </h2>
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
L'ozono è un gas naturale con un alto potere ossidante, in grado di eliminare batteri, muffe, virus e odori anche negli spazi più difficili da raggiungere.
Grazie alla sua capacità di diffondersi uniformemente nell'aria, consente di sanificare ambienti di grandi dimensioni e mezzi di trasporto senza l'uso di sostanze chimiche o acqua.
                </p>
            </div>
            <div class="container-md">
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
Piena penetrazione negli spazi complessi
                </h3>
                <p style="color: #1f1f1f; margin-bottom: 3rem;">
I magazzini presentano scaffalature alte, angoli nascosti e volumi estesi che rendono difficile una sanificazione uniforme con i metodi tradizionali. L'ozono, essendo un gas, si diffonde naturalmente in ogni direzione e raggiunge anche le zone meno accessibili, garantendo una copertura completa dell'ambiente senza interventi manuali.
                </p>
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
Perfetto per mezzi di trasporto e container
                </h3>
                <p style="color: #1f1f1f; margin-bottom: 3rem;">
I mezzi di trasporto e i container richiedono cicli di sanificazione frequenti per evitare contaminazioni tra una spedizione e l'altra. L'ozono permette trattamenti rapidi, elimina odori persistenti e neutralizza batteri e muffe, riportando il mezzo a una condizione igienica ottimale senza l'uso di sostanze chimiche.
                </p>
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
Cicli rapidi, senza interrompere la produttività
                </h3>
                <p style="color: #1f1f1f; margin-bottom: 3rem;">
Nel settore logistico la continuità operativa è fondamentale. I trattamenti all'ozono possono essere programmati in orari di pausa o durante la notte e non richiedono tempi di asciugatura o risciacquo. Gli ambienti sono subito disponibili, permettendo di mantenere ritmi di lavoro elevati senza interruzioni.
                </p>
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
Nessun residuo chimico, solo ossigeno
                </h3>
                <p style="color: #1f1f1f; margin-bottom: 3rem;">
L'ozono si riconverte naturalmente in ossigeno dopo il trattamento, lasciando gli ambienti privi di residui e completamente sicuri per merci, operatori e materiali sensibili. Questo rende la tecnologia ideale in contesti dove è necessario evitare composti chimici o sostanze potenzialmente irritanti.
               </p>
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
Soluzione sostenibile e a basso impatto
                </h3>
                <p style="color: #1f1f1f; margin-bottom: 3rem;">
L'ozono non richiede acqua né detergenti e non genera plastica monouso o residui chimici. È una soluzione eco-compatibile che contribuisce a ridurre l'impatto ambientale delle operazioni di sanificazione, supportando le aziende nella transizione verso modelli logistici più sostenibili.
                </p>
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
Conforme agli standard igienico-sanitari europei
                </h3>
                <p style="color: #1f1f1f;">
I trattamenti ad ozono aiutano a rispettare gli standard igienici richiesti nelle strutture logistiche e nei mezzi di trasporto. La tecnologia è riconosciuta come metodo efficace per il controllo microbiologico quando utilizzata correttamente, facilitando la compliance con le normative europee e con le linee guida sulla sicurezza nei luoghi di lavoro.
                </p>
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # servizi
    ########################################
    servizi_data = [
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M140-180h120v-320h440v320h120v-460L480-776 140-640v460Zm-60 60v-560l400-160 400 160v560H640v-320H320v320H80Zm290 0v-60h60v60h-60Zm80-120v-60h60v60h-60Zm80 120v-60h60v60h-60ZM260-500h440-440Z"/></svg>
            ''',
            'title': f'''
Sanificazione ambienti di magazzino
            ''',
            'description': f'''
Eliminiamo batteri, muffe, virus e odori da scaffalature, corsie, baie di carico, zone picking e depositi refrigerati.
L'ozono garantisce una copertura uniforme anche in volumi ampi e difficili da raggiungere, assicurando standard di igiene costanti in ogni area operativa.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M743-631q-26 26-58 38.5T619-580q-34 0-66-12.5T495-631l-75-75q-17-17-37.5-25t-42.5-8q-22 0-42.5 8T260-706l-68 68-43-43 68-68q26-26 58-38.5t65-12.5q33 0 64.5 12.5T462-749l75 75q17 17 37.5 25.5T618-640q23 0 44-8.5t38-25.5l68-68 43 43-68 68Zm0 210q-26 26-58 38.5T619-370q-34 0-66-12.5T495-421l-75-75q-17-17-37.5-25t-42.5-8q-22 0-42.5 8T260-496l-68 68-43-42 68-69q26-26 58-38.5t65-12.5q33 0 64.5 12.5T462-539l75 75q17 17 38 25.5t44 8.5q23 0 43.5-8.5T700-464l68-68 43 43-68 68Zm-1 210q-26 26-57.5 38.5T619-160q-34 0-66-12.5T495-211l-76-75q-17-17-37.5-25t-42.5-8q-22 0-42.5 8T259-286l-68 68-42-42 68-69q26-26 57.5-38.5T339-380q33 0 65 12.5t58 38.5l75 75q17 17 38 25.5t44 8.5q23 0 43.5-8.5T700-254l68-68 42 43-68 68Z"/></svg>
            ''',
            'title': f'''
Trattamento aria e condotte di ventilazione
            ''',
            'description': f'''
L'aria nei magazzini tende a stagnare, accumulando aerosol, particelle organiche e odori.
I nostri sistemi permettono di sanificare l'intero volume d'aria e di trattare le condotte HVAC, prevenendo la proliferazione di contaminanti e migliorando la salute degli operatori.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M224.12-161q-49.12 0-83.62-34.42Q106-229.83 106-279H40v-461q0-24 18-42t42-18h579v167h105l136 181v173h-71q0 49.17-34.38 83.58Q780.24-161 731.12-161t-83.62-34.42Q613-229.83 613-279H342q0 49-34.38 83.5t-83.5 34.5Zm-.12-60q24 0 41-17t17-41q0-24-17-41t-41-17q-24 0-41 17t-17 41q0 24 17 41t41 17ZM100-339h22q17-27 43.04-43t58-16q31.96 0 58.46 16.5T325-339h294v-401H100v401Zm631 118q24 0 41-17t17-41q0-24-17-41t-41-17q-24 0-41 17t-17 41q0 24 17 41t41 17Zm-52-204h186L754-573h-75v148ZM360-529Z"/></svg>
            ''',
            'title': f'''
Sanificazione mezzi di trasporto e container
            ''',
            'description': f'''
Offriamo cicli rapidi e certificati per camion, furgoni refrigerati, container e van logistici.
L'ozono raggiunge superfici difficili, neutralizza odori persistenti e previene contaminazioni crociate tra un carico e l'altro.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M80-200v-100h610v100H80Zm655 0v-100h50v100h-50Zm95 0v-100h50v100h-50Zm-95-145v-56q0-42-24.5-66T651-491h-71q-54 0-90.5-41.5T453-628q0-54 36.5-90.5T580-755v50q-35 0-56 21t-21 56q0 35 21 61t56 26h71q54 0 94 37t40 91v68h-50Zm95 0v-100q0-75-50-123t-125-48v-50q34 0 55.5-24t21.5-58q0-34-21.5-58T655-830v-50q54 0 90.5 39t36.5 93q0 33-12.5 57T737-650q58 20 100.5 75T880-445v100h-50Z"/></svg>
            ''',
            'title': f'''
Deodorizzazione e abbattimento odori
            ''',
            'description': f'''
Gli odori forti o persistenti derivanti da merci, rifiuti organici o attività operative sono un problema comune nei centri logistici.
L'ozono ossida le molecole odorose alla radice, lasciando ambienti neutri, sani e professionali.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M80-570v-170q0-24 18-42t42-18h680q24 0 42 18t18 42v170h-60v-170H140v170H80Zm60 410q-24 0-42-18t-18-42v-170h60v170h680v-170h60v170q0 24-18 42t-42 18H140Zm259.81-130q8.19 0 15.79-4t11.4-12l133-266 53 106q3.75 8 11.25 12t15.75 4h240v-60H659l-72-143q-3.72-8.25-11.17-11.63-7.45-3.37-15.64-3.37-8.19 0-15.79 3.37-7.6 3.38-11.4 11.63L400-388l-53-106q-3.75-8-11.25-12T320-510H80v60h221l72 144q3.72 8 11.17 12 7.45 4 15.64 4ZM480-480Z"/></svg>
            ''',
            'title': f'''
Monitoraggio microbiologico post-trattamento
            ''',
            'description': f'''
Ogni intervento può essere accompagnato da test di verifica che misurano la carica microbica su superfici e nell'aria.
Offriamo report certificati, utili per audit interni, controlli qualità e conformità agli standard di sicurezza.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
<svg xmlns="http://www.w3.org/2000/svg" height="48px" viewBox="0 -960 960 960" width="48px" fill="#327CFA"><path d="M592-302 450-444v-196h60v171l124 124-42 43ZM450-730v-90h60v90h-60Zm280 280v-60h90v60h-90ZM450-140v-90h60v90h-60ZM140-450v-60h90v60h-90ZM480.27-80q-82.74 0-155.5-31.5Q252-143 197.5-197.5t-86-127.34Q80-397.68 80-480.5t31.5-155.66Q143-709 197.5-763t127.34-85.5Q397.68-880 480.5-880t155.66 31.5Q709-817 763-763t85.5 127Q880-563 880-480.27q0 82.74-31.5 155.5Q817-252 763-197.68q-54 54.31-127 86Q563-80 480.27-80Zm.23-60Q622-140 721-239.5t99-241Q820-622 721.19-721T480-820q-141 0-240.5 98.81T140-480q0 141 99.5 240.5t241 99.5Zm-.5-340Z"/></svg>
            ''',
            'title': f'''
Programmi periodici per continuità operativa
            ''',
            'description': f'''
Un servizio opzionale ma molto apprezzato nel settore.
Stabiliamo piani programmati (settimanali, mensili o stagionali) per garantire igiene costante, ridurre i fermi e mantenere elevata la qualità operativa nel tempo.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in servizi_data:
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
            </div>
        ''')
    cards = ''.join(cards)
    html_servizi = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            <div class="container-md" style="margin-bottom: 5rem;">
                <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
Servizi di sanificazione per logistica e magazzini
                </h2>
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
La logistica richiede protocolli rapidi, affidabili e compatibili con l'operatività continua.
Per questo abbiamo sviluppato soluzioni specifiche per ambienti di stoccaggio, aree di transito, flotte di trasporto e container, garantendo una sanificazione profonda e l'eliminazione di odori e agenti contaminanti senza interrompere i flussi di lavoro.
                </p>       
            </div>
            <div class="grid-3" style="column-gap: 5rem; row-gap: 3rem;">
                {cards}
            </div>
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
                {html_hero}
                {html_problemi}
                {html_soluzioni}
                {html_servizi}
                {cta()}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    try: os.makedirs(f'{g.website_folderpath}/settori')
    except: pass
    html_filepath = f'{g.website_folderpath}/settori/{page_slug}.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)

def settori_horeca_gen():
    data = settori_data.data[2]
    page_slug = data['page_slug']
    ########################################
    # hero
    ########################################
    html_hero = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_hero_py};">
            <div style="display: flex; justify-content: space-between; center;">
                <div style="flex: 2;">
                    <h1 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
Sanificazione ad ozono per il settore Ho.Re.Ca.
                    </h1>
                    <p style="color: #1f1f1f;">                        
Nel settore Ho.Re.Ca., igiene e qualità dell'aria non sono solo standard da rispettare, ma un elemento di fiducia immediata per clienti e ospiti. L'ozono offre un metodo sicuro, veloce e senza residui per eliminare batteri, virus, odori e allergeni in camere, cucine, sale ristorante e aree comuni.
                    </p>
                </div>
                {hero_button}
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # problemi
    ########################################
    problemi_data = [
        {
            'icon': f'''
{g.BACTERIA_48_BLUE_SVG}
            ''',
            'title': f'''
Eliminazione di batteri, virus e allergeni
            ''',
            'description': f'''
Camere, bagni, cucine e tessili sono soggetti a una costante esposizione a microrganismi patogeni e allergeni. Le pulizie tradizionali non sempre riescono a raggiungere superfici, tessuti e punti nascosti.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.SMOKE_48_BLUE_SVG}
            ''',
            'title': f'''
Odori persistenti in camere e ambienti chiusi
            ''',
            'description': f'''
Fumo, cibo, muffe, prodotti chimici e permanenza prolungata degli ospiti possono generare odori difficili da neutralizzare. I deodoranti coprono, ma non eliminano la fonte.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.GAVEL_48_BLUE_SVG}
            ''',
            'title': f'''
Normative stringenti su cucine e aree ristoro
            ''',
            'description': f'''
Il personale è tenuto a rispettare protocolli HACCP, tempi rapidi e standard di igiene elevati. Superfici, utensili, celle frigo e impianti di aerazione richiedono trattamenti costanti e controllabili.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.CLOCK_48_BLUE_SVG}
            ''',
            'title': f'''
Riduzione dei tempi di sanificazione tra un ospite e l'altro
            ''',
            'description': f'''
Il tempo è critico: camere, aree comuni e cucine devono essere pronte in pochi minuti, senza rischi residui o lunghi tempi di asciugatura.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.SURFACE_48_BLUE_SVG}
            ''',
            'title': f'''
Sanificazione efficace di tessili e superfici delicate
            ''',
            'description': f'''
Materassi, tende, divani, moquette e altre superfici assorbenti possono trattenere odori e cariche batteriche, rendendo difficile una pulizia profonda senza interventi invasivi.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.CHEMICAL_48_BLUE_SVG}
            ''',
            'title': f'''
Sostenibilità e riduzione dei prodotti chimici
            ''',
            'description': f'''
Gli ospiti sono sempre più sensibili all'impatto ambientale. Meno prodotti chimici significa meno residui, meno allergeni e un ambiente più naturale.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in problemi_data:
        cards.append(f'''
            <div>
                <div style="display: inline-block; margin-bottom: 2rem; border: 1px solid #f2f2f2; border-radius: 2rem; padding: 2rem;">
                    { item['icon'] }
                </div>
                <h3 style="color: #1f1f1f; font-size: 1.5rem; line-height: 1.25; font-weight: bold; margin-bottom: 1rem;">
                    { item['title'] }
                </h3> 
                <p style="color: #555555; margin-bottom: 2rem;">
                    { item['description'] }                    
                </p>
            </div>
        ''')
                # <p>
                #     <a style="color: #555555;" href="{ item['link_href'] }">{ item['link_anchor'] }</a>
                # </p>
    cards = ''.join(cards)
    html_problemi = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            <div class="container-md" style="margin-bottom: 5rem;">
                <h2 style="color: #1f1f1f; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
Le sfide igieniche del settore Ho.Re.Ca.
                </h2>
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
Nell'ospitalità la percezione dell'igiene è immediata: un odore sgradevole, una camera non perfettamente sanificata o un ambiente poco salubre possono compromettere recensioni, reputazione e ritorno dei clienti.
A questo si aggiungono normative sanitarie stringenti, rotazione elevata degli ospiti e la necessità di ridurre i tempi di fermo tra una prenotazione e l'altra.
                </p>     
            </div>
            <div class="grid-3" style="column-gap: 8rem; row-gap: 3rem;">
                {cards}
            </div>
        </section> 
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # soluzioni
    ########################################
    html_soluzioni = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            <div class="container-md" style="margin-bottom: 5rem;">
                <h2 style="color: #1f1f1f; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
Come l'ozono risolve le criticità del settore Ho.Re.Ca.
                </h2>
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
L'ozono è un ossidante naturale ad altissima efficacia, in grado di penetrare nei punti difficili da raggiungere, trattare superfici complesse, tessuti e volumi d'aria senza lasciare residui. Agisce in profondità eliminando batteri, virus, muffe, lieviti, allergeni e odori organici direttamente alla radice, senza l'uso di prodotti chimici o deodoranti coprenti.
               </p>
            </div>
            <div class="container-md">
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
Eliminazione profonda di batteri, virus e allergeni
                </h3>
                <p style="color: #1f1f1f; margin-bottom: 3rem;">
L'ozono agisce direttamente sulle membrane dei microrganismi, inattivando batteri, virus, funghi e allergeni presenti sulle superfici, nei tessuti e nell'aria. Grazie alla sua natura gassosa, raggiunge fessure, angoli nascosti e punti difficili da trattare con i metodi tradizionali, garantendo un livello di igiene uniforme e superiore in camere, cucine, bagni e spazi comuni.
                </p>
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
Trattamenti rapidi, senza risciacquo
                </h3>
                <p style="color: #1f1f1f; margin-bottom: 3rem;">
I cicli di trattamento all'ozono durano pochi minuti e non richiedono risciacquo, asciugatura o tempi di attesa prolungati. Una volta completato il protocollo, l'ambiente è immediatamente pronto per essere riutilizzato, rendendo la tecnologia ideale per strutture con elevata rotazione delle camere e tempi stretti nella gestione operativa.
                </p>
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
Nessun residuo chimico
                </h3>
                <p style="color: #1f1f1f; margin-bottom: 3rem;">
L'ozono non lascia tracce o sottoprodotti e riduce drasticamente la necessità di detergenti aggressivi. Questo significa ambienti più sicuri per ospiti e personale, minore rischio di allergie o irritazioni e totale assenza di contaminazioni che potrebbero alterare odori o sapori nelle aree cucina. Al termine del ciclo, l'ozono si riconverte in semplice ossigeno.
                </p>
                <h3 style="color: #1f1f1f; font-size: 1.25rem; line-height: 1; font-weight: bold; margin-bottom: 1rem;">
Applicabile a superfici, aria e tessuti
                </h3>
                <p style="color: #1f1f1f;">
L'ozono è una delle poche tecnologie in grado di sanificare efficacemente anche materiali porosi e oggetti difficili da trattare, come materassi, tende, moquette, cuscini e imbottiti. Il processo è non invasivo e non danneggia i materiali, offrendo una sanificazione profonda impossibile da ottenere con i metodi tradizionali e migliorando la qualità percepita degli ambienti Ho.Re.Ca.
                </p>
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # servizi
    ########################################
    servizi_data = [
        {
            'icon': f'''
{g.BEDROOM_48_BLUE_SVG}
            ''',
            'title': f'''
Sanificazione camere e spazi di accoglienza
            ''',
            'description': f'''
Ideale per camere d'hotel, hall, reception e aree comuni. L'ozono elimina rapidamente batteri, virus e odori da superfici e volumi d'aria, garantendo un livello di igiene superiore rispetto alla sola pulizia manuale. I cicli sono rapidi, non lasciano residui chimici e permettono una gestione più efficiente della rotazione camere.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.SMOKE_48_BLUE_SVG}
            ''',
            'title': f'''
Deodorizzazione professionale per hotel e ristoranti
            ''',
            'description': f'''
Pensata per camere, sale ristorante, cucine aperte e zone a rischio odori. L'ozono neutralizza definitivamente fumo, odori alimentari, muffe e composti organici volatili, intervenendo direttamente sulle molecole responsabili del cattivo odore. Il risultato è un ambiente più accogliente e una percezione immediata di freschezza.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.KITCHEN_48_BLUE_SVG}
            ''',
            'title': f'''
Sanificazione cucine e aree HACCP
            ''',
            'description': f'''
Un protocollo studiato per cucine professionali, dispense e aree di preparazione. I trattamenti a ozono riducono la carica microbica su superfici e attrezzature, migliorano l'igiene delle linee di lavoro e supportano il rispetto delle procedure HACCP, facilitando la conformità ai controlli ASL.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.HVAC_48_BLUE_SVG}
            ''',
            'title': f'''
Trattamento aria e impianti di ventilazione
            ''',
            'description': f'''
Adatto a materassi, tende, moquette, divani e superfici sensibili ai liquidi. L'ozono penetra nelle fibre eliminando odori, acari e batteri senza rischiare di danneggiare i materiali. È un trattamento sicuro, asciutto e non invasivo, ideale per mantenere i tessili freschi e igienizzati più a lungo.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.LOOP_48_BLUE_SVG}
            ''',
            'title': f'''
Servizio programmato per strutture ricettive
            ''',
            'description': f'''
Un piano ricorrente studiato sulle esigenze della struttura, con interventi programmati e continuità di igiene garantita. Riduce i costi nel lungo termine, assicura un livello costante di sanificazione e fornisce report periodici utili per audit e verifiche interne.
           ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in servizi_data:
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
            </div>
        ''')
    cards = ''.join(cards)
    html_servizi = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            <div class="container-md" style="margin-bottom: 5rem;">
                <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
Servizi per hotel, ristoranti e strutture ricettive
                </h2>
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
Ogni ambiente dell'ospitalità richiede standard igienici elevati e risultati immediati. I nostri servizi sono pensati per rispondere alle esigenze operative del settore Ho.Re.Ca.: interventi rapidi, senza residui chimici e completamente sicuri per ospiti, personale e superfici delicate. Abbiamo sviluppato protocolli integrati che coprono ogni fase dell'attività — dalla cucina alle camere, dalla reception alle aree comuni — garantendo ambienti sempre freschi, igienizzati e perfettamente conformi alle normative.
                </p>       
            </div>
            <div class="grid-3" style="column-gap: 5rem; row-gap: 3rem;">
                {cards}
            </div>
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
                {html_hero}
                {html_problemi}
                {html_soluzioni}
                {html_servizi}
                {cta()}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    try: os.makedirs(f'{g.website_folderpath}/settori')
    except: pass
    html_filepath = f'{g.website_folderpath}/settori/{page_slug}.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)

def settori_farmaceutico_gen():
    data = settori_data.data[3]
    page_slug = data['page_slug']
    ########################################
    # hero
    ########################################
    html_hero = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_hero_py};">
            <div style="display: flex; justify-content: space-between; center;">
                <div style="flex: 2;">
                    <h1 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
Sanificazione ad ozono per l'industria farmaceutica e cosmetica
                    </h1>
                    <p style="color: #1f1f1f;">                        
Soluzioni certificate per laboratori, clean room e linee di confezionamento: sicurezza, conformità e qualità garantite.
                    </p>
                </div>
                {hero_button}
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # problemi
    ########################################
    problemi_data = [
        {
            'icon': f'''
{g.BACTERIA_48_BLUE_SVG}
            ''',
            'title': f'''
Contaminazione microbiologica in ambienti sterili
            ''',
            'description': f'''
Clean room e laboratori devono mantenere valori estremamente bassi di carica microbica. Anche una minima variazione può invalidare interi lotti, test o campionature, con impatti economici significativi.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.CONTAMINATION_48_BLUE_SVG}
            ''',
            'title': f'''
Rischio di contaminazione incrociata (cross-contamination)
            ''',
            'description': f'''
In ambienti dove si manipolano principi attivi, composti sensibili o formulazioni cosmetiche, la contaminazione incrociata è un rischio critico. Si richiedono sistemi di igienizzazione che non introducano particelle, residui o sottoprodotti.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.SURFACE_48_BLUE_SVG}
            ''',
            'title': f'''
Superfici complesse e strumenti delicati
            ''',
            'description': f'''
Strumentazioni di laboratorio, cappe chimiche, aree di pesatura e macchine di confezionamento presentano superfici difficili da raggiungere. I metodi chimici spesso richiedono lunghi tempi di attesa o rischiano interazioni indesiderate con materiali sensibili.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.GAVEL_48_BLUE_SVG}
            ''',
            'title': f'''
Conformità a standard GMP, FDA e ISO 14644
            ''',
            'description': f'''
Le normative per ambienti controllati sono estremamente stringenti, come classificazione particellare, controllo microbico aerodisperso, validazioni periodiche delle procedure. Qualsiasi deviazione può portare a non conformità, sospensioni o perdita di certificazioni.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.CHEMICAL_48_BLUE_SVG}
            ''',
            'title': f'''
Limiti dei detergenti chimici tradizionali
            ''',
            'description': f'''
Molti sanificanti impiegati in ambito industriale possono lasciare residui, interagire con i materiali o alterare l'ambiente controllato. Occorre un sistema efficace e verificabile che non introduca contaminanti aggiuntivi.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.CLOCK_48_BLUE_SVG}
            ''',
            'title': f'''
Riduzione dei tempi di fermo e continuità operativa
            ''',
            'description': f'''
Clean room e linee di confezionamento devono garantire alta produttività con il minimo downtime. Servono protocolli rapidi, ripetibili e con tempi di rientro brevi per mantenere gli standard di efficienza.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in problemi_data:
        cards.append(f'''
            <div>
                <div style="display: inline-block; margin-bottom: 2rem; border: 1px solid #f2f2f2; border-radius: 2rem; padding: 2rem;">
                    { item['icon'] }
                </div>
                <h3 style="color: #1f1f1f; font-size: 1.5rem; line-height: 1.25; font-weight: bold; margin-bottom: 1rem;">
                    { item['title'] }
                </h3> 
                <p style="color: #555555; margin-bottom: 2rem;">
                    { item['description'] }                    
                </p>
            </div>
        ''')
                # <p>
                #     <a style="color: #555555;" href="{ item['link_href'] }">{ item['link_anchor'] }</a>
                # </p>
    cards = ''.join(cards)
    html_problemi = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            <div class="container-md" style="margin-bottom: 5rem;">
                <h2 style="color: #1f1f1f; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
Le sfide igieniche dell'industria farmaceutica e cosmetica                </h2>
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
In laboratori, clean room e ambienti di confezionamento, anche piccole contaminazioni possono compromettere la qualità dei prodotti e la sicurezza dei consumatori. Normative severe e protocolli rigorosi richiedono trattamenti mirati e tracciabili.
                </p>     
            </div>
            <div class="grid-3" style="column-gap: 8rem; row-gap: 3rem;">
                {cards}
            </div>
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
                {html_hero}
                {html_problemi}
                {cta()}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    try: os.makedirs(f'{g.website_folderpath}/settori')
    except: pass
    html_filepath = f'{g.website_folderpath}/settori/{page_slug}.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)

def settori_agroalimentare_gen():
    data = settori_data.data[4]
    page_slug = data['page_slug']
    ########################################
    # hero
    ########################################
    html_hero = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_hero_py};">
            <div style="display: flex; justify-content: space-between; center;">
                <div style="flex: 2;">
                    <h1 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
Sanificazione ad ozono per l'industria agroalimentare
                    </h1>
                    <p style="color: #1f1f1f;">                        
Soluzioni certificate per garantire igiene, sicurezza alimentare e conformità HACCP in stabilimenti produttivi, magazzini e cucine industriali.
                    </p>
                </div>
                {hero_button}
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # problemi
    ########################################
    problemi_data = [
        {
            'icon': f'''
{g.BACTERIA_48_BLUE_SVG}
            ''',
            'title': f'''
Rischio contaminazioni da batteri e muffe su macchinari e superfici
            ''',
            'description': f'''
Le superfici di lavorazione, i nastri trasportatori e le linee di confezionamento possono accumulare microrganismi nocivi se non sanificate correttamente. Batteri come Listeria monocytogenes o muffe invisibili possono proliferare rapidamente in ambienti umidi o poco ventilati. Controllare queste contaminazioni richiede tecniche precise e protocolli costanti, altrimenti il rischio di non conformità HACCP aumenta notevolmente.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.FRIDGE_48_BLUE_SVG}
            ''',
            'title': f'''
Difficoltà di sanificazione in celle frigorifere e impianti complessi
            ''',
            'description': f'''
Le celle frigorifere, essenziali per la conservazione dei prodotti, rappresentano spazi critici poiché basse temperature e umidità favoriscono la proliferazione di microrganismi. Alcuni impianti industriali presentano geometrie complesse e punti difficili da raggiungere, rendendo inefficaci i metodi tradizionali di pulizia. La sanificazione deve essere profonda, uniforme e non interferire con le operazioni quotidiane, senza generare residui chimici che compromettano la sicurezza degli alimenti.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.GAVEL_48_BLUE_SVG}
            ''',
            'title': f'''
Conformità rigorosa alle normative HACCP e ISO 22000
            ''',
            'description': f'''
Ogni stabilimento agroalimentare è soggetto a controlli ispettivi e deve rispettare norme severe sulla sicurezza alimentare. Errori nella sanificazione o mancanza di tracciabilità nei protocolli possono comportare sanzioni, richiami dei prodotti o danni reputazionali. Garantire conformità significa implementare interventi certificati, documentati e verificabili con report dettagliati.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.SMOKE_48_BLUE_SVG}
            ''',
            'title': f'''
Necessità di eliminare odori senza introdurre residui chimici
            ''',
            'description': f'''
L'odore è un indicatore spesso sottovalutato della presenza di microrganismi o contaminazioni. Molti prodotti chimici per la pulizia lasciano residui che possono contaminare gli alimenti o alterarne il gusto e l'aroma. La sfida è trovare soluzioni sicure, efficaci e compatibili con le normative, in grado di abbattere odori e microrganismi senza compromettere la qualità dei prodotti.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in problemi_data:
        cards.append(f'''
            <div>
                <div style="display: inline-block; margin-bottom: 2rem; border: 1px solid #f2f2f2; border-radius: 2rem; padding: 2rem;">
                    { item['icon'] }
                </div>
                <h3 style="color: #1f1f1f; font-size: 1.5rem; line-height: 1.25; font-weight: bold; margin-bottom: 1rem;">
                    { item['title'] }
                </h3> 
                <p style="color: #555555; margin-bottom: 2rem;">
                    { item['description'] }                    
                </p>
            </div>
        ''')
                # <p>
                #     <a style="color: #555555;" href="{ item['link_href'] }">{ item['link_anchor'] }</a>
                # </p>
    cards = ''.join(cards)
    html_problemi = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            <div class="container-md" style="margin-bottom: 5rem;">
                <h2 style="color: #1f1f1f; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
Le sfide igieniche dell'industria agroalimentare
                </h2>
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
La produzione agroalimentare richiede standard igienici elevatissimi. Ogni fase della lavorazione, dalla ricezione delle materie prime fino allo stoccaggio dei prodotti finiti, può rappresentare un punto critico per la sicurezza alimentare. Contaminazioni microbiche, residui organici e odori persistenti non solo compromettono la qualità dei prodotti, ma possono avere impatti legali e reputazionali significativi. Per questo, ogni intervento di sanificazione deve essere preciso, mirato e conforme alle normative vigenti.
                </p>     
            </div>
            <div class="grid-3" style="column-gap: 8rem; row-gap: 3rem;">
                {cards}
            </div>
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
                {html_hero}
                {html_problemi}
                {cta()}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    try: os.makedirs(f'{g.website_folderpath}/settori')
    except: pass
    html_filepath = f'{g.website_folderpath}/settori/{page_slug}.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)

def settori_sportivo_gen():
    data = settori_data.data[5]
    page_slug = data['page_slug']
    ########################################
    # hero
    ########################################
    html_hero = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_hero_py};">
            <div style="display: flex; justify-content: space-between; center;">
                <div style="flex: 2;">
                    <h1 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
Sanificazione ad ozono per strutture sportive
                    </h1>
                    <p style="color: #1f1f1f;">                        
Soluzioni sicure e certificate per palestre, centri fitness, piscine e impianti sportivi, per garantire ambienti igienizzati e conformi alle normative sanitarie.
                    </p>
                </div>
                {hero_button}
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # problemi
    ########################################
    problemi_data = [
        {
            'icon': f'''
{g.SURFACE_48_BLUE_SVG}
            ''',
            'title': f'''
Superfici di attrezzi e pavimenti ad alto rischio di contaminazione
            ''',
            'description': f'''
Pesi, tapis roulant, cyclette, panche e tappeti sono a contatto diretto con mani e piedi degli utenti, diventando veicoli ideali per batteri e virus. Anche i pavimenti delle sale corsi e degli spogliatoi accumulano residui di sudore, prodotti cosmetici e polveri, aumentando il rischio microbiologico. La sanificazione tradizionale manuale spesso non basta o richiede tempi e risorse significative.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.HVAC_48_BLUE_SVG}
            ''',
            'title': f'''
Aria chiusa e affollamento di ambienti indoor
            ''',
            'description': f'''
Sale fitness, palestre e piscine al chiuso hanno una ventilazione spesso limitata. L'alta densità di persone negli spazi indoor aumenta il rischio di trasmissione aerea di virus e batteri. I sistemi HVAC non sempre garantiscono un ricambio d'aria ottimale, rendendo necessario un trattamento dell'aria mirato e costante.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.CLOCK_48_BLUE_SVG}
            ''',
            'title': f'''
Necessità di sanificazione rapida tra turni di utilizzo
            ''',
            'description': f'''
Le strutture sportive operano con orari continuativi e frequenti cambi di utenti. Interventi di pulizia lunghi possono ridurre la disponibilità della struttura e interrompere i programmi dei corsi. Serve quindi un sistema di sanificazione efficace e rapido, che non interferisca con l'attività quotidiana.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.SMOKE_48_BLUE_SVG}
            ''',
            'title': f'''
Odori persistenti da spogliatoi e piscine
            ''',
            'description': f'''
Sudore, cloro, umidità e materiali sintetici possono generare odori sgradevoli difficili da eliminare con pulizie tradizionali. La presenza di cattivi odori influisce sulla percezione della pulizia da parte degli utenti e sul loro grado di soddisfazione. Il trattamento deve garantire un ambiente fresco e igienicamente sicuro.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
        {
            'icon': f'''
{g.GAVEL_48_BLUE_SVG}
            ''',
            'title': f'''
Conformità a normative locali e linee guida sanitarie
            ''',
            'description': f'''
Palestre e centri sportivi devono rispettare regolamenti igienico-sanitari locali, linee guida nazionali e protocolli HACCP dove applicabili. La mancata conformità può comportare sanzioni, chiusure temporanee o danni reputazionali. Le procedure di sanificazione devono essere tracciabili e certificabili, garantendo sicurezza e trasparenza.
            ''',
            'link_href': f'''#''',
            'link_anchor': f'''Maggiori info''',
        },
    ]
    cards = []
    for item in problemi_data:
        cards.append(f'''
            <div>
                <div style="display: inline-block; margin-bottom: 2rem; border: 1px solid #f2f2f2; border-radius: 2rem; padding: 2rem;">
                    { item['icon'] }
                </div>
                <h3 style="color: #1f1f1f; font-size: 1.5rem; line-height: 1.25; font-weight: bold; margin-bottom: 1rem;">
                    { item['title'] }
                </h3> 
                <p style="color: #555555; margin-bottom: 2rem;">
                    { item['description'] }                    
                </p>
            </div>
        ''')
                # <p>
                #     <a style="color: #555555;" href="{ item['link_href'] }">{ item['link_anchor'] }</a>
                # </p>
    cards = ''.join(cards)
    html_problemi = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            <div class="container-md" style="margin-bottom: 5rem;">
                <h2 style="color: #1f1f1f; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
Le sfide igieniche nelle strutture sportive
                </h2>
                <p style="color: #1f1f1f; margin-bottom: 1rem;">    
In palestre, centri fitness e piscine, la concentrazione di persone e il contatto con superfici condivise aumentano il rischio di batteri, virus e cattivi odori. Garantire un'igiene costante è fondamentale per la sicurezza degli utenti e la reputazione della struttura.
                </p>     
            </div>
            <div class="grid-3" style="column-gap: 8rem; row-gap: 3rem;">
                {cards}
            </div>
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
                {html_hero}
                {html_problemi}
                {cta()}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    try: os.makedirs(f'{g.website_folderpath}/settori')
    except: pass
    html_filepath = f'{g.website_folderpath}/settori/{page_slug}.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)

def gen():
    settori_alimentare_gen()
    settori_alimentare_lattiero_caseario_gen()
    settori_logistico_gen()
    settori_horeca_gen()
    settori_farmaceutico_gen()
    settori_agroalimentare_gen()
    settori_sportivo_gen()
    
    ########################################
    # hero
    ########################################
    hero_button = f'''
        <div style="flex: 1; display: flex; justify-content: end; margin-top: 0.25rem;">
            <div style="display: inline-block;">
                <a class="button-default-1" href="/contatti.html">
                    <span>Prenota Consulenza Gratuita</span>
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                </a>
            </div>
        </div>
    '''
    hero = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_hero_py};">
            <div style="display: flex; justify-content: space-between; center;">
                <div style="flex: 2;">
                    <h1 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
                        Soluzioni ad ozono su misura per ogni settore industriale
                    </h1>
                    <p style="color: #1f1f1f;">                        
                        Dal trattamento dell'aria alla sanificazione degli impianti produttivi, le nostre tecnologie si adattano alle esigenze specifiche di ogni settore.
                    </p>
                </div>
                {hero_button}
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # settori
    ########################################
    data = settori_data.data
    cards = []
    for item in data:
        cards.append(f'''
            <div> 
                <img style="margin-bottom: 1rem; border-radius: 1rem; height: 15rem; object-fit: cover;" 
                    src="{ item['image_src'] }
                ">
                <h3 style="color: #222222; font-size: 1.5rem; line-height: 1.25; font-weight: bold; margin-bottom: 1rem;">
                    { item['title'] }
                </h3> 
                <p style="color: #555555; margin-bottom: 2rem;">
                    { item['description'] }                    
                </p>
                <p>
                    <a style="color: #555555;" href="{ item['href'] }">Maggiori info</a>
                </p>
            </div>
        ''')
    cards = ''.join(cards)
    settori_overview = f'''
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;">
            <div style="flex: 2;">
                <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal;">
                    I nostri principali ambiti di applicazione
                </h2>
            </div>
            <div style="flex: 1; display: flex; justify-content: end;">

            </div>
        </div>
        <div class="grid-3" style="column-gap: 3rem; row-gap: 3rem;">
            {cards}
        </div>
    '''

    settori = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_py};">
            {settori_overview}
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
                {settori}
                {cta()}
            </main>
                
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_filepath = f'{g.website_folderpath}/settori.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)
