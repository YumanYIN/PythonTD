
import csv

# Exercice1
from Connection import Connection

file_commune = "files/communes.csv"
file_department = "files/departements.csv"
file_region = "files/regions.csv"

communes_all = []
departments_all = []
regions_all = []


with open(file_commune, 'r', encoding='iso-8859-1') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        communes_all.append(row)

with open(file_department, 'r', encoding='iso-8859-1') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        departments_all.append(row)

with open(file_region, 'r', encoding='iso-8859-1') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        regions_all.append(row)

#print (regions_all)

# db
db = Connection("db/database.db")
db.init()
db.importData(communes_all, departments_all, regions_all)

department_dic = {departments_all[i][0].split(';')[2]: departments_all[i][0].split(';')
                  for i in range(8, len(departments_all) - 1)}
region_dic = {int(regions_all[i][0].split(';')[0]): regions_all[i][0].split(';')
              for i in range(8, len(regions_all))}

departments = db.getDataBySqlStr("select * from department")
for department in departments:
    # department_populaire = department[2]
    department_populaire_count = db.getDataBySqlStr("select sum(population_totale) from commune where code_departement = \"" + str(department[0]) +"\"")
    pc = department_populaire_count[0][0]
    pt = int(str(department_dic[department[0]][-2]).replace(" ", ""))
    print("In department " + department[1] +
          ": population count = " + str(pc) +
          ", population total = " + str(pt) +
          ", equal or not? " + str(pc == pt))
print("\n")

regions = db.getDataBySqlStr("select * from region")
for region in regions:
    region_populaire_count = db.getDataBySqlStr("select sum(commune.population_totale) from commune join department on (commune.code_departement = department.code_departement) where department.code_region = \"" + str(region[0]) + "\"")
    pc = region_populaire_count[0][0]
    pt = int(str(region_dic[region[0]][-1]).replace(" ", ""))
    print("In region " + region[1] +
          ": population count = " + str(pc) +
          ", population total = " + str(pt) +
          ", equal or not? " + str(pc == pt))
