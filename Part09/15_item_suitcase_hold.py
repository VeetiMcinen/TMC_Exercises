class Item:
    def __init__(self, name:str, weight:int) -> None:
        self.__name = name
        self.__weight = weight

    @classmethod
    def name(self):
        return self.__name

    
    @classmethod
    def weight(self):
        return self.__weight


    @property
    def weight(self):
        return self.__weight

    def __str__(self) -> str:
        return (f"{self.__name} ({self.__weight} kg)")


book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)

print("Name of the book:", book.name)
print("Weight of the book:", book.weight)



print("Book:", book)
print("Phone:", phone)