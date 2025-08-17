from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
"""El patrón Singleton garantiza que una clase tenga una única instancia 
en todo el sistema, y proporciona un punto de acceso global a ella.
En el contexto de bases de datos, esto es útil para evitar crear múltiples 
engines o conexiones innecesarias, que pueden ser costosas o conflictivas."""

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
    def dispose(self):
        """Cierra el engine y libera recursos."""
        if self._instance:
            self._instance.engine.dispose()
            self._instance = None
            print("Engine SQLAlchemy cerrado y recursos liberados.")


# Uso
db = DatabaseSingleton()
db1 = DatabaseSingleton()

# Verifica que ambos objetos sean la misma instancia
print(db is db1)  # True → Ambos son la misma instancia

# Ejemplo de uso de la sesión
session1 = db.get_session()
session2 = db.get_session()

print(session1 is session2)  # False → Cada sesión es nueva \
                             #pero el engine es unico
