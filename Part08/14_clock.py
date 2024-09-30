# Write your solution here:
class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return(f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")

    def set(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0
clock = Clock(23, 59, 55)

print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()

clock.set(12, 5)
print(clock)
clock.tick()
print(clock)