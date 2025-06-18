import os
import json
from tkinter import *

import chromadb
from chromadb.utils import embedding_functions

from oliark_io import json_read, json_write
from oliark_llm import llm_reply

model_filepath = '/home/ubuntu/vault-tmp/llms/Qwen3-8B-Q4_K_M.gguf'
AUTHOR_NAME = 'Martin Pellizzer'

proj = 'ozonogroup'
collection_name = 'ozone'

vault = '/home/ubuntu/vault'
vault_tmp = '/home/ubuntu/vault-tmp'
db_path = f'{vault}/{proj}/studies/chroma'

model = f'{vault_tmp}/llms/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf'
model_validator_filepath = f'{vault_tmp}/llms/Llama-3-Partonus-Lynx-8B-Intstruct-Q4_K_M.gguf'

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name='all-mpnet-base-v2', 
    device='cuda',
)
chroma_client = chromadb.PersistentClient(path=db_path)
collection = chroma_client.get_or_create_collection(
    name=collection_name, 
    embedding_function=sentence_transformer_ef,
)

study_cur = {
    'pmid': '',
    'journal': '',
    'abstract': '',
}

study_list = []

def get_studies_rejected():
    studies_rejected = []
    article = article_entry.get()
    folderpath = f'articles/{article}/rejected'
    for filename in os.listdir(folderpath):
        pmid = filename.split('.')[0]
        studies_rejected.append(pmid)
    return studies_rejected

def get_studies_approved():
    studies_approved = []
    article = article_entry.get()
    folderpath = f'articles/{article}/approved'
    for filename in os.listdir(folderpath):
        pmid = filename.split('.')[0]
        studies_approved.append(pmid)
    return studies_approved

def tk_get_studies():
    global study_cur
    global study_list
    study_cur = {}
    study_list = []
    article = article_entry.get()
    keyword = keyword_entry.get()
    if not os.path.exists(f'articles/{article}'):
        os.makedirs(f'articles/{article}')
    if not os.path.exists(f'articles/{article}/approved'):
        os.makedirs(f'articles/{article}/approved')
    if not os.path.exists(f'articles/{article}/rejected'):
        os.makedirs(f'articles/{article}/rejected')
    if not os.path.exists(f'articles/{article}/data.json'):
        j = json.dumps({"_": "_", "studies": []}, indent=4)
        with open(f'articles/{article}/data.json', 'w') as f:
            print(j, file=f)
    results = collection.query(query_texts=[keyword], n_results=100)
    print(results)
    documents = results['documents'][0]
    metadatas = results['metadatas'][0]
    for i in range(len(documents)):
        document = documents[i]
        metadata = metadatas[i]
        print(document)
        print(metadata)
        studies_rejected = get_studies_rejected()
        studies_approved = get_studies_approved()
        if metadata['pmid'] not in studies_rejected and metadata['pmid'] not in studies_approved:
            study_list.append({
                'pmid': metadata['pmid'], 
                'journal_title': metadata['journal_title'], 
                'abstract': document,
            })
    study_cur = study_list[0]
    abstract_text_widget.delete(1.0, END)
    abstract_text_widget.insert(END, study_cur['abstract'])
    tk_ozone_gen()
    tk_article_section_gen()
    tk_article_section_title_gen()
    tk_problem_gen()
    tk_where_gen()

def tk_translation_gen():
    abstract = abstract_text_widget.get('1.0', END)
    prompt = f'''
        Translate in italian the following text:
        {abstract}
        /no_think
    '''
    print(prompt)
    reply = llm_reply(prompt, model_path=model_filepath).strip()
    if '</think>' in reply:
        reply = reply.split('</think>')[1].strip()
    translation_text_widget.delete(1.0, END)
    translation_text_widget.insert(END, reply)

def tk_summary_gen():
    cotent = translation_text_widget.get('1.0', END)
    prompt = f'''
        Summarize the following text:
        {cotent}
        /no_think
    '''
    print(prompt)
    reply = llm_reply(prompt, model_path=model_filepath).strip()
    if '</think>' in reply:
        reply = reply.split('</think>')[1].strip()
    summary_text_widget.delete(1.0, END)
    summary_text_widget.insert(END, reply)

def tk_ozone_gen():
    content = abstract_text_widget.get('1.0', END)
    prompt = f'''
        Does the following content talk about ozone?
        {content}
        /no_think
    '''
    print(prompt)
    reply = llm_reply(prompt, model_path=model_filepath).strip()
    if '</think>' in reply:
        reply = reply.split('</think>')[1].strip()
    ozone_text_widget.delete(1.0, END)
    ozone_text_widget.insert(END, reply)

def tk_article_section_gen():
    content = abstract_text_widget.get('1.0', END)
    study_title = study_cur['journal_title']
    prompt = f'''
        Write a 5-sentence section for an article about ozone sanitization in the food industry.
        To write the article use the CONTENT, STRUCTURE, and GUIDELINES below.
        CONTENT:
        {content}
        STRUCTURE:
        Start by explaining the problem the above study try to solve.
        Follow up by explaining the methods used in the study.
        End by explaining the result of the study, only the positive ones about ozone.
        GUIDELINES:
        Reply in italian.
        Reply in 5 sentences.
        Start the reply with the following words: Uno studio pubblicato dal "{study_title}" ha valutato .
        {content}
        /no_think
    '''
    print(prompt)
    reply = llm_reply(prompt, model_path=model_filepath).strip()
    if '</think>' in reply:
        reply = reply.split('</think>')[1].strip()
    article_section_text_widget.delete(1.0, END)
    article_section_text_widget.insert(END, reply)

def tk_article_section_title_gen():
    content = article_section_text_widget.get('1.0', END)
    prompt = f'''
        Write a title for the following CONTENT by using the following GUIDELINES.
        CONTENT:
        {content}
        GUIDELINES:
        Reply in italian.
        Write as few words as possible.
        Write the title in less than 7 words.
        The title must name the problem that the content attempt to solve.
        {content}
        /no_think
    '''
    print(prompt)
    reply = llm_reply(prompt, model_path=model_filepath).strip()
    if '</think>' in reply:
        reply = reply.split('</think>')[1].strip()
    title_entry.delete(0, END)
    title_entry.insert(0, reply)

def tk_problem_gen():
    content = article_section_text_widget.get('1.0', END)
    prompt = f'''
        Write the problem that the below STUDY is trying to solve using ozone.
        STUDY:
        {content}
        GUIDELINES:
        Reply in italian.
        Write as few words as possible.
        Write the problem in 1 word (max 2).
        {content}
        /no_think
    '''
    print(prompt)
    reply = llm_reply(prompt, model_path=model_filepath).strip()
    if '</think>' in reply:
        reply = reply.split('</think>')[1].strip()
    problem_entry.delete(0, END)
    problem_entry.insert(0, reply)

def tk_where_gen():
    content = article_section_text_widget.get('1.0', END)
    prompt = f'''
        Write me the location of where is problem that the below STUDY is trying to solve using ozone?
        STUDY:
        {content}
        GUIDELINES:
        Example of location can be a surfaca, a food, an animal, etc.
        Reply in italian.
        Reply as few words as possible.
        Reply the problem in 1 word (max 2).
        {content}
        /no_think
    '''
    print(prompt)
    reply = llm_reply(prompt, model_path=model_filepath).strip()
    if '</think>' in reply:
        reply = reply.split('</think>')[1].strip()
    where_entry.delete(0, END)
    where_entry.insert(0, reply)

def tk_approve():
    article = article_entry.get()
    filepath = f'articles/{article}/approved/{study_cur["pmid"]}.json'
    j = json.dumps(study_cur, indent=4)
    with open(filepath, 'w') as f:
        print(j, file=f)
    ###
    filepath = f'articles/{article}/data.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    content = article_section_text_widget.get('1.0', END).strip()
    title = title_entry.get()
    category = category_entry.get()
    problem = problem_entry.get()
    where = where_entry.get()
    obj = {
        'pmid': study_cur['pmid'],
        'journal_title': study_cur['journal_title'],
        'abstract': study_cur['abstract'],
        'content': content,
        'title': title,
        'category': category,
        'problem': problem,
        'where': where,
    }
    data['studies'].append(obj)
    j = json.dumps(data, indent=4)
    with open(filepath, 'w') as f:
        print(j, file=f)
    tk_get_studies()

def tk_reject():
    article = article_entry.get()
    j = json.dumps(study_cur, indent=4)
    filepath = f'articles/{article}/rejected/{study_cur["pmid"]}.json'
    with open(filepath, 'w') as f:
        print(j, file=f)
    tk_get_studies()

root = Tk() 

width = 100
study_frame = Frame(root)
study_frame.pack(side=LEFT)
article_label = Label(study_frame, text='article')
article_label.pack()
article_entry = Entry(study_frame)
article_entry.pack()
article_entry.delete(0, END)
article_entry.insert(0, 'ittico')
###
keyword_label = Label(study_frame, text='keyword')
keyword_label.pack()
keyword_entry = Entry(study_frame)
keyword_entry.pack()
keyword_entry.delete(0, END)
keyword_entry.insert(0, 'fish')
###
keyword_button = Button(study_frame, text='get studies by keyword', command=tk_get_studies)
keyword_button.pack()
abstract_text_widget = Text(study_frame, width=width)
abstract_text_widget.pack()
###
'''
translation_button = Button(study_frame, text='get translation', command=tk_translation_gen)
translation_button.pack()
translation_text_widget = Text(study_frame, width=width)
translation_text_widget.pack()
'''
###
'''
summary_button = Button(study_frame, text='get summary', command=tk_summary_gen)
summary_button.pack()
summary_text_widget = Text(study_frame, width=width, height=18)
summary_text_widget.pack()
'''

'''
pmid_label = Label(study_frame, text='pmid')
pmid_label.pack()
pmid_entry = Entry(study_frame)
pmid_entry.pack()
pmid_button = Button(study_frame, text='get pmid', command=tk_get_study)
pmid_button.pack()
'''

ozone_frame = Frame(root)
ozone_frame.pack(side=LEFT)

'''
ozone_button = Button(ozone_frame, text='get ozone', command=tk_ozone_gen)
ozone_button.pack()
'''
ozone_text_widget = Text(study_frame, width=width)
ozone_text_widget.pack()

'''
article_section_title_button = Button(ozone_frame, text='write title', command=tk_article_section_title_gen)
article_section_title_button.pack()
article_section_title_text_widget = Text(ozone_frame, width=width, height=5)
article_section_title_text_widget.pack()
'''

category_label = Label(ozone_frame, text='category')
category_label.pack()
category_entry = Entry(ozone_frame, width=width)
category_entry.pack()

problem_label = Label(ozone_frame, text='problem')
problem_label.pack()
problem_entry = Entry(ozone_frame, width=width)
problem_entry.pack()

where_label = Label(ozone_frame, text='where')
where_label.pack()
where_entry = Entry(ozone_frame, width=width)
where_entry.pack()

title_label = Label(ozone_frame, text='title')
title_label.pack()
title_entry = Entry(ozone_frame, width=width)
title_entry.pack()

article_section_text_widget = Text(ozone_frame, width=width)
article_section_text_widget.pack()
article_section_button = Button(ozone_frame, text='write article section', command=tk_article_section_gen)
article_section_button.pack()

approve_button = Button(ozone_frame, text='approve', command=tk_approve)
approve_button.pack()
reject_button = Button(ozone_frame, text='reject', command=tk_reject)
reject_button.pack()

root.mainloop()
