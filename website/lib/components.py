import os

from lib import g

def css_create_if_not_exists():
    if not os.path.exists(css_filepath):
        with open(css_filepath, 'w') as f: 
            f.write('')

css_filepath = g.styles_components_filepath

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
    text = text.replace('è', '&#232;')
    text = text.replace('à', '&#224;')
    ###
    css_align = ''
    if align == 'center': css_align = 'text-align: center; '

    style_inline = f'style="{css_align}"'
    if style_inline == 'style=""': style_inline = ''
    html = f'''
        <h2 class="h2_default" {style_inline}>{text}</p>
    '''
    return html

def paragraph_default(paragraph_text):
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
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    paragraph_text = paragraph_text.replace('è', '&#232;')
    paragraph_text = paragraph_text.replace('à', '&#224;')
    ###
    html = f'''
        <p class="paragraph_default">{paragraph_text}</p>
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
    # with open(css_filepath) as f: css = f.read()
    # class_name = '.h2_default'
    # if f'{class_name} ' not in css:
    #     css += f'''
    #         {class_name} {{
    #             color: {g.color_black_pearl};
    #             font-size: {g.typography_size_xl};
    #             line-height: {g.typography_line_height_xl};
    #             font-weight: normal;
    #             margin-bottom: 16px;
    #         }}
    #     '''
    # with open(css_filepath, 'w') as f: f.write(css)
    ###
    paragraph = paragraph.replace('è', '&#232;')
    paragraph = paragraph.replace('à', '&#224;')
    html = f'''
        <div style="background-color: #F8F9FB; padding: 32px; border-radius: 16px;">
            {icon}
            {title}
            {paragraph}
        </div>
    '''
    return html