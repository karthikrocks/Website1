from cryptography.fernet import Fernet


class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key


encryptor = Encryptor()

# Driver Code..
# mykey = encryptor.key_create()

# loaded_key = encryptor.key_load(str('keys/key.key'))

# print(f"This is my Key: ", {loaded_key})
