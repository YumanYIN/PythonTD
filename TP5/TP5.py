
import csv

# Exercice1
from Connection import Connection

file_commune = "files/communes.csv"
file_department = "files/departements.csv"
file_region = "files/regions.csv"

communes_all = []
departments_all = []
regions_all = []


with open(file_commune, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        communes_all.append(row)

with open(file_department, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        departments_all.append(row)

with open(file_region, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        regions_all.append(row)

#print (regions_all)

# db
db = Connection("db/database.db")
db.init()
db.importData(communes_all, departments_all, regions_all)