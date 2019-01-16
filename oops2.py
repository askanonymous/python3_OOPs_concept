#Example of Class attributes and instance attributes
#Here numberOfworkingHoursPerDay is class attribute and others are instance attributes

class Employee():
    numberOfworkingHoursPerDay = float(9.25)
    def __init__(self,name,days,avghours):
        self.name = name
        self.days = days
        self.avghours = avghours

    def hoursWorked(self):
        print("Total Number of workings hours = {} ".format(self.days * self.avghours))
        if (self.avghours >= self.numberOfworkingHoursPerDay):
            print("The employee : {} has worked for extra {} hours".format(self.name, ((self.avghours * self.days) - (self.numberOfworkingHoursPerDay * self.days))))
        else:
            print("The employee : {} has worked less for {} hours".format(self.name, ((self.avghours * self.days) - (self.numberOfworkingHoursPerDay * self.days))))

emp1 = Employee("Abhishek Singh",10,9.25)
emp1.hoursWorked()
