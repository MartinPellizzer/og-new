from oliark_llm import llm_reply

with open('keywords/listeria-monocytogenes.txt') as f: 
    keywords = [line.strip() for line in f.read().split('\n') if line.strip() != '']

keywords_cluster_1 = keywords[:800]

prompt = f'''
    I have to write an article that target the KEYWORDS below.
    This article must be SEO friendly and include as many keywords possible.
    Write me an outline for this article.
    In this outline include the following:
    - 1 main title in <h1> tag
    - 4-7 sections in <h2> tags
    - 4 subsections for each section in <h3> tags
    Organize and cluster the keywords so that I can write the most comprehensive article possible.
    Avoid repetitions.
    Reply in italian.
    Reply in as few words as possible.
    The KEYWORS to target and cluster in the outline are the following:
    {keywords_cluster_1}
'''

reply = llm_reply(prompt)

