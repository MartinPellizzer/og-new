import os

from lib import g

def aschii(paragraph):
    paragraph = paragraph.replace('è', '&#232;')
    paragraph = paragraph.replace('à', '&#224;')
    paragraph = paragraph.replace('°', '&#176;')
    return paragraph

def css_create_if_not_exists():
    if not os.path.exists(css_filepath):
        with open(css_filepath, 'w') as f: 
            f.write('')

css_filepath = g.styles_components_filepath

def suptitle_default(text, align='left'):
    if not os.path.exists(css_filepath):
        with open(css_filepath, 'w') as f: 
            f.write('')
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.suptitle_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_blue};
                font-size: {g.typography_size_md};
                line-height: {g.typography_size_md};
                font-weight: normal;
                margin-bottom: 16px;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    text = aschii(text)
    css_align = ''
    if align == 'center': css_align = 'text-align: center; '
    style_inline = f'style="{css_align}"'
    if style_inline == 'style=""': style_inline = ''
    html = f'''
        <h2 class="suptitle_default" {style_inline}>{text}</h2>
    '''
    return html

def h2_default(text, align='left'):
    if not os.path.exists(css_filepath):
        with open(css_filepath, 'w') as f: 
            f.write('')
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.h2_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                font-size: {g.typography_size_xl};
                line-height: {g.typography_line_height_xl};
                font-weight: normal;
                margin-bottom: 16px;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    text = aschii(text)
    css_align = ''
    if align == 'center': css_align = 'text-align: center; '

    style_inline = f'style="{css_align}"'
    if style_inline == 'style=""': style_inline = ''
    html = f'''
        <h2 class="h2_default" {style_inline}>{text}</h2>
    '''
    return html

def h3_default(text, align='left'):
    # margin-bottom: 16px; font-size: 24px; line-height: 32px; font-weight: normal; color: #0F1F2E;
    if not os.path.exists(css_filepath):
        with open(css_filepath, 'w') as f: 
            f.write('')
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.h3_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                font-size: {g.typography_size_lg};
                line-height: {g.typography_line_height_lg};
                font-weight: normal;
                margin-bottom: 16px;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    text = aschii(text)
    css_align = ''
    if align == 'center': css_align = 'text-align: center; '

    style_inline = f'style="{css_align}"'
    if style_inline == 'style=""': style_inline = ''
    html = f'''
        <h3 class="h3_default" {style_inline}>{text}</h3>
    '''
    return html

def paragraph_default(text):
    if not os.path.exists(css_filepath):
        with open(css_filepath, 'w') as f: 
            f.write('')
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.paragraph_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                font-size: {g.typography_size_md};
                line-height: {g.typography_line_height_md};
                margin-bottom: 1.6rem;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    text = aschii(text)
    html = f'''
        <p class="paragraph_default">{text}</p>
    '''
    return html

def link_fill():
    if not os.path.exists(css_filepath):
        with open(css_filepath, 'w') as f: f.write('')
    with open(css_filepath) as f: css = f.read()
    class_name = '.link_fill'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_white};
                background-color: {g.color_black_pearl};
                border: 1px solid {g.color_black_pearl};
                border-radius: 9999px;
                padding: 8px 16px;
                text-decoration-line: none;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html = f'''
        <div>
            <a class="link_fill" href="/contatti.html">Prenota consulenza</a>
        </div>
    '''
    return html

def link_fill_reverse():
    if not os.path.exists(css_filepath):
        with open(css_filepath, 'w') as f: f.write('')
    with open(css_filepath) as f: css = f.read()
    class_name = '.link_fill_reverse'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                background-color: {g.color_white};
                border: 1px solid {g.color_white};
                border-radius: 9999px;
                padding: 8px 16px;
                text-decoration-line: none;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html = f'''
        <div>
            <a class="link_fill_reverse" href="/contatti.html">Prenota consulenza</a>
        </div>
    '''
    return html

def link_ghost_reverse():
    if not os.path.exists(css_filepath):
        with open(css_filepath, 'w') as f: f.write('')
    with open(css_filepath) as f: css = f.read()
    class_name = '.link_ghost_reverse'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_white}; 
                border: 1px solid {g.color_white};
                border-radius: 9999px; 
                padding: 8px 16px; 
                text-decoration-line: none;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html = f'''
        <div>
            <a class="link_ghost_reverse" href="#">Come funziona</a>
        </div>
    '''
    return html

def card_default(icon, title, paragraph):
    css_create_if_not_exists()
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.card_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                background-color: {g.color_gray_extralight}; 
                padding: 32px; 
                border-radius: 16px;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    paragraph = aschii(paragraph)
    html = f'''
        <div class="card_default">
            {icon}
            {title}
            {paragraph}
        </div>
    '''
    return html

def card_default_1(suptitle, title, paragraph, icon, link):
    css_create_if_not_exists()
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.card_default_1'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                background-color: {g.color_gray_extralight}; 
                padding: 32px; 
                border-radius: 16px;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    paragraph = aschii(paragraph)
    html = f'''
        <div class="card_default_1">
            {suptitle}
            {title}
            {paragraph}
            <div style="margin-bottom: 64px;"></div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                {icon}
                <div style="display: flex; gap: 8px;">
                    {link}
                    <svg style="height: 24px;" xmlns="http://www.w3.org/2000/svg" fill="none"
                        viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
                    </svg>
                </div>
            </div>
        </div>
    '''
    return html
