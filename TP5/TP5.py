
import csv

# Exercice1
from Connection import Connection

file_commune = "files/communes.csv"
file_department = "files/departements.csv"
file_region = "files/regions.csv"

communes_all = []
departments_all = []
regions_all = []

f = open(file_commune, 'r')
communes_all = f.readlines()
f.close()

"""
with open(file_commune, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    code_communes = [row[5] for row in reader]
    for row in reader:
        communes_all.append(row)

with open(file_department, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        departments_all.append(row)

with open(file_region, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        regions_all.append(row)
"""


# db
#db = Connection("db/database.db")
#db.init()
#db.importData(communes_all, departments_all, regions_all)