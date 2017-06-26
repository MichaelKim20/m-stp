from mtrading.core import *


class VR(Indicator):

    # Set the default initialization. The first one is executed.
    def initialize(self):
        self.options = [12]
        self.displays = ["VR"]

    # It generates indicators that is used internally. The first one is executed.
    def calculating(self):
        length = self.options[0]
        plus_sum = 0.0
        minus_sum = 0.0
        equal_sum = 0.0
        for index in range(length):
            volume = self.lines["V", index]
            if self.lines["C", index] > self.lines["C", index+1]:
                plus_sum += volume
            if self.lines["C", index] < self.lines["C", index+1]:
                minus_sum += volume
            else:
                equal_sum += volume
    
        value = (plus_sum + 0.5 * equal_sum) * 100.0 / (minus_sum + 0.5 * equal_sum)
        self.lines["VR"] = value
