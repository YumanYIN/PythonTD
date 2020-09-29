from tkinter import *
import hashlib
import bcrypt

global filename

class LoginWindow:

    def __init__(self, root, users):
        self.root = root

        self.root.title("Login")
        self.root.geometry("300x250")

        self.username = StringVar()
        self.password = StringVar()
        self.users = users

        Label(self.root, text='Username').pack()
        username_entry = Entry(self.root, textvariable=self.username)
        username_entry.pack()

        Label(self.root, text='Password').pack()
        password_entry = Entry(self.root, textvariable=self.password, show="*")
        password_entry.pack()

        Button(self.root, text="Login", width=10, height=1, command=lambda: self.login()).pack()
        Button(self.root, text="Register", width=10, height=1, command=lambda: self.register()).pack()

    def register(self):
        username = self.username.get()

        for key in self.users:
            if key == username:
                print("This username is used by else, please choose another one")
                return

        salt = bcrypt.gensalt()
        passwordHash = bcrypt.hashpw(self.password.get().encode('utf-8'), salt)

        self.users[username] = [passwordHash, salt]
        if writeFile(users, username):
            print("Register successfully")

    def login(self):
        username = self.username.get()

        for key in self.users:
            # old hash password, saved in file
            oPw = users[key][0]

            # new hash password, generated by salt saved in file
            nPw = bcrypt.hashpw(self.password.get().encode('utf-8'), bytes(users[key][1], 'utf-8')).decode('utf-8')
            if (key == username) & (oPw == nPw):
                print("Login success")

                input("Choose: \n\t1. Encrypt ")

                return

        print("Login failed")
        return


def readFile():
    # save username, password hash, and salt, username is the key,
    # every value is an array consist of password hash and salt
    users = {}
    with open(filename, 'rt') as fp:
        lines = fp.readlines()
        for line in lines:
            line = line.split(";")
            # the first is hash password, the second is salt
            users[line[0]] = [line[1], line[2][:-1]]
    # so, users = {username : [password hash, salt]}
    return users


def writeFile(users, username):
    try:
        with open(filename, 'at') as fp:
            # save username, hash password and salt in the file
            fp.write(username + ';' + users[username][0].decode('utf-8') + ';' + users[username][1].decode('utf-8') + '\n')
    except IOError:
        return False
    return True


if __name__ == '__main__':
    filename = "usersWithSalt.txt"
    users = readFile()
    root = Tk()
    myCal = LoginWindow(root, users)

    root.mainloop()
