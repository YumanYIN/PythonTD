import hashlib
import os
from base64 import b64encode
import bcrypt
import random


if __name__ == "__main__":
    str = "user1".encode('utf-8')
    print(hashlib.sha512(str).hexdigest())
    print(b64encode(os.urandom(128)).decode('utf-8'))
    dic = {"1": "hhh", "2": "dhsfush"}

    password = "mon mot de passe".encode('utf-8')

    salt = bcrypt.gensalt()
    a = bcrypt.hashpw(password, salt)

    b = bcrypt.hashpw(password, salt)

    print(a, b)
    if a == b:
        print("same")



