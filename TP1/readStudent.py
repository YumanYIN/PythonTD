from Student import Student
from Date import Date
import csv

# create a list for Student
stuList = []

# open csv file
with open('fichetu.csv', newline='') as csvfile:
    # read csv file, delimiter is ';'
    reader = csv.reader(csvfile, delimiter=';')
    # read each row
    for row in reader:
        # split date part by '/'
        date = row[2].split("/")
        # get date by order : Day, Month, Year
        date = Date(int(date[0]), int(date[1]), int(date[2]))
        # Create a Student class (Firstname, Lastname, Birthday),
        # append it to the list
        stuList.append(Student(row[1], row[0], row[2]))

print("Student List: ")
# print all students
for stu in stuList:
    print(stu)