from Student import Student
from Date import Date
import datetime

# Test Class Student

stu1 = Student('Yuman', 'Yin', Date(1996, 8, 28))

print("Student is: ", stu1)

print("Email: ", stu1.email())

print("Age: ", stu1.age())
