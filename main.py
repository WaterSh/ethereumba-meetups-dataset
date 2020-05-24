import sqlite3
from db import create_schema, create_anon_schema
from anonymize_data import anonymize_data
from import_data import import_meetup_data, import_meetups

meetups_file = "./import/meetups_list.csv"
meetup_export = "./import/meetup_dump.csv"

# Anonymize users data first
anon_db = sqlite3.connect('./dataset/sensitive-data.db')
create_anon_schema(anon_db)

# Process meetups details
dataset_db = sqlite3.connect('./dataset/ethba-dataset.db')
create_schema(dataset_db)

# TODO: This file will be processed twice but a refactor might be expected when
# cmd arguments get implemented so no need to worry about it now (also
# the input file is quite small)
print("[main] Running data anonymization")
anonymize_data(anon_db=anon_db,
               meetup_dump=meetup_export)


print("[main] Importing meetups list")
import_meetups(meetups_file, dataset_db)

print("[main] Importing meetups attendance")
import_meetup_data(path=meetup_export, dataset_db=dataset_db, anon_db=anon_db)

print("[main] Import finished")