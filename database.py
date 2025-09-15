from typing import List, Tuple
from contextlib import contextmanager

Poll = Tuple[int, str, str]
Option = Tuple[int, str, int]
Vote = Tuple[str, int]


CREATE_POLL_SCHEMA = """CREATE SCHEMA IF NOT EXISTS poll;"""

CREATE_POLLS = "CREATE TABLE IF NOT EXISTS poll.polls (id SERIAL PRIMARY KEY, title TEXT, owner_username TEXT);"
CREATE_OPTIONS = """CREATE TABLE IF NOT EXISTS poll.options
(id SERIAL PRIMARY KEY, option_text TEXT, poll_id INTEGER, FOREIGN KEY(poll_id) REFERENCES poll.polls(id));"""
CREATE_VOTES = """CREATE TABLE IF NOT EXISTS poll.votes
(username TEXT, option_id INTEGER, vote_timestamp INTEGER, FOREIGN KEY(option_id) REFERENCES poll.options(id));"""

SELECT_ALL_POLLS = "SELECT * FROM poll.polls;"
SELECT_POLL = "SELECT * FROM poll.polls WHERE id = %s;"
SELECT_LATEST_POLL = """SELECT * FROM poll.polls
WHERE polls.id = (
    SELECT id FROM poll.polls ORDER BY id DESC LIMIT 1
);"""

SELECT_POLL_OPTIONS = "SELECT * FROM poll.options WHERE poll_id = %s;"
SELECT_OPTION = "SELECT * FROM poll.options WHERE id = %s;"

SELECT_VOTES_FOR_OPTION = "SELECT * FROM poll.votes WHERE option_id = %s;"

INSERT_POLL_RETURN_ID = "INSERT INTO poll.polls (title, owner_username) VALUES (%s, %s) RETURNING id;"
INSERT_OPTION = "INSERT INTO poll.options (option_text, poll_id) VALUES (%s, %s) RETURNING id;"
INSERT_VOTE = "INSERT INTO poll.votes (username, option_id, vote_timestamp) VALUES (%s, %s, %s);"


@contextmanager
def get_cursor(connection):
    with connection:
        with connection.cursor() as cursor:
            yield cursor


def create_poll_schema(connection):
    with get_cursor(connection) as cursor:
        cursor.execute(CREATE_POLL_SCHEMA)
        connection.commit()

def create_tables(connection):
    with get_cursor(connection) as cursor:
        cursor.execute(CREATE_POLLS)
        cursor.execute(CREATE_OPTIONS)
        cursor.execute(CREATE_VOTES)
        connection.commit()


# -- polls --


def create_poll(connection, title: str, owner: str):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_POLL_RETURN_ID, (title, owner))

        poll_id = cursor.fetchone()[0]
        connection.commit()
        return poll_id


def get_polls(connection) -> List[Poll]:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_ALL_POLLS)
        connection.commit()
        return cursor.fetchall()


def get_poll(connection, poll_id: int) -> Poll:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_POLL, (poll_id,))
        connection.commit()
        return cursor.fetchone()


def get_latest_poll(connection) -> list[Poll]:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_LATEST_POLL)
        connection.commit()
        return cursor.fetchone()


def get_poll_options(connection, poll_id: int) -> list[Option]:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_POLL_OPTIONS, (poll_id,))
        connection.commit()
        return cursor.fetchall()


# -- options --


def get_option(connection, option_id: int) -> Option:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_OPTION, (option_id,))
        connection.commit()
        return cursor.fetchone()


def add_option(connection, option_text: str, poll_id: int):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_OPTION, (option_text, poll_id))
        option_id = cursor.fetchone()[0]
        connection.commit()
        return option_id


# -- votes --


def get_votes_for_option(connection, option_id: int) -> list[Vote]:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_VOTES_FOR_OPTION, (option_id,))
        connection.commit()
        return cursor.fetchall()


def add_poll_vote(connection, username: str, vote_timestamp: float, option_id: int):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_VOTE, (username, option_id, vote_timestamp))
        connection.commit()
