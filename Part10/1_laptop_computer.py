# Write your solution here:
class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed

class Laptop(Computer):
    def __init__(self, model:str, speed: int, weight:int) -> None:
        super().__init__(model=model, speed=speed)
        self.weight = weight

    def __str__(self):
        return (f"{self.model}, {self.speed}, {self.weight}")

laptop = Laptop("aaa", 200, 200)

print(laptop)