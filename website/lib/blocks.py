from lib import g
from lib import utils

from lib import components

css_filepath = g.styles_blocks_filepath
css_mobile_filepath = g.styles_blocks_mobile_filepath

####################################################
# ;headers
####################################################
def heading_default_1(title, paragraph):
    utils.css_create_if_not_exists(css_filepath)
    utils.css_create_if_not_exists(css_mobile_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    with open(css_mobile_filepath) as f: css_mobile = f.read()
    class_name = '.heading_default_1'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                display: flex;
                align-items: center;
                gap: 48px;
                margin-bottom: 32px;
            }}
        '''
    class_name = '.heading_default_1'
    if f'{class_name} ' not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                    gap: 0;
                }}
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    with open(css_mobile_filepath, 'w') as f: f.write(css_mobile)
    ###
    html = f'''
        <div class="heading_default_1">
            <div style="flex: 3;">
                {title}
            </div>
            <div style="flex: 2;">
                {paragraph}
            </div>
        </div>
    '''
    return html

def heading_default_2(title, paragraph):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.heading_default_2'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                max-width: 768px;
                margin-right: auto;
                margin-left: auto;
                display: flex;
                flex-direction: column;
                margin-bottom: 32px;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html = f'''
        <div class="heading_default_2">
            {title}
            {paragraph}
        </div>
    '''
    return html

####################################################
# ;cards
####################################################
def card_default_1(title, paragraph, icon, link='', suptitle=''):
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
    html_link = ''
    if link != '':
        html_link = f'''
            {link}
            <svg style="height: 24px;" xmlns="http://www.w3.org/2000/svg" fill="none"
                viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                    d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
            </svg>
        '''
    html = f'''
        <div class="card_default_1">
            {suptitle}
            {title}
            {paragraph}
            <div style="margin-bottom: 64px;"></div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                {icon}
                <div style="display: flex; gap: 8px;">
                    {html_link}
                </div>
            </div>
        </div>
    '''
    return html

def card_default_2(icon, title, paragraph):
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
    html = f'''
        <div class="card_default">
            {icon}
            <div style="margin-bottom: 1.6rem;"></div>
            {title}
            {paragraph}
        </div>
    '''
    return html

def card_itp_default(image, title, paragraph):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.card_itp_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                background-color: {g.color_gray_extralight}; 
                padding: 3.2rem; 
                border-radius: 1.6rem;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html = f'''
        <div class="card_itp_default">
            {image}
            <div style="margin-bottom: 1.6rem;"></div>
            {title}
            {paragraph}
        </div>
    '''
    return html

####################################################
# ;contacts
####################################################
def contact_card_default(icon, cta, contact):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.contact_card_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                background-color: {g.color_gray_extralight};
                padding: 1.6rem;
                display: flex; 
                justify-content: space-between; 
                align-items: center;
                gap: 8px;
            }}
        '''
    class_name = '.contact_card_default_content'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                display: flex; 
                gap: 8px;
            }}
        '''
    class_name = '.contact_card_default_content p'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                font-size: {g.typography_size_md}; 
                line-height: {g.typography_line_height_md}; 
            }}
        '''
                # margin-bottom: 16px; 
    # class_name = '.contact_card_default_content p:nth-last-of-type(1)'
    # if f'{class_name} ' not in css:
    #     css += f'''
    #         {class_name} {{
    #             margin-bottom: 0; 
    #         }}
    #     '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    cta = utils.aschii(cta)
    html = f'''
        <div class="contact_card_default">
            <div class="contact_card_default_content">
                {icon}
                <p>{cta}<br>{contact}</p>
            </div>
            <svg style="height: 32px; color: #0f1f2e;" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
            </svg>
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

