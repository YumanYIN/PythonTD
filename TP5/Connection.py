import sqlite3
import xml.etree.ElementTree as ET


class Connection:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    # Create the Database
    def init(self):
        self.cursor.execute("drop table if exists commune")
        self.cursor.execute("drop table if exists department")
        self.cursor.execute("drop table if exists region")
        self.cursor.execute("create table commune( code_departement VARCHAR(16), code_commune INTEGER,nom_commune VARCHAR(100), population_totale INTEGER)")
        self.cursor.execute("create table department(code_departement VARCHAR(16), nom_departement VARCHAR(100), code_region INTEGER )")
        self.cursor.execute("create table region(code_region INTEGER , nom_region VARCHAR(100))")
        self.conn.commit()

    # Close the connection
    def closeConnection(self):
        self.conn.close()

    def getDataBySqlStr(self, sqlStr):
        return self.cursor.execute(sqlStr).fetchall()

    def exportToXML(self):
        outfile = open('files/data.xml', 'w')
        outfile.write('<?xml version="1.0" ?>\n')
        outfile.write('<data>\n')

        rows = self.getDataBySqlStr("select * from commune")
        outfile.write('\t<table name="commune">\n')
        for row in rows:
            outfile.write('\t\t<row>\n')
            outfile.write('\t\t\t<code_departement>%s</code_departement>\n' % row[0])
            outfile.write('\t\t\t<code_commune>%s</code_commune>\n' % row[1])
            outfile.write('\t\t\t<nom_commune>%s</nom_commune>\n' % row[2])
            outfile.write('\t\t\t<population_totale>%s</population_totale>\n' % row[3])
            outfile.write('\t\t</row>\n')
        outfile.write('\t</table>\n')

        rows = self.getDataBySqlStr("select * from department")
        outfile.write('\t<table name="department">\n')
        for row in rows:
            outfile.write('\t\t<row>\n')
            outfile.write('\t\t\t<code_departement>%s</code_departement>\n' % row[0])
            outfile.write('\t\t\t<nom_departement>%s</nom_departement>\n' % row[1])
            outfile.write('\t\t\t<code_region>%s</code_region>\n' % row[2])
            outfile.write('\t\t</row>\n')
        outfile.write('\t</table>\n')

        rows = self.getDataBySqlStr("select * from region")
        outfile.write('\t<table name="region">\n')
        for row in rows:
            outfile.write('\t\t<row>\n')
            outfile.write('\t\t\t<code_region>%s</code_region>\n' % row[0])
            outfile.write('\t\t\t<nom_region>%s</nom_region>\n' % row[1])
            outfile.write('\t\t</row>\n')
        outfile.write('\t</table>\n')
        outfile.write('</data>')
        outfile.close()

    def importXML(self):
        f = open('files/data.xml', 'r')
        data = f.read()
        xml = ET.fromstring(data)
        for table in xml.iter('table'):
            for row in table:
                data = []
                for child in row:
                    data.append(child.text)
                try:
                    if table.get('name') == 'commune':
                        query = "insert into commune value ('{}', '{}', '{}', '{}')".format(data[0],data[1],data[2],data[3])
                    if table.get('name') == 'department':
                        query = "insert into commune value ('{}', '{}', '{}')".format(data[0], data[1], data[2])
                    if table.get('name') == 'region':
                        query = "insert into commune value ('{}', '{}')".format(data[0], data[1])
                    self.cursor.excute(query)
                except:
                    pass

    # Import CSV Data into DB
    def importData(self, communes, departments, regions):

        try:
            commune_arr = [(communes[i][0].split(';')[2],
                            communes[i][0].split(';')[5],
                            str(communes[i][0].split(';')[6]).replace("'", ""),
                            str(communes[i][0].split(';')[9]).replace(" ", "")
                            ) for i in range(8, len(communes) - 1)]
            insert_commune = "insert into commune values (?, ?, ?, ?)"
            self.cursor.executemany(insert_commune, commune_arr)
            self.conn.commit()
        except :
            print("there is an error, when insert into communes")

        try:
            department_arr = [(departments[i][0].split(';')[2],
                               str(departments[i][0].split(';')[3]).replace("'", ""),
                               departments[i][0].split(';')[0])
                              for i in range(8, len(departments) - 1)]
            insert_department = "insert into department values (?, ?, ?)"
            self.cursor.executemany(insert_department, department_arr)
            self.conn.commit()
        except:
            print("there is an error, when insert into department")

        try:
            region_arr = [(regions[i][0].split(';')[0],
                           str(regions[i][0].split(';')[1]).replace(" ", ""))
                          for i in range(8, len(regions))]
            insert_region = "insert into region values (?, ?)"
            self.cursor.executemany(insert_region, region_arr)
            self.conn.commit()
        except:
            print("there is an error, when insert into region")



        """for i in range(8, len(communes)-1):
            commune = communes[i][0].split(';')
            try:
                query = "insert into commune values('{}','{}','{}','{}')".format(
                    commune[2],
                    commune[5],
                    str(commune[6]).replace("'", ""),
                    int(str(commune[9]).replace(' ', ''))
                )
                # queryStr = "insert into commune values (\"" + str(commune[2]) + "\", " + str(commune[5]) + ", \"" + str(commune[6]).replace("'", "") + "\", " + str(commune[9]).replace(' ', '') + ")"
                self.cursor.execute(query)
                self.conn.commit()
            except:
                print("Failed: insert into table commune")
                print (commune[2], commune[5], str(commune[6]).replace("'", ""))"""

        """for i in range(8, len(departments)):
            department = departments[i][0].split(';')
            try:
                query = "insert into department values('{}','{}','{}')" .format(
                    department[2],
                    str(department[3]).replace("'", ""),
                    department[0]
                )
                self.cursor.execute(query)
                self.conn.commit()
            except:
                print("Failed: insert into table department")"""

        """for i in range(8, len(regions)):
            region = regions[i][0].split(';')
            try:
                query = "insert into region values('{}','{}')" .format(
                    region[0],
                    str(region[1]).replace("'", "")
                )
                self.cursor.execute(query)
                self.conn.commit()
            except:
                print("Failed: insert into table region")"""

