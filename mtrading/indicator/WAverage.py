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


class WAverage(Indicator):

    # Set the default initialization. The first one is executed.
    def initialize(self):
        self.options = [10]
        self.inputs = ["C"]
        self.displays = ["WAverage"]

    # It generates indicators that is used internally. The first one is executed.
    def declare_using(self):
        pass

    # The computation is executed each time data is added or changed.
    def calculating(self):
        length = self.options[0]
        linename = self.inputs[0]
        sum_value = 0
        csum_value = 0
        for index in range(length):
            factor = length - index
            sum_value += self.lines[linename, index] * factor
            csum_value += factor
        self.lines["WAverage"] = sum_value / csum_value
