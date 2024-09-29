# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.initial_value = initial_value
    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:
            self.value = self.value - 1
            return self.value
        else:
            return self.value
    def increase(self):
        self.value = self.value + 1
        return self.value
    
    def set_to_zero(self):
        self.value = 0
        return self.value

    def reset_original_value(self):
        self.value = self.initial_value

    # Write the rest of the methods here!
counter = DecreasingCounter(1)
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()
counter.reset_original_value()
counter.print_value()