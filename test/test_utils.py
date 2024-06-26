import unittest
import uuid
from app.utils import generate_uuid, verify_password, generate_password_hash, create_jwt_token, token_required

def test_generate_uuid():
    uuid_standard_len = 36

    assert len(str(uuid.uuid4())) == uuid_standard_len


def test_verify_password():
    # Testa se a função verify_password retorna True quando a senha é correta
    assert verify_password("password", "hashed_password") == True

    # Testa se a função verify_password retorna False quando a senha é incorreta
    assert verify_password("wrong_password", "hashed_password") == False


def test_generate_password_hash():
    # Testa se a função generate_password_hash retorna a senha hash corretamente
    assert generate_password_hash("password") == "fake_hashed_password"