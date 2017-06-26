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
from mtrading.indicator.XAverage import *


class TRIX(Indicator):

    # Set the default initialization. The first one is executed.
    def initialize(self):
        self.options = [12]
        self.displays = ["TRIX"]

    # It generates indicators that is used internally. The first one is executed.
    def declare_using(self):
        self.ind1 = XAverage(self, self.options[0], None, ("XAverage", "__TRIX_MA1"))
        self.ind2 = XAverage(self, self.options[0], "__TRIX_MA1", ("XAverage", "__TRIX_MA2"))
        self.ind3 = XAverage(self, self.options[0], "__TRIX_MA2", ("XAverage", "__TRIX_MA3"))

    # The computation is executed each time data is added or changed.
    def calculating(self):
        self.ind1.calculate()
        self.ind2.calculate()
        self.ind3.calculate()
        value1 = self.lines["__TRIX_MA3", self.options[0]]
        value0 = self.lines["__TRIX_MA3"]

        val = (value0 - value1) * 100.0 / value1

        self.lines["TRIX"] = val
