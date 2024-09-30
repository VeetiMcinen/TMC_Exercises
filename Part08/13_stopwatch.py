# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def __str__(self):
        if self.minutes <10 and self.seconds <10:
            return (f"0{self.minutes}:0{self.seconds}")
        elif self.minutes <10 and self.seconds >= 10:
            return (f"0{self.minutes}:{self.seconds}")
        elif self.minutes >= 10 and self.seconds <10:
            return (f"{self.minutes}:0{self.seconds}")
        else:
            return (f"{self.minutes}:{self.seconds}")

    def tick(self):
        if self.minutes == 59 and self.seconds == 59:
            self.minutes = 0
            self.seconds = 0
        
        else: self.seconds += 1
        
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        


watch = Stopwatch()
for i in range(3602):
    print(watch)
    watch.tick()