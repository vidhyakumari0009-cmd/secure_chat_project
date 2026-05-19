from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.fernet import Fernet


# ---------- RSA KEYS ----------

def generate_rsa_keys():

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    return private_key, public_key


def serialize_public_key(public_key):
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )


# ---------- AES (FERNET) ----------

def generate_aes_key():
    return Fernet.generate_key()


def encrypt_message(aes_key, message):
    f = Fernet(aes_key)
    return f.encrypt(message.encode())


def decrypt_message(aes_key, encrypted_message):
    f = Fernet(aes_key)
    return f.decrypt(encrypted_message).decode()
