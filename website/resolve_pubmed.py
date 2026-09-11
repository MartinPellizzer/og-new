import os
import json
import time
import shutil

from lib import g
from lib import io
from lib import llm

import sectors_data

model_filepath = '/home/ubuntu/vault-tmp/llm/gemma-4-26B-A4B-it-UD-Q4_K_M.gguf'

def resolve_sector_subsectors_manual(target_sector_name='Food & Beverage'):
    subsectors_ideas = f'''
        Beverage sector
        Dairy sector
        Egg sector
        Fish sector
        Fruit sector
        Grain sector
        Meat sector
        Nut sector
        Pet sector
        Seafood sector
        Spice sector
        Vegetable sector
    '''

def resolve_sector_subsectors_llm(target_sector_name='Food & Beverage'):
    subsectors_ideas = f'''
        Beverage sector
        Dairy sector
        Egg sector
        Fish sector
        Fruit sector
        Grain sector
        Meat sector
        Nut sector
        Pet sector
        Seafood sector
        Spice sector
        Vegetable sector
    '''
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/subsectors/sort/{target_sector_name}'
    ###
    input_filenames = os.listdir(input_folderpath)
    not_found_count = 0
    subsectors_names = []
    i = 0
    for input_filename in input_filenames[i:]:
        input_filename_base = input_filename.split('.')[0].strip()
        i += 1
        # print(f'{i}/{len(input_filenames)}')
        input_filepath = f'{input_folderpath}/{input_filename}'
        input_data = io.json_read(input_filepath)
        output_data = {}
        for input_item in input_data['reply']:
            output_data['resource_sector'] = target_sector_name
            output_data['resource_subsector'] = input_item['subsector_name']
            output_data['resource_subsector_passage'] = input_item['passage']
            output_data['resource_id'] = input_data['source_id']
            output_data['resource_title'] = input_data['title']
            output_data['resource_abstract'] = input_data['abstract']
        print(json.dumps(output_data, indent=4))
        quit()
        for item in input_data['reply']:
            try: 
                print(item['subsector_name'])
                subsectors_names.append(item['subsector_name'])
            except: not_found_count += 1
    print(not_found_count)
    ###
    prompt_subsectors_names = '\n'.join(subsectors_names)
    prompt = f'''
        I need to create a list of subsectors of the food and beverage sector.
        I need to create this list of subsectors using the list below and the MECE principle (Mutually Exclusive, Collectively Exhaustive).
        Name the subsectors using as few words as possible, ideally one word for sector.
        Reply only with the list of subsectors.
        Each item in the list of subsectors must be the umbrella term followed by the word "sector".
        LIST:
        {prompt_subsectors_names}
    '''.strip()
    # print(prompt)
    reply = llm.reply(prompt, model_filepath, max_tokens=512)
    print()
    print('########################################')
    print(reply)
    print('########################################')
    print()


def run():
    print('RESOLVE >> pubmed')
    resolve_sector_subsectors_manual(target_sector_name='Food & Beverage')
    resolve_sector_subsectors_llm(target_sector_name='Food & Beverage')

run()
