import os

import torch
from diffusers import DiffusionPipeline
from diffusers import StableDiffusionXLPipeline
from diffusers import DPMSolverMultistepScheduler

from lib import io
from lib import utils

from oliark import img_resize

checkpoint_filepath = f'/home/ubuntu/vault/stable-diffusion/checkpoints/xl/juggernautXL_ragnarokBy.safetensors'
pipe = None

def html_header_get():
    html = f'''
        <header class="header-default container-xl">
            <div class="header-default-menu">
                <a class="header-default-menu-logo" href="/">Ozonogroup</a>
                <nav class="header-default-menu-nav">
                    <a href="/">Home</a>
                    <a href="/settori.html">Settori</a>
                    <a href="/prodotti.html">Prodotti</a>
                    <a href="/contatti.html">Contatti</a>
                </nav>
            </div>
            <div>
                <a class="header-default-button" href="/contatti.html">Prenota consulenza</a>
            </div>
        </header>
    '''
    return html

def html_footer_get():
    html = f'''
        <footer style="background-color: #0F1F2E; padding-top: 96px; padding-bottom: 96px;">
            <div class="container-xl">
                <div class="home-footer-intro-container">
                    <div>
                        <p style="color: #ffffff; margin-bottom: 16px; font-size: 32px;">Contatti</p>
                        <p style="color: #ffffff; margin-bottom: 8px;">Via dell'Artigianato, 23, 31011 Asolo TV</p>
                        <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 8px;">
                            <svg xmlns="http://www.w3.org/2000/svg" height="16px" viewBox="0 -960 960 960" width="16px"
                                fill="#ffffff">
                                <path
                                    d="M798-120q-125 0-247-54.5T329-329Q229-429 174.5-551T120-798q0-18 12-30t30-12h162q14 0 25 9.5t13 22.5l26 140q2 16-1 27t-11 19l-97 98q20 37 47.5 71.5T387-386q31 31 65 57.5t72 48.5l94-94q9-9 23.5-13.5T670-390l138 28q14 4 23 14.5t9 23.5v162q0 18-12 30t-30 12ZM241-600l66-66-17-94h-89q5 41 14 81t26 79Zm358 358q39 17 79.5 27t81.5 13v-88l-94-19-67 67ZM241-600Zm358 358Z" />
                            </svg>
                            <p style="color: #ffffff;">+39 0423 952833</p>
                        </div>
                        <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 8px;">
                            <svg xmlns="http://www.w3.org/2000/svg" height="16px" viewBox="0 -960 960 960" width="16px"
                                fill="#ffffff">
                                <path
                                    d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm320-280L160-640v400h640v-400L480-440Zm0-80 320-200H160l320 200ZM160-640v-80 480-400Z" />
                            </svg>
                            <p style="color: #ffffff;">
                                elena@ozonogroup.it
                            </p>
                        </div>
                    </div>
                    <div>
                        <p style="color: #ffffff; margin-bottom: 16px; font-size: 32px;">Links</p>
                        <a style="display: block; color: #ffffff; text-decoration-line: none; margin-bottom: 8px;"
                            href="#">Prodotti</a>
                        <a style="display: block; color: #ffffff; text-decoration-line: none; margin-bottom: 8px"
                            href="#">Contatti</a>
                        <a style="display: block; color: #ffffff; text-decoration-line: none; margin-bottom: 8px"
                            href="#">Blog</a>
                    </div>
                </div>
                <div class="home-footer-copyright-container">
                    <a style="font-size: 24px; color: #ffffff; text-decoration-line: none;" href="#">Ozonogroup</a>
                    <p style="color: #ffffff;">Copyright © Ozonogroup | Tutti i diritti riservati</p>
                </div>
            </div>
        </footer>
    '''
    return html

def html_sidebar_get():
    html = f'''
        <div style="flex: 1;" class="article-sidebar">
            <div class="contact-card">
                <div>
                    <p class="article-contact-card-title">Contattaci</p>
                    <p class="article-contact-card-desc">Se vuoi richiedere informazioni sull'utilizzo dell'ozono in
                        questo settore, usa uno dei contatti elencati qui sotto.</p>
                </div>
                <div style="display: flex; flex-direction: column; gap: 16px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div style="display: flex; gap: 8px;">
                            <svg style="color: #0f1f2e;" xmlns="http://www.w3.org/2000/svg" height="32px"
                                viewBox="0 -960 960 960">
                                <path
                                    d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm320-280L160-640v400h640v-400L480-440Zm0-80 320-200H160l320 200ZM160-640v-80 480-400Z" />
                            </svg>
                            <p class="contact-text">
                                Mandaci una email<br>elena@ozonogroup.it
                            </p>
                        </div>
                        <svg style="height: 32px; color: #0f1f2e;" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
                        </svg>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div style="display: flex; gap: 8px;">
                            <svg style="color: #0f1f2e;" xmlns="http://www.w3.org/2000/svg" height="32px"
                                viewBox="0 -960 960 960">
                                <path
                                    d="M798-120q-125 0-247-54.5T329-329Q229-429 174.5-551T120-798q0-18 12-30t30-12h162q14 0 25 9.5t13 22.5l26 140q2 16-1 27t-11 19l-97 98q20 37 47.5 71.5T387-386q31 31 65 57.5t72 48.5l94-94q9-9 23.5-13.5T670-390l138 28q14 4 23 14.5t9 23.5v162q0 18-12 30t-30 12ZM241-600l66-66-17-94h-89q5 41 14 81t26 79Zm358 358q39 17 79.5 27t81.5 13v-88l-94-19-67 67ZM241-600Zm358 358Z" />
                            </svg>
                            <p class="contact-text">
                                Chiamaci<br>+39 0423 952833
                            </p>
                        </div>
                        <svg style="height: 32px; color: #0f1f2e;" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
                        </svg>
                    </div>
                </div>
            </div>
        </div>
    '''
    return html

def ai_img_gen(article_slug, regen=False, dispel=False):
    global pipe
    img_filepath = f'/home/ubuntu/vault/ozonogroup/website/ozonogroup/immagini/settori/{article_slug}.jpg'
    if regen:
        try: os.remove(img_filepath)
        except: pass
    if dispel:
        try: os.remove(img_filepath)
        except: pass
        return
    if not os.path.exists(img_filepath):
        quality = 30
        if pipe == None:
            pipe = StableDiffusionXLPipeline.from_single_file(
                checkpoint_filepath, 
                torch_dtype=torch.float16, 
                use_safetensors=True, 
                variant="fp16"
            ).to('cuda')
            pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
        prompt = f'''
            vegetables, field, 
            depth of field,
            bokeh,
            high detail,
        '''
        negative_prompt = ''
        image = pipe(prompt=prompt, negative_prompt=negative_prompt, width=1024, height=1024, num_inference_steps=30, guidance_scale=7.0).images[0]
        image = img_resize(image, w=768, h=768)
        image.save(img_filepath, format='JPEG', subsampling=0, quality=quality)

def gen(article_slug):
    json_article_filepath = f'articles/{article_slug}/data.json'
    html_article_filepath = f'articles/{article_slug}/{article_slug}.html'
    html_out_article_filepath = f'/home/ubuntu/vault/ozonogroup/website/ozonogroup/settori/{article_slug}.html'
    ###
    json_article = io.json_read(json_article_filepath)
    html_article = ''
    # html_article += f'<h1>{article_slug}</h1>\n'
    ###
    key = 'problem'
    studies = json_article['studies']
    group_list = []
    for study_id, study in enumerate(studies):
        found = False
        for group in group_list:
            if study[key].strip().lower() == group[key].strip().lower():
                group['studies'].append(study)
                found = True
                break
        if not found:
            group_list.append({key: study[key], 'studies': [study]})
    html_article += f'<h1 class="article-title">{len(group_list)} applicazioni della sanificazione a ozono nel settore {article_slug}</h1>'
    html_article += f'''
        <img src="/immagini/settori/{article_slug}.jpg" alt="ozono settore {article_slug}">
    '''
    for group_i, group in enumerate(group_list):
        study = group['studies'][0]
        study_title = study['title']
        study_content = study['content']
        html_article += f'<h2>{group_i+1}. {study_title}</h2>\n'
        html_article += f'{utils.text_format_1N1_html(study_content)}\n'
        # html_article += f'{study_content}\n'
    # <meta property="og:image" content="/immagini/home/sanificazione-ozono.png">
    # <meta name="description" content="Lista di study sulla sanificazione ozono nel settore carni">
    html_header = html_header_get()
    html_footer = html_footer_get()
    html_sidebar = html_sidebar_get()
    html_article = f'''
        <div style="flex: 2;" class="article">
            {html_article}
        </div>
    '''
    html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="author" content="Ozonogroup">
            <link rel="stylesheet" href="/style.css">
            <title>Settore Ittico</title>
            <link rel="icon" href="/immagini/ozonogroup-favicon.ico">
        </head>
        <body>
            {html_header}
            <div class="spacer-xl"></div>
            <section>
                <div class="container-xl article-layout-container">
                    {html_article}
                    {html_sidebar}
                </div>
            </section>
            <div class="spacer-xl"></div>
            {html_footer}
        </body>
        </html>
    '''
    with open(html_article_filepath, 'w') as f: f.write(html)
    with open(html_out_article_filepath, 'w') as f: f.write(html)
    ai_img_gen(article_slug, regen=False, dispel=False)

gen(article_slug='ortofrutticolo')
