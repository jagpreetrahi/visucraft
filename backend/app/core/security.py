from datetime import datetime, timedelta, timezone
from uuid import UUID
import bcrypt
from jose import JWTError, jwt
from app.core.config import get_settings

settings = get_settings()

_BCRYPT_MAX_BYTES = 72

def hashPassword(password: str) -> str:
    truncated = password.encode("utf-8")[:_BCRYPT_MAX_BYTES]
    return bcrypt.hashpw(truncated, bcrypt.gensalt()).decode("utf-8")

def verify_password(plainPassword: str, hashedPassword: str) -> bool:
    truncated_plain = plainPassword.encode("utf-8")[:_BCRYPT_MAX_BYTES]
    return bcrypt.checkpw(truncated_plain, hashedPassword.encode("utf-8"))


def create_access_token(user_id: UUID) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    payload = { "sub": str(user_id), "exp": expire}
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)

def decode_access_token(token: str) -> UUID | None: 
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=settings.jwt_algorithm)
        return UUID(payload["sub"])
    except (JWTError, KeyError, ValueError):
        return None