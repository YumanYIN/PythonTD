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

date = Date(2020,9,3)
print(date)


