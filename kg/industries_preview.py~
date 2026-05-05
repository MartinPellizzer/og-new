import os
import json

from lib import io

DATABASE_FOLDERPATH = f'/home/ubuntu/vault/ozonogroup/database'
DATABASE_FOLDERPATH = f'C:/vault/ozonogroup/database'
PROJECT_FOLDERPATH = f'C:/vault/ozonogroup'

def studies__read_one_by_one(studies_folderpath):
    filepaths = sorted([f'{studies_folderpath}/{filename}' for filename in os.listdir(studies_folderpath)])
    for filepath in filepaths:
        json_data = io.json_read(filepath)
        abstract_title = json_data['PubmedArticle'][0]['MedlineCitation']['Article']['ArticleTitle']
        try: abstract_text = ' '.join(json_data['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract']['AbstractText'])
        except: pass
        # print(json.dumps(json_data, indent=4))
        print()
        print()
        print()
        print(abstract_title)
        print('---')
        print(abstract_text)
        print()
        print()
        print()
        input('>> ')
        # quit()


def nace_groups_print():
    groups_data = io.json_read(f'{DATABASE_FOLDERPATH}/studies/industries-grouped.json')
    # print(json.dumps(groups_data, indent=4))
    for group_lvl_1 in groups_data:
        # print(group_lvl_1['industry_nace_lvl_1'])
        for group_lvl_2 in group_lvl_1['industries_nace_lvl_2']:
            if 'win' in group_lvl_2['industry_llm']:
                print(
                    group_lvl_1['industry_nace_lvl_1'], '---',
                    group_lvl_2['industry_nace_lvl_2'], '---',
                    group_lvl_2['industry_llm'],'',
                )
    
studies__read_one_by_one(f'{PROJECT_FOLDERPATH}/studies/pubmed/ozone-wine/json')
# nace_groups_print()
