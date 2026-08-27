import os
import json
import time
import shutil

from lib import g
from lib import io
from lib import llm

model_filepath = '/home/ubuntu/vault-tmp/llm/gemma-4-26B-A4B-it-UD-Q4_K_M.gguf'
# model_filepath = '/home/ubuntu/vault-tmp/llm/gemma-4-31B-it-Q4_K_M.gguf'

def parse_problems_extract_raw():
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/fetch/pubmed/ozone/json'
    output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/problems/raw'
    # try: shutil.rmtree(output_folderpath)
    # except: pass
    io.folders_recursive_gen(output_folderpath)
    ###
    relationships_found = []
    input_filenames = os.listdir(input_folderpath)
    i = 0
    for input_filename in input_filenames[i:]:
        i += 1
        print(f'{i}/{len(input_filenames)}')
        output_filepath = f'{output_folderpath}/{input_filename}'
        if os.path.exists(output_filepath): continue
        input_filepath = f'{input_folderpath}/{input_filename}'
        input_data = io.json_read(input_filepath)
        try: article_data = input_data['PubmedArticle'][0]['MedlineCitation']['Article']
        except: pass
        try: input_title = article_data['ArticleTitle']
        except: input_title = ''
        try: input_abstract = ' '.join(article_data['Abstract']['AbstractText'])
        except: continue
        # print(json.dumps(input_title, indent=4))
        # print(input_title)
        # print(input_abstract)
        # quit()
        content_to_extract = f'{input_title} {input_abstract}'
        prompt = f'''
            From the scientific study ABSTRACT below, extract all the relationships (observations) between ozone and the problems solved by ozone.
            Write each observation using this format: [ozone, solves, problem name]
            RULES:
            Always write the names of the probloems exactly how you find them in the text.
            Only reply with the relationships requested.
            If you can't find any of these relationships, reply with "NONE".
            ABSTRACT:
            {content_to_extract}
        '''.strip()
        prompt = prompt.replace('<text>', content_to_extract)
        reply = llm.reply(prompt, model_filepath, max_tokens=512)
        if '</think>' in reply:
            reply = reply.split('</think>')[1].strip()
        print('################################################################################')
        print(reply)
        print('########################################')
        # print(prompt)
        print('################################################################################')
        if 'NONE'.strip() not in reply.strip():
            relationships_found.append(reply)
            output_data = {
                'title': input_title,
                'abstract': input_abstract,
                'reply': reply,
            }
            io.json_write(
                output_filepath,
                output_data,
            )
        if i > 10:
            quit()
    print(len(relationships_found))
    # quit()

def parse_sector_extract_raw():
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/fetch/pubmed/ozone/json'
    output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/sector/raw'
    # try: shutil.rmtree(output_folderpath)
    # except: pass
    io.folders_recursive_gen(output_folderpath)
    ###
    relationships_found = []
    input_filenames = os.listdir(input_folderpath)
    i = 0
    for input_filename in input_filenames[i:]:
        i += 1
        print(f'{i}/{len(input_filenames)}')
        output_filepath = f'{output_folderpath}/{input_filename}'
        if os.path.exists(output_filepath): continue
        input_filepath = f'{input_folderpath}/{input_filename}'
        try: input_data = io.json_read(input_filepath)
        except: continue
        try: article_data = input_data['PubmedArticle'][0]['MedlineCitation']['Article']
        except: pass
        try: input_title = article_data['ArticleTitle']
        except: input_title = ''
        try: input_abstract = ' '.join(article_data['Abstract']['AbstractText'])
        except: continue
        # print(json.dumps(input_title, indent=4))
        # print(input_title)
        # print(input_abstract)
        # quit()
        '''
            Water
            Food & Beverage
            Agriculture
            Healthcare
            Hospitality
            Buildings
            Manufacturing
            Energy
            Environment
            Transportation
            Residential
            Research
        '''
        content_to_extract = f'{input_title} {input_abstract}'
        prompt = f'''
            Categorize the scientific study ABSTRACT below.
            Choose only one of the CATEGORIES below.

            ABSTRACT:
            {content_to_extract}

            CATEGORIES:
            Water
            Food & Beverage
            Agriculture
            Healthcare
            Hospitality
            Buildings
            Manufacturing
            Energy
            Environment
            Transportation
            Residential
            Research
            Others

            RULES:
            Reply only with the category.
            If you think no category represents the abtract, reply with "Others".
        '''.strip()
        prompt = prompt.replace('<text>', content_to_extract)
        reply = llm.reply(prompt, model_filepath, max_tokens=512)
        if '</think>' in reply:
            reply = reply.split('</think>')[1].strip()
        print('################################################################################')
        print(reply)
        print('########################################')
        # print(prompt)
        print('################################################################################')
        if 'Altro'.strip() not in reply.strip():
            relationships_found.append(reply)
            output_data = {
                'title': input_title,
                'abstract': input_abstract,
                'reply': reply,
            }
            io.json_write(
                output_filepath,
                output_data,
            )
        # if i > 10:
            # quit()
    print(len(relationships_found))
    # quit()

def parse_sector_analyze():
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/sector/raw'
    input_filenames = os.listdir(input_folderpath)
    alimentare_count = 0
    for input_filename in input_filenames:
        input_filepath = f'{input_folderpath}/{input_filename}'
        input_data = io.json_read(input_filepath)
        # print(input_data['reply'])
        if input_data['reply'] == 'Alimentare e Bevande':
            alimentare_count += 1
            print(input_data['reply'])
        # quit()
    print(alimentare_count)

def parse_sector_sort_raw():
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/sector/raw'
    input_filenames = os.listdir(input_folderpath)
    alimentare_count = 0
    for input_filename in input_filenames:
        input_filepath = f'{input_folderpath}/{input_filename}'
        input_data = io.json_read(input_filepath)
        # print(input_data['reply'])
        ###
        sector_foldername = input_data['reply']
        output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/sector/sort/{sector_foldername}'
        io.folders_recursive_gen(output_folderpath)
        output_filepath = f'{output_folderpath}/{input_filename}'
        io.json_write(output_filepath, input_data)

def parse_sector_problems_extract_raw(sector_name):
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/sector/sort/{sector_name}'
    output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/problems/sort/{sector_name}'
    # try: shutil.rmtree(output_folderpath)
    # except: pass
    io.folders_recursive_gen(output_folderpath)
    ###
    relationships_found = []
    input_filenames = os.listdir(input_folderpath)
    i = 0
    for input_filename in input_filenames[i:]:
        i += 1
        print(f'{i}/{len(input_filenames)}')
        output_filepath = f'{output_folderpath}/{input_filename}'
        if os.path.exists(output_filepath): continue
        input_filepath = f'{input_folderpath}/{input_filename}'
        input_data = io.json_read(input_filepath)
        input_title = input_data['title']
        input_abstract = input_data['abstract']
        content_to_extract = f'{input_title} {input_abstract}'
            # From the scientific study ABSTRACT below, extract all the relationships between ozone and the problems solved by ozone.
        prompt = f'''
            From the scientific study ABSTRACT below, extract all the problems solved by ozone.
            Also, for each problem write the passage (single sentence, or block of text) from which the problem was exracted.
            OUTPUT STRUCTURE:
            Reply using the following JSON structure:
            [
                {{"problem_name": "insert problem name 1 here", "passage": "insert passage text where you extracted this problem here"}},
                {{"problem_name": "insert problem name 2 here", "passage": "insert passage text where you extracted this problem here"}},
                {{"problem_name": "insert problem name 3 here", "passage": "insert passage text where you extracted this problem here"}}
            ]
            Use the JSON structure only as reference for the output structure, extract as many problems as you find.
            RULES:
            Always write the names of the problems exactly how you find them in the text.
            Only reply with the json requested.
            If you can't extract anything based on the abstract provided, reply with "NONE".
            ABSTRACT:
            {content_to_extract}
        '''.strip()
        prompt = prompt.replace('<text>', content_to_extract)
        reply = llm.reply(prompt, model_filepath, max_tokens=512)
        print('################################################################################')
        print(reply)
        print('########################################')

        if 'NONE'.strip() in reply.strip(): continue

        if '</think>' in reply:
            reply = reply.split('</think>')[1].strip()

        reply = reply.replace('```json', '')
        reply = reply.replace('```', '')
        reply = reply.strip()

        json_data = {}
        try: json_data = json.loads(reply)
        except: pass 
        # print(reply)
        # quit()
        if json_data != {}:
            output_data = {
                'title': input_title,
                'abstract': input_abstract,
                'reply': json_data,
            }
            io.json_write(
                output_filepath,
                output_data,
            )
        # if i > 10:
            # quit()
    # quit()

def parse_sector_contaminations_extract_raw(sector_name):
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/sector/sort/{sector_name}'
    output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/contaminations/sort/{sector_name}'
    # try: shutil.rmtree(output_folderpath)
    # except: pass
    io.folders_recursive_gen(output_folderpath)
    ###
    relationships_found = []
    input_filenames = os.listdir(input_folderpath)
    i = 0
    for input_filename in input_filenames[i:]:
        input_filename_base = input_filename.split('.')[0].strip()
        i += 1
        print(f'{i}/{len(input_filenames)}')
        output_filepath = f'{output_folderpath}/{input_filename}'
        if os.path.exists(output_filepath): continue
        input_filepath = f'{input_folderpath}/{input_filename}'
        input_data = io.json_read(input_filepath)
        input_title = input_data['title']
        input_abstract = input_data['abstract']
        content_to_extract = f'{input_title} {input_abstract}'
            # From the scientific study ABSTRACT below, extract all the relationships between ozone and the problems solved by ozone.
        prompt = f'''
            From the scientific study ABSTRACT below, extract all the contaminations that might be eliminated by ozone.
            Also, for each contamination write the passage (single sentence, or block of text) from which the contamination was exracted.
            OUTPUT STRUCTURE:
            Reply using the following JSON structure:
            [
                {{"contamination_name": "insert contamination name 1 here", "passage": "insert passage text where you extracted this contamination here"}},
                {{"contamination_name": "insert contamination name 2 here", "passage": "insert passage text where you extracted this contamination here"}},
                {{"contamination_name": "insert contamination name 3 here", "passage": "insert passage text where you extracted this contamination here"}}
            ]
            Use the JSON structure only as reference for the output structure, extract as many contaminations as you find.
            RULES:
            Always write the names of the contaminations exactly how you find them in the text.
            Only reply with the json requested.
            If you can't extract anything based on the abstract provided, reply with "NONE".
            ABSTRACT:
            {content_to_extract}
        '''.strip()
        prompt = prompt.replace('<text>', content_to_extract)
        reply = llm.reply(prompt, model_filepath, max_tokens=512)
        print('################################################################################')
        print(reply)
        print('########################################')

        if 'NONE'.strip() in reply.strip(): continue

        if '</think>' in reply:
            reply = reply.split('</think>')[1].strip()

        reply = reply.replace('```json', '')
        reply = reply.replace('```', '')
        reply = reply.strip()

        json_data = {}
        try: json_data = json.loads(reply)
        except: pass 
        # print(reply)
        # quit()
        if json_data != {}:
            output_data = {
                'source_id': input_filename_base,
                'title': input_title,
                'abstract': input_abstract,
                'reply': json_data,
            }
            io.json_write(
                output_filepath,
                output_data,
            )
        # if i > 10:
            # quit()
    # quit()

def parse_sector_sectors_extract_raw(sector_name):
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/sector/sort/{sector_name}'
    output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/sectors/sort/{sector_name}'
    # try: shutil.rmtree(output_folderpath)
    # except: pass
    io.folders_recursive_gen(output_folderpath)
    ###
    relationships_found = []
    input_filenames = os.listdir(input_folderpath)
    i = 0
    for input_filename in input_filenames[i:]:
        input_filename_base = input_filename.split('.')[0].strip()
        i += 1
        print(f'{i}/{len(input_filenames)}')
        output_filepath = f'{output_folderpath}/{input_filename}'
        if os.path.exists(output_filepath): continue
        input_filepath = f'{input_folderpath}/{input_filename}'
        input_data = io.json_read(input_filepath)
        input_title = input_data['title']
        input_abstract = input_data['abstract']
        content_to_extract = f'{input_title} {input_abstract}'
            # From the scientific study ABSTRACT below, extract all the relationships between ozone and the problems solved by ozone.
        prompt = f'''
            From the scientific study ABSTRACT below, extract all the sectors (industries) where ozone can be used.
            Also, for each sector write the passage (single sentence, or block of text) from which the sector was exracted.
            OUTPUT STRUCTURE:
            Reply using the following JSON structure:
            [
                {{"sector_name": "insert sector name 1 here", "passage": "insert passage text where you extracted this sector here"}},
                {{"sector_name": "insert sector name 2 here", "passage": "insert passage text where you extracted this sector here"}},
                {{"sector_name": "insert sector name 3 here", "passage": "insert passage text where you extracted this sector here"}}
            ]
            Use the JSON structure only as reference for the output structure, extract as many sectors as you find.
            RULES:
            Always write the names of the sectors exactly how you find them in the text.
            Only reply with the json requested.
            If you can't extract anything based on the abstract provided, reply with "NONE".
            ABSTRACT:
            {content_to_extract}
        '''.strip()
        prompt = prompt.replace('<text>', content_to_extract)
        reply = llm.reply(prompt, model_filepath, max_tokens=512)
        print('################################################################################')
        print(reply)
        print('########################################')
        if 'NONE'.strip() in reply.strip(): continue
        if '</think>' in reply:
            reply = reply.split('</think>')[1].strip()
        reply = reply.replace('```json', '')
        reply = reply.replace('```', '')
        reply = reply.strip()
        json_data = {}
        try: json_data = json.loads(reply)
        except: pass 
        # print(reply)
        # quit()
        if json_data != {}:
            output_data = {
                'source_id': input_filename_base,
                'title': input_title,
                'abstract': input_abstract,
                'reply': json_data,
            }
            io.json_write(
                output_filepath,
                output_data,
            )
        # if i > 10:
            # quit()
    # quit()

def parse_sector_subsectors_extract_raw(sector_name):
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/sector/sort/{sector_name}'
    output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/subsectors/sort/{sector_name}'
    # try: shutil.rmtree(output_folderpath)
    # except: pass
    io.folders_recursive_gen(output_folderpath)
    ###
    relationships_found = []
    input_filenames = os.listdir(input_folderpath)
    i = 0
    for input_filename in input_filenames[i:]:
        input_filename_base = input_filename.split('.')[0].strip()
        i += 1
        print(f'{i}/{len(input_filenames)}')
        output_filepath = f'{output_folderpath}/{input_filename}'
        if os.path.exists(output_filepath): continue
        input_filepath = f'{input_folderpath}/{input_filename}'
        input_data = io.json_read(input_filepath)
        input_title = input_data['title']
        input_abstract = input_data['abstract']
        content_to_extract = f'{input_title} {input_abstract}'
            # From the scientific study ABSTRACT below, extract all the relationships between ozone and the problems solved by ozone.
        prompt = f'''
            From the scientific study ABSTRACT below about the {sector_name} sector, extract all the subsectors (subindustries) where ozone can be used.
            Also, for each subsector write the passage (single sentence, or block of text) from which the subsector was exracted.
            OUTPUT STRUCTURE:
            Reply using the following JSON structure:
            [
                {{"subsector_name": "insert subsector name 1 here", "passage": "insert passage text where you extracted this subsector here"}},
                {{"subsector_name": "insert subsector name 2 here", "passage": "insert passage text where you extracted this subsector here"}},
                {{"subsector_name": "insert subsector name 3 here", "passage": "insert passage text where you extracted this subsector here"}}
            ]
            Use the JSON structure only as reference for the output structure, extract as many subsectors as you find.
            RULES:
            Always write the names of the subsectors exactly how you find them in the text.
            Only reply with the json requested.
            If you can't extract anything based on the abstract provided, reply with "NONE".
            ABSTRACT:
            {content_to_extract}
        '''.strip()
        prompt = prompt.replace('<text>', content_to_extract)
        reply = llm.reply(prompt, model_filepath, max_tokens=512)
        print('################################################################################')
        print(reply)
        print('########################################')
        if 'NONE'.strip() in reply.strip(): continue
        if '</think>' in reply:
            reply = reply.split('</think>')[1].strip()
        reply = reply.replace('```json', '')
        reply = reply.replace('```', '')
        reply = reply.strip()
        json_data = {}
        try: json_data = json.loads(reply)
        except: pass 
        # print(reply)
        # quit()
        if json_data != {}:
            output_data = {
                'source_id': input_filename_base,
                'title': input_title,
                'abstract': input_abstract,
                'reply': json_data,
            }
            io.json_write(
                output_filepath,
                output_data,
            )
        # if i > 10:
            # quit()
    # quit()

def run():
    print('parse >> pubmed')

    # parse_sector_extract_raw() ### WARNING: takes many many hours (nightly running)

    start = time.perf_counter()
    # parse_problems_extract_raw() ### WARNING: takes many many hours (nightly running)
    print(f'observations symptoms() - execution time: ', time.perf_counter() - start)

    # parse_sector_analyze() ### WARNING: takes many many hours (nightly running)

    # parse_sector_sort_raw()
    # parse_sector_contaminations_extract_raw(sector_name='Food & Beverage')
    # parse_sector_problems_extract_raw(sector_name='Food & Beverage')
    # parse_sector_sectors_extract_raw(sector_name='Food & Beverage')
    parse_sector_subsectors_extract_raw(sector_name='Food & Beverage')


run()
