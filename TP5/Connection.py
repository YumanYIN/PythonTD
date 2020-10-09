import sqlite3


class Connection:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    # Create the Database
    def init(self):
        self.cursor.execute("drop table if exists commune")
        self.cursor.execute("drop table if exists department")
        self.cursor.execute("drop table if exists region")
        self.cursor.execute("create table commune( code_departement INTEGER, code_commune INTEGER,nom_commune VARCHAR(100), population_totale INTEGER)")
        self.cursor.execute("create table department(code_departement INTEGER, nom_departement VARCHAR(100), code_region INTEGER )")
        self.cursor.execute("create table region(code_region INTEGER , nom_region VARCHAR(100))")
        self.conn.commit()

    # Close the connection
    def closeConnection(self):
        self.conn.close()

    # Import CSV Data into DB
    def importData(self, communes, departments, regions):
        for i in range(8, len(communes)-1):
            commune = communes[i][0].split(';')
            try:
                query = "insert into commune values('{}','{}','{}','{}')".format(
                    commune[2],
                    commune[5],
                    str(commune[6]).replace("'", ""),
                    int(str(commune[9]).replace(' ', ''))
                )
                self.cursor.execute(query)
            except:
                print("Failed: insert into table commune")
                print (commune[2], commune[5], str(commune[6]).replace("'", ""))

        for i in range(8, len(departments)):
            department = departments[i][0].split(';')
            try:
                query = "insert into department values('{}','{}','{}')" .format(
                    department[2],
                    str(department[3]).replace("'", ""),
                    department[0]
                )
                self.cursor.execute(query)
            except:
                print("Failed: insert into table department")

        for i in range(8, len(regions)):
            region = regions[i][0].split(';')
            try:
                query = "insert into region values('{}','{}')" .format(
                    region[0],
                    str(region[1]).replace("'", "")
                )
                self.cursor.execute(query)
            except:
                print("Failed: insert into table region")

