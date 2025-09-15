from ..connection_pool import get_connection
from .. import database

class Option:
    def __init__(self, option_text: str, poll_id: int, id: int = None):
        self.id = id
        self.option_text = option_text
        self.poll_id = poll_id

    def __repr__(self):
        return f"Option({self.option_text!r}, {self.poll_id!r}, {self.id!r})"

    def save(self):
        with get_connection() as connection:
            new_option_id = database.add_option(connection, self.option_text, self.poll_id)
            self.id = new_option_id

    @property
    def votes(self) -> list[tuple]:
        with get_connection() as connection:
            return database.get_votes_for_option(connection, self.id)

    def vote(self, username: str):
        import time
        with get_connection() as connection:
            database.add_poll_vote(connection, username, time.time(), self.id)

    @classmethod
    def get(cls, option_id: int) -> "Option":
        with get_connection() as connection:
            option = database.get_option(connection, option_id)
            return cls(option[1], option[2], option[0])


