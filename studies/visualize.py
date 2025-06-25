# TODO: fix mouse wheel press and scroll at the same time, it gives bugs

import json
import pygame

pygame.init()

window_w = 1920
window_h = 1080

screen = pygame.display.set_mode([window_w, window_h])
font_size = 48
font = pygame.font.SysFont('Arial', font_size)

font_size = 16
font_16 = pygame.font.SysFont('Arial', font_size)
font_size = 32
font_32 = pygame.font.SysFont('Arial', font_size)
font_size = 48
font_48 = pygame.font.SysFont('Arial', font_size)
font_size = 64
font_64 = pygame.font.SysFont('Arial', font_size)
fonts = []
fonts.append(font_16)
fonts.append(font_32)
fonts.append(font_48)
fonts.append(font_64)

mouse = {
    'x': 0,
    'y': 0,
    'left_click_cur': 0,
    'left_click_old': 0,
    'left_click_drag': 0,
    'middle_click_cur': 0,
    'middle_click_old': 0,
    'middle_click_pan': 0,
    'right_click_cur': 0,
    'right_click_old': 0,
}

camera = {
    'zoom': 1,
    'x': 0,
    'y': 0,
    'x_start': 0,
    'y_start': 0,
    'x_abs': 0,
    'y_abs': 0,
    'x_abs_start': 0,
    'y_abs_start': 0,
}

nodes = []
edges = []

node_active_id = -1
if node_active_id != -1: 
    node_active = [node for node in nodes if node['id'] == node_active_id][0]
else: node_active = None

def input_keybord_node_add():
    global nodes
    if nodes != []: id_next = nodes[-1]['id'] + 1
    else: id_next = 0
    # ;jump
    line = 'enter note here'
    _font = fonts[camera['zoom']-1]
    text_surface = _font.render(line, False, (255, 255, 255))
    text_w, text_h = _font.size(line)
    node = {
        'id': id_next,
        'lines': [line],
        'line_index': 0,
        'char_index': 0,
        'x_start': (mouse['x'] - camera['x'])//camera['zoom'],
        'y_start': (mouse['y'] - camera['y'])//camera['zoom'],
        'x': (mouse['x'] - camera['x'])//camera['zoom'],
        'y': (mouse['y'] - camera['y'])//camera['zoom'],
        'w': text_w//camera['zoom'],
        'h': text_h//camera['zoom'],
    }
    nodes.append(node)

def input_mouse_middle():
    mouse_middle_press = pygame.mouse.get_pressed()[1]
    if mouse_middle_press == True:
        mouse['middle_click_cur'] = 1
        if mouse['middle_click_old'] != mouse['middle_click_cur']:
            mouse['middle_click_old'] = mouse['middle_click_cur']
            mouse['middle_click_pan'] = 1
            mouse['x_pan_start'] = mouse['x']
            mouse['y_pan_start'] = mouse['y']
            camera['x_start'] = camera['x']
            camera['y_start'] = camera['y']
            camera['x_abs_start'] = camera['x_abs']
            camera['y_abs_start'] = camera['y_abs']
    else:
        mouse['middle_click_cur'] = 0
        if mouse['middle_click_old'] != mouse['middle_click_cur']:
            mouse['middle_click_old'] = mouse['middle_click_cur']
            mouse['middle_click_pan'] = 0
    if mouse['middle_click_pan'] == 1:
        camera['x'] = camera['x_start'] + (mouse['x'] - mouse['x_pan_start'])
        camera['y'] = camera['y_start'] + (mouse['y'] - mouse['y_pan_start'])
        camera['x_abs'] = camera['x_abs_start'] + (mouse['x'] - mouse['x_pan_start'])//camera['zoom']
        camera['y_abs'] = camera['y_abs_start'] + (mouse['y'] - mouse['y_pan_start'])//camera['zoom']

def input_mouse():
    mouse['x'], mouse['y'] = pygame.mouse.get_pos()
    input_mouse_middle()

def project_load(key='problem'):
    global nodes
    global edges
    nodes = []
    edges = []
    filepath = f'articles/ortofrutticolo/data.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    studies = data['studies']
    x_cur = 0
    y_cur = 0
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
                
    for group_id, group in enumerate(group_list):
        y_cur = 200
        node_cur = {
            'id': 0,
            'lines': [group[key]],
            'line_index': 0,
            'char_index': 0,
            'x_start': x_cur,
            'y_start': y_cur,
            'x': x_cur,
            'y': y_cur,
            'w': 0,
            'h': 0,
        }
        nodes.append(node_cur)
        y_cur += 100
        for study in group['studies']:
            node_cur = {
                'id': 0,
                'lines': [study['problem']],
                'line_index': 0,
                'char_index': 0,
                'x_start': x_cur,
                'y_start': y_cur,
                'x': x_cur,
                'y': y_cur,
                'w': 0,
                'h': 0,
            }
            nodes.append(node_cur)
            y_cur += 20
            node_cur = {
                'id': 0,
                'lines': [study['where']],
                'line_index': 0,
                'char_index': 0,
                'x_start': x_cur,
                'y_start': y_cur,
                'x': x_cur,
                'y': y_cur,
                'w': 0,
                'h': 0,
            }
            nodes.append(node_cur)
            y_cur += 20
            node_cur = {
                'id': 0,
                'lines': [study['title']],
                'line_index': 0,
                'char_index': 0,
                'x_start': x_cur,
                'y_start': y_cur,
                'x': x_cur,
                'y': y_cur,
                'w': 0,
                'h': 0,
            }
            nodes.append(node_cur)
            y_cur += 100
        x_cur += 400
    # nodes = data['nodes']
    # edges = data['edges']

def input_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_l and pygame.key.get_mods() & pygame.KMOD_CTRL:
                project_load()
            elif event.key == pygame.K_p:
                project_load(key='problem')
            elif event.key == pygame.K_w:
                project_load(key='where')
        if event.type == pygame.MOUSEWHEEL:
            offset_x = window_w//2 - camera['x_abs']
            offset_y = window_h//2 - camera['y_abs']
            if event.y == -1:
                if camera['zoom'] > 1:
                    camera['zoom'] -= 1
                    camera['x'] += offset_x
                    camera['y'] += offset_y
            else:
                if camera['zoom'] < len(fonts):
                    camera['zoom'] += 1
                    camera['x'] -= offset_x
                    camera['y'] -= offset_y

def input_main():
    input_events()
    input_mouse()

def draw_edges():
    for edge in edges:
        id_1 = edge['id_1']
        id_2 = edge['id_2']
        id_1_found = False
        id_2_found = False
        for node in nodes:
            if not id_1_found:
                if node['id'] == id_1:
                    start_x, start_y, start_w, start_h = node_rect_get(node)
                    start_x += start_w//2
                    start_y += start_h//2
                    id_1_found = True
            if not id_2_found:
                if node['id'] == id_2:
                    end_x, end_y, end_w, end_h = node_rect_get(node)
                    end_x += end_w//2
                    end_y += end_h//2
                    id_2_found = True
            if id_1_found and id_2_found:
                break
        pygame.draw.line(screen, '#ffffff', (start_x, start_y), (end_x, end_y), 1)

def node_bounding_box_get(node):
    text_w, text_h = node_text_size_get(node)
    x1, y1 = node_pos_get(node)
    x2 = x1 + text_w
    y2 = y1 + text_h
    return [x1, y1, x2, y2]

def node_text_size_get(node):
    _font = fonts[camera['zoom']-1]
    w_max = 0
    h_tot = 0
    for line_i, line in enumerate(node['lines']):
        text_surface = _font.render(line, False, (255, 255, 255))
        text_w, text_h = _font.size(line)
        if w_max < text_w: w_max = text_w
        h_tot += text_h
    return w_max, h_tot

def node_pos_get(node):
    x = node['x'] * camera['zoom'] + camera['x']
    y = node['y'] * camera['zoom'] + camera['y']
    return [x, y]

def node_rect_get(node):
    node_x, node_y = node_pos_get(node)
    text_w, text_h = node_text_size_get(node)
    x = node_x
    y = node_y
    w = text_w
    h = text_h
    return [x, y, w, h]

def view_pos_get(val):
    view_pos = val * camera['zoom'] + camera['x']
    return view_pos

def draw_nodes():
    for node in nodes:
        ### node rect
        x, y, w, h = node_rect_get(node)
        pygame.draw.rect(screen, '#101010', pygame.Rect(x, y, w, h))
        pygame.draw.rect(screen, '#ffffff', pygame.Rect(x, y, w, h), 1)
        ### node text
        _font = fonts[camera['zoom']-1]
        for line_i, line in enumerate(node['lines']):
            text_surface = _font.render(line, False, (255, 255, 255))
            text_w, text_h = _font.size(line)
            screen.blit(text_surface, (x, y+text_h*line_i))
        ### node pos debug
        if 0:
            y_cur = y
            y_cur -= 24*camera['zoom']
            line = f"{x}, {y}"
            text_surface = _font.render(line, False, (255, 255, 255))
            screen.blit(text_surface, (x, y_cur))
            y_cur -= 24*camera['zoom']
            line = f"{node['x']}, {node['y']}"
            text_surface = _font.render(line, False, (255, 255, 255))
            screen.blit(text_surface, (x, y_cur))
        ### node active
        if node['id'] == node_active_id:
            pygame.draw.rect(screen, '#00ff00', pygame.Rect(x, y, w, h), 1)

def draw_debug():
    _font = fonts[camera['zoom']-1]
    ###
    x = 32
    y = 32
    line = f"{mouse['x']}, {mouse['y']}"
    text_surface = _font.render(line, False, (255, 255, 255))
    screen.blit(text_surface, (x, y))
    y += 24
    line = f"{camera['x']}, {camera['y']}"
    text_surface = _font.render(line, False, (255, 255, 255))
    screen.blit(text_surface, (x, y))
    y += 24
    line = f"{camera['x_abs']}, {camera['y_abs']}"
    text_surface = _font.render(line, False, (255, 255, 255))
    screen.blit(text_surface, (x, y))
    if 0:
        y += 24
        line = f"{node_active_id}, {node_active}"
        text_surface = _font.render(line, False, (255, 255, 255))
        screen.blit(text_surface, (x, y))

def draw_main():
    screen.fill('#101010')
    draw_edges()
    draw_nodes()
    draw_debug()
    pygame.display.flip()

running = True
while running:
    input_main()
    draw_main()

pygame.quit()
