
def smallest_average(p1: dict, p2: dict, p3: dict):
    scores = [person1,person2,person3]
    a = []
    
    for person in scores:
        score = 0
        for stat in person.values():
            if type(stat) == int:
                score += stat
            average = score/3
        a.append(average)
 
    return scores[a.index(min(a))]

person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3":3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3":8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3":1}

print(smallest_average(person1, person2, person3))

