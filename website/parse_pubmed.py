import os
import json
import time
import shutil

from lib import g
from lib import io
from lib import llm

import sectors_data

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

def parse_nouns_llm():
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/fetch/pubmed/ozone/json'
    output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/nouns/raw'
    # try: shutil.rmtree(output_folderpath)
    # except: pass
    io.folders_recursive_gen(output_folderpath)
    ###
    # relationships_found = []
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
        content_to_extract = f'{input_title} {input_abstract}'
        prompt = f'''
            Extract all the nouns from the scientific study ABSTRACT below.
            ABSTRACT:
            {content_to_extract}
            RULES:
            Reply only with the nouns.
            Write the nouns exactly how you find them in the abstract.
            Write each noun in a new line.
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
        # relationships_found.append(reply)
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
    # print(len(relationships_found))
    # quit()

def parse_nouns_phrases_llm():
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/fetch/pubmed/ozone/json'
    output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/nouns_phrases/raw'
    # try: shutil.rmtree(output_folderpath)
    # except: pass
    io.folders_recursive_gen(output_folderpath)
    ###
    # relationships_found = []
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
        content_to_extract = f'{input_title} {input_abstract}'
            # Extract all the nouns from the scientific study ABSTRACT below.
        prompt = f'''
            Extract all noun phrases and nominal expressions from this document.
            Preserve the complete noun phrase when multiple words together form the expression.
            Do not extract verbs, adjectives, complete clauses, propositions, relationships, claims, or sentences.
            Do not interpret, normalize, categorize, merge, or judge the extracted terms.
            Do not use any assumptions about the subject matter or domain.
            Preserve the terminology exactly as used by the author.
            When a noun phrase contains a coordinated list of independent nouns, extract the individual noun phrases separately where grammatically appropriate.
            Return the extracted noun phrases in their original wording.
            ABSTRACT:
            {content_to_extract}
            RULES:
            Reply only with the nouns.
            Write the nouns exactly how you find them in the abstract.
            Write each noun in a new line.
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
        # relationships_found.append(reply)
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
    # print(len(relationships_found))
    # quit()

def parse_concepts_llm():
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/fetch/pubmed/ozone/json'
    output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/concepts/raw'
    # try: shutil.rmtree(output_folderpath)
    # except: pass
    io.folders_recursive_gen(output_folderpath)
    ###
    # relationships_found = []
    input_filenames = os.listdir(input_folderpath)
    i = 0
    for input_filename in input_filenames[i:100]:
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
        content_to_extract = f'{input_title} {input_abstract}'
        prompt = f'''
            Read the document ABSTRACT below and identify the distinct, semantically meaningful concepts expressed in it. Extract each concept as a self-contained phrase, using enough words to preserve the concept's meaning but no unnecessary words. Do not simply extract nouns or noun phrases mechanically. Combine words when they form a single meaningful concept and keep phrases separate when they represent different meanings. Infer concepts from the document's context rather than from a predefined list of domain categories.
            ABSTRACT:
            {content_to_extract}
            RULES:
            Reply only with the concepts.
            Write the concepts exactly how you find them in the abstract.
            Write each concept in a new line.
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
        # relationships_found.append(reply)
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
    # print(len(relationships_found))
    # quit()

def parse_expressions_llm():
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/fetch/pubmed/ozone/json'
    output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/expressions/raw'
    # try: shutil.rmtree(output_folderpath)
    # except: pass
    io.folders_recursive_gen(output_folderpath)
    ###
    # relationships_found = []
    input_filenames = os.listdir(input_folderpath)
    i = 0
    for input_filename in input_filenames[i:10]:
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
        content_to_extract = f'{input_title} {input_abstract}'
        prompt = f'''
            Extract the noun phrases and nominal expressions fron the ABSTRACT document below that refer to identifiable things, concepts, objects, substances, phenomena, activities, methods, measurements, locations, organisms, materials, or other subjects discussed by the author.
            Do not extract complete statements, claims, findings, relationships, events, or propositions.
            Do not extract a noun merely because it is grammatically a noun. Prefer the complete noun phrase when multiple words together form the referring expression.
            For each expression, preserve the wording used by the author. Do not normalize, classify, interpret, generalize, or merge expressions.
            Your task is linguistic extraction only. Do not decide what constitutes a domain entity.
            ABSTRACT:
            {content_to_extract}
            RULES:
            Reply only with the concepts.
            Write the concepts exactly how you find them in the abstract.
            Write each concept in a new line.
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
        # relationships_found.append(reply)
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
    # print(len(relationships_found))
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

def parse_sector_contaminations_categorize_raw(target_sector_name='Food & Beverage'):
    input_data = sectors_data.data
    for sector_item in input_data:
        sector_name_eng = sector_item['sector_name_eng']
        sector_name = sector_item['sector_name']
        sector_slug = sector_item['sector_slug']
        url_slug = f'''settori/{sector_slug}'''

        # print(sector_item)
        # quit()
        if sector_name_eng.lower() != target_sector_name.lower(): continue
        # print(json.dumps(sector_item, indent=4))
        # quit()

        ###
        regen = True
        json_data_filepath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/articles/{target_sector_name}.json'
        json_data = io.json_read(json_data_filepath, create=True)
        key = 'contaminants'
        if key not in json_data: json_data[key] = []
        if regen: json_data[key] = []
        if json_data[key] == []:
            pubmed_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/contaminations/sort/{sector_name_eng}'
            pubmed_filenames = sorted(os.listdir(pubmed_folderpath))
            for pubmed_filename in pubmed_filenames:
                pubmed_filepath = f'{pubmed_folderpath}/{pubmed_filename}'
                pubmed_data = io.json_read(pubmed_filepath)
                # print(json.dumps(pubmed_data, indent=4))
                # quit()
                pubmed_title = pubmed_data['title']
                pubmed_abstract = pubmed_data['abstract']
                content_to_extract = f'{pubmed_title} {pubmed_abstract}'
                for reply_item in pubmed_data['reply']:
                    contamination_name = reply_item['contamination_name']
                    print('################################################################################')
                    print(contamination_name)
                    print('################################################################################')
                    nature = None
                    _class = None
                    ### FACET A: NATURE
                    prompt = f'''
                        From the scientific study ABSTRACT below about the {sector_name_eng} sector, I extracted the following contamination: {contamination_name}.
                        Choose the best category name for this contaminant from the CATEGORIES below.
                        CATEGORIES NAMES:
                        - Biological
                        - Chemical
                        - Physical
                        ADDITIONAL CONTEXT:

                        - Biological: Living organisms or biologically active structures (Bacteria, viruses, fungi, yeasts, parasites, spores, biofilms)
                        - Chemical: Molecules, compounds, residues, toxins (Pesticides, aflatoxins, heavy metals, antibiotics, allergens, VOCs)
                        - Physical: Solid foreign matter or particulate material (Dust, glass, plastic, insects, soil, metal fragments)
                        RULES:
                        Pick only one category, the one that best represent the contamination.
                        Reply only with the category name.
                        ABSTRACT:
                        {content_to_extract}
                    '''.strip()
                    # print(prompt)
                    prompt = prompt.replace('<text>', content_to_extract)
                    reply = llm.reply(prompt, model_filepath, max_tokens=512)
                    print()
                    nature = reply

                    classes_names = f''
                    classes_context = f''
                    if nature.strip().lower() == 'biological':
                        classes_names = f'''
                            - Bacterium
                            - Virus
                            - Fungus
                            - Parasite
                            - Microbial Community
                        '''
                        classes_context = f'''
                            - Bacterium: including Prokaryotic bacteria (Salmonella, E. coli, Listeria, Pseudomonas)
                            - Virus: including All viruses (Norovirus, SARS-CoV-2, HAV)
                            - Fungus: including Molds and yeasts (Aspergillus, Penicillium, Saccharomyces, Candida)
                            - Parasite: including Protozoa and helminths (Cryptosporidium, Giardia, Angiostrongylu)
                            - Microbial Community: including Non-specific microbial populations (Microbiota, indigenous flora, total bacteria, microbial contamination)
                        '''
                    else: continue

                    ### FACET B: CLASS
                    prompt = f'''
                        From the scientific study ABSTRACT below about the {sector_name_eng} sector, I extracted the following contamination: {contamination_name}.
                        I also categorized this contamination as: {nature}.
                        Now, choose the best category name for this contaminant of nature {nature} from the CLASSES below.
                        CLASSES NAMES:
                        {classes_names}
                        ADDITIONAL CONTEXT:
                        {classes_context}
                        RULES:
                        Pick only one class, the one that best represent the contamination.
                        Reply only with the class name.
                        ABSTRACT:
                        {content_to_extract}
                    '''.strip()
                    # print(prompt)
                    prompt = prompt.replace('<text>', content_to_extract)
                    reply = llm.reply(prompt, model_filepath, max_tokens=512)
                    print()
                    _class = reply

                    ### FACET C: SPECIFIC ENTITY
                    prompt = f'''
                        From the scientific study ABSTRACT below about the {sector_name_eng} sector, I extracted the following contamination: {contamination_name}.
                        I also categorized this contamination as {nature} nature and {_class} class.
                        Now, identify its specific entity name.
                        By entity name I mean the canonical name of the individual biological target, chemical compound, physical contaminant, or composite being studied.
                        For example, canonical names are like Escherichia coli O157:H7, Listeria monocytogenes, Norovirus, Aflatoxin B1, Chlorpyrifos, Geosmin, Glass fragment, Indigenous microbiota.
                        RULES:
                        Pick only one canonical name, the one that best represent the contamination.
                        Reply only with the canonical name.
                        If the contamination can't match to a canonical entity name because is a category or something else: reply with "NONE".
                        ABSTRACT:
                        {content_to_extract}
                    '''.strip()
                    # print(prompt)
                    prompt = prompt.replace('<text>', content_to_extract)
                    reply = llm.reply(prompt, model_filepath, max_tokens=512)
                    print()
                    entity_name = reply
                    # quit()

                    ### FACET D: FUNCTIONAL ROLEs
                    prompt = f'''
                        From the scientific study ABSTRACT below about the {sector_name_eng} sector, I extracted the following contamination: {contamination_name}.
                        I also categorized this contamination as {nature} nature, {_class} class, and {entity_name} specific entity.
                        Now, choose the best functional role (or roles) for this contaminant from the FUNCTIONAL ROLE NAMES below.
                        FUNCTIONAL ROLE NAMES NAMES:
                        - Pathogen
                        - Spoilage Agent
                        - Indicator
                        - Beneficial Organism
                        - Producer
                        - Unknown / Unspecified
                        ADDITIONAL CONTEXT:
                        - Pathogen: Causes disease in humans, animals, or plants (examples are Salmonella, Listeria monocytogenes, Norovirus, Cryptosporidium)
                        - Spoilage Agent: Causes food or material deterioration without necessarily causing disease (examples are Pseudomonas fluorescens, Botrytis cinerea, Brettanomyces bruxellensis)
                        - Indicator: Used as a surrogate or hygiene indicator (examples are Coliforms, Total aerobic bacteria, Enterococci, E. coli generic)
                        - Beneficial Organism: Desirable microorganisms that may be unintentionally affected by ozone (examples are Lactic acid bacteria, probiotics, starter cultures, yeasts used in fermentation)
                        - Producer: (Produces undesirable metabolites, toxins, odors, or biofilms (examples are Aspergillus flavus (aflatoxin producer), Streptomyces (geosmin producer), biofilm-forming Listeria)
                        - Unknown / Unspecified: Functional role not stated or not applicable in the study (examples are Generic "bacteria", environmental isolates, unidentified microbiota)
                        - RULES:
                        Pick only the functional role/roles that best represent the contamination in the context of the study.
                        Reply only with the roles name separated by commas.
                        ABSTRACT:
                        {content_to_extract}
                    '''.strip()
                    # print(prompt)
                    prompt = prompt.replace('<text>', content_to_extract)
                    reply = llm.reply(prompt, model_filepath, max_tokens=512)
                    print()
                    functional_role_name = reply
                    # quit()

                    ### Facet E — BIOLOGICAL STATE
                    prompt = f'''
                        From the scientific study ABSTRACT below about the {sector_name_eng} sector, I extracted the following contamination: {contamination_name}.
                        I also categorized this contamination as {nature} nature, {_class} class, {entity_name} specific entity, {functional_role_name} functional role.
                        Now, choose the best biological state for this contaminant from the BIOLOGICAL STATE NAMES below.
                        BIOLOGICAL STATES:
                        - Vegetative
                        - Spore
                        - Biofilm
                        - Dormant
                        - Unknown / Unspecified
                        ADDITIONAL CONTEXT:
                        - Vegetative: Metabolically active, free-living cells or organisms (examples are E. coli, Listeria, yeasts, protozoa)
                        - Spore: Dormant, highly resistant reproductive or survival structure (examples are Bacillus spores, Clostridium spores, fungal spores)
                        - Biofilm: Surface-attached microbial community embedded in an extracellular matrix (examples are Listeria biofilm, Pseudomonas biofilm, mixed biofilm)
                        - Dormant: Viable but metabolically inactive forms other than spores (examples are VBNC bacteria, latent viruses, dormant fungal cells)
                        - Unknown / Unspecified: Biological state not reported or not applicable (examples are Most papers simply stating "Salmonella")
                        - RULES:
                        Pick only the biological state that best represent the contamination in the context of the study.
                        Reply only with the biological state name.
                        If the biological state is not applicable to the contamination, reply with "NONE".
                        ABSTRACT:
                        {content_to_extract}
                    '''.strip()
                    # print(prompt)
                    prompt = prompt.replace('<text>', content_to_extract)
                    reply = llm.reply(prompt, model_filepath, max_tokens=512)
                    print()
                    biological_state_name = reply
                    # quit()

                    json_data[key].append({
                        'contamination': contamination_name,
                        'nature': nature,
                        '_class': _class,
                        'entity': entity_name,
                        'functional_role': functional_role_name,
                        'biological_state': biological_state_name,
                    })
                    io.json_write(json_data_filepath, json_data)


def analyze_sector_subsectors_raw(target_sector_name):
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/subsectors/sort/{target_sector_name}'
    ###
    input_filenames = os.listdir(input_folderpath)
    not_found_count = 0
    i = 0
    for input_filename in input_filenames[i:]:
        input_filename_base = input_filename.split('.')[0].strip()
        i += 1
        # print(f'{i}/{len(input_filenames)}')
        input_filepath = f'{input_folderpath}/{input_filename}'
        input_data = io.json_read(input_filepath)
        # print(json.dumps(input_data, indent=4))
        # quit()
        for item in input_data['reply']:
            try: print(item['subsector_name'])
            except: not_found_count += 1
    print(not_found_count)

def analyze_sector_subsectors_group_llm(target_sector_name):
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
        # print(json.dumps(input_data, indent=4))
        # quit()
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

def nouns_phrases_string_match():
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/nouns_phrases/raw'
    output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/nouns_phrases/string_match'
    # try: shutil.rmtree(output_folderpath)
    # except: pass
    io.folders_recursive_gen(output_folderpath)
    ###
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
        ###
        study_id = input_filename.strip().split('.')[0]
        study_title = input_data['title']
        study_abstract = input_data['abstract']
        terms = []
        for term in input_data['reply'].strip().split('\n'):
            if term.lower() in study_abstract.lower():
                terms.append(term)
        ###
        output_data = {
            'study_id': study_id,
            'study_title': study_title,
            'study_abstract': study_abstract,
            'reply': terms,
        }
        io.json_write(
            output_filepath,
            output_data,
        )

def nouns_phrases_find_passages_llm():
    input_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/nouns_phrases/string_match'
    output_folderpath = f'{g.VAULT_FOLDERPATH}/ozonogroup/data/parse/pubmed/nouns_phrases/passages'
    # try: shutil.rmtree(output_folderpath)
    # except: pass
    io.folders_recursive_gen(output_folderpath)
    ###
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
        ###
        study_id = input_data['study_id']
        study_title = input_data['study_title']
        study_abstract = input_data['study_abstract']
        study_terms = input_data['reply']
        output_data = {
            'study_id': study_id,
            'study_title': study_title,
            'study_abstract': study_abstract,
            'terms': [],
        }
        for study_term in study_terms:
            prompt = f'''
                Extract all the passages from the ABSTRACT below where is mentioned this term: {study_term}.
                Write these passages exactly as they are in the abstract.
                By passage I mean the full sentence where the term is mentioned.
                Write one passage per new line.
                Reply only with the asked content.
                ABSTRACT:
                {study_abstract}
            '''.strip()
            reply = llm.reply(prompt, model_filepath, max_tokens=512)
            if '</think>' in reply:
                reply = reply.split('</think>')[1].strip()
            print()
            print('################################################################################')
            print(reply)
            print('################################################################################')

            output_item = {
                'term': study_term,
                'passages': reply.strip().split('\n'),
            }
            output_data['terms'].append(output_item)
        ###
        io.json_write(
            output_filepath,
            output_data,
        )
        # quit()

def run():
    print('parse >> pubmed')

    # parse_nouns_llm() ### WARNING: takes many many hours (nightly running)
    # parse_concepts_llm() ### WARNING: takes many many hours (nightly running)
    # parse_expressions_llm() ### WARNING: takes many many hours (nightly running)
    # parse_nouns_phrases_llm() ### WARNING: takes many many hours (nightly running)
    nouns_phrases_string_match()
    nouns_phrases_find_passages_llm() ### WARNING: takes many many hours (nightly running)

    # parse_sector_extract_raw() ### WARNING: takes many many hours (nightly running)

    start = time.perf_counter()
    # parse_problems_extract_raw() ### WARNING: takes many many hours (nightly running)
    print(f'observations symptoms() - execution time: ', time.perf_counter() - start)

    # parse_sector_analyze() ### WARNING: takes many many hours (nightly running)

    # parse_sector_sort_raw()
    # parse_sector_contaminations_extract_raw(sector_name='Food & Beverage')
    # parse_sector_problems_extract_raw(sector_name='Food & Beverage')
    # parse_sector_sectors_extract_raw(sector_name='Food & Beverage')

    # parse_sector_contaminations_categorize_raw(target_sector_name='Food & Beverage')

    # parse_sector_subsectors_extract_raw(sector_name='Food & Beverage')
    # analyze_sector_subsectors_group_llm(target_sector_name='Food & Beverage')
    # analyze_sector_subsectors_raw(target_sector_name='Food & Beverage')

run()
