"""
Business logic for User authentication
"""
import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import HTTPException
from backend.models.user import User
from backend.schemas.user import UserCreate, UserLogin
from backend.core.config import app_settings


SECRET_KEY = app_settings.secret_key
ALGORITHM = app_settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = app_settings.access_token_expire_minutes
REFRESH_TOKEN_EXPIRE_DAYS = app_settings.refresh_token_expire_days

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password_service(plain_password: str, hashed_password: str) -> bool:
    """Verify if plain password matches hashed password
    :param plain_password: plain text password
    :param hashed_password: hashed password from database
    :return: True if passwords match, False otherwise
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash_service(password: str) -> str:
    """Hash a password
    :param password: plain text password
    :return: hashed password
    """
    return pwd_context.hash(password)

def create_access_token_service(user_id: int) -> str:
    """Create JWT access token for user
    :param user_id: integer id of user
    :return: encoded JWT access token
    """
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": str(user_id), "exp": expire, "type": "access"}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token_service(user_id: int) -> str:
    """Create JWT refresh token for user
    :param user_id: integer id of user
    :return: encoded JWT refresh token
    """
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode = {"sub": str(user_id), "exp": expire, "type": "refresh"}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token_service(token: str) -> dict:
    """Decode JWT token
    :param token: JWT token string
    :return: decoded token payload
    :raises HTTPException: if token is invalid or expired
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user_service(token: str, db: Session) -> User:
    """Get current user from JWT token
    :param token: JWT access token
    :param db: database session
    :return: User model object
    :raises HTTPException: if token is invalid or user not found
    """
    payload = decode_token_service(token)
    if payload["type"] != "access":
        raise HTTPException(status_code=401, detail="Invalid token type")
    user = db.query(User).filter(User.id == int(payload["sub"])).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

def create_user_service(db: Session, user: UserCreate) -> User:
    """Create a new user
    :param db: database session
    :param user: Pydantic UserCreate object
    :return: created User model object
    :raises HTTPException: if email or username already exists or passwords don't match
    """
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")
    if user.password1 != user.password2:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    db_user = User(
        username=user.username,
        email=user.email,
        password=get_password_hash_service(user.password1),
        bio=user.bio,
        avatar_url=user.avatar_url
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user_service(db: Session, login: UserLogin) -> User:
    """Authenticate user by login (email or username) and password
    :param db: database session
    :param login: Pydantic UserLogin object
    :return: User model object if authenticated, None otherwise
    """
    user = db.query(User).filter(
        (User.email == login.login) | (User.username == login.login)
    ).first()
    if not user or not verify_password_service(login.password, user.password):
        return None
    return user