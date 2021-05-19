from cryptography.fernet import Fernet

def genwrite_key():
    key = Fernet.generate_key()
    print(key)
print(genwrite_key())