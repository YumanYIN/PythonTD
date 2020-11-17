#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import cgi

"""
to show form
"""
def show_form():
    print("Content-type: text/html; charset=utf-8\n")
    html = """<!DOCTYPE html> <head>
            <title>Mon programme</title>
            </head>
            <body>
            <form action="/cgi-bin/login.py" method="POST">
            <input type="text" name="name" value="Username" />
            <input type="password" name="pd" />
            <input type="submit" value="Se connecter">
            </form>
            </body>
            </html>
            """
    print(html)

"""
to show information in names.txt
those name could be write by index.py
"""
def show_names():
    print("Content-type: text/html; charset=utf-8\n")
    html = """<!DOCTYPE html> <head>
                <title>Mon programme</title>
                </head>
                <body>"""

    with open("./cgi-bin/names.txt", "r") as f:
        names = f.readlines()
        html += """<p>Fichier name.txt:<p>"""
        for theName in names:
            html += """<h1>""" + theName + """</h1>"""
    html += """</body>
            </html>"""
    print(html)


if __name__ == '__main__':
    form = cgi.FieldStorage()
    name = form.getvalue("name")
    pd = form.getvalue("pd")

    # if user doesn't input username or password
    if (name is None) or (pd is None):
        show_form()
    else:
        user_dic = {}
        with open("./cgi-bin/user.txt", "r") as f:
            users = f.readlines()
            for user in users:
                user_dic[user.split(',')[0]] = user.split(',')[1]
        try:
            # if password is correct
            if user_dic[name] == pd:
                show_names()
            else:
                show_form()
        except:
            pass
