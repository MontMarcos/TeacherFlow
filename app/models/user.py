<<<<<<< Updated upstream
import json
import os
=======
from ..db.database import db, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from bcrypt import hashpw, gensalt, checkpw
>>>>>>> Stashed changes

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

<<<<<<< Updated upstream
APP_ROOT = os.path.dirname(BASE_DIR) 

USERS_FILE = os.path.join(APP_ROOT, 'db', 'user.json') 

class User:    
    def __init__(self, user_data):
        self.id = user_data.get('id')
        self.name = user_data.get('name') 
        self.password = user_data.get('password')
=======
class User(Base):
    __tablename__ = "user"
>>>>>>> Stashed changes

    def __repr__(self):
        return f'<User {self.name} (ID: {self.id})>'

    @staticmethod
    def load_users():
        with open(USERS_FILE, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                processed_users = []
                for item in data:
                    user_info = item.get('user', {}) 
                    user_info['id'] = item.get('id')
                    processed_users.append(user_info)
                
                return processed_users

<<<<<<< Updated upstream
    @staticmethod
    def get_by_name(name):
        """Busca um usuário pelo nome. Retorna uma instância de User ou None."""
        users_list = User.load_users()
        for user_data in users_list:
            if user_data.get('name') == name:
                return User(user_data) 
        return None

    def check_password(self, password):
        return str(self.password) == str(password)
=======
    def set_password(self, password: str):
        # Gera o hash da senha usando bcrypt
        self.hashed_password = hashpw(
            password.encode("utf-8"), gensalt()
        ).decode("utf-8")

    def verify_password(self, password: str) -> bool:
        # Verifica a senha usando bcrypt
        return checkpw(
            password.encode("utf-8"),
            self.hashed_password.encode("utf-8")
        )
    

    # ==============================
    # CRUD
    # ==============================

    # -------- CREATE --------
    @classmethod
    def create(cls, username: str, email: str, password: str,
               full_name: str = None, db_session: Session = None):

        try:
            if cls.get_by_username(username, db_session):
                raise ValueError(f"Username '{username}' já está em uso.")

            if cls.get_by_email(email, db_session):
                raise ValueError(f"E-mail '{email}' já está cadastrado.")

            user = cls(
                username=username,
                email=email,
                full_name=full_name
            )

            user.set_password(password)

            db_session.add(user)
            db_session.commit()
            db_session.refresh(user)
            return user

        except (SQLAlchemyError, ValueError) as e:
            db_session.rollback()
            raise e

    # -------- READ --------
    @classmethod
    def get_by_username(cls, username: str, db_session: Session = None):
        return db_session.query(cls).filter(cls.username == username).first()

    @classmethod
    def get_by_email(cls, email: str, db_session: Session = None):
        return db_session.query(cls).filter(cls.email == email).first()

    @classmethod
    def get_by_id(cls, user_id: int, db_session: Session = None):
        return db_session.query(cls).filter(cls.id == user_id).first()

    @classmethod
    def get_all(cls, db_session: Session = None):
        return db_session.query(cls).all()

    # -------- UPDATE --------
    def edit_user(self, username: str = None, email: str = None,
                  password: str = None, full_name: str = None,
                  db_session: Session = None):

        try:
            if username and username != self.username:
                if User.get_by_username(username, db_session):
                    raise ValueError(f"Username '{username}' já existe.")
                self.username = username

            if email and email != self.email:
                if User.get_by_email(email, db_session):
                    raise ValueError(f"E-mail '{email}' já existe.")
                self.email = email

            if password:
                self.set_password(password)

            if full_name:
                self.full_name = full_name

            db_session.commit()
            db_session.refresh(self)
            return self

        except (SQLAlchemyError, ValueError) as e:
            db_session.rollback()
            raise e

    def edit_password(self, new_password: str, db_session: Session = None):
        try:
            self.set_password(new_password)
            db_session.commit()
            db_session.refresh(self)
            return self
        except SQLAlchemyError as e:
            db_session.rollback()
            raise e

    def edit_email(self, new_email: str, db_session: Session = None):
        try:
            if User.get_by_email(new_email, db_session):
                raise ValueError(f"E-mail '{new_email}' já está em uso.")

            self.email = new_email
            db_session.commit()
            db_session.refresh(self)
            return self

        except (SQLAlchemyError, ValueError) as e:
            db_session.rollback()
            raise e

    def edit_username(self, new_username: str, db_session: Session = None):
        try:
            if User.get_by_username(new_username, db_session):
                raise ValueError(f"Username '{new_username}' já está em uso.")

            self.username = new_username
            db_session.commit()
            db_session.refresh(self)
            return self

        except (SQLAlchemyError, ValueError) as e:
            db_session.rollback()
            raise e

    # -------- DELETE --------
    def delete_user(self, db_session: Session = None):
        try:
            db_session.delete(self)
            db_session.commit()
            return True
        except SQLAlchemyError as e:
            db_session.rollback()
            raise e
>>>>>>> Stashed changes
