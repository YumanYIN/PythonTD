#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import cgi


if __name__ == '__main__':
    form = cgi.FieldStorage()
    name = form.getvalue("name")
    if name is not None:
        print("Content-type: text/html; charset=utf-8\n")
        html = """<!DOCTYPE html> <head>
                <title>Mon programme</title>
                </head>
                <body>
                <h1> """ + name + """</h1>
                </body>
                </html>
                """
        print(html)
        with open("./cgi-bin/names.txt", "a") as f:
            f.write("\n" + name)
    else:
        print("Content-type: text/html; charset=utf-8\n")
        html = """<!DOCTYPE html> <head>
        <title>Mon programme</title>
        </head>
        <body>
        <form action="/cgi-bin/index.py" method="GET">
        <input type="text" name="name" value="Votre nom" />
        <input type="submit" name="send" value="Envoyer information au serveur"> </form>
        </body>
        </html>
        """
        print(html)
