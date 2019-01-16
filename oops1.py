# Implementing classes and objects in python.

class Employee:
    def __init__(self, name, designation, target):
        self.name = name
        self.designation = designation
        self.target = target

    def employee_details(self):
        print("Employee name is : {} ".format(self.name))
        print("Employee designation is : {} ".format(self.designation))

    def hasAchievedTarget(self):
        if self.target >= 5:
            print("The employee : {} has achieved his target and has made additional {} targets !".format(self.name,(self.target - 5)))
        else:
            print("The employee : {} has not achieved his target and lags behind by {} !".format(self.name,(5 - self.target)))


emp1 = Employee("Abhishek Singh", "Technology Analyst",10)
emp1.employee_details()
emp1.hasAchievedTarget()
