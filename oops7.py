# This is an example of multi-level inheritance

class MusicalInstruments:
    numberOfMajorKeys = 12

class StringInstruments(MusicalInstruments):
    typeOfWood = "Tonewood"
    name = "Apple"


class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings=6
        print("This guitar consists of {} strings. It is made of {} and can play {} keys.".format(self.numberOfStrings,self.typeOfWood,self.numberOfMajorKeys))

guitar1 = Guitar()
