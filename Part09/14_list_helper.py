class ListHelper:

    def __init__(self) -> None:
        pass

    @classmethod
    def greatest_frequency(self, mylist:list):
        return max(set(mylist), key=mylist.count)
    
    @classmethod
    def doubles(self, mylist:list):
        return len(list(set([x for x in mylist if mylist.count(x) > 1])))



numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))
