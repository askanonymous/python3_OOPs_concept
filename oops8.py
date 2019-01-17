# Public => memberName
# Protected => _memberName
# Private => __memberName

class Car:
    numberOfWheels = 4
    _color = "Black"
    __yearOfManufacture = 2017

class Bmw(Car):
    def __init__(self):
	    print("Protected attribute color : {}".format(self._color))

car1 = Car()
print("Public attribute numberOfWheels : ", car1.numberOfWheels)

bmw1 = Bmw()
# The below commented code will not work
#print("Private attribute yearOfManufature :", bmw1.__yearOfManufacture)
# The below code will work
print("Private attribute yearOfManufature :", bmw1._Car__yearOfManufacture)
