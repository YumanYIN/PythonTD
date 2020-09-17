# define class Date
class Date:
    """

    """

    def __init__(self, y=2020, m=1, d=1):
        if y > 0 and m >= 1 and d >= 1:
            self.Year = y
            self.Month = m
            self.Day = d
        else:
            self.Year = 2020
            self.Month = 1
            self.Day = 1

    def __str__(self):
        """

        :return:
        """
        month = self.Month
        if month < 10:
            month = '0' + str(month)

        day = self.Day
        if day < 10:
            day = '0' + str(day)

        return str(self.Year) + "-" + str(month) + "-" + str(day)

    def __eq__(self, other):
        """
        override equal fonction
        :param other:
        :return: if self == other , reture True. If not, return False
        """
        # Determine the class of other
        if not other.__class__ is Date:
            print('Could not compare Date with the other class')
            return NotImplemented
        if isinstance(other, Date):
            return self.Year == other.Year and self.Month == other.Month and self.Day == other.Day

    def __lt__(self, other):
        """
        override less than fonction
        :param other:
        :return:
        """
        # Determine the class of other
        if not other.__class__ is Date:
            print('Could not compare Date with the other class')
            return NotImplemented

        if isinstance(other, Date):
            return self.Year < other.Year or \
                (self.Year == other.Year and self.Month < other.Month) or \
                (self.Year == other.Year and self.Month == other.Month and self.Day < other.Day)



# Test class Date()
date = Date(2020, 9, 3)

print(date)

# Test __eq__
a = Date(2020, 9, 17)
b = Date(2020, 9, 18)
c = 2020
print("test __eq__ :")
print(a == b)
print(a == c)

# Test __lt__
print("test __lt__ :")
print(a < b)

