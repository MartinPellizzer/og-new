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
collection = chroma_client.get_or_create_collection(
    name=collection_name, 
    embedding_function=sentence_transformer_ef,
)
results = collection.query(query_texts=['dairy'], n_results=5)
documents = results['documents'][0]
metadatas = results['metadatas'][0]
print(documents[0])
print(metadatas[0])
