from lib import g
from lib import utils

from lib import components

css_filepath = g.styles_blocks_filepath

####################################################
# ;cards
####################################################
def card_default_1(suptitle_text, title_text, paragraph_text, icon, link_text, link_href):
    utils.css_create_if_not_exists(css_filepath)
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
    suptitle = components.suptitle_default(text=suptitle_text)
    title = components.h3_default(text=title_text)
    paragraph = components.paragraph_default(text=paragraph_text)
    link = components.link_default(link_text=link_text, link_href=link_href)
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

def card_default_2(icon, title_text, paragraph_text):
    utils.css_create_if_not_exists(css_filepath)
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
    title = components.h3_default(text=title_text)
    paragraph = components.paragraph_default(text=paragraph_text)
    html = f'''
        <div class="card_default">
            {icon}
            {title}
            {paragraph}
        </div>
    '''
    return html



def contact_reverse(icon, cta, contact):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.contact_reverse'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                display: flex; 
                gap: 8px;
            }}
        '''
    class_name = '.contact_reverse p'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_white};
                font-size: {g.typography_size_md}; 
                line-height: {g.typography_line_height_md}; 
                margin-bottom: 16px; 
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    cta = utils.aschii(cta)
    html = f'''
        <div class="contact_reverse">
            {icon}
            <p>
                {cta}<br>{contact}
            </p>
        </div>
    '''
    return html