def create_schema(db, path="./dataset/ethba-dataset.db"):
    """ 
    Creates the tables that will be part of the dataset
    """
    db.execute("PRAGMA foreign_keys = 1")
    cursor = db.cursor()
    statement = """
    CREATE TABLE IF NOT EXISTS meetups (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL UNIQUE,
      date DATE NOT NULL,
      unknown_attendees INTEGER
    )
  """
    cursor.execute(statement)

    statement = """
    CREATE TABLE IF NOT EXISTS people (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL UNIQUE
    )
    """
    cursor.execute(statement)

    statement = """
    CREATE TABLE IF NOT EXISTS meetup_attendance (
      meetup_id INTEGER,
      person_id INTEGER,
      attended BOOLEAN,

      PRIMARY KEY (meetup_id, person_id)
      FOREIGN KEY(meetup_id) REFERENCES meetups(id)
      FOREIGN KEY(person_id) REFERENCES people(id)
    )
    """
    cursor.execute(statement)

    cursor.close()
    db.commit()


def create_anon_schema(db, path="./dataset/ethba-dataset.db"):
    """
    Creates the table to map between real user nicknames and fake ones
    """
    cursor = db.cursor()
    statement = """
    CREATE TABLE IF NOT EXISTS users_mapping (
      real_name TEXT NOT NULL UNIQUE,
      fake_name TEXT NOT NULL UNIQUE
    )
  """
    cursor.execute(statement)

    cursor.close()
    db.commit()


def get_anon_mapping(anon_db, real_name):
    """
    Looks for an anon user in the db 
    """
    cursor = anon_db.cursor()
    cursor.execute("""
      SELECT 
        fake_name 
      FROM 
        users_mapping 
      WHERE
        real_name = (?)
      """, (real_name, ))
    result = cursor.fetchone()
    cursor.close()
    return result


def insert_fake_mapping(anon_db, person_name, fake_name):
    """
    Inserts a new mapping to hide identity
    """
    cursor = anon_db.cursor()
    cursor.execute("""
      INSERT INTO users_mapping
        (real_name, fake_name)
      VALUES
        (?, ?)
    """, (person_name, fake_name))
    anon_db.commit()


def insert_meetup(cursor, name, date, unknown_attendees):
    statement = """
    INSERT INTO meetups
      (name, date, unknown_attendees)
    VALUES
      (?, ?, ?)
    ON CONFLICT (name) DO UPDATE set name = name, unknown_attendees = unknown_attendees
  """
    cursor.execute(statement, (name, date, unknown_attendees))


def insert_person(cursor, name):
    statement = """
    INSERT INTO people
      (name)
    VALUES
      (?)
    ON CONFLICT (name) DO NOTHING
  """
    cursor.execute(statement, (name, ))


def insert_meetup_data(cursor, meetup_id, person_id, attended):
    statement = """
      INSERT INTO meetup_attendance
        (meetup_id, person_id, attended)
      VALUES
        (?, ?, ?)
      ON CONFLICT (meetup_id, person_id) DO UPDATE set attended = attended
    """
    cursor.execute(statement, (meetup_id, person_id, attended))


def look_for_person(cursor, name):
    cursor.execute("SELECT id FROM people WHERE name = (?)", (name, ))
    return cursor.fetchone()


def look_for_meetup(cursor, name):
    cursor.execute("SELECT id FROM meetups WHERE name = (?)", (name, ))
    return cursor.fetchone()
