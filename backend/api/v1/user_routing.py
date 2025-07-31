"""
Router for User model
"""
from fastapi import APIRouter, Depends, status
from typing import Union
from sqlalchemy.orm import Session
from backend.db.session import get_db
from backend.schemas import UserSelfRead, UserEveryoneRead, UserCreate, UserLogin
from backend.models import User


router = APIRouter()


@router.get('/<user_id>', status_code=status.HTTP_200_OK, response_model=Union[UserEveryoneRead, UserSelfRead])
def get_user(user_id: int, db: Session = Depends(get_db)) -> Union[UserSelfRead, UserEveryoneRead]:
    """Endpoint for get a certain user request
    :param user_id: integer id of user
    :param db: database session
    :return: Pydantic UserSelfRead or UserEveryoneRead model object
    """
    current_user = get_current_user_service(credentials.credentials, db)
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if current_user.id == user_id:
        return UserSelfRead.model_validate(user)
    return UserEveryoneRead.model_validate(user)


@router.post('/sign_up', status_code=status.HTTP_201_CREATED)
def sign_up(user: UserCreate, db: Session = Depends(get_db)) -> int:
    """Endpoint for user sign up request
    :param user: Pydantic UserCreate model object
    :param db: database session
    :return: integer id of new user
    """
    db_user = create_user_service(db, user)
    return db_user.id


@router.post('/login', status_code=status.HTTP_200_OK)
def login(user: UserLogin, db: Session = Depends(get_db)) -> dict[str, str]:
    """Endpoint for user login request
    :param user: Pydantic UserCreate model object
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    db_user = authenticate_user_service(db, user)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token_service(db_user.id)
    refresh_token = create_refresh_token_service(db_user.id)

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        max_age=30 * 60,  # 30 minutes
        secure=True,
        samesite="lax"
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        max_age=7 * 24 * 60 * 60,  # 7 days
        secure=True,
        samesite="lax"
    )

    return {"message": "success", "access_token": access_token}


@router.post('/logout', status_code=status.HTTP_200_OK)
def logout(db: Session = Depends(get_db)) -> dict[str, str]:
    """Endpoint for user logout request
    :param db: database session
    :return: if success -> {'message': 'success'}; else -> {'error': <error_msg>}
    """
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return {"message": "success"}


@router.post('/refresh', status_code=status.HTTP_200_OK)
def refresh_token_service(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)
) -> dict:
    """Function that refreshes access token using refresh token
    :param credentials: JWT token credentials
    :param db: database session
    :return: new access token
    """
    payload = decode_token_service(credentials.credentials)
    if payload["type"] != "refresh":
        raise HTTPException(status_code=401, detail="Invalid token type")

    user = db.query(User).filter(User.id == int(payload["sub"])).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    new_access_token = create_access_token_service(user.id)
    return {"access_token": new_access_token}
