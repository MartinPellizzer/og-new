import os

import torch
from diffusers import DiffusionPipeline, StableDiffusionXLPipeline
from diffusers import DPMSolverMultistepScheduler
from PIL import Image, ImageFont, ImageDraw, ImageColor, ImageOps

from oliark_io import json_read, json_write

website_folderpath = 'public'

vault = '/home/ubuntu/vault'

checkpoint_filepath = f'{vault}/stable-diffusion/checkpoints/xl/juggernautXL_juggXIByRundiffusion.safetensors'
pipe = StableDiffusionXLPipeline.from_single_file(
    checkpoint_filepath, 
    torch_dtype=torch.float16, 
    use_safetensors=True, 
    variant="fp16"
).to('cuda')
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

def gen_image_food(food_name_eng, food_name_ita):
    image_web_filepath = f'public/immagini/alimenti/{food_name_ita}.jpg'
    if os.path.exists(image_web_filepath): return
    prompt = f'''
        close-up of {food_name_eng},
        on a stainless steel table,
        natural lighting,
        depth of field, bokeh,
        high resolution,
        cinematic
    '''
    print(prompt)
    image = pipe(prompt=prompt, width=1024, height=1024, num_inference_steps=30, guidance_scale=7.0).images[0]
    image.save(f'public/immagini/alimenti/{food_name_ita}.jpg')

def gen_image_contamination(contamination_name_scientific):
    contamination_slug = contamination_name_scientific.strip().lower().replace(' ', '-')
    category = 'contaminazioni'
    tmp_filepath = f'database/immagini/contaminazioni-tmp/{contamination_slug}.jpg'
    ast_filepath = f'database/immagini/contaminazioni/{contamination_slug}.jpg'
    if os.path.exists(ast_filepath): return
    prompt = f'''
        midshot of {contamination_name_scientific},
        science, 
        under microscope, 
        dark background,
        depth of field, bokeh,
        high resolution,
        cinematic,
    '''
    print(prompt)
    image = pipe(prompt=prompt, width=1024, height=1024, num_inference_steps=30, guidance_scale=7.0).images[0]
    image.save(tmp_filepath)

vertices_contaminations = json_read('vertices.json')
contaminations_names_scientific = [vertex['contamination_name_scientific'] for vertex in vertices_contaminations if vertex['entity_type'] == 'contaminazione']
for contamination_name_scientific in contaminations_names_scientific:
    # gen_image_contamination('listeria monocytogenes')
    gen_image_contamination(contamination_name_scientific)

def gen_home_pathogen(eng, ita):
    slug = ita.strip().lower().replace(' ', '-')
    category = 'contaminazioni'
    tmp_filepath = f'database/immagini/contaminazioni-tmp/{slug}.jpg'
    ast_filepath = f'database/immagini/contaminazioni/{slug}.jpg'
    if os.path.exists(ast_filepath): return
    prompt = f'''
        midshot of {eng},
        science, 
        under microscope, 
        dark background,
        depth of field, bokeh,
        high resolution,
        cinematic,
    '''
    print(prompt)
    image = pipe(prompt=prompt, width=1024, height=1024, num_inference_steps=30, guidance_scale=7.0).images[0]
    image.save(tmp_filepath)

gen_home_pathogen(eng='bacteria', ita='batteri')
gen_home_pathogen(eng='virus', ita='virus')
gen_home_pathogen(eng='molds', ita='muffe')

def gen_home_benefit_chemical(ita_slug):
    slug = ita_slug.strip().lower().replace(' ', '-')
    category = 'contaminazioni'
    out_filepath = f'{website_folderpath}/immagini/{slug}.jpg'
    if os.path.exists(out_filepath): return
    prompt = f'''
        midshot of chemical bottle with colorless liquid,
        toxic logo on label,
        science style, 
        silver color background,
        depth of field, bokeh,
        high resolution,
        cinematic,
    '''
    print(prompt)
    image = pipe(prompt=prompt, width=1024, height=1024, num_inference_steps=30, guidance_scale=7.0).images[0]
    image.save(out_filepath)

gen_home_benefit_chemical(ita_slug='ozono-senza-sostanze-chimiche')

def gen_home_benefit_pathogen(ita_slug):
    slug = ita_slug.strip().lower().replace(' ', '-')
    category = 'contaminazioni'
    out_filepath = f'{website_folderpath}/immagini/{slug}.jpg'
    if os.path.exists(out_filepath): return
    prompt = f'''
        midshot of pathogen,
        under microscope, 
        science style, 
        dark background,
        depth of field, bokeh,
        high resolution,
        cinematic,
    '''
    print(prompt)
    image = pipe(prompt=prompt, width=1024, height=1024, num_inference_steps=30, guidance_scale=7.0).images[0]
    image.save(out_filepath)

gen_home_benefit_pathogen(ita_slug='ozono-altamente-efficace')

def gen_home_benefit_eco(ita_slug):
    slug = ita_slug.strip().lower().replace(' ', '-')
    category = 'contaminazioni'
    out_filepath = f'{website_folderpath}/immagini/{slug}.jpg'
    if os.path.exists(out_filepath): return
    prompt = f'''
        midshot of water flow,
        science style, 
        dark background,
        depth of field, bokeh,
        high resolution,
        cinematic,
    '''
    print(prompt)
    image = pipe(prompt=prompt, width=1024, height=1024, num_inference_steps=30, guidance_scale=7.0).images[0]
    image.save(out_filepath)

gen_home_benefit_eco(ita_slug='ozono-ecologico')

def gen_home_benefit_certified(ita_slug):
    slug = ita_slug.strip().lower().replace(' ', '-')
    category = 'contaminazioni'
    out_filepath = f'{website_folderpath}/immagini/{slug}.jpg'
    if os.path.exists(out_filepath): return
    prompt = f'''
        midshot of a pile of docs,
        science style, 
        silver color background,
        depth of field, bokeh,
        high resolution,
        cinematic,
    '''
    print(prompt)
    image = pipe(prompt=prompt, width=1024, height=1024, num_inference_steps=30, guidance_scale=7.0).images[0]
    image.save(out_filepath)

gen_home_benefit_certified(ita_slug='ozono-sicuro')

quit()

################################################
# ;treatments
################################################
category = 'trattamenti'
name_eng = 'sodium hypochlorite'
name_ita = 'ipoclorito di sodio'
slug_ita = name_ita.lower().strip().replace(' ', '-')
# image_web_filepath = f'public/immagini/{category}/{slug_ita}.jpg'
# if not os.path.exists(image_web_filepath): 
if True:
    for i in range(10):
        prompt = f'''
            a tank of {name_eng},
            on a stainless steel table,
            dark background,
            depth of field, bokeh,
            high resolution,
            cinematic,
        '''
        print(prompt)
        image = pipe(prompt=prompt, width=1024, height=1024, num_inference_steps=30, guidance_scale=7.0).images[0]
        image.save(f'public/immagini/{category}/{slug_ita}-{i}.jpg')

