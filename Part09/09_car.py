class Car:
    def __init__(self) -> None:
        self.__petrol = 0
        self.__odometer = 0

    def fill_up(self):
        self.__petrol = 60
    
    def drive(self,km:int):
        if km >= self.__petrol:
            self.__odometer += self.__petrol
            self.__petrol = 0
        else: 
            self.__petrol -= km
            self.__odometer += km
    
    def __str__(self) -> str:
        return (f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres")
    
car = Car()
print(car)
car.fill_up()
print(car)
car.drive(20)
print(car)
car.drive(50)
print(car)
car.drive(10)
print(car)
car.fill_up()
car.fill_up()
print(car)