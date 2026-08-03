from datetime import UTC, datetime, timedelta
from uuid import UUID

import jwt
from app.core.config import settings
from app.core.exceptions import UnauthorizedError
from jwt import InvalidTokenError


def create_access_token(subject: str) -> str:
    """
    Create a signed JWT access token.
    """

    expires_at = datetime.now(UTC) + timedelta(
        minutes=settings.jwt_access_token_expire_minutes,
    )

    payload = {
        "sub": subject,
        "exp": expires_at,
    }

    return jwt.encode(
        payload,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm,
    )


def decode_access_token(token: str) -> str:
    """
    Decode and validate an access token.
    """

    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm],
        )

        subject = payload.get("sub")

        if subject is None:
            raise InvalidTokenError()

        UUID(subject)

        return subject

    except InvalidTokenError as exc:
        raise UnauthorizedError("Invalid authentication credentials.") from exc
