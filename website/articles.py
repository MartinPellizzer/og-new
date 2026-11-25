import markdown
import textwrap

from lib import g
from lib import components

def gen():
    urls_slugs = [
        'ozono/index_brief',
        'ozono/index_parts',
        'ozono/index',
    ]
    for url_slug in urls_slugs:
        with open(f'articles/{url_slug}.md', encoding='utf-8') as f: text = f.read()    

        article_html = markdown.markdown(text, extensions=["tables"])
        print(article_html)

        title = 'Ozono'
        html = f'''
            <!DOCTYPE html>
            <html lang="it">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="/styles.css">
                <title>{title}</title>
            </head>
            <body>
                {components.header_light_logo()}
                <main 
                    class="article-new container-md"
                    style="
                        margin-top: 5rem; margin-bottom: 5rem;
                    "
                >
                    {article_html}
                </main>
                {components.footer_dark()}
            </body>
            </html>
        '''

        html_filepath = f'{g.WEBSITE_FOLDERPATH}/{url_slug}.html'
        with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
            f.write(html)
        print(html_filepath)
        print(html)
        # quit()