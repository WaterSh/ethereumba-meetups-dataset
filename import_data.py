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
            meetup_name = row[0]
            meetup_user_id = row[2]
            rsvp = row[7] != '' # TODO: We can parse the date here
            attended = row[10] == 'x'
            print("[import_meetup_data] Processing row {}".format(row))
            # FIXME: This assumes users were processed first and there are no new ones on this file
            ethereumba_user_id = db.get_user_mapping(anon_db, meetup_user_id)
            print("[import_meetup_data] ethereumba user found {}".format(
                ethereumba_user_id))
            meetup_id = db.look_for_meetup(cursor, meetup_name)
            if meetup_id is not None and ethereumba_user_id is not None:
                print("[import_meetup_data] Inserting meetup_id: {}, ethereumba_user_id: {}, rsvp: {}, attended: {}".format(
                    meetup_id, ethereumba_user_id, rsvp, attended))
                db.insert_meetup_data(
                    cursor, meetup_id[0], ethereumba_user_id[0], rsvp, attended)
            else:
                # FIXME: this should be handled properly instead of raising an error
                raise Exception('Error when importing')
    cursor.close()
    dataset_db.commit()
