output_xml = ''

output_xml += f'''
    <?cml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
    <vnext id="oxygen-sensor" type="critical">
        <title>Sensore Ossigeno</title>
        <description>
            <p></p>
        </description>
    </vnext>
'''.strip()

with open(f'{g.TASKS_FOLDERPATH}/04_Feature_Prioritization_vNext.dita', 'w') as f: f.write(output_xml)
