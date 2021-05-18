from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("my_key.key", "wb") as key_file:
        key_file.write(key)



