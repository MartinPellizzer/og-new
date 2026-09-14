import os

project_folderpath = f'C:/og-new'

help_commands_product = f'''
SELECT COMMAND:
- enter "p" to add product
- enter "q" to quit
''' 

help_commands_version = f'''
SELECT COMMAND:
- enter "p" to add product
- enter "v" to add product version
- enter "q" to quit
'''

help_commands_component = f'''
SELECT COMMAND:
- enter "p" to add product
- enter "v" to add product version
- enter "c" to add product version component
- enter "q" to quit
'''

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

def product_gen():
    product_foldername = input(f'enter "product_foldername" (es. centralina) >> ')
    if product_foldername.strip() == '': return
    product_foldername = product_foldername.replace(' ', '_')
    product_foldername = product_foldername.strip()
    product_foldername = product_foldername.lower()
    product_folderpath = f'{project_folderpath}/products/{product_foldername}'
    os.makedirs(product_folderpath, exist_ok=True)
    state_cur = 1
    return [state_cur, product_foldername]
    
def version_gen(product_foldername):
    version_foldername = input(f'enter "version_foldername" (es. 0_1_0) >> ')
    if version_foldername.strip() == '': return
    version_foldername = version_foldername.replace('.', '_')
    version_foldername = version_foldername.replace('v', '')
    version_foldername = version_foldername.replace(' ', '_')
    version_foldername = version_foldername.strip()
    version_foldername = version_foldername.lower()
    version_folderpath = f'{project_folderpath}/products/{product_foldername}/{product_foldername}__v{version_foldername}'
    os.makedirs(version_folderpath, exist_ok=True)
    state_cur = 2
    return [state_cur, product_foldername, version_foldername]
    
def component_gen(product_foldername, version_foldername):
    component_foldername = input(f'enter "component_foldername" (es. scheda_madre) >> ')
    if component_foldername.strip() == '': return
    component_foldername = component_foldername.replace(' ', '_')
    component_foldername = component_foldername.strip()
    component_foldername = component_foldername.lower()
    component_folderpath = f'{project_folderpath}/products/{product_foldername}/{product_foldername}__v{version_foldername}/{product_foldername}__{component_foldername}__v{version_foldername}'
    os.makedirs(component_folderpath, exist_ok=True)
    ### SUBCOMPONENTS
    subcomponent_folderpath = f'{project_folderpath}/products/{product_foldername}/{product_foldername}__v{version_foldername}/{product_foldername}__{component_foldername}__v{version_foldername}/{product_foldername}__{component_foldername}__hardware__v{version_foldername}'
    os.mkdir(subcomponent_folderpath)
    subcomponent_folderpath = f'{project_folderpath}/products/{product_foldername}/{product_foldername}__v{version_foldername}/{product_foldername}__{component_foldername}__v{version_foldername}/{product_foldername}__{component_foldername}__software__v{version_foldername}'
    os.mkdir(subcomponent_folderpath)
    state_cur = 2
    return [state_cur, product_foldername, version_foldername, component_foldername]

def gen():
    state_cur = 0
    product_foldername = ''
    version_foldername = ''
    component_foldername = ''
    running = True
    while running:
        if state_cur == 0:
            command = input(f'{help_commands_product}\n>> ')
            if command == 'p':
                state_cur, product_foldername = product_gen()
            elif command == 'q':
                running = False
        elif state_cur == 1:
            command = input(f'{help_commands_version}\n>> ')
            if command == 'p':
                state_cur, product_foldername = product_gen()
            elif command == 'v':
                state_cur, product_foldername, version_foldername = version_gen(product_foldername)
            elif command == 'q':
                running = False
        if state_cur == 2:
            command = input(f'{help_commands_component}\n>> ')
            if command == 'p':
                state_cur, product_foldername = product_gen()
            elif command == 'v':
                state_cur, product_foldername, version_foldername = version_gen(product_foldername)
            elif command == 'c':
                state_cur, product_foldername, version_foldername, component_foldername = component_gen(product_foldername, version_foldername)
            elif command == 'q':
                running = False

gen()
# product_add()
# component_add()