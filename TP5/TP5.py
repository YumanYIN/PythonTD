
import csv

# Exercice1
from Connection import Connection

file_commune = "files/communes.csv"
file_department = "files/departements.csv"
file_region = "files/regions.csv"

communes_all = []
departments_all = []
regions_all = []

def print_department_population(departments_all, db):
    department_dic = {departments_all[i][0].split(';')[2]: departments_all[i][0].split(';')
                      for i in range(8, len(departments_all) - 1)}
    departments = db.getDataBySqlStr("select * from department")
    for department in departments:
        # department_populaire = department[2]
        department_populaire_count = db.getDataBySqlStr(
            "select sum(population_totale) from commune where code_departement = \"" + str(department[0]) + "\"")
        pc = department_populaire_count[0][0]
        pt = int(str(department_dic[department[0]][-2]).replace(" ", ""))
        print("In department " + department[1] +
              ": population count = " + str(pc) +
              ", population total = " + str(pt) +
              ", equal or not? " + str(pc == pt))
    print("\n")

def print_region_population(regions_all, db):
    region_dic = {int(regions_all[i][0].split(';')[0]): regions_all[i][0].split(';')
                  for i in range(8, len(regions_all))}

    regions = db.getDataBySqlStr("select * from region")
    for region in regions:
        region_populaire_count = db.getDataBySqlStr(
            "select sum(commune.population_totale) from commune join department on (commune.code_departement = department.code_departement) where department.code_region = \"" + str(
                region[0]) + "\"")
        pc = region_populaire_count[0][0]
        pt = int(str(region_dic[region[0]][-1]).replace(" ", ""))
        print("In region " + region[1] +
              ": population count = " + str(pc) +
              ", population total = " + str(pt) +
              ", equal or not? " + str(pc == pt))

def print_communes_same_name(db):
    communes_same_name = db.getDataBySqlStr("Select distinct c1.* "
                                            "from commune as c1 join commune as c2 "
                                            "where c1.nom_commune=c2.nom_commune and c1.code_departement<>c2.code_departement "
                                            "order by c1.nom_commune")
    for c in communes_same_name:
        print("commune name: " + c[2] + ", No. department: " + c[0])


if __name__ == '__main__':
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

    db = Connection("db/database.db")
    db.init()
    db.importData(communes_all, departments_all, regions_all)

    # print_department_population(departments_all, db)
    # print_region_population(regions_all, db)
    # print_communes_same_name(db)

    db.exportToXML()
    db.importXML()
