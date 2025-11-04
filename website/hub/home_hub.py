from lib import g
from lib import components

def gen():
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
                <section class="home-hero-section">
                    <div class="container-xl" style="height: 100%;">
                        <div class="home-hero-container">
                            <div class="home-hero-title-container">
                                <div style="flex: 2;">
                                    <h1 style="font-size: 4rem; line-height: 1;">Sistemi di sanificazione ad ozono per l'igiene e la sostenibilità industriale</h1>
                                </div>
                                <div style="flex: 1;"></div>
                            </div>
                            <div class="home-hero-content-container">
                                <div style="flex: 2;"></div>
                                <div style="flex: 1;">
                                    <p style="color: #ffffff; font-size: 16px; line-height: 24px; margin-bottom: 24px;">Progettiamo e produciamo tecnologie di disinfezione a base di ozono per settori industriali come quello alimentare, agricolo e dei rifiuti.
                                    </p>
                                    <div class="home-hero-buttons-container">
                                        <div>
                                            <a class="link_fill_reverse" href="/soluzioni.html">Esplora Soluzioni</a>
                                        </div>
                                        <div>
                                            <a class="link_ghost_reverse" href="/ozono.html">Scopri La Sanificazione Con Ozono</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                                
                                    <div class="home-hero-buttons-container">
                                        <div>
                                            <a class="link_fill_reverse" href="/soluzioni.html">Esplora Soluzioni</a>
                                        </div>
                                        <div>
                                            <a class="link_ghost_reverse" href="/ozono.html">Scopri La Sanificazione Con Ozono</a>
                                        </div>
                                    </div>
                </section>
                <section class="container-xl" style="margin-top: 6.4rem; margin-bottom: 6.4rem;">
                    <div class="container-sm" style="margin-bottom: 3rem;">
                        <h2 style="color: #222222; text-align: center; font-size: 3rem;" class="h2_default">A cosa serve l'ozono?</h2>
                        <p style="color: #555555; text-align: center;">L'ozono elimina le contaminazioni biologiche nell'industria alimentare, neutralizzando batteri, virus, muffe, parassiti e odori. Elimina anche le contaminazioni chimiche nell'industria alimentare, riducendo micotossine, pesticidi, fitofarmaci e residui di detergenti.</p>
                    </div>
                    <div class="grid-3">
                        <div class="card_default_1">
                            <div style="margin-bottom: 4rem;">
                                <h2 class="suptitle_default">01</h2>
                                <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">Batteri</h3>
                                <p style="color: #555555;">L'ozono elimina i batteri grazie al suo forte potere ossidante, che distrugge le membrane cellulari e inibisce la loro capacità di riprodursi.</p>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M600-80q-17 0-28.5-11.5T560-120v-43q-23-4-43.5-11.5T478-195l-40 40q-12 11-28.5 11.5T381-155q-12-12-12-28.5t12-28.5l41-41q-3-5-6-10.5t-6-10.5l-27-53-49 49q-12 11-28 11.5T278-278q-12-12-12-28t12-28l49-50-53-26q-5-2-9-4.5t-9-5.5l-36 36q-12 11-28.5 11.5T163-384q-12-12-12-28t12-28l35-35q-14-19-22.5-40.5T163-560h-43q-17 0-28.5-11.5T80-600q0-17 11.5-28.5T120-640h45q5-19 12-36t18-33l-35-35q-12-12-12-28t12-28q12-12 28-12t28 12l35 35q16-11 33-18t36-12v-45q0-17 11.5-28.5T360-880q17 0 28.5 11.5T400-840v43q24 4 45.5 13t40.5 23l35-35q12-12 28.5-12t28.5 12q12 12 12 28t-12 28l-37 37q2 4 4.5 8t4.5 9l25 50 46-46q12-12 28.5-12t28.5 12q12 12 12 28.5T678-625l-48 47 56 28q6 3 12.5 6.5T710-536l40-40q12-12 28-12t28 12q12 12 12 28.5T806-519l-40 39q12 18 19.5 38t11.5 42h43q17 0 28.5 11.5T880-360q0 17-11.5 28.5T840-320h-45q-5 19-12 35.5T765-252l34 34q12 12 12 28.5T799-161q-12 11-28.5 11.5T742-161l-33-34q-16 11-33 18t-36 12v45q0 17-11.5 28.5T600-80Zm-6-160q58 0 95.5-44T718-386q-5-30-22.5-54T650-478l-66-34q-23-12-41.5-30.5T512-584l-34-66q-16-32-46-51t-66-19q-58 0-95.5 44T242-574q5 30 22.5 54t45.5 38l66 34q23 12 41.5 30.5T448-376l34 66q16 32 46 51t66 19ZM380-540q25 0 42.5-17.5T440-600q0-25-17.5-42.5T380-660q-25 0-42.5 17.5T320-600q0 25 17.5 42.5T380-540Zm200 250q21 0 35.5-14.5T630-340q0-21-14.5-35.5T580-390q-21 0-35.5 14.5T530-340q0 21 14.5 35.5T580-290ZM480-480Z"/></svg>
                            </div>
                        </div>
                        <div class="card_default_1">
                            <div style="margin-bottom: 4rem;">
                                <h2 class="suptitle_default">02</h2>
                                <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">Virus</h3>
                                <p style="color: #555555;">L'ozono inattiva i virus ossidando le proteine del loro rivestimento e il materiale genetico, impedendo loro di infettare altre cellule.</p>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M450-80q-12 0-21-9t-9-21q0-12 9-21t21-9v-62q-42-5-79-20t-67-40l-43 44q9 9 9 21t-9 21q-9 9-21 9t-21-9l-43-42q-9-9-9-21.5t9-21.5q9-9 21-8.5t21 8.5l44-44q-25-31-40-67t-20-78h-62q0 12-9 21t-21 9q-12 0-21-9t-9-21v-60q0-12 9-21t21-9q12 0 21 9t9 21h62q5-42 20.5-78t39.5-67l-44-44q-9 8-21 8.5t-21-8.5q-9-9-9-21.5t9-21.5l42-42q9-9 21.5-9t21.5 9q9 9 9 21.5t-9 21.5l43 43q31-25 67-40t78-20v-62q-12 0-20.5-9t-8.5-21q0-12 9-21t21-9h60q12 0 21 9t9 21q0 12-9 21t-21 9v62q42 5 78 20t67 40l44-44q-9-9-9-21t9-21q9-9 21.5-9t21.5 9l42 43q9 9 9 21t-9 21q-9 9-21.5 9t-21.5-9l-43 43q25 31 40 67.5t20 78.5h62q0-12 9-21t21-9q12 0 21 9t9 21v60q0 12-9 21t-21 9q-12 0-21-9t-9-21h-62q-5 42-20 78.5T698-304l43 43q9-9 21.5-9t21.5 9q9 9 9 21.5t-9 21.5l-42 42q-9 9-21.5 9t-21.5-9q-9-9-8.5-21t8.5-21l-44-44q-31 25-67 40.5T510-201v61q12 0 21 9t9 21q0 12-9 21t-21 9h-60Zm30-200q83 0 141.5-58.5T680-480q0-83-58.5-141.5T480-680q-83 0-141.5 58.5T280-480q0 83 58.5 141.5T480-280Zm-70-40q17 0 28.5-11.5T450-360q0-17-11.5-28.5T410-400q-17 0-28.5 11.5T370-360q0 17 11.5 28.5T410-320Zm140 0q17 0 28.5-11.5T590-360q0-17-11.5-28.5T550-400q-17 0-28.5 11.5T510-360q0 17 11.5 28.5T550-320ZM340-440q17 0 28.5-11.5T380-480q0-17-11.5-28.5T340-520q-17 0-28.5 11.5T300-480q0 17 11.5 28.5T340-440Zm140 0q17 0 28.5-11.5T520-480q0-17-11.5-28.5T480-520q-17 0-28.5 11.5T440-480q0 17 11.5 28.5T480-440Zm140 0q17 0 28.5-11.5T660-480q0-17-11.5-28.5T620-520q-17 0-28.5 11.5T580-480q0 17 11.5 28.5T620-440ZM410-560q17 0 28.5-11.5T450-600q0-17-11.5-28.5T410-640q-17 0-28.5 11.5T370-600q0 17 11.5 28.5T410-560Zm140 0q17 0 28.5-11.5T590-600q0-17-11.5-28.5T550-640q-17 0-28.5 11.5T510-600q0 17 11.5 28.5T550-560Zm-70 80Z"/></svg>
                            </div>
                        </div>
                        <div class="card_default_1">
                            <div style="margin-bottom: 4rem;">
                                <h2 class="suptitle_default">03</h2>
                                <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">Muffe</h3>
                                <p style="color: #555555;">L'ozono neutralizza le muffe distruggendo le spore fungine presenti nell'aria e sulle superfici, prevenendone la proliferazione.</p>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M200-120v-80h200v-80q-83 0-141.5-58.5T200-480q0-61 33.5-111t90.5-73q8-34 35.5-55t62.5-21l-22-62 38-14-14-36 76-28 12 38 38-14 110 300-38 14 14 38-76 28-12-38-38 14-24-66q-15 14-34.5 21t-39.5 5q-22-2-41-13.5T338-582q-27 16-42.5 43T280-480q0 50 35 85t85 35h320v80H520v80h240v80H200Zm346-458 36-14-68-188-38 14 70 188Zm-126-22q17 0 28.5-11.5T460-640q0-17-11.5-28.5T420-680q-17 0-28.5 11.5T380-640q0 17 11.5 28.5T420-600Zm126 22Zm-126-62Zm0 0Z"/></svg>
                            </div>
                        </div>
                        <div class="card_default_1">
                            <div style="margin-bottom: 4rem;">
                                <h2 class="suptitle_default">04</h2>
                                <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">Parassiti</h3>
                                <p style="color: #555555;">L'ozono contribuisce a eliminare i parassiti attraverso l'ossidazione delle loro strutture biologiche, interrompendone il ciclo vitale.</p>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M480-120q-64 0-114.5-33T283-240l-95 54-40-69 103-60q-3-11-5-22.5t-4-22.5H120v-80h122q2-12 4-23.5t5-22.5l-103-60 40-69 94 55q8-14 18.5-27.5T322-612q-2-7-2-14v-14q0-24 7-46t19-41l-66-66 56-57 70 68q17-9 35.5-13.5T480-800q20 0 39 5t36 14l69-69 56 57-66 66q12 19 18.5 41t6.5 46v13.5q0 6.5-2 13.5 11 11 21.5 25t18.5 28l95-54 40 69-104 59q3 11 5.5 22.5T718-440h122v80H718q-2 12-4 23.5t-5 22.5l103 60-40 69-95-55q-32 54-82.5 87T480-120Zm-76-546q17-7 36.5-10.5T480-680q20 0 38.5 3t35.5 10q-8-23-28-38t-46-15q-26 0-47 15.5T404-666Zm76 466q73 0 116.5-61T640-400q0-70-40.5-135T480-600q-78 0-119 64.5T320-400q0 78 43.5 139T480-200Zm-40-80v-240h80v240h-80Z"/></svg>
                            </div>
                        </div>
                        <div class="card_default_1">
                            <div style="margin-bottom: 4rem;">
                                <h2 class="suptitle_default">05</h2>
                                <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">Odori</h3>
                                <p style="color: #555555;">L'ozono elimina gli odori scomponendo chimicamente le molecole organiche volatili responsabili dei cattivi odori, neutralizzandole alla fonte.</p>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M80-200v-120h600v120H80Zm640 0v-120h60v120h-60Zm100 0v-120h60v120h-60ZM720-360v-52q0-39-23-59.5T642-492h-62q-56 0-95-39t-39-95q0-56 39-95t95-39v60q-30 0-52 21t-22 53q0 32 22 53t52 21h62q56 0 97 36t41 90v66h-60Zm100 0v-90q0-66-46-114t-114-48v-60q30 0 52-22t22-52q0-30-22-52t-52-22v-60q56 0 95 39t39 95q0 29-11 52.5T754-650q56 26 91 80t35 120v90h-60Z"/></svg>
                            </div>
                        </div>
                        <div class="card_default_1">
                            <div style="margin-bottom: 4rem;">
                                <h2 class="suptitle_default">06</h2>
                                <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">Pesticidi</h3>
                                <p style="color: #555555;">L'ozono ossida i residui di pesticidi su frutta, verdura e superfici, riducendoli in composti meno nocivi o completamente innocui.</p>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M200-120q-51 0-72.5-45.5T138-250l222-270v-240h-40q-17 0-28.5-11.5T280-800q0-17 11.5-28.5T320-840h320q17 0 28.5 11.5T680-800q0 17-11.5 28.5T640-760h-40v240l222 270q32 39 10.5 84.5T760-120H200Zm0-80h560L520-492v-268h-80v268L200-200Zm280-280Z"/></svg>
                            </div>
                        </div>
                    </div>
                </section>
                <section class="container-xl" style="margin-top: 6.4rem; margin-bottom: 6.4rem;">
                    <div class="container-sm" style="margin-bottom: 3rem;">
                        <h2 style="color: #222222; text-align: center; font-size: 3rem;" class="h2_default">Perché usare l'ozono?</h2>
                        <p style="color: #555555; text-align: center;">L'ozono garantisce una potente attività antimicrobica, penetra superfici complesse, non lascia residui chimici, è compatibile con alimenti biologici e prolunga la shelf-life degli alimenti.</p>
                    </div>
                    <div style="display: flex; gap: 1.6rem;">
                        <div style="flex: 10;">
                            <div class="card_3_default">
                                <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">Igiene in Secondi</h3>
                                <p style="color: #555555;">L'ozono è circa 3.000 volte più rapido ed efficace del cloro nel distruggere batteri, virus, muffe e funghi.<br><br>Riduce drasticamente i tempi di sanificazione, permette cicli produttivi più rapidi, minimizza il downtime degli impianti e garantisce igiene efficace in ambienti ad alta rotazione.</p>
                            </div>
                        </div>
                        <div style="flex: 9;">
                            <img class="image_sm_default" src="/immagini/veloce.webp">
                        </div>
                    </div>
                    <div style="margin-bottom: 1.6rem;"></div>
                    <div style="display: flex; gap: 1.6rem;">
                        <div style="flex: 9;">
                            <img class="image_sm_default" src="/immagini/ecologico.webp">
                        </div>
                        <div style="flex: 10;">
                            <div class="card_3_default">
                                <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">Zero Residui Chimici</h3>
                                <p style="color: #555555;">L'ozono si decompone rapidamente in ossigeno, senza lasciare residui chimici su superfici o alimenti.<br><br>Garantisce sicurezza alimentare, preserva gusto e freschezza, ed elimina il risciacquo finale, con conseguente risparmio di tempo, acqua e costi produttivi.</p>
                            </div>
                        </div>
                    </div>
                </section>
                <section class="container-xl" style="margin-bottom: 6rem;">
                    <div class="container-sm" style="margin-bottom: 3rem;">
                        <h2 style="color: #222222; text-align: center; font-size: 3rem;" class="h2_default">Tecnologia personalizzata per ogni esigenza dell'industria alimentare</h2>
                        <p style="color: #555555; text-align: center;">I nostri sistemi di sanificazione all'ozono sono progettati su misura per adattarsi a ogni fase del processo produttivo. Che tu operi nella trasformazione, nel confezionamento o nella logistica, Ozonogroup ha una soluzione efficace, sicura e automatizzata.</p>
                    </div>
                    <div class="home-services-cards-container">
                        <div style="flex: 1;">
                            <div style="display: flex; flex-direction: column; gap: 24px;">
                                <div class="card_default">
                                    <svg style="margin-bottom: 16px;" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                                        <path d="M784-120 532-372q-30 24-69 38t-83 14q-109 0-184.5-75.5T120-580q0-109 75.5-184.5T380-840q109 0 184.5 75.5T640-580q0 44-14 83t-38 69l252 252-56 56ZM380-400q75 0 127.5-52.5T560-580q0-75-52.5-127.5T380-760q-75 0-127.5 52.5T200-580q0 75 52.5 127.5T380-400Z" />
                                    </svg>
                                    <div style="margin-bottom: 1.6rem;"></div>
                                    <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">1. Analisi e Valutazione</h3>
                                    <p style="color: #555555;">Sviluppiamo una soluzione su misura, combinando le migliori tecnologie a ozono con un design personalizzato per otimizzare igiene, efficienza e sostenibilita.</p>
                                </div>
                                <div class="card_default">
                                    <svg style="margin-bottom: 16px;" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                                        <path d="m352-522 86-87-56-57-44 44-56-56 43-44-45-45-87 87 159 158Zm328 329 87-87-45-45-44 43-56-56 43-44-57-56-86 86 158 159Zm24-567 57 57-57-57ZM290-120H120v-170l175-175L80-680l200-200 216 216 151-152q12-12 27-18t31-6q16 0 31 6t27 18l53 54q12 12 18 27t6 31q0 16-6 30.5T816-647L665-495l215 215L680-80 465-295 290-120Zm-90-80h56l392-391-57-57-391 392v56Zm420-419-29-29 57 57-28-28Z" />
                                    </svg>
                                    <div style="margin-bottom: 1.6rem;"></div>
                                    <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">2. Progettazione e Realizzazione</h3>
                                    <p style="color: #555555;">Sviluppiamo una soluzione su misura, combinando le migliori tecnologie a ozono con un design personalizzato per otimizzare igiene, efficienza e sostenibilita.</p>
                                </div>
                            </div>
                        </div>
                        <div style="flex: 1;">
                            <div class="home-services-card-offset">
                                <div class="card_default">
                                    <svg style="margin-bottom: 16px;" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                                        <path d="M686-132 444-376q-20 8-40.5 12t-43.5 4q-100 0-170-70t-70-170q0-36 10-68.5t28-61.5l146 146 72-72-146-146q29-18 61.5-28t68.5-10q100 0 170 70t70 170q0 23-4 43.5T584-516l244 242q12 12 12 29t-12 29l-84 84q-12 12-29 12t-29-12Zm29-85 27-27-256-256q18-20 26-46.5t8-53.5q0-60-38.5-104.5T386-758l74 74q12 12 12 28t-12 28L332-500q-12 12-28 12t-28-12l-74-74q9 57 53.5 95.5T360-440q26 0 52-8t47-25l256 256ZM472-488Z" />
                                    </svg>
                                    <div style="margin-bottom: 1.6rem;"></div>
                                    <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">3. Installazione e Formazione</h3>
                                    <p style="color: #555555;">Il nostro team tecnico si occupa dell'installazione e forma il tuo personale sull'utilizzo sicuro e ottimale del sistema.</p>
                                </div>
                                <div class="card_default">
                                    <svg style="margin-bottom: 16px;" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                                        <path d="M240-400h320v-80H240v80Zm0-120h480v-80H240v80Zm0-120h480v-80H240v80ZM80-80v-720q0-33 23.5-56.5T160-880h640q33 0 56.5 23.5T880-800v480q0 33-23.5 56.5T800-240H240L80-80Zm126-240h594v-480H160v525l46-45Zm-46 0v-480 480Z" />
                                    </svg>
                                    <div style="margin-bottom: 1.6rem;"></div>
                                    <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">4. Assistenza e Manutenzione</h3>
                                    <p style="color: #555555;">Forniamo supporto tecnico continuo e piano di manutenzione preventiva per assicurare performance costanti e conformita normativa nel tempo.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
                <section class="container-xl" style="margin-bottom: 5rem;">
                    <div class="home-industries-cards-container">
                        <div style="flex: 1;">
                            <div class="container-sm" style="margin-bottom: 3rem;">
                                <h2 style="color: #222222; font-size: 3rem;" class="h2_default">Soluzioni specifiche per ogni filiera alimentar</h2>
                                <p style="color: #555555;">Ogni settore dell'industria alimentare ha esigenze diverse in termini di igiene, normativa e tipo di contaminazione microbiologica. I sistemi di sanificazione all'ozono di Ozonogroup sono progettati per adattarsi perfettamente a questi contesti, garantendo efficacia microbiologica, sostenibilità ambientale e conformità normativa.</p>
                            </div>
                        </div>
                        <div style="flex: 1;">
                            <div class="card_default_1">
                                <div style="margin-bottom: 4rem;">
                                    <h2 class="suptitle_default">01</h2>
                                    <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">Carne e Pollame</h3>
                                    <p style="color: #555555;">Sanificazione profonda in ambienti ad alto rischio microbiologico. Eliminazione di patogeni come Salmonella, Listeria e E. coli da superfici, macchinari e ambienti. Sistemi integrati nelle linee di disosso, sezionamento e confezionamento. Controllo degli odori e prevenzione della formazione di biofilm.</p>
                                </div>
                                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                                    <path d="M250-40v-160h-30q-42 0-71-29t-29-71q0-42 29-71t71-29h30v-40H120v-200h130v-40h-30q-42 0-71-29t-29-71q0-42 29-71t71-29h30v-40h60v40h30q42 0 71 29t29 71q0 42-29 71t-71 29h-30v40h130v200H310v40h30q42 0 71 29t29 71q0 42-29 71t-71 29h-30v160h-60Zm400 0v-160h-30q-42 0-71-29t-29-71q0-42 29-71t71-29h30v-40H520v-200h130v-40h-30q-42 0-71-29t-29-71q0-42 29-71t71-29h30v-40h60v40h30q42 0 71 29t29 71q0 42-29 71t-71 29h-30v40h130v200H710v40h30q42 0 71 29t29 71q0 42-29 71t-71 29h-30v160h-60ZM220-760h120q8 0 14-6t6-14q0-8-6-14t-14-6H220q-8 0-14 6t-6 14q0 8 6 14t14 6Zm400 0h120q8 0 14-6t6-14q0-8-6-14t-14-6H620q-8 0-14 6t-6 14q0 8 6 14t14 6ZM200-520h160v-40H200v40Zm400 0h160v-40H600v40ZM220-280h120q8 0 14-6t6-14q0-8-6-14t-14-6H220q-8 0-14 6t-6 14q0 8 6 14t14 6Zm400 0h120q8 0 14-6t6-14q0-8-6-14t-14-6H620q-8 0-14 6t-6 14q0 8 6 14t14 6ZM200-760v-40 40Zm400 0v-40 40ZM200-520v-40 40Zm400 0v-40 40ZM200-280v-40 40Zm400 0v-40 40Z" />
                                </svg>
                            </div>
                        </div>
                        <div style="flex: 1;">
                            <div class="card_default_1">
                                <div style="margin-bottom: 4rem;">
                                    <h2 class="suptitle_default">02</h2>
                                    <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">Pesce e Frutti di Mare</h3>
                                    <p style="color: #555555;">Igiene in ambienti umidi, a bassa temperatura e ad alto carico organico. Ozono efficace anche in ambienti freddi (5°C), ideale per celle e zone di lavorazione pesce. Riduzione della carica batterica su filetti, crostacei, superfici e nastri trasportatori. Prolungamento della shelf-life senza additivi chimici.</p>
                                </div>
                                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                                    <path d="M440-120q-100 0-170-70t-70-170v-240l200 200-56 57-64-64v47q0 66 47 113t113 47q66 0 113-47t47-113v-127q-36-14-58-44.5T520-600q0-38 22-68.5t58-44.5v-167h80v167q36 14 58 44.5t22 68.5q0 38-22 69t-58 44v127q0 100-70 170t-170 70Zm200-440q17 0 28.5-11.5T680-600q0-17-11.5-28.5T640-640q-17 0-28.5 11.5T600-600q0 17 11.5 28.5T640-560Zm0-40Z" />
                                </svg>
                            </div>
                        </div>
                    </div>
                    <div class="home-industries-cards-container">
                        <div style="flex: 1;">
                            <div class="card_default_1">
                                <div style="margin-bottom: 4rem;">
                                    <h2 class="suptitle_default">03</h2>
                                    <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">Ortofrutta</h3>
                                    <p style="color: #555555;">Sanificazione post-raccolta, durante lo stoccaggio e nel confezionamento. Rimozione di muffe e lieviti (Botrytis, Penicillium) responsabili del deterioramento precoce. Disinfezione di casse, nastri, vasche di lavaggio e aria nelle aree di confezionamento.</p>
                                </div>
                                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                                    <path d="M480-120q-117 0-198.5-81.5T200-400q0-94 55.5-168.5T401-669q-20-5-39-14.5T328-708q-33-33-42.5-78.5T281-879q47-5 92.5 4.5T452-832q23 23 33.5 52t13.5 61q13-31 31.5-58.5T572-828q11-11 28-11t28 11q11 11 11 28t-11 28q-22 22-39 48.5T564-667q88 28 142 101.5T760-400q0 117-81.5 198.5T480-120Zm0-80q83 0 141.5-58.5T680-400q0-83-58.5-141.5T480-600q-83 0-141.5 58.5T280-400q0 83 58.5 141.5T480-200Zm0-200Z" />
                                </svg>
                            </div>
                        </div>
                        <div style="flex: 1;">
                            <div class="card_default_1">
                                <div style="margin-bottom: 4rem;">
                                    <h2 class="suptitle_default">04</h2>
                                    <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">Latticini e Derivati del Latte</h3>
                                    <p style="color: #555555;">Controllo microbiologico in ambienti sensibili alla contaminazione crociata. Rimozione di Listeria monocytogenes in vasche, superfici e impianti CIP. Disinfezione di aria e superfici nelle aree di fermentazione e maturazione. Sistemi compatibili con ambienti ad alta umidità e carico proteico.</p>
                                </div>
                                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                                    <path d="M482-40 294-400q-71 3-122.5-41T120-560q0-51 29.5-92t74.5-58q18-91 89.5-150.5T480-920q95 0 166.5 59.5T736-710q45 17 74.5 58t29.5 92q0 75-53 119t-119 41L482-40ZM280-480q15 0 29.5-5t26.5-17l22-22 26 16q21 14 45.5 21t50.5 7q26 0 50.5-7t45.5-21l26-16 22 22q12 12 26.5 17t29.5 5q33 0 56.5-23.5T760-560q0-30-19-52.5T692-640l-30-4-2-32q-5-69-57-116.5T480-840q-71 0-123 47.5T300-676l-2 32-30 6q-30 6-49 27t-19 51q0 33 23.5 56.5T280-480Zm202 266 108-210q-24 12-52 18t-58 6q-27 0-54.5-6T372-424l110 210Zm-2-446Z" />
                                </svg>
                            </div>
                        </div>
                        <div style="flex: 1;">
                            <div class="card_default_1">
                                <div style="margin-bottom: 4rem;">
                                    <h2 class="suptitle_default">05</h2>
                                    <h3 style="color: #222222; margin-bottom: 1rem; font-size: 1.5rem; font-weight: normal;">Bevande e Imbottigliamento</h3>
                                    <p style="color: #555555;">Igienizzazione delle linee e prevenzione di alterazioni microbiologiche nei liquidi. Ozono in forma gassosa e acquosa per la sanificazione di serbatoi, tubazioni, riempitrici. Sistemi integrati nei processi CIP e SIP. Nessun residuo chimico: ideale per produzione biologica o senza conservanti.</p>
                                </div>
                                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                                    <path d="M491-200q12-1 20.5-9.5T520-230q0-14-9-22.5t-23-7.5q-41 3-87-22.5T343-375q-2-11-10.5-18t-19.5-7q-14 0-23 10.5t-6 24.5q17 91 80 130t127 35ZM480-80q-137 0-228.5-94T160-408q0-100 79.5-217.5T480-880q161 137 240.5 254.5T800-408q0 140-91.5 234T480-80Zm0-80q104 0 172-70.5T720-408q0-73-60.5-165T480-774Q361-665 300.5-573T240-408q0 107 68 177.5T480-160Zm0-320Z" />
                                </svg>
                            </div>
                        </div>
                    </div>
                </section>
                <div style="background-color: #ededed; height: 1px;"></div>
                <section class="container-xl" style="margin-top: 6rem; margin-bottom: 6rem;">
                    <div style="display: flex; align-items: center; gap: 3rem;">
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
                </section>
                
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_filepath = f'{g.website_folderpath}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)
