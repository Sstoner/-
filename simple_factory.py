class car: #Product interface
    def drive(self):
        pass

class BMW(car): #Product A
    def __init__(self,carname):
        self.__name = carname
    def drive(self):
        print("Drive the BMW as" + self.__name)

class Benz(car): #Product B
    def __init__(self,carname):
        self.__name = carname
    def drive(self):
        print("Drive the Benz as "+ self.__name)

class driver:   #Factory
    def driverCar(self,name):
        if name == "BMW":
            return BMW(name)
        elif name == "Benz":
            return Benz(name)
        else:
            raise MyInputException(name)


class MyInputException(Exception):
    def __init__(self,name):
        Exception.__init__(self)
        self.name = name

if __name__ == "__main__":
    print("Please input \'BMW\' or \'Benz\' :")
    carname = input()
    dier = driver()
    try:
        d = dier.driverCar(carname)
    except MyInputException:
        print("input worry name" + e.name)
    else:
        d.drive()

