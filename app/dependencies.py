from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "aisjdiaSJ$D@8123#2312"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
