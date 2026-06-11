import os

project_folderpath = f'C:/og-new'

def product_add():
    command = input(f'enter "product_foldername" >> ')
    if command.strip() == '': return
    version_filename = f'v0_1_0'
    product_foldername = command
    ### PRODUCT
    product_folderpath = f'{project_folderpath}/products/{product_foldername}'
    os.mkdir(product_folderpath)
    while True:
        command = input(f'enter "product_component_foldername" >> ')
        if command.strip() == '': continue
        product_component_foldername = command
        ### COMPONENT
        product_component_folderpath = f'{product_folderpath}/{product_component_foldername}_{version_filename}'
        os.mkdir(product_component_folderpath)
        ### SUBCOMPONENTS
        product_subcomponent_folderpath = f'{product_component_folderpath}/{product_component_foldername}_hardware_{version_filename}'
        os.mkdir(product_subcomponent_folderpath)
        product_subcomponent_folderpath = f'{product_component_folderpath}/{product_component_foldername}_software_{version_filename}'
        os.mkdir(product_subcomponent_folderpath)

def component_add():
    command = input(f'COMPONENT ADD: enter "product_foldername" >> ')
    if command.strip() == '': return
    version_filename = f'v0_1_0'
    product_foldername = command
    ### PRODUCT
    product_folderpath = f'{project_folderpath}/products/{product_foldername}'
    if os.path.exists(product_folderpath):
        while True:
            command = input(f'enter "product_component_foldername" >> ')
            if command.strip() == '': continue
            product_component_foldername = command
            ### COMPONENT
            product_component_folderpath = f'{product_folderpath}/{product_component_foldername}_{version_filename}'
            os.mkdir(product_component_folderpath)
            ### SUBCOMPONENTS
            product_subcomponent_folderpath = f'{product_component_folderpath}/{product_component_foldername}_hardware_{version_filename}'
            os.mkdir(product_subcomponent_folderpath)
            product_subcomponent_folderpath = f'{product_component_folderpath}/{product_component_foldername}_software_{version_filename}'
            os.mkdir(product_subcomponent_folderpath)

# product_add()
component_add()