"""
Business logic for User authentication
"""
from typing import Union
from sqlalchemy.orm import Session
from fastapi import HTTPException, Response
from fastapi.security import HTTPAuthorizationCredentials
from backend.models import User
from backend.schemas import UserCreate, UserLogin, UserSelfRead, UserEveryoneRead
from backend.utils import AuthUtilsHelper


def get_user_service(db: Session, user_id: int, credentials: HTTPAuthorizationCredentials
                     ) -> Union[UserSelfRead, UserEveryoneRead]:
    """Function that returns a certain user. The return info depends on current auth user
    :param credentials: JWT token credentials
    :param db: database session
    :param user_id: integer id of user
    :return: Pydantic UserSelfRead or UserEveryoneRead model object
    :raises: HTTPException: if no user was found
    """
    current_user = AuthUtilsHelper.get_current_user(credentials.credentials, db)
    user = db.query(User).get(user_id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    if current_user.id == user_id:
        return UserSelfRead.model_validate(user)
    return UserEveryoneRead.model_validate(user)


def create_user_service(db: Session, user: UserCreate) -> int:
    """Function that creates User object
    :param db: database session
    :param user: Pydantic UserCreate object
    :return: new created User model object
    :raises: HTTPException: if email or username already exists or passwords don't match
    """
    if db.query(User).filter_by(email=user.email).first():
        raise HTTPException(status_code=400, detail='Email already registered')
    if db.query(User).filter_by(username=user.username).first():
        raise HTTPException(status_code=400, detail='Username already taken')
    if user.password1 != user.password2:
        raise HTTPException(status_code=400, detail='Passwords do not match')

    db_user = User(
        username=user.username,
        email=user.email,
        password=AuthUtilsHelper.get_password_hash(user.password1),
        bio=user.bio,
        avatar_url=user.avatar_url
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.id


def login_service(db: Session, response: Response, user: UserLogin) -> dict[str, str]:
    """Function that authenticates user, creates cookie for user and log him in
    :param db: database session
    :param response: FastAPI Response object
    :param user: Pydantic UserLogin object
    :return: if success -> {'message': 'success', 'access_token': <token>}
    :raises: HTTPException: if no user was found
    """
    db_user = AuthUtilsHelper.authenticate_user(db, user.login, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail='Invalid credentials')

    access_token = AuthUtilsHelper.create_access_token(db_user.id)
    refresh_token = AuthUtilsHelper.create_refresh_token(db_user.id)

    response.set_cookie(
        key='access_token',
        value=access_token,
        httponly=True,
        max_age=30 * 60,
        secure=True,
        samesite='lax'
    )
    response.set_cookie(
        key='refresh_token',
        value=refresh_token,
        httponly=True,
        max_age=7 * 24 * 60 * 60,
        secure=True,
        samesite='lax'
    )
    return {'message': 'success', 'access_token': access_token}


def logout_service(response: Response) -> dict[str, str]:
    """Function that deletes cookie for user and log him out
    :param response: FastAPI Response object
    :return: if success -> {'message': 'success'}
    """
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return {"message": "success"}


def refresh_token_service(db: Session, credentials: HTTPAuthorizationCredentials):
    payload = AuthUtilsHelper.decode_token(credentials.credentials)
    if payload['type'] != 'refresh':
        raise HTTPException(status_code=401, detail='Invalid token type')

    user = db.query(User).filter_by(id=int(payload['sub'])).first()
    if not user:
        raise HTTPException(status_code=401, detail='User not found')

    new_access_token = AuthUtilsHelper.create_access_token(user.id)
    return {'access_token': new_access_token}
