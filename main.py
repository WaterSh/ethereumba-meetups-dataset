import sqlite3
from db import create_schema, create_users_mapping_schema
from import_data import import_meetup_data, import_meetups

meetups_users = "./import/meetup_users.csv"
meetups_file = "./import/meetups_list.csv"
meetup_export = "./import/meetup_dump.csv"
attendees_without_rsvp = "./import/attendees_without_rsvp.csv"

# Anonymize users data first
anon_db = sqlite3.connect('./dataset/sensitive-data.db')
create_users_mapping_schema(anon_db)

# Process meetups details
dataset_db = sqlite3.connect('./dataset/ethereumba-dataset.db')
create_schema(dataset_db)

print("[main] Importing meetups list")
import_meetups(meetups_file, dataset_db)

print("[main] Importing meetups attendance")
import_meetup_data(path=meetup_export, dataset_db=dataset_db, anon_db=anon_db)
import_meetup_data(path=attendees_without_rsvp, dataset_db=dataset_db, anon_db=anon_db)

print("[main] Import finished")
