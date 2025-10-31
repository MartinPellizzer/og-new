def header_light():
    html = f'''
        <nav class="navbar-light">
            <div class="logo">Ozonogroup</div>

            <input type="checkbox" id="menu-toggle" class="menu-toggle" />

            <label for="menu-toggle" class="menu-icon">
                <span></span>
                <span></span>
                <span></span>
            </label>

            <ul class="menu">
                <li><a href="#">Home</a></li>
                <li><a href="#">Applicazioni</a></li>
                <li><a href="#">Prodotti</a></li>
                <li><a href="#">Servizi</a></li>
                <li><a href="#">Ozono</a></li>
            </ul>
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
                <li><a href="#">Home</a></li>
                <li><a href="#">Applicazioni</a></li>
                <li><a href="#">Prodotti</a></li>
                <li><a href="#">Servizi</a></li>
                <li><a href="#">Ozono</a></li>
            </ul>
        </nav>
    '''
    return html
