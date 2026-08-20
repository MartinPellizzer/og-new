### generate list of facilities
### normalize / resolve (canonicalize)

### for each facility generate list of processes

### for each facility generate list of problems


import os
import json
import shutil

from lib import g
from lib import io
from lib import llm
from lib import polish
from lib import components

model_filepath = '/home/ubuntu/vault-tmp/llm/gemma-4-12b-it-Q4_K_S.gguf'
model_filepath = '/home/ubuntu/vault-tmp/llm/gemma-4-12B-it-qat-UD-Q4_K_XL.gguf'

import sectors_data


def sectors_gen():
    prompt = f'''
        Write a list of sectors where ozone is being used.
        Use as few words as possible.
        Write only one sector per line.
        By sectors, i mean like food and beverage, hospitality, etc.
    '''.strip()
    print(prompt)
    reply = llm.reply(prompt, model_filepath)
    if '</think>' in reply: reply = reply.split('</think>')[1].strip()
    reply = polish.vanilla(reply)
    print()
    print('########################################################################')
    print(reply)
    print('########################################################################')
    print()
def facility_gen():
    prompt = f'''
        Write a list of facility types in the food industry where ozone is being used.
        Use as few words as possible.
        Write only one facility per line.
        Give me the normalized, canonical name for each facility type.
        Use the minimum amount of words as term for each facility type.
    '''.strip()
    print(prompt)
    reply = llm.reply(prompt, model_filepath)
    if '</think>' in reply: reply = reply.split('</think>')[1].strip()
    reply = polish.vanilla(reply)
    print()
    print('########################################################################')
    print(reply)
    print('########################################################################')
    print()

def render_sector_html():
    input_data = sectors_data.data
    for sector_item in input_data:
        sector_name = sector_item['sector_name']
        sector_name_simple = sector_item['sector_name_simple']
        sector_slug = sector_item['sector_slug']
        ###
        children = []
        for candidate_child_item in input_data:
            if sector_item['sector_name_normalize'] == candidate_child_item['sector_parent_name_normalize']:
                print(sector_item['sector_name'])
                children.append(candidate_child_item)
        ###
        html_h1 = f'''<h1>{sector_name_simple}</h1>'''
        html_children = ''
        if children != []:
            html_children += '<ul>'
            for child in children:
                html_children += f'''<li><a href="/settori/{child['sector_slug']}">{child['sector_name']}</a></li>'''
            html_children += '</ul>'
        
        ###
        article_html = f'''
            {html_h1}
            {html_children}
        '''

        ###
        url_slug = f'''settori/{sector_slug}'''
        meta_title = f'''{sector_name_simple}'''
        html = f''' 
            <!DOCTYPE html>
            <html lang="it">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="/styles.css">
                <title>{meta_title}</title>
            </head>
            <body>
                {components.header_light_logo()}
                <main class="listing container-md">
                    {article_html}
                </main>
                {components.footer_dark()}
            </body>
            </html>
        '''.strip()
        ###
        html_folderpath = f'{g.website_folderpath}/{url_slug}'
        io.folders_recursive_gen(html_folderpath)
        html_filepath = f'{g.website_folderpath}/{url_slug}/index.html'
        with open(html_filepath, 'w') as f: f.write(html)
        print(html_filepath)

def render_sectors_html():

    input_data = sectors_data.data
    for sector_item in input_data:
        sector_name = sector_item['sector_name']
        sector_name_simple = sector_item['sector_name_simple']
        sector_slug = sector_item['sector_slug']
        ###
        children = []
        for candidate_child_item in input_data:
            if sector_item['sector_name_normalize'] == candidate_child_item['sector_parent_name_normalize']:
                print(sector_item['sector_name'])
                children.append(candidate_child_item)
        ###
        html_children = ''
        if children != []:
            html_children += '<ul>'
            for child in children:
                html_children += f'''<li><a href="/settori/{child['sector_slug']}">{child['sector_name']}</a></li>'''
            html_children += '</ul>'
        
    sectors_lvl_1 = [item for item in input_data if item['sector_parent_name_normalize'] == None]

    ###
    html_h1 = f'''<h1>Settori</h1>'''
    html_sectors = ''
    if sectors_lvl_1 != []:
        html_sectors += '<ul>'
        for sector in sectors_lvl_1:
            html_sectors += f'''<li><a href="/settori/{sector['sector_slug']}">{sector['sector_name']}</a></li>'''
        html_sectors += '</ul>'
    article_html = f'''
        {html_h1}
        {html_sectors}
    '''

    ###
    url_slug = f'''settori'''
    meta_title = f'''Settori'''
    html = f''' 
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="/styles.css">
            <title>{meta_title}</title>
        </head>
        <body>
            {components.header_light_logo()}
            <main class="listing container-md">
                {article_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''.strip()
    ###
    html_folderpath = f'{g.website_folderpath}/{url_slug}'
    io.folders_recursive_gen(html_folderpath)
    html_filepath = f'{g.website_folderpath}/{url_slug}/index.html'
    with open(html_filepath, 'w') as f: f.write(html)
    print(html_filepath)

def run():
    shutil.copy2(f'styles.css', f'{g.WEBSITE_FOLDERPATH}/styles.css')

    output_folderpath = f'{g.WEBSITE_FOLDERPATH}/settori'
    try: shutil.rmtree(output_folderpath)
    except: pass
    io.folders_recursive_gen(output_folderpath)
    ###

    render_sectors_html()
    ###
    render_sector_html()

run()
