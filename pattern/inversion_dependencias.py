from abc import ABC, abstractmethod


class DB(ABC):
    @abstractmethod
    def connect(self):
        pass


class MySQL(DB):
    def connect(self):
        print("Conectado a MySQL")


class PostgreSQL(DB):
    def connect(self):
        print("Conectado a PostgreSQL")


class App:
    def __init__(self, db: DB):
        self.db = db


# Inyección de dependencia
app = App(PostgreSQL())
app.db.connect()
