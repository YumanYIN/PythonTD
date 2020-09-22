from tkinter import *
import hashlib

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

        self.users[username] = hashlib.sha512(self.password.get().encode('utf-8')).hexdigest()
        if writeFile(users, username):
            print("Register successfully")

    def login(self):
        username = self.username.get()

        for key in self.users:
            if (key == username) & (hashlib.sha512(self.password.get().encode('utf-8')).hexdigest() == users[key]):
                print("Login success")
                return

        print("Login failed")
        return


def readFile():
    users = {}
    with open(filename, 'rt') as fp:
        lines = fp.readlines()
        for line in lines:
            line = line.split(";")
            users[line[0]] = line[1][:-1]
    return users


def writeFile(users, username):
    try:
        with open(filename, 'at') as fp:
            fp.write(username + ';' + users[username] + '\n')
    except IOError:
        return False
    return True


if __name__ == '__main__':
    filename = "users.txt"
    users = readFile()
    root = Tk()
    myCal = LoginWindow(root, users)

    root.mainloop()
