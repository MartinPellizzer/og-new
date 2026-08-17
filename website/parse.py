import os
import csv
import sys
import json
import time
import shutil
import sqlite3

from lib import g
from lib import io

HUB_FOLDERPATH = f'{g.DATA_FOLDERPATH}/sectors'

def parse_main():
    input_folderpath = f'{HUB_FOLDERPATH}/fetch/source_1/dataset'
    output_folderpath = f'{HUB_FOLDERPATH}/reference/source_1'
    io.folders_recursive_gen(output_folderpath)

    conn = sqlite3.connect(f"{output_folderpath}/source_1.db")

    table_name = 'sectors'
    conn.executescript(
    f"""
        PRAGMA journal_mode = OFF;
        PRAGMA synchronous = OFF;
        PRAGMA temp_store = MEMORY;
        PRAGMA cache_size = -500000;

        DROP TABLE IF EXISTS {table_name};

        CREATE TABLE {table_name} (
            work_id TEXT NOT NULL,
            genus_id TEXT NOT NULL,
            work_genus TEXT NOT NULL,
            work_species TEXT NOT NULL,
            work_author TEXT,
            work_species_norm TEXT NOT NULL
        );
    """)

    conn.commit()

    csv.field_size_limit(sys.maxsize)

    input_filepath = f"{input_folderpath}/NATIONAL_ALTERNATIVE_NAME_FILE.CSV"
    input_filepath = f"{input_folderpath}/NATIONAL_FACILITY_FILE.CSV"
    input_filepath = f"{input_folderpath}/NATIONAL_CONTACT_FILE.CSV"

    BATCH_SIZE = 100000
    processed = 0
    start = time.time()
    conn.execute("BEGIN")
    with open(
        input_filepath,
        "r",
        encoding="utf8",
        errors="ignore",
        newline="",
    ) as f:
        reader = csv.DictReader(f, delimiter=",")
        batch = []
        for row in reader:
            print(json.dumps(row, indent=4))
            quit() 


def run():
    print(f'''OZONE >> PARSE >> ???''')

    start = time.perf_counter()
    parse_main()
    print(f'parse main() - execution time: ', time.perf_counter() - start)

run()
