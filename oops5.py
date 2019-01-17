# Inheritance examples
# This is to demonstrate Single Inheritance
# Here Apple class is inherited by MacBook Class.

class Apple:
    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("To contact us, log on to {} .".format(self.contactWebsite))


class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2007

    def manufactureDetails(self):
        print("This MacBook was manufactured in the year {} by {} ".format(self.yearOfManufacture, self.manufacturer))


lap1 = MacBook()
lap1.manufactureDetails()
lap1.contactDetails()
