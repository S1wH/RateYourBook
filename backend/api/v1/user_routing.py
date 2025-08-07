"""
Router for User model
"""
from fastapi import APIRouter, Depends, Response, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import Union
from sqlalchemy.orm import Session
from db.session import get_db
from schemas import UserSelfRead, UserEveryoneRead, UserCreate, UserLogin
from services.auth_service import get_user_service, create_user_service, login_service, logout_service, refresh_token_service


router = APIRouter()
security = HTTPBearer()


@router.get('/<user_id>', status_code=status.HTTP_200_OK, response_model=Union[UserEveryoneRead, UserSelfRead])
def get_user(user_id: int, db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Depends(security)
             ) -> Union[UserSelfRead, UserEveryoneRead]:
    """Endpoint for get a certain user request
    :param credentials: JWT token credentials
    :param user_id: integer id of user
    :param db: database session
    :return: Pydantic UserSelfRead or UserEveryoneRead model object
    """
    return get_user_service(db, user_id, credentials)


@router.post('/sign_up', status_code=status.HTTP_201_CREATED)
def sign_up(user: UserCreate, db: Session = Depends(get_db)) -> int:
    """Endpoint for user sign up request
    :param user: Pydantic UserCreate model object
    :param db: database session
    :return: integer id of new user
    """
    return create_user_service(db, user)


@router.post('/login', status_code=status.HTTP_200_OK)
def login(user: UserLogin, response: Response, db: Session = Depends(get_db)) -> dict[str, str]:
    """Endpoint for user login request
    :param response: FastAPI Response object
    :param user: Pydantic UserCreate model object
    :param db: database session
    :return: if success -> {'message': 'success', 'access_token': <token>}
    """
    return login_service(db, response, user)


@router.post('/logout', status_code=status.HTTP_200_OK)
def logout(response: Response) -> dict[str, str]:
    """Endpoint for user logout request
    :param response: FastAPI Response object
    :return: if success -> {'message': 'success'}
    """
    return logout_service(response)


@router.post('/refresh', status_code=status.HTTP_200_OK)
def refresh_token(db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Depends(security)
                  ) -> dict[str, str]:
    """Function that refreshes access token using refresh token
    :param credentials: JWT token credentials
    :param db: database session
    :return: if success -> {'access_token': <new_token>}
    """
    return refresh_token_service(db, credentials)
