from Date import Date

# Test class Date()
date = Date(2020, 9, 3)

print(date)

# Test __eq__
a = Date(2020, 9, 17)
b = Date(2020, 9, 18)
c = 2020
print("test '__eq__' : a == b")
print(a == b)
print("test '__eq__' : a == c")
print(a == c)

# Test __lt__
print("test '__lt__' : a < b")
print(a < b)