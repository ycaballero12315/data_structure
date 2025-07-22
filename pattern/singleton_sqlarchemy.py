from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseSingleton:
    _instance = None

    def __new__(cls, db_url="postgresql+psycopg2://mi_user:mi_pass@localhost/mydb"):
        if cls._instance is None:
            print("Creando engine SQLAlchemy...")
            cls._instance = super().__new__(cls)
            cls._instance.engine = create_engine(db_url)
            cls._instance.Session = sessionmaker(bind=cls._instance.engine)
        return cls._instance

    def get_session(self):
        return self.Session()


# Uso
db = DatabaseSingleton()
session1 = db.get_session()
session2 = db.get_session()

print(session1 is session2)  # False → Cada sesión es nueva \
                             #pero el engine es unico
