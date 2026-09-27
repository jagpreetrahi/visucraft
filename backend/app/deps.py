from fastapi import Cookie, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.core.security import decode_access_token
from app.models.user import User

async def get_current_user(
    access_token: str | None = Cookie(default=None),
    db: AsyncSession = Depends(get_db)  
) -> User:
    unauthorized = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")
    if not access_token: 
        raise unauthorized

    user_id = decode_access_token(access_token)
    if user_id is None:
        raise unauthorized

    user = await db.get(User, user_id)
    if user is None:
        raise unauthorized

    return user 

    
