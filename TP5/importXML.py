import ET as ET

def importXML(self):
    f = open('data.xml', 'r')
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
