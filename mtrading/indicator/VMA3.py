# -*- Mode: Python; tab-width: 4 -*-
#       Author: Mukeun Kim<mukeunkim@gmail.com>

# ======================================================================
# Copyright 2016 by Mukeun Kim
#
#                         All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of Sam
# Rushing not be used in advertising or publicity pertaining to
# distribution of the software without specific, written prior
# permission.
#
# Mukeun Kim RUSHING DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN
# NO EVENT SHALL SAM RUSHING BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# ======================================================================

from mtrading.core import *
from mtrading.indicator.TrueRange import *
from mtrading.indicator.NAverage import *


class VMA3(Indicator):

    # Set the default initialization. The first one is executed.
    def initialize(self):
        self.options = [10, 20, 60]
        self.inputs = ["V"]
        self.displays = ["VMA1", "VMA2", "VMA3"]

    # It generates indicators that is used internally. The first one is executed.
    def declare_using(self):
        self.ind1 = NAverage(self, self.options[0], self.inputs[0])
        self.ind2 = NAverage(self, self.options[1], self.inputs[0])
        self.ind3 = NAverage(self, self.options[2], self.inputs[0])

    # The computation is executed each time data is added or changed.
    def calculating(self):
        self.ind1.calculate()
        self.ind2.calculate()
        self.ind3.calculate()
        self.lines["VMA1"] = self.ind1.lines["NAverage"]
        self.lines["VMA2"] = self.ind2.lines["NAverage"]
        self.lines["VMA3"] = self.ind3.lines["NAverage"]
