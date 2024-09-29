# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.numberlist = []
    
    def add_number(self, number:int):
        self.numberlist.append(number)

    def count_numbers(self):
        return len(self.numberlist)
    
    def get_sum(self):
        return sum(self.numberlist)
    
    def evensum(self):
        evens = [i for i in self.numberlist if i%2 == 0]
        return sum(evens)
    
    def oddsum(self):
        odds = [i for i in self.numberlist if i%2 != 0]
        return sum(odds)

    def average(self):
        avg = 0
        if len(self.numberlist) > 0:
            avg = sum(self.numberlist)/len(self.numberlist) 
        return avg


def main(numbers:NumberStats):
    while True:
        number = int(input("Please type in integer numbers: "))
        if number >= 0:
            numbers.add_number(number)
        else:
            print(f"Sum of numbers: {numbers.get_sum()}")
            print(f"Mean of numbers: {numbers.average()}")
            print(f"Sum of even numbers: {numbers.evensum()}")
            print(f"Sum of odd numbers: {numbers.oddsum()}")
            break

number = NumberStats()
main(number)

#meow