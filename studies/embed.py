import os
import json

import chromadb
from chromadb.utils import embedding_functions

from oliark_io import json_read, json_write
from oliark_llm import llm_reply

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
collection = chroma_client.get_or_create_collection(name=collection_name, embedding_function=sentence_transformer_ef)
documents_folderpath = f'{vault}/{proj}/studies/pubmed/{collection_name}/json'
documents_filenames = os.listdir(documents_folderpath)
for i, document_filename in enumerate(documents_filenames):
    print(f'{i}/{len(documents_filenames)}')
    document_filepath = f'{documents_folderpath}/{document_filename}'
    try: data = json_read(document_filepath)
    except: continue
    try: article = data['PubmedArticle'][0]['MedlineCitation']['Article']
    except: continue
    try: abstract_text = article['Abstract']['AbstractText']
    except: continue
    try: journal_title = article['Journal']['Title']
    except: continue
    abstract_text = ' '.join(abstract_text).replace('  ', ' ')
    pmid = document_filename.split('.')[0]
    metadata = {
        'pmid': pmid,
        'journal_title': journal_title,
    }
    collection.add(
        documents=[abstract_text],
        metadatas=[metadata],
        ids=[pmid],
    )
results = collection.query(query_texts=['test'], n_results=5)
print(results)
