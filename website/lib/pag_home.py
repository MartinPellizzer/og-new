import os

from lib import g
from lib import sections
from lib import blocks
from lib import components

def gen():
    html_heading = blocks.heading_default_2(
        title = components.h2_default(
            text = f'''A cosa serve la sanificazione con ozono?''',
            align = f'center',
        ),
        paragraph = components.paragraph_default(
            text = f'''L'ozono elimina le contaminazioni biologiche nell'industria alimentare, neutralizzando batteri, virus, muffe, parassiti e odori. Elimina anche le contaminazioni chimiche nell'industria alimentare, riducendo micotossine, pesticidi, fitofarmaci e residui di detergenti.''',
            align = f'center',
        ),
    )
    html_card_1 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'01',
        ),
        title = components.h3_default(
            text = f'Batteri',
        ),
        paragraph = components.paragraph_default(
            text = f'''L’ozono elimina i batteri grazie al suo forte potere ossidante, che distrugge le membrane cellulari e inibisce la loro capacità di riprodursi.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M600-80q-17 0-28.5-11.5T560-120v-43q-23-4-43.5-11.5T478-195l-40 40q-12 11-28.5 11.5T381-155q-12-12-12-28.5t12-28.5l41-41q-3-5-6-10.5t-6-10.5l-27-53-49 49q-12 11-28 11.5T278-278q-12-12-12-28t12-28l49-50-53-26q-5-2-9-4.5t-9-5.5l-36 36q-12 11-28.5 11.5T163-384q-12-12-12-28t12-28l35-35q-14-19-22.5-40.5T163-560h-43q-17 0-28.5-11.5T80-600q0-17 11.5-28.5T120-640h45q5-19 12-36t18-33l-35-35q-12-12-12-28t12-28q12-12 28-12t28 12l35 35q16-11 33-18t36-12v-45q0-17 11.5-28.5T360-880q17 0 28.5 11.5T400-840v43q24 4 45.5 13t40.5 23l35-35q12-12 28.5-12t28.5 12q12 12 12 28t-12 28l-37 37q2 4 4.5 8t4.5 9l25 50 46-46q12-12 28.5-12t28.5 12q12 12 12 28.5T678-625l-48 47 56 28q6 3 12.5 6.5T710-536l40-40q12-12 28-12t28 12q12 12 12 28.5T806-519l-40 39q12 18 19.5 38t11.5 42h43q17 0 28.5 11.5T880-360q0 17-11.5 28.5T840-320h-45q-5 19-12 35.5T765-252l34 34q12 12 12 28.5T799-161q-12 11-28.5 11.5T742-161l-33-34q-16 11-33 18t-36 12v45q0 17-11.5 28.5T600-80Zm-6-160q58 0 95.5-44T718-386q-5-30-22.5-54T650-478l-66-34q-23-12-41.5-30.5T512-584l-34-66q-16-32-46-51t-66-19q-58 0-95.5 44T242-574q5 30 22.5 54t45.5 38l66 34q23 12 41.5 30.5T448-376l34 66q16 32 46 51t66 19ZM380-540q25 0 42.5-17.5T440-600q0-25-17.5-42.5T380-660q-25 0-42.5 17.5T320-600q0 25 17.5 42.5T380-540Zm200 250q21 0 35.5-14.5T630-340q0-21-14.5-35.5T580-390q-21 0-35.5 14.5T530-340q0 21 14.5 35.5T580-290ZM480-480Z"/></svg>
            ''',
        ),
    )
    html_card_2 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'02',
        ),
        title = components.h3_default(
            text = f'Virus',
        ),
        paragraph = components.paragraph_default(
            text = f'''L’ozono inattiva i virus ossidando le proteine del loro rivestimento e il materiale genetico, impedendo loro di infettare altre cellule.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M450-80q-12 0-21-9t-9-21q0-12 9-21t21-9v-62q-42-5-79-20t-67-40l-43 44q9 9 9 21t-9 21q-9 9-21 9t-21-9l-43-42q-9-9-9-21.5t9-21.5q9-9 21-8.5t21 8.5l44-44q-25-31-40-67t-20-78h-62q0 12-9 21t-21 9q-12 0-21-9t-9-21v-60q0-12 9-21t21-9q12 0 21 9t9 21h62q5-42 20.5-78t39.5-67l-44-44q-9 8-21 8.5t-21-8.5q-9-9-9-21.5t9-21.5l42-42q9-9 21.5-9t21.5 9q9 9 9 21.5t-9 21.5l43 43q31-25 67-40t78-20v-62q-12 0-20.5-9t-8.5-21q0-12 9-21t21-9h60q12 0 21 9t9 21q0 12-9 21t-21 9v62q42 5 78 20t67 40l44-44q-9-9-9-21t9-21q9-9 21.5-9t21.5 9l42 43q9 9 9 21t-9 21q-9 9-21.5 9t-21.5-9l-43 43q25 31 40 67.5t20 78.5h62q0-12 9-21t21-9q12 0 21 9t9 21v60q0 12-9 21t-21 9q-12 0-21-9t-9-21h-62q-5 42-20 78.5T698-304l43 43q9-9 21.5-9t21.5 9q9 9 9 21.5t-9 21.5l-42 42q-9 9-21.5 9t-21.5-9q-9-9-8.5-21t8.5-21l-44-44q-31 25-67 40.5T510-201v61q12 0 21 9t9 21q0 12-9 21t-21 9h-60Zm30-200q83 0 141.5-58.5T680-480q0-83-58.5-141.5T480-680q-83 0-141.5 58.5T280-480q0 83 58.5 141.5T480-280Zm-70-40q17 0 28.5-11.5T450-360q0-17-11.5-28.5T410-400q-17 0-28.5 11.5T370-360q0 17 11.5 28.5T410-320Zm140 0q17 0 28.5-11.5T590-360q0-17-11.5-28.5T550-400q-17 0-28.5 11.5T510-360q0 17 11.5 28.5T550-320ZM340-440q17 0 28.5-11.5T380-480q0-17-11.5-28.5T340-520q-17 0-28.5 11.5T300-480q0 17 11.5 28.5T340-440Zm140 0q17 0 28.5-11.5T520-480q0-17-11.5-28.5T480-520q-17 0-28.5 11.5T440-480q0 17 11.5 28.5T480-440Zm140 0q17 0 28.5-11.5T660-480q0-17-11.5-28.5T620-520q-17 0-28.5 11.5T580-480q0 17 11.5 28.5T620-440ZM410-560q17 0 28.5-11.5T450-600q0-17-11.5-28.5T410-640q-17 0-28.5 11.5T370-600q0 17 11.5 28.5T410-560Zm140 0q17 0 28.5-11.5T590-600q0-17-11.5-28.5T550-640q-17 0-28.5 11.5T510-600q0 17 11.5 28.5T550-560Zm-70 80Z"/></svg>
            ''',
        ),
    )
    html_card_3 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'03',
        ),
        title = components.h3_default(
            text = f'Muffe',
        ),
        paragraph = components.paragraph_default(
            text = f'''L’ozono neutralizza le muffe distruggendo le spore fungine presenti nell’aria e sulle superfici, prevenendone la proliferazione.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M200-120v-80h200v-80q-83 0-141.5-58.5T200-480q0-61 33.5-111t90.5-73q8-34 35.5-55t62.5-21l-22-62 38-14-14-36 76-28 12 38 38-14 110 300-38 14 14 38-76 28-12-38-38 14-24-66q-15 14-34.5 21t-39.5 5q-22-2-41-13.5T338-582q-27 16-42.5 43T280-480q0 50 35 85t85 35h320v80H520v80h240v80H200Zm346-458 36-14-68-188-38 14 70 188Zm-126-22q17 0 28.5-11.5T460-640q0-17-11.5-28.5T420-680q-17 0-28.5 11.5T380-640q0 17 11.5 28.5T420-600Zm126 22Zm-126-62Zm0 0Z"/></svg>
            ''',
        ),
    )
    html_card_4 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'04',
        ),
        title = components.h3_default(
            text = f'Parassiti',
        ),
        paragraph = components.paragraph_default(
            text = f'''L’ozono contribuisce a eliminare i parassiti attraverso l’ossidazione delle loro strutture biologiche, interrompendone il ciclo vitale.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M480-120q-64 0-114.5-33T283-240l-95 54-40-69 103-60q-3-11-5-22.5t-4-22.5H120v-80h122q2-12 4-23.5t5-22.5l-103-60 40-69 94 55q8-14 18.5-27.5T322-612q-2-7-2-14v-14q0-24 7-46t19-41l-66-66 56-57 70 68q17-9 35.5-13.5T480-800q20 0 39 5t36 14l69-69 56 57-66 66q12 19 18.5 41t6.5 46v13.5q0 6.5-2 13.5 11 11 21.5 25t18.5 28l95-54 40 69-104 59q3 11 5.5 22.5T718-440h122v80H718q-2 12-4 23.5t-5 22.5l103 60-40 69-95-55q-32 54-82.5 87T480-120Zm-76-546q17-7 36.5-10.5T480-680q20 0 38.5 3t35.5 10q-8-23-28-38t-46-15q-26 0-47 15.5T404-666Zm76 466q73 0 116.5-61T640-400q0-70-40.5-135T480-600q-78 0-119 64.5T320-400q0 78 43.5 139T480-200Zm-40-80v-240h80v240h-80Z"/></svg>
            ''',
        ),
    )
    html_card_5 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'05',
        ),
        title = components.h3_default(
            text = f'Odori',
        ),
        paragraph = components.paragraph_default(
            text = f'''L’ozono elimina gli odori scomponendo chimicamente le molecole organiche volatili responsabili dei cattivi odori, neutralizzandole alla fonte.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M80-200v-120h600v120H80Zm640 0v-120h60v120h-60Zm100 0v-120h60v120h-60ZM720-360v-52q0-39-23-59.5T642-492h-62q-56 0-95-39t-39-95q0-56 39-95t95-39v60q-30 0-52 21t-22 53q0 32 22 53t52 21h62q56 0 97 36t41 90v66h-60Zm100 0v-90q0-66-46-114t-114-48v-60q30 0 52-22t22-52q0-30-22-52t-52-22v-60q56 0 95 39t39 95q0 29-11 52.5T754-650q56 26 91 80t35 120v90h-60Z"/></svg>
            ''',
        ),
    )
    html_card_6 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'06',
        ),
        title = components.h3_default(
            text = f'Pesticidi',
        ),
        paragraph = components.paragraph_default(
            text = f'''L’ozono ossida i residui di pesticidi su frutta, verdura e superfici, riducendoli in composti meno nocivi o completamente innocui.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M200-120q-51 0-72.5-45.5T138-250l222-270v-240h-40q-17 0-28.5-11.5T280-800q0-17 11.5-28.5T320-840h320q17 0 28.5 11.5T680-800q0 17-11.5 28.5T640-760h-40v240l222 270q32 39 10.5 84.5T760-120H200Zm0-80h560L520-492v-268h-80v268L200-200Zm280-280Z"/></svg>
            ''',
        ),
    )
    html_cards = ''
    html_cards += html_card_1
    html_cards += html_card_2
    html_cards += html_card_3
    html_cards += html_card_4
    html_cards += html_card_5
    html_cards += html_card_6

    html_button = ''
    # html_button = components.button_fill_default(
    #     text = f'Scopri Contaminazioni',
    #     link = f'',
    # )

    with open('styles/tmp/pag-home.css', 'w') as f: f.write('')
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write('')
    html_index = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            {sections.header_dark()}
            <main>
                {sections.home_hero()}
                {sections.home_proof()}
                {sections.separator('Utilizzi')}
                {sections.grid_1_default(html_heading, html_cards, html_button)}
                {sections.separator('Benefici')}
                {sections.home_benefits()}
                {sections.separator('Servizi')}
                {sections.home_services()}
                {sections.separator('Settori')}
                {sections.home_sectors()}
                {sections.separator('Azienda')}
                {sections.home_about()}
                {sections.separator('Contatti')}
                {sections.home_contact()}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/index.html'
    with open(html_index_filepath, 'w') as f: f.write(html_index)

