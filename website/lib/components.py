import os

from lib import g
from lib import utils

css_filepath = g.styles_components_filepath

def suptitle_default(text, align='left'):
    utils.css_create_if_not_exists(css_filepath)
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
    text = utils.aschii(text)
    css_align = ''
    if align == 'center': css_align = 'text-align: center; '
    style_inline = f'style="{css_align}"'
    if style_inline == 'style=""': style_inline = ''
    html = f'''
        <h2 class="suptitle_default" {style_inline}>{text}</h2>
    '''
    return html

####################################################
# ;headings
####################################################
def h1_reverse(text, align='left'):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.h1_reverse'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_white};
                font-size: {g.typography_size_xxxl};
                line-height: {g.typography_line_height_xxxl};
                font-weight: normal;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    text = utils.aschii(text)
    css_align = ''
    if align == 'center': css_align = 'text-align: center; '
    style_inline = f'style="{css_align}"'
    if style_inline == 'style=""': style_inline = ''
    html = f'''
        <h1 class="h1_reverse" {style_inline}>{text}</h1>
    '''
    return html

def h2_default(text, align='left'):
    utils.css_create_if_not_exists(css_filepath)
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
    text = utils.aschii(text)
    css_align = ''
    if align == 'center': css_align = 'text-align: center; '
    style_inline = f'style="{css_align}"'
    if style_inline == 'style=""': style_inline = ''
    html = f'''
        <h2 class="h2_default" {style_inline}>{text}</h2>
    '''
    return html

def h2_reverse(text, align='left'):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.h2_reverse'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_white};
                font-size: {g.typography_size_xl};
                line-height: {g.typography_line_height_xl};
                font-weight: normal;
                margin-bottom: 16px;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    text = utils.aschii(text)
    css_align = ''
    if align == 'center': css_align = 'text-align: center; '
    style_inline = f'style="{css_align}"'
    if style_inline == 'style=""': style_inline = ''
    html = f'''
        <h2 class="h2_reverse" {style_inline}>{text}</h2>
    '''
    return html

def h3_default(text, align='left'):
    utils.css_create_if_not_exists(css_filepath)
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
    text = utils.aschii(text)
    css_align = ''
    if align == 'center': css_align = 'text-align: center; '
    style_inline = f'style="{css_align}"'
    if style_inline == 'style=""': style_inline = ''
    html = f'''
        <h3 class="h3_default" {style_inline}>{text}</h3>
    '''
    return html

####################################################
# ;paragraph
####################################################
def paragraph_default(text, align='left'):
    utils.css_create_if_not_exists(css_filepath)
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
    text = utils.aschii(text)
    css_align = ''
    if align == 'center': css_align = 'text-align: center; '
    style_inline = f'style="{css_align}"'
    if style_inline == 'style=""': style_inline = ''
    html = f'''
        <p class="paragraph_default" {style_inline}>{text}</p>
    '''
    return html

def paragraph_reverse(text, margin_bottom='1.6rem'):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.paragraph_reverse'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_white};
                font-size: {g.typography_size_md};
                line-height: {g.typography_line_height_md};
                margin-bottom: {margin_bottom};
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    text = utils.aschii(text)
    css_margin_bottom = ''
    if margin_bottom != '1.6rem': css_margin_bottom = f'margin-bottom: {margin_bottom}; '
    style_inline = f'style="{css_margin_bottom}"'
    if style_inline == 'style=""': style_inline = ''
    html = f'''
        <p class="paragraph_reverse" {style_inline}>{text}</p>
    '''
    return html

####################################################
# ;links
####################################################
def link_default(link_text, link_href):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.link_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                text-decoration-line: none;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html = f'''
        <a class="link_default" href="{link_href}">
            {link_text}
        </a>
    '''
    return html

def link_fill():
    utils.css_create_if_not_exists(css_filepath)
    ###
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
    utils.css_create_if_not_exists(css_filepath)
    ###
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
    utils.css_create_if_not_exists(css_filepath)
    ###
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

####################################################
# ;buttons
####################################################
def button_fill_reverse(text, link):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.button_fill_reverse'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                background-color: {g.color_white};
                border: 1px solid {g.color_white};
                border-radius: 9999px;
                padding: 8px 16px;
                display: flex;
                justify-content: center; 
                gap: 8px; 
            }}
        '''
    class_name = '.button_fill_reverse a'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                text-decoration-line: none;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html = f'''
        <div class="button_fill_reverse">
            <a href="{link}">{text}</a>
            <svg style="height: 24px; color: #0f1f2e;" xmlns="http://www.w3.org/2000/svg"
                fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                class="size-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                    d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
            </svg>
        </div>
    '''
    return html
    
def button_ghost_reverse(text, link):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.button_ghost_reverse'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                border: 1px solid {g.color_white};
                border-radius: 9999px; 
                padding: 8px 16px; 
                display: flex;
                justify-content: center; 
                gap: 8px; 
            }}
        '''
    class_name = '.button_ghost_reverse a'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_white};
                text-decoration-line: none;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html = f'''
        <div class="button_ghost_reverse">
            <a href="{link}">{text}</a>
            <svg style="height: 24px; color: #0f1f2e;" xmlns="http://www.w3.org/2000/svg"
                fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                class="size-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                    d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
            </svg>
        </div>
    '''
    return html



####################################################
# ;icons
####################################################
def icon_default(svg):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.icon_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                height: 24px;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html = f'''
        <div class="icon_default">
            {svg}
        </div>
    '''
    return html


                                