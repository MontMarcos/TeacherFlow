import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
class Database:
    def __init__(self, url=None, echo=False):
        self.url = url or os.getenv("DATABASE_URL", "sqlite:///app.db")

        try:
            self.engine = create_engine(self.url, echo=echo, future=True)
        except OperationalError as e:
            print(f"[ERRO] Erro ao conectar ao banco: {e}")
            self.engine = None

        self.Base = declarative_base()

        if self.engine:
            self.SessionLocal = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine
            )
            self._check_sqlite_database()

    def _check_sqlite_database(self):
        """Verifica se o arquivo SQLite existe."""
        if self.url.startswith("sqlite:///"):
            db_path = self.url.replace("sqlite:///", "")
            if not os.path.exists(db_path):
                print(f"[INFO] Arquivo de Banco de Dados '{db_path}' será criado.")
            else:
                print(f"[INFO] Arquivo de Banco de Dados '{db_path}' encontrado.")

    def get_db(self):
        """Gera uma sessão e garante que ela será fechada depois."""
        if not self.engine:
             raise RuntimeError("A engine do banco de dados não foi inicializada corretamente.")
             
        db_session = self.SessionLocal()
        try:
            yield db_session
        finally:
            db_session.close()


db = Database()
Base = db.Base 