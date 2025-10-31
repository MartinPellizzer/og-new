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
                max-width: {g.container_xs};
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

def heading_default_3(title, paragraph, button):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.heading_default_3'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                max-width: {g.container_xs};
                margin-right: auto;
                margin-left: auto;
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-bottom: 32px;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html = f'''
        <div class="heading_default_3">
            {title}
            <div style="margin-bottom: 0.8rem"></div>
            {paragraph}
            <div style="display: flex;">
                {button}
            </div>
        </div>
    '''
    return html

def heading_2col_1(title, button):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.heading_2col_1'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                max-width: {g.container_xl};
                margin-right: auto;
                margin-left: auto;
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 32px;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html = f'''
        <div class="heading_2col_1">
            {title}
            <div style="display: flex;">
                {button}
            </div>
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
                box-shadow: rgba(0, 0, 0, 0.04) 0px 3px 5px;
                display: flex; 
                flex-direction: column; 
                justify-content: space-between;
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
            <div>
            {suptitle}
            {title}
            {paragraph}
            <div style="margin-bottom: 64px;"></div>
            </div>
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

def card_ihc_default(image, heading, content):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.card_ihc_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                background-color: {g.color_gray_extralight}; 
                border-radius: 1.6rem;
            }}
        '''
    class_name = '.card_ihc_default img'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                border-top-left-radius: 1.6rem;
                border-top-right-radius: 1.6rem;
                border-radius: 1.6rem;
                height: 16rem;
                object-fit: cover;
            }}
        '''
    class_name = '.card_hc_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{ 
                padding-left: 2.4rem; 
                padding-right: 2.4rem; 
                padding-left: 1.6rem; 
                padding-right: 1.6rem; 
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html = f'''
        <div class="card_ihc_default">
            {image}
            <div style="margin-bottom: 1.6rem;"></div>
            <div class="card_hc_default">
                {heading}
                {content}
            </div>
        </div>
    '''
    return html

def card_3_default(heading, content):
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.card_3_default'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                background-color: {g.color_gray_extralight}; 
                border-radius: 1.6rem;
                padding: 1.6rem;
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html = f'''
        <div class="card_3_default">
            {heading}
            {content}
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

def contact_col():
    utils.css_create_if_not_exists(css_filepath)
    ###
    with open(css_filepath) as f: css = f.read()
    class_name = '.contact_col'
    if f'{class_name} ' not in css:
        css += f'''
            {class_name} {{
                display: flex; 
                flex-direction: column; 
                gap: 16px;
            }}
        '''
    with open(css_filepath, 'w') as f: f.write(css)
    ###
    html_contact_card_default_1 = contact_card_default(
        icon = f'''
            <svg style="color: #0f1f2e;" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
                <path d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm320-280L160-640v400h640v-400L480-440Zm0-80 320-200H160l320 200ZM160-640v-80 480-400Z" />
            </svg>
        ''',
        cta = f'''
            Mandaci una email
        ''',
        contact = f'''
            elena@ozonogroup.it
        ''',
    )
    html_contact_card_default_2 = contact_card_default(
        icon = f'''
            <svg style="color: #0f1f2e;" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
                <path d="M798-120q-125 0-247-54.5T329-329Q229-429 174.5-551T120-798q0-18 12-30t30-12h162q14 0 25 9.5t13 22.5l26 140q2 16-1 27t-11 19l-97 98q20 37 47.5 71.5T387-386q31 31 65 57.5t72 48.5l94-94q9-9 23.5-13.5T670-390l138 28q14 4 23 14.5t9 23.5v162q0 18-12 30t-30 12ZM241-600l66-66-17-94h-89q5 41 14 81t26 79Zm358 358q39 17 79.5 27t81.5 13v-88l-94-19-67 67ZM241-600Zm358 358Z" />
            </svg>
        ''',
        cta = f'''
            Chiamaci
        ''',
        contact = f'''
            +39 0423 952833
        ''',
    )
    ###
    html = f'''
        <div class="contact_col">
            {html_contact_card_default_1}
            {html_contact_card_default_2}
        </div>
    '''
    return html

    