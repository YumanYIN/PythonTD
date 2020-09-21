from tkinter import *


class LoginWindow:

    def __init__(self, root):
        self.root = root

        self.root.title("Login")
        self.root.geometry("300x250")

        Label(self.root, text='Username').pack()
        username_login_entry = Entry(self.root, textvariable="username")
        username_login_entry.pack()

        Label(self.root, text='Password').pack()
        username_login_entry = Entry(self.root, textvariable="password", show="*")
        username_login_entry.pack()

        Button(self.root, text="Login", width=10, height=1).pack()
        Button(self.root, text="Register", width=10, height=1).pack()

    def register(self):
        pass

    def login(self):
        pass

    def readFile(self):
        pass










if __name__ == '__main__':
    root = Tk()
    myCal = LoginWindow(root)

    root.mainloop()