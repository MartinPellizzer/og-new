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

def aggregate():
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/nouns_phrases/passages'
    filter_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/sectors/sort/Food & Beverage'
    input_filenames = os.listdir(input_folderpath)
    filter_filenames = [filename.split('.')[0] for filename in os.listdir(filter_folderpath)]
    # print(filter_filenames[:10])
    i = 0
    terms_aggregates = []
    for input_filename in input_filenames[i:]:
        i += 1
        print(f'{i}/{len(input_filenames)}')
        input_filename_base = input_filename.split('.')[0]
        input_filepath = f'{input_folderpath}/{input_filename}'
        input_data = io.json_read(input_filepath)
        # print(json.dumps(input_data, indent=4))
        # print(input_filename)
        # quit()
        if input_filename_base not in filter_filenames: continue
        terms = input_data['terms']
        # terms = sorted(terms)
        # print(json.dumps(input_data, indent=4))
        # print(input_filename)
        # quit()
        for term in terms:
            term_name = term['term'].lower().strip()
            term_passages = term['passages']
            found = False
            for term_aggregate in terms_aggregates:
                # print(term_aggregate, '->', term)
                if term_aggregate['name'] == term_name:
                    for term_passage in term_passages: 
                        term_aggregate['passages'].append(term_passage)
                        term_aggregate['passages'] = list(set(term_aggregate['passages']))
                    term_aggregate['frequency_total'] += 1
                    found = True
                    break
            if not found:
                term_aggregate = {
                    'name': term_name,
                    'passages': term_passages,
                    'frequency_total': 1,
                }
                terms_aggregates.append(term_aggregate)
    ###
    terms_aggregates = sorted(terms_aggregates, key=lambda x: x['frequency_total'], reverse=True)
    terms_aggregates_filter = [term for term in terms_aggregates if term['frequency_total'] > 1]
    for term in terms_aggregates:
        if term['frequency_total'] > 1:
            print(json.dumps(term, indent=4))
    print(len(terms_aggregates_filter))
    output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/resolve/pubmed/aggregate'
    io.folders_recursive_gen(output_folderpath)
    output_filepath = f'{output_folderpath}/data.json'
    io.json_write(output_filepath, terms_aggregates)

def find_candidates(input_name, output_terms):
    candidate_terms = []
    for output_term in output_terms:
        for output_name in output_term['names']:
            # print(input_term, '->', output_term['names'])
            input_words = input_name.split(' ')
            output_words = output_name.split(' ')
            found = False
            for input_word in input_words:
                if input_word in output_words:
                    candidate_terms.append(output_term)
                    found = True
                    break
            if found:
                break
    return candidate_terms

def find_term_exact_match(input_name, output_terms):
    for output_term in output_terms:
        for output_name in output_term['names']:
            if input_name == output_name:
                print(f'DONE: {input_name}')
                return True
    return False

def resolve_manual_console():
    ### INPUT
    ### loop input terms and ask user to add new term or add term as var to another term
    # print('')
    input_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/resolve/pubmed/aggregate/data.json'
    input_terms = io.json_read(input_filepath)
    ###
    output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/resolve/pubmed/resolve'
    io.folders_recursive_gen(output_folderpath)
    output_filepath = f'{output_folderpath}/data.json'
    if os.path.exists(output_filepath):
        output_terms = io.json_read(output_filepath)
    else:
        output_terms = []
    # 1. serve new term
    max_num = 100
    for i, input_term in enumerate(input_terms[:max_num]):
        input_name = input_term['name']
        sample_passage = input_term['passages'][0]
        ### CHECK IF DONE ALREADY
        found = find_term_exact_match(input_name, output_terms)
        if found: continue
        ### FUNC: find candidates
        candidate_terms = find_candidates(input_name, output_terms)

        running = True
        while running:
            # 3. propose string match if found
            print()
            print('################################################')
            print(f'{i}/{max_num}')
            print(input_name)
            print(sample_passage)
            if candidate_terms == []:
                print('[]')
            else:
                for candidate_term in candidate_terms:
                    print(candidate_term)

            # 4. ask input
            raw = input('>> ')
            raw = raw.strip()

            if raw != '':
                if raw.startswith('add '):
                    raw = raw.replace('add ', '')
                    for output_term in output_terms:
                        found = False
                        for output_name in output_term['names']:
                            # print('here')
                            # print(raw, '->', output_name)
                            if raw == output_name:
                                # print(output_term)
                                output_term['names'].append(input_name)
                                output_term['frequency_total'] += input_term['frequency_total']
                                running = False
                                found = True
                                break
                        if found:
                            break
                else:
                    candidate_terms = find_candidates(raw, output_terms)
                    continue
            else:
                output_term = {
                    'names': [input_name],
                    'frequency_total': input_term['frequency_total'],
                }
                output_terms.append(output_term)

                running = False

                # if candidate_terms != []:
                    # for candidate_term in candidate_terms:
                        # print(candidate_term)
                # quit()

                io.json_write(output_filepath, output_terms)

def categoryze_llm():
    input_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/resolve/pubmed/resolve/data.json'
    input_data = io.json_read(input_filepath)
    aggregate_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/resolve/pubmed/aggregate/data.json'
    aggregate_data = io.json_read(aggregate_filepath)
    # print(json.dumps(input_data, indent=4))
    # quit()
    # input_terms = [f'''{item['names'][0]}\n{item['']}''' for item in input_data]
    ###
    batches = []
    batch = []
    for item in input_data:
        term_name = item['names'][0]
        term_passage = ''
        for aggregate_item in aggregate_data:
            if aggregate_item['name'] == term_name:
                term_passage = aggregate_item['passages'][0]
                break
        batch.append({'term_name': term_name, 'term_passage': term_passage})
        if len(batch) >= 50:
            batches.append(batch)
            batch = []
    if batch != []:
        batches.append(batch)
    # print(json.dumps(batches[0], indent=4))
    # print(len(batches))
    # print(len(batches[0]))
    # print(len(batches[1]))
    # print(input_data)
    # print(len(input_data))
    # quit()
    ###
    terms_types = []
    for batch in batches:
        prompt_batch = f''
        for item in batch:
            prompt_batch += f'''term name: {item['term_name']}\nterm passage: {item['term_passage']}\n\n'''
        prompt = f'''
            For each term name in the following LIST, identify the most general type of thing that the term denotes. 
            For context, each term name have an associated term passage from where it was extracted, so you can identify the type better. 
            Do not use a predefined taxonomy. 
            If the appropriate type is unknown, create a short type label. 
            Use the same type label whenever multiple terms denote the same kind of thing.
            Reply only with the content asked.
            OUTPUT FORMAT:
            term name 1: type 1
            term name 2: type 2
            term name 3: type 3
            etc...
            LIST:
            {prompt_batch}
        '''.strip()
        # print(prompt)
        # quit()
        reply = llm.reply(prompt, model_filepath, max_tokens=4096)
        print()
        print('########################################')
        print(reply)
        print('########################################')
        print()
        lines = []
        for line in reply.strip().split('\n'):
            term_type = line.split(': ')[1]
            terms_types.append(term_type)
    terms_types = list(set(terms_types))
    for term_type in terms_types:
        print(term_type)

    ###
    types_resolved = None
    prompt = f'''
        Resolve equivalent type labels from the LIST below.
        Reply only with the asked content.
        OUTPUT FORMAT:
        resolved term 1
        resolved term 2
        resolved term 3
        etc...
        LIST:
        {terms_types}
    '''.strip()
    # print(prompt)
    # quit()
    reply = llm.reply(prompt, model_filepath, max_tokens=4096)
    print()
    print('########################################')
    print(reply)
    print('########################################')
    print()
    types_resolved = reply.strip().split('\n')

    ###
    for item in input_data:
        term_name = item['names'][0]
        term_passages = ''
        for aggregate_item in aggregate_data:
            found = False
            if aggregate_item['name'] == term_name:
                for passage in aggregate_item['passages'][:10]:
                    term_passages += passage + '\n'
                found = True
            if found:
                break
        prompt = f'''
            Choose the most appropriate type for the following CONCEPT from this LIST below. 
            Also, for the concept I'll give you also the passages for CONTEXT where the concept was extracted from, so you can categorize it better.
            Reply only with the asked content.
            CONCEPT:
            {term_name}
            CONTEXT:
            {term_passages}
            LIST:
            {types_resolved}
            OUTPUT FORMAT:
            concept: type
        '''.strip()
        # print(prompt)
        # quit()
        reply = llm.reply(prompt, model_filepath, max_tokens=4096)
        print()
        # print('########################################')
        # print(reply)
        # print('########################################')
        # print()
    quit()

def aggregate_relationships():
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/relationships/raw'
    filter_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/sectors/sort/Food & Beverage'
    input_filenames = os.listdir(input_folderpath)
    filter_filenames = [filename.split('.')[0] for filename in os.listdir(filter_folderpath)]
    # print(filter_filenames[:10])
    i = 0
    term_all = []
    terms_aggregates = []
    for input_filename in input_filenames[i:]:
        relationships_all = []
        i += 1
        print(f'{i}/{len(input_filenames)}')
        input_filename_base = input_filename.split('.')[0]
        input_filepath = f'{input_folderpath}/{input_filename}'
        input_data = io.json_read(input_filepath)
        # print(json.dumps(input_data, indent=4))
        # print(input_filename)
        # quit()
        if input_filename_base not in filter_filenames: continue
        terms = input_data['terms']
        # terms = sorted(terms)
        # print(json.dumps(input_data, indent=4))
        print(json.dumps(terms, indent=4))
        # print(input_filename)
        for term in terms:
            relationships = term['relationships']
            for relationship_str in relationships:
                print(type(relationship_str))
                for line in relationship_str.split('\n'):
                    line = line.strip()
                    line = line.replace('[', '')
                    line = line.replace(']', '')
                    chunks = line.split(',')
                    if len(chunks) != 3: continue
                    relationships_all.append(chunks[1].strip())
                # quit()
        relationships_unique = sorted(list(set(relationships_all)))
        for x in sorted(relationships_all):
            print(x)
        for x in relationships_unique:
            print(x)
        print(len(relationships_all))
        print(len(relationships_unique))
        # prompt_batch = f''
        # for item in batch:
            # prompt_batch += f'''term name: {item['term_name']}\nterm passage: {item['term_passage']}\n\n'''
            # For context, each term name have an associated term passage from where it was extracted, so you can identify the type better. 
        """
        prompt = f'''
            For each term name in the following LIST, identify the most general type of thing that the term denotes. 
            Do not use a predefined taxonomy. 
            If the appropriate type is unknown, create a short type label. 
            Use the same type label whenever multiple terms denote the same kind of thing.
            Reply only with the content asked.
            OUTPUT FORMAT:
            term name 1: type 1
            term name 2: type 2
            term name 3: type 3
            etc...
            LIST:
            {relationships_unique}
        '''.strip()
        # print(prompt)
        # quit()
        reply = llm.reply(prompt, model_filepath, max_tokens=4096)
        print()
        print('########################################')
        print(reply)
        print('########################################')
        quit()
        """
        prompt = f'''
            Group equivalent relationships from the LIST below.
            By equivalent relationships I mean relationships that essentially mean the same thing.
            For each group choose the canonical relationship term from that group.
            Reply only with the asked content.
            Include all relationships of the list in the reply.
            OUTPUT FORMAT:
            canonical term 1: group equivalent relationship 1, group equivalent relationship 2, etc.
            canonical term 2: group equivalent relationship 1, group equivalent relationship 2, etc.
            canonical term 3: group equivalent relationship 1, group equivalent relationship 2, etc.
            etc...
            LIST:
            {relationships_unique}
        '''.strip()
        # print(prompt)
        # quit()
        reply = llm.reply(prompt, model_filepath, max_tokens=4096)
        print()
        print('########################################')
        print(reply)
        print('########################################')
        print()
        # types_resolved = reply.strip().split('\n')
        quit()
    

def run():
    print('RESOLVE >> pubmed')
    # resolve_sector_subsectors_manual(target_sector_name='Food & Beverage')
    # resolve_sector_subsectors_llm(target_sector_name='Food & Beverage')

    start = time.perf_counter()
    # aggregate()
    print(f'''
################################################################################
parse gmap() - execution time: 
---
SECONDS: {(time.perf_counter() - start)}
MINUTES: {(time.perf_counter() - start)/60}
HOURS:   {(time.perf_counter() - start)/60/60}
################################################################################
    ''')
    # resolve_manual_console()
    # categoryze_llm()

    aggregate_relationships()

run()
