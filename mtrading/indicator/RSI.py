from mtrading.core import *
from mtrading.indicator.NAverage import *


class RSI(Indicator):

    # Set the default initialization. The first one is executed.
    def initialize(self):
        self.options = [12, 9]
        self.inputs = ["C"]
        self.displays = ["RSI", "RSI_MA"]

    # It generates indicators that is used internally. The first one is executed.
    def declare_using(self):
        self.ind1 = NAverage(self, self.options[1], "RSI")

    # The computation is executed each time data is added or changed.
    def calculating(self):
        length = self.options[0]
        up_sum = 0
        dn_sum = 0

        for index in range(length):
            old_value = self.lines[self.inputs[0], index+1]
            new_value = self.lines[self.inputs[0], index+0]
            amount = new_value - old_value
            if amount >= 0:
                up_sum += amount
            else:
                dn_sum += abs(amount)

        self.lines["RSI"] = up_sum / (up_sum + dn_sum) * 100.0

        self.ind1.calculate()
        self.lines["RSI_MA"] = self.ind1.lines["NAverage"]
