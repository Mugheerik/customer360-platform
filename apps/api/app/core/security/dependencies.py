from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.exceptions import UnauthorizedError
from app.core.security.jwt import decode_access_token
from app.database.dependencies import get_db
from app.modules.users.models import User
from app.modules.users.repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login",
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    """
    Return the authenticated user.
    """

    print("=" * 50)
    print("TOKEN:", token)

    user_id = decode_access_token(token)
    print("DECODED USER ID:", user_id)
    

    repository = UserRepository(db)

    user = repository.get_by_id(user_id)
   

    if user is None:
        raise UnauthorizedError("Invalid authentication credentials.")

    return user