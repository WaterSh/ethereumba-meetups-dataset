def create_schema(db, path="./dataset/ethereumba-dataset.db"):
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
    CREATE TABLE IF NOT EXISTS meetup_attendance (
      meetup_id INTEGER,
      ethereumba_user_id INTEGER,
      rsvp BOOLEAN,
      attended BOOLEAN,

      PRIMARY KEY (meetup_id, ethereumba_user_id)
      FOREIGN KEY(meetup_id) REFERENCES meetups(id)
    )
    """
    cursor.execute(statement)

    cursor.close()
    db.commit()


def create_users_mapping_schema(db, path="./dataset/sensitive-data.db"):
    """
    Creates the table to map between meetup userid and ethereumba userid 
    """
    cursor = db.cursor()
    statement = """
    CREATE TABLE IF NOT EXISTS users_mapping (
      ethereumba_user_id INTEGER PRIMARY KEY, 
      meetup_user_id TEXT NOT NULL UNIQUE
    ) WITHOUT ROWID
  """
    cursor.execute(statement)

    cursor.close()
    db.commit()


def get_user_mapping(anon_db, meetup_user_id):
    """
    Looks for an anon user in the db 
    """
    cursor = anon_db.cursor()
    cursor.execute("""
      SELECT 
         ethereumba_user_id
      FROM 
        users_mapping 
      WHERE
        meetup_user_id = (?)
      """, (meetup_user_id, ))
    result = cursor.fetchone()
    cursor.close()
    return result


def insert_userid_mapping(anon_db, meetup_user_id, ethereumba_user_id):
    """
    Inserts a new mapping to hide identity
    """
    cursor = anon_db.cursor()
    cursor.execute("""
      INSERT INTO users_mapping
        (meetup_user_id, ethereumba_user_id)
      VALUES
        (?, ?)
    """, (meetup_user_id, ethereumba_user_id))
    anon_db.commit()


def insert_meetup(cursor, name, date, unknown_attendees):
    statement = """
    INSERT INTO meetups
      (name, date, unknown_attendees)
    VALUES
      (?, ?, ?)
    ON CONFLICT (name) DO UPDATE SET unknown_attendees = excluded.unknown_attendees
  """
    cursor.execute(statement, (name, date, unknown_attendees))

def insert_meetup_data(cursor, meetup_id, ethereumba_user_id, rsvp, attended):
    statement = """
      INSERT INTO meetup_attendance
        (meetup_id, ethereumba_user_id, rsvp, attended)
      VALUES
        (?, ?, ?, ?)
      ON CONFLICT (meetup_id, ethereumba_user_id) DO UPDATE SET attended = excluded.attended, rsvp = excluded.rsvp
    """
    cursor.execute(statement, (meetup_id, ethereumba_user_id, rsvp, attended))

def look_for_meetup(cursor, name):
    cursor.execute("SELECT id FROM meetups WHERE name = (?)", (name, ))
    return cursor.fetchone()
