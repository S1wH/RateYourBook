"""
Utils module for auth methods
"""
import jwt
from typing import Optional
from fastapi import HTTPException
from datetime import datetime, timedelta
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from backend.models import User
from backend.core.config import app_settings


SECRET_KEY = app_settings.secret_key
ALGORITHM = app_settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = app_settings.access_token_expire_minutes
REFRESH_TOKEN_EXPIRE_DAYS = app_settings.refresh_token_expire_days

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class AuthUtilsHelper:
    """
    Class for all auth utils help functionality
    """

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify if plain password matches hashed password
        :param plain_password: plain text password
        :param hashed_password: hashed password from database
        :return: True if passwords match, False otherwise
        """
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        """Hash a password
        :param password: plain text password
        :return: hashed password
        """
        return pwd_context.hash(password)

    @staticmethod
    def create_access_token(user_id: int) -> str:
        """Create JWT access token for user
        :param user_id: integer id of user
        :return: encoded JWT access token
        """
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = {'sub': str(user_id), 'exp': expire, 'type': 'access'}
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def create_refresh_token(user_id: int) -> str:
        """Create JWT refresh token for user
        :param user_id: integer id of user
        :return: encoded JWT refresh token
        """
        expire = datetime.now() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode = {'sub': str(user_id), 'exp': expire, 'type': 'refresh'}
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def decode_token(token: str) -> dict:
        """Decode JWT token
        :param token: JWT token string
        :return: decoded token payload
        :raises HTTPException: if token is invalid or expired
        """
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token has expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')

    @staticmethod
    def get_current_user(token: str, db: Session) -> User:
        """Get current user from JWT token
        :param token: JWT access token
        :param db: database session
        :return: User model object
        :raises HTTPException: if token is invalid or user not found
        """
        payload = AuthUtilsHelper.decode_token(token)
        if payload['type'] != 'access':
            raise HTTPException(status_code=401, detail='Invalid token type')
        user = db.query(User).get(id=int(payload['sub']))
        if not user:
            raise HTTPException(status_code=401, detail='User not found')
        return user

    @staticmethod
    def authenticate_user(db: Session, login: str, password: str) -> Optional[User]:
        """Authenticate user by login (email or username) and password
        :param password: user's hashed password
        :param db: database session
        :param login: user's login
        :return: User model object if authenticated, None otherwise
        """
        user = db.query(User).filter((User.email == login) | (User.username == login)).first()
        if not user or not AuthUtilsHelper.verify_password(password, user.password):
            return None
        return user
