def header_light():
    html = f'''
        <nav class="navbar-light">
            <div class="logo"><a style="color: #222222;" href="/">Ozonogroup</a></div>

            <input type="checkbox" id="menu-toggle" class="menu-toggle" />

            <label for="menu-toggle" class="menu-icon">
                <span></span>
                <span></span>
                <span></span>
            </label>

            <ul class="menu">
                <li><a href="/servizi.html">Servizi</a></li>
                <li><a href="/prodotti.html">Prodotti</a></li>
                <li><a href="/settori.html">Settori</a></li>
                <li><a href="/ozono.html">Guida all'Ozono</a></li>
                <li><a href="/chi-siamo.html">Chi Siamo</a></li>
            </ul>
            
            <a class="header-button" href="/contatti.html">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M680-80v-120H560v-80h120v-120h80v120h120v80H760v120h-80Zm-480-80q-33 0-56.5-23.5T120-240v-480q0-33 23.5-56.5T200-800h40v-80h80v80h240v-80h80v80h40q33 0 56.5 23.5T760-720v244q-20-3-40-3t-40 3v-84H200v320h280q0 20 3 40t11 40H200Zm0-480h480v-80H200v80Zm0 0v-80 80Z"/></svg>
                <span>Prenota Consulenza</span>
            </a>
        </nav>
    '''
    return html

def header_dark():
    html = f'''
        <nav class="navbar">
            <div class="logo">Ozonogroup</div>

            <input type="checkbox" id="menu-toggle" class="menu-toggle" />

            <label for="menu-toggle" class="menu-icon">
                <span></span>
                <span></span>
                <span></span>
            </label>

            <ul class="menu">
                <li><a href="/servizi.html">Servizi</a></li>
                <li><a href="/prodotti.html">Prodotti</a></li>
                <li><a href="/settori.html">Settori</a></li>
                <li><a href="/ozono.html">Guida all'Ozono</a></li>
                <li><a href="/chi-siamo.html">Chi Siamo</a></li>
            </ul>
        </nav>
    '''
    return html


def footer_dark():
    html = f'''
        <footer class="home-footer-container">
            <div class="container-xl">
                <div class="home-footer-intro-container">
                    <div>
                        <h2>Contatti</h2>
                        <p style="margin-bottom: 1rem;">Via dell'Artigianato, 23, 31011 Asolo TV</p>
                        <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 8px;">
                            <svg xmlns="http://www.w3.org/2000/svg" height="16px" viewBox="0 -960 960 960" width="16px" fill="#ffffff">
                                <path d="M798-120q-125 0-247-54.5T329-329Q229-429 174.5-551T120-798q0-18 12-30t30-12h162q14 0 25 9.5t13 22.5l26 140q2 16-1 27t-11 19l-97 98q20 37 47.5 71.5T387-386q31 31 65 57.5t72 48.5l94-94q9-9 23.5-13.5T670-390l138 28q14 4 23 14.5t9 23.5v162q0 18-12 30t-30 12ZM241-600l66-66-17-94h-89q5 41 14 81t26 79Zm358 358q39 17 79.5 27t81.5 13v-88l-94-19-67 67ZM241-600Zm358 358Z" />
                            </svg>
                            <p>+39 0423 952833</p>
                        </div>
                        <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 8px;">
                            <svg xmlns="http://www.w3.org/2000/svg" height="16px" viewBox="0 -960 960 960" width="16px" fill="#ffffff">
                                <path d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm320-280L160-640v400h640v-400L480-440Zm0-80 320-200H160l320 200ZM160-640v-80 480-400Z" />
                            </svg>
                            <p>info@ozonogroup.it</p>
                        </div>
                    </div>
                    <div>
                        <h2>Risorse</h2>
                        <div class="home-footer-nav">
                            <a href="/chi-siamo.html">Chi Siamo</a>
                            <a href="/contatti.html">Contatti</a>
                        </div>
                    </div>
                </div>
                <div class="home-footer-copyright-container">
                    <a style="font-size: 24px; color: #ffffff; text-decoration-line: none;" href="#">Ozonogroup</a>
                    <p>Copyright © Ozonogroup | Tutti i diritti riservati</p>
                </div>
            </div>
        </footer>
    '''
    return html
