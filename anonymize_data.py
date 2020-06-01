from random import SystemRandom
import csv
import db


def import_users(anon_db, users_dump):
    """
    This function reads Meetup dump information and creates a mapping between a real
    user_id and our id. The mapping will be used to keep a _user identity_ 
    without revealing his real data allowing metrics like churn rate to be calculated.
    """
    random = SystemRandom()
    with open(users_dump) as csv_file:
        print("[anonymize_data] About to process file {}".format(users_dump))
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # Skip headers
        for row in csv_reader:
            meetup_user_id = row[1]
            print("[anonymize_data] Procesing {}".format(meetup_user_id))
            ethereumba_meetup_id = db.get_user_mapping(anon_db, meetup_user_id)
            if ethereumba_meetup_id is None:
                new_ethereumba_meetup_id = random.randint(0, 2**32)
                print("[anonymize_data] User not found. Assigning {} to {}".format(
                    new_ethereumba_meetup_id, meetup_user_id))
                db.insert_userid_mapping(
                    anon_db, meetup_user_id, new_ethereumba_meetup_id)
