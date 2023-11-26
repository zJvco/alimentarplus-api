import boto3
import os
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

SECRET_KEY = "aisjdiaSJ$D@8123#2312"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
s3_client = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name=os.environ.get("AWS_REGION")
)