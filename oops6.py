# This is an example of multiple inheritance

class OperatingSystem:
    multitasking = True
    name = "OS"


class Apple:
    website = "www.apple.com"
    name = "Apple"


class MacBook(OperatingSystem,Apple):
    def __init__(self):
        if self.multitasking is True:
            print("This is a multi-tasking system.Visit {} for more details.".format(self.website))
        print(self.name)


mac1 = MacBook()
