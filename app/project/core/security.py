from jose import jwt
import datetime
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from core.config import settings

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme (token endpoint define karna hoga in auth router)
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/token",
    scopes={
        "user": "Basic user access",
        "admin": "Admin access"
    },
)

# ======================
# Password hashing utils
# ======================
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

# ======================
# JWT utils
# ======================
def create_access_token(subject: str, scopes: list[str] = None, expires_minutes: int = 15) -> str:
    if scopes is None:
        scopes = []
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_minutes)
    payload = {"sub": subject, "scopes": scopes, "exp": expire}
    return jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

# ======================
# Current User Dependency (with RBAC)
# ======================
async def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    username: str = payload.get("sub")
    token_scopes = payload.get("scopes", [])

    # RBAC: check required scopes
    for scope in security_scopes.scopes:
        if scope not in token_scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )

    return {"username": username, "scopes": token_scopes}

