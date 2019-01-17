# This is for demonstration of Polymorphism
#Super function usage to pass control to base class and use it

class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40

    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)

class Trainee(Employee):
    #Overriding base class method
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45

    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()

employee = Employee()
employee.setNumberOfWorkingHours()
print("Number of working hours of employee: ", end=" ")
employee.displayNumberOfWorkingHours()
trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours of trainee: ", end=" ")
trainee.displayNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print("Number of working hours of trainee: ", end=" ")
trainee.displayNumberOfWorkingHours()
