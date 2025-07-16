from lib import g
from lib import utils

css_filepath = g.styles_components_filepath
css_mobile_filepath = g.styles_components_mobile_filepath

####################################################
# ;suptitles
####################################################
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
def h1_default(text, align='left', align_mobile='left'):
    utils.css_create_if_not_exists(css_filepath)
    utils.css_create_if_not_exists(css_mobile_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    with open(css_mobile_filepath) as f: css_mobile = f.read()
    class_name = '.h1_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                font-size: {g.typography_size_xxxl};
                line-height: {g.typography_line_height_xxxl};
                font-weight: normal;
                margin-bottom: 16px;
            }}
        '''
    if align != '':
        class_name = f'.align_{align}'
        if f'{class_name} ' not in css:
            css += f'''
                {class_name} {{
                    text-align: {align};
                }}
            '''
    if align_mobile != '':
        class_name = f'.align_{align_mobile}_mobile'
        if f'{class_name} ' not in css_mobile:
            css_mobile += f'''
                @media screen and (max-width: 768px) {{
                    {class_name} {{
                        text-align: {align_mobile};
                    }}
                }}
            '''
    with open(css_filepath, 'w') as f: f.write(css)
    with open(css_mobile_filepath, 'w') as f: f.write(css_mobile)
    ###
    text = utils.aschii(text)
    ###
    class_inline = ''
    if align != '': class_inline += f'align_{align} '
    ###
    class_inline_mobile = ''
    if align_mobile != '': class_inline_mobile += f'align_{align_mobile}_mobile '
    ###
    html = f'''
        <h2 class="h1_default {class_inline} {class_inline_mobile}">{text}</h2>
    '''
    return html

def h1_reverse(text, align='left', align_mobile='left'):
    utils.css_create_if_not_exists(css_filepath)
    utils.css_create_if_not_exists(css_mobile_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    with open(css_mobile_filepath) as f: css_mobile = f.read()
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
    if align_mobile == 'center':
        class_name = '.align_center_mobile'
        if f'{class_name} ' not in css_mobile:
            css_mobile += f'''
                @media screen and (max-width: 768px) {{
                    {class_name} {{
                        text-align: center;
                    }}
                }}
            '''
    with open(css_filepath, 'w') as f: f.write(css)
    with open(css_mobile_filepath, 'w') as f: f.write(css_mobile)
    ###
    text = utils.aschii(text)
    ###
    css_align = ''
    if align == 'center': css_align = 'text-align: center; '
    style_inline = f'style="{css_align}"'
    if style_inline == 'style=""': style_inline = ''
    ###
    css_align_mobile = ''
    class_inline_mobile = ''
    if align_mobile == 'center': css_align_mobile = 'align_center_mobile '
    class_inline_mobile += f'{css_align_mobile}'
    if class_inline_mobile == '': class_inline_mobile = ''
    html = f'''
        <h1 class="h1_reverse {class_inline_mobile}" {style_inline}>{text}</h1>
    '''
    return html

def h2_default(text, align='', align_mobile=''):
    utils.css_create_if_not_exists(css_filepath)
    utils.css_create_if_not_exists(css_mobile_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    with open(css_mobile_filepath) as f: css_mobile = f.read()
    class_name = '.h2_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                font-size: {g.typography_size_xxl};
                line-height: {g.typography_line_height_xxl};
                font-weight: normal;
                margin-bottom: 16px;
            }}
        '''
    if align != '':
        class_name = f'.align_{align}'
        if f'{class_name} ' not in css:
            css += f'''
                {class_name} {{
                    text-align: {align};
                }}
            '''
    if align_mobile != '':
        class_name = f'.align_{align_mobile}_mobile'
        if f'{class_name} ' not in css_mobile:
            css_mobile += f'''
                @media screen and (max-width: 768px) {{
                    {class_name} {{
                        text-align: {align_mobile};
                    }}
                }}
            '''
    with open(css_filepath, 'w') as f: f.write(css)
    with open(css_mobile_filepath, 'w') as f: f.write(css_mobile)
    ###
    text = utils.aschii(text)
    ###
    class_inline = ''
    if align != '': class_inline += f'align_{align} '
    ###
    class_inline_mobile = ''
    if align_mobile != '': class_inline_mobile += f'align_{align_mobile}_mobile '
    ###
    html = f'''
        <h2 class="h2_default {class_inline} {class_inline_mobile}">{text}</h2>
    '''
    return html

def h2_reverse(text, align='', align_mobile=''):
    utils.css_create_if_not_exists(css_filepath)
    utils.css_create_if_not_exists(css_mobile_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    with open(css_mobile_filepath) as f: css_mobile = f.read()
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
    if align != '':
        class_name = f'.align_{align}'
        if f'{class_name} ' not in css:
            css += f'''
                {class_name} {{
                    text-align: {align};
                }}
            '''
    if align_mobile != '':
        class_name = f'.align_{align_mobile}_mobile'
        if f'{class_name} ' not in css_mobile:
            css_mobile += f'''
                @media screen and (max-width: 768px) {{
                    {class_name} {{
                        text-align: {align_mobile};
                    }}
                }}
            '''
    with open(css_filepath, 'w') as f: f.write(css)
    with open(css_mobile_filepath, 'w') as f: f.write(css_mobile)
    ###
    text = utils.aschii(text)
    ###
    class_inline = ''
    if align != '': class_inline += f'align_{align} '
    ###
    class_inline_mobile = ''
    if align_mobile != '': class_inline_mobile += f'align_{align_mobile}_mobile '
    ###
    html = f'''
        <h2 class="h2_reverse {class_inline} {class_inline_mobile}">{text}</h2>
    '''
    return html

def h3_default(text, align='', align_mobile=''):
    utils.css_create_if_not_exists(css_filepath)
    utils.css_create_if_not_exists(css_mobile_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    with open(css_mobile_filepath) as f: css_mobile = f.read()
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
    with open(css_mobile_filepath, 'w') as f: f.write(css_mobile)
    ###
    text = utils.aschii(text)
    ###
    class_inline = ''
    if align != '': class_inline += f'align_{align} '
    ###
    class_inline_mobile = ''
    if align_mobile != '': class_inline_mobile += f'align_{align_mobile}_mobile '
    ###
    html = f'''
        <h3 class="h3_default {class_inline} {class_inline_mobile}">{text}</h3>
    '''
    return html
    
def h3_reverse(text, align='', align_mobile=''):
    utils.css_create_if_not_exists(css_filepath)
    utils.css_create_if_not_exists(css_mobile_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    with open(css_mobile_filepath) as f: css_mobile = f.read()
    class_name = '.h3_reverse'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_white};
                font-size: {g.typography_size_lg};
                line-height: {g.typography_line_height_lg};
                font-weight: normal;
                margin-bottom: 16px;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    with open(css_mobile_filepath, 'w') as f: f.write(css_mobile)
    ###
    text = utils.aschii(text)
    ###
    class_inline = ''
    if align != '': class_inline += f'align_{align} '
    ###
    class_inline_mobile = ''
    if align_mobile != '': class_inline_mobile += f'align_{align_mobile}_mobile '
    ###
    html = f'''
        <h3 class="h3_reverse {class_inline} {class_inline_mobile}">{text}</h3>
    '''
    return html

####################################################
# ;paragraph
####################################################
def paragraph_default(text, align='', align_mobile='', margin_bottom=''):
    utils.css_create_if_not_exists(css_filepath)
    utils.css_create_if_not_exists(css_mobile_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    with open(css_mobile_filepath) as f: css_mobile = f.read()
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
    if align != '':
        class_name = f'.align_{align}'
        if f'{class_name} ' not in css:
            css += f'''
                {class_name} {{
                    text-align: {align};
                }}
            '''
    if align_mobile != '':
        class_name = f'.align_{align_mobile}_mobile'
        if f'{class_name} ' not in css_mobile:
            css_mobile += f'''
                @media screen and (max-width: 768px) {{
                    {class_name} {{
                        text-align: {align_mobile};
                    }}
                }}
            '''
    if margin_bottom != '':
        class_name = f'.margin_bottom_{margin_bottom}'
        if f'{class_name} ' not in css:
            css += f'''
                {class_name} {{
                    margin-bottom: {margin_bottom};
                }}
            '''
    with open(css_filepath, 'w') as f: f.write(css)
    with open(css_mobile_filepath, 'w') as f: f.write(css_mobile)
    ###
    text = utils.aschii(text)
    ###
    class_inline = ''
    if align != '': class_inline += f'align_{align} '
    ###
    class_inline_mobile = ''
    if align_mobile != '': class_inline_mobile += f'align_{align_mobile}_mobile '
    if margin_bottom != '': class_inline_mobile += f'margin_bottom_{margin_bottom} '
    ###
    ###
    html = f'''
        <p class="paragraph_default {class_inline} {class_inline_mobile}">{text}</p>
    '''
    return html

def paragraph_lg(text, align='', align_mobile='', margin_bottom=''):
    utils.css_create_if_not_exists(css_filepath)
    utils.css_create_if_not_exists(css_mobile_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    with open(css_mobile_filepath) as f: css_mobile = f.read()
    class_name = '.paragraph_lg'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                font-size: 20px;
                line-height: 30px;
                margin-bottom: 1.6rem;
            }}
        '''
    if align != '':
        class_name = f'.align_{align}'
        if f'{class_name} ' not in css:
            css += f'''
                {class_name} {{
                    text-align: {align};
                }}
            '''
    if align_mobile != '':
        class_name = f'.align_{align_mobile}_mobile'
        if f'{class_name} ' not in css_mobile:
            css_mobile += f'''
                @media screen and (max-width: 768px) {{
                    {class_name} {{
                        text-align: {align_mobile};
                    }}
                }}
            '''
    if margin_bottom != '':
        class_name = f'.margin_bottom_{margin_bottom}'
        if f'{class_name} ' not in css:
            css += f'''
                {class_name} {{
                    margin-bottom: {margin_bottom};
                }}
            '''
    with open(css_filepath, 'w') as f: f.write(css)
    with open(css_mobile_filepath, 'w') as f: f.write(css_mobile)
    ###
    text = utils.aschii(text)
    ###
    class_inline = ''
    if align != '': class_inline += f'align_{align} '
    ###
    class_inline_mobile = ''
    if align_mobile != '': class_inline_mobile += f'align_{align_mobile}_mobile '
    ###
    class_inline = ''
    if margin_bottom != '': class_inline_mobile += f'margin_bottom_{margin_bottom} '
    ###
    html = f'''
        <p class="paragraph_lg {class_inline} {class_inline_mobile}">{text}</p>
    '''
    return html

def paragraph_reverse(text, margin_bottom='1.6rem', align='', align_mobile=''):
    utils.css_create_if_not_exists(css_filepath)
    utils.css_create_if_not_exists(css_mobile_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    with open(css_mobile_filepath) as f: css_mobile = f.read()
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
    if align != '':
        class_name = f'.align_{align}'
        if f'{class_name} ' not in css:
            css += f'''
                {class_name} {{
                    text-align: {align};
                }}
            '''
    if align_mobile != '':
        class_name = f'.align_{align_mobile}_mobile'
        if f'{class_name} ' not in css_mobile:
            css_mobile += f'''
                @media screen and (max-width: 768px) {{
                    {class_name} {{
                        text-align: {align_mobile};
                    }}
                }}
            '''
    with open(css_filepath, 'w') as f: f.write(css)
    with open(css_mobile_filepath, 'w') as f: f.write(css_mobile)
    ###
    text = utils.aschii(text)
    css_margin_bottom = ''
    if margin_bottom != '1.6rem': css_margin_bottom = f'margin-bottom: {margin_bottom}; '
    style_inline = f'style="{css_margin_bottom}"'
    if style_inline == 'style=""': style_inline = ''
    ###
    text = utils.aschii(text)
    ###
    class_inline = ''
    if align != '': class_inline += f'align_{align} '
    ###
    class_inline_mobile = ''
    if align_mobile != '': class_inline_mobile += f'align_{align_mobile}_mobile '
    ###
    html = f'''
        <p class="paragraph_reverse {class_inline} {class_inline_mobile}" {style_inline}>{text}</p>
    '''
    return html

####################################################
# ;lists
####################################################
def list_ordered_default(lines):
    utils.css_create_if_not_exists(css_filepath)
    utils.css_create_if_not_exists(css_mobile_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    with open(css_mobile_filepath) as f: css_mobile = f.read()
    class_name = '.list_ordered_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                font-size: {g.typography_size_md};
                line-height: {g.typography_line_height_md};
                margin-bottom: 1.6rem;
                margin-left: 1.6rem;
                display: flex;
                flex-direction: column;
                gap: 0.4rem;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    with open(css_mobile_filepath, 'w') as f: f.write(css_mobile)
    ###
    html_lines = ''
    for line in lines:
        line = utils.aschii(line)
        html_lines += f'''<li>{line}</li>'''
    html = f'''
        <ol class="list_ordered_default">
            {html_lines}
        </ol>
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

def link_reverse(link_text, link_href):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.link_reverse'
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
        <a class="link_reverse" href="{link_href}">
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


####################################################
# ;images
####################################################
def image_sm_default(src, alt):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.image_sm_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                height: 24rem;
                border-radius: {g.border_radius_xl};
                object-fit: cover;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html = f'''
        <img class="image_sm_default" src="{src}" alt="{alt}">
    '''
    return html