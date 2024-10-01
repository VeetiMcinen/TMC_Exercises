# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return (f"{self.name} ({self.height} cm)")


class Room:
    def __init__(self) -> None:
        self.personlist = []
    
    def add(self,person:Person):
        self.personlist.append(person)
    
    def is_empty(self):
        if len(self.personlist) == 0:
            return True
        return False

    def print_contents(self):
        combined_height = 0
        for i in self.personlist:
            combined_height += i.height

        print(f"There are {len(self.personlist)} persons in the room, and their combined height is {combined_height} cm")
        for person in self.personlist:
            print(person)

    def shortest(self):
        if len(self.personlist) == 0:
            return None
        
        shortest_person = self.personlist[0]
        for person in self.personlist:
            if person.height < shortest_person.height:
                shortest_person = person
        return shortest_person

    def remove_shortest(self):
        if len(self.personlist) == 0:
            return None
        shortest_person = self.personlist[0]
        for person in self.personlist:
            if person.height < shortest_person.height:
                shortest_person = person
        self.personlist.remove(shortest_person)
        return shortest_person
room = Room()

room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Nina", 162))
room.add(Person("Ally", 166))
room.print_contents()

print()

removed = room.remove_shortest()
print(f"Removed from room: {removed.name}")

print()

room.print_contents()