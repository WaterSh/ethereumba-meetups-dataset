import csv
from faker import Faker
import db


def anonymize_data(anon_db, meetup_dump="./import/meetup_dump.csv"):
    """
    This function reads Meetup dump information and creates a mapping between a real
    username and a fake one. The mapping will be used to keep a _user identity_ 
    without revealing his real data allowing metrics like churn rate to be calculated.

    Once data does not contain real names, will be inserted in the actual data set db
    to analyze the information.
    """
    fake = Faker()
    with open(meetup_dump) as csv_file:
        print("[anonymize_data] About to process file {}".format(meetup_dump))
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # Skip headers
        for row in csv_reader:
            meetup_name, source, person_name, _ = row
            print("[anonymize_data] Procesing {}".format(person_name))
            fake_name = db.get_anon_mapping(anon_db, person_name)
            if fake_name is None:
                # FIXME: It seems some duplicates are being generated
                fake_name = fake.name()
                print("[anonymize_data] Fake name not found. Assigning {} to {}".format(
                    fake_name, person_name))
                db.insert_fake_mapping(anon_db, person_name, fake_name)