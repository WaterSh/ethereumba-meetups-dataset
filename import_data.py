import sqlite3
import csv

import db


def import_meetups(path, dataset_db):
    """
    Inserts meetups event details into the db
    """
    cursor = dataset_db.cursor()
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # Skip headers
        for row in csv_reader:
            name, date, unknown_attendees = row
            print("[import_meetups] Inserting meetup {}".format(name))
            db.insert_meetup(cursor, name, date, unknown_attendees)
    cursor.close()
    dataset_db.commit()

def import_meetup_data(path, dataset_db, anon_db):
    """
    Imports Meetup dump into the dataset using anonymized names
    """
    cursor = dataset_db.cursor()
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # Skip headers
        for row in csv_reader:
            meetup_name, source, person_name, _, attended = row
            print("[import_meetup_data] Processing row {}".format(row))
            # FIXME: This assumes we have anonymized the file first
            anon_person_name = db.get_anon_mapping(anon_db, person_name)
            print("[import_meetup_data] Anon name found {}".format(
                anon_person_name))
            db.insert_person(cursor, anon_person_name[0])
            print("[import_meetup_data] Person {} inserted".format(
                anon_person_name))
            person_id = db.look_for_person(cursor, anon_person_name[0])
            meetup_id = db.look_for_meetup(cursor, meetup_name)
            print("[import_meetup_data_] {} meetup_attendance {} person {}".format(
                row, meetup_id, person_id))
            if meetup_id is not None and person_id is not None:
                db.insert_meetup_data(cursor, meetup_id[0], person_id[0], attended == 'x')
    cursor.close()
    dataset_db.commit()
