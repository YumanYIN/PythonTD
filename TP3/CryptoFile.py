# coding=utf-8
import base64
import hashlib
import getpass
import ast
import os
from Crypto.Cipher import AES
from Crypto import Random

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:- ord(s[len(s) - 1:])]


# Méthode pour décrypter un fichier par rapport à un mot de passe
def decrypt(enc, password):
    enc = base64.b64decode(enc)
    iv = enc[: 16]
    cipher = AES.new(password[: 32], AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))


# Methode pour que l'utilisateur se connecte
def login():
    # récupération de l'id 
    user = input("Username: ")
    # encryptage du mot de passe pour vérification 
    passw = encrypt_string(getpass.getpass("Password: ") + user + "loremipsumdolorsitamet")
    f = open("usersFile.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split("|")
        # vérification de la véracité des informations if (user == us) and (passw == pw):
        print ("Login successful!")
        return passw
    print ("Wrong username/password")
    return False


# Encrypte le mot de passe avec un algorithme de type sha 256
def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


# connexion
passw = login()
# vérification du mot de passe
if (passw != False):
    filepath = input("Enter the filepath to decrypt: ")
    f = open(filepath, "rb")
    content = ""
    # lecture du contenu et decryptage 
    for line in f.readlines():
        content += bytes.decode(decrypt(line, passw))
        print (content)
