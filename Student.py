from Date import Date
import datetime


class Student:
    """

    """

    def __init__(self, firstname, lastname, date):
        self.Firstname = firstname
        self.Lastname = lastname

        if isinstance(date, Date):
            self.Birthday = date
        else:
            self.Birthday = Date()

    def __str__(self):
        return "Nom: " + str(self.Lastname) + "\t" \
               + "Prenom: " + str(self.Firstname) + "\t" \
               + "Date de naissance: " + str(self.Birthday) + "\n"

    def email(self):
        return str(self.Firstname).lower() + "." \
               + str(self.Lastname).lower() \
               + "@etu.univ-tours.fr"

    def age(self):
        """

        :return:
        """
        now = datetime.datetime.now()

        if now.year < self.Birthday.Year \
                or (now.year == self.Birthday.Year and now.month < self.Birthday.Month) \
                or (now.year == self.Birthday.Year and now.month == self.Birthday.Month and now.day < self.Birthday.Day):
            return "The student’s birthday was entered incorrectly !"

        if now.month > self.Birthday.Month \
                or (now.month == self.Birthday.Month and now.day >= self.Birthday.Day):
            return now.year - self.Birthday.Year
        else:
            return now.year - self.Birthday.Year - 1


