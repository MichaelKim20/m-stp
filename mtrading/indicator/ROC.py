from mtrading.core import *


class ROC(Indicator):

    # Set the default initialization. The first one is executed.
    def initialize(self):
        self.options = [12]
        self.inputs = ["C"]
        self.displays = ["ROC"]

    # It generates indicators that is used internally. The first one is executed.
    def declare_using(self):
        pass

    # The computation is executed each time data is added or changed.
    def calculating(self):
        length = self.options[0]
    
        value1 = self.lines[self.inputs[0], length]
        value0 = self.lines[self.inputs[0]]      

        self.lines["ROC"] = (value0 - value1) * 100.0 / value1
