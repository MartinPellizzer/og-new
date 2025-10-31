import chromadb
from chromadb.utils import embedding_functions

vault_tmp = '/home/ubuntu/vault-tmp'
collection_name = 'ozone'

db_path = f'{vault_tmp}/terrawhisper/chroma'
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name='all-mpnet-base-v2', 
    device='cuda',
)
chroma_client = chromadb.PersistentClient(path=db_path)

def retrieve_docs(query, n_results):
    collection = chroma_client.get_or_create_collection(
        name=collection_name, 
        embedding_function=sentence_transformer_ef,
    )
    results = collection.query(query_texts=[query], n_results=n_results)
    documents = results['documents'][0]
    metadatas = results['metadatas'][0]
    return documents, metadatas

n_results = 100
query = f'ozone'
documents, metadatas = retrieve_docs(query, n_results=n_results)
print(documents[:5])
