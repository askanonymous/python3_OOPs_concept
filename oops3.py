#This is to demonstrate static methods and instance method:
#we are not sending self parameter as it is not being used in the welcomeMessage method. So we use keyword @staticmethod

class Employee():
    def employeeDetails(self):
	    self.name = "Abhishek Singh"

    @staticmethod
    def welcomeMessage():
        print("Welcome to our Organization")

    def welcomeMessage2(self):
        print("Welcome {} to our Organization !".format(self.name))

employee = Employee()
employee.employeeDetails()
employee.welcomeMessage()
employee.welcomeMessage2()
