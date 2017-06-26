from mtrading.order import *
import datetime
import math
NAN = -1.0E18

SIGNAL_NONE = 0
SIGNAL_LONG_ENTER = 1
SIGNAL_LONG_EXIT = 2
SIGNAL_SHORT_ENTER = 3
SIGNAL_SHORT_EXIT = 4


class LineValue :
    def __init__(self, avalue=None):
        self.__value = 0

        if avalue is not None:
            if isinstance(avalue, LineValue):
                self.__value = avalue.get_value()
            elif isinstance(avalue, (int, float)):
                self.__value = float(avalue)

    def get_value(self):
        return self.__value

    def get_valid(self):
        if self.__value != NAN:
            return True
        else:
            return False

    @classmethod
    def is_nan(cls, *args):
        if isinstance(args, tuple):
            for i in range(len(args)):
                if isinstance(args[i], LineValue):
                    if args[i].get_value() == NAN:
                        return True
                elif isinstance(args[i], (int, float)):
                    if args[i] == NAN:
                        return True
                else:
                    return True
            return False
        elif isinstance(args, (int, float)):
            return args == NAN
        else:
            return True

    def __str__(self):
        if self.__value != NAN:
            return "(L)%.2f" % self.__value
        else:
            return "NAN"

    def __add__(self, other):
        if LineValue.is_nan(self.__value, other):
            return LineValue(NAN)
        if isinstance(other, LineValue):
            return LineValue(self.__value + other.get_value())
        elif isinstance(other, (int, float)):
            return LineValue(self.__value + other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if LineValue.is_nan(self.__value, other):
            return LineValue(NAN)
        if isinstance(other, LineValue):
            return LineValue(self.__value - other.get_value())
        elif isinstance(other, (int, float)):
            return LineValue(self.__value - other)
        else:
            return NotImplemented

    def __mul__(self, other):
        if LineValue.is_nan(self.__value, other):
            return LineValue(NAN)
        if isinstance(other, LineValue):
            return LineValue(self.__value * other.get_value())
        elif isinstance(other, (int, float)):
            return LineValue(self.__value * other)
        else:
            return NotImplemented

    def __div__(self, other):
        if LineValue.is_nan(self.__value, other):
            return LineValue(NAN)
        if isinstance(other, LineValue):
            if other.get_value() != 0:
                return LineValue(self.__value / other.get_value())
            else:
                return LineValue(0)
        elif isinstance(other, (int, float)):
            if other != 0:
                return LineValue(self.__value / float(other))
            else:
                return LineValue(0)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if LineValue.is_nan(self.__value, other):
            return LineValue(NAN)
        if isinstance(other, LineValue):
            if other.get_value() != 0:
                return LineValue(self.__value / other.get_value())
            else:
                return LineValue(0)
        elif isinstance(other, (int, float)):
            if other != 0:
                return LineValue(self.__value / float(other))
            else:
                return LineValue(0)
        else:
            return NotImplemented

    def __radd__(self, other):
        if LineValue.is_nan(self.__value, other):
            return LineValue(NAN)
        if isinstance(other, LineValue):
            return LineValue(other.get_value() + self.__value)
        elif isinstance(other, (int, float)):
            return LineValue(other + self.__value)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if LineValue.is_nan(self.__value, other):
            return LineValue(NAN)
        if isinstance(other, LineValue):
            return LineValue(other.get_value() - self.__value)
        elif isinstance(other, (int, float)):
            return LineValue(other - self.__value)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if LineValue.is_nan(self.__value, other):
            return LineValue(NAN)
        if isinstance(other, LineValue):
            return LineValue(other.get_value() * self.__value)
        elif isinstance(other, (int, float)):
            return LineValue(float(other) * self.__value)
        else:
            return NotImplemented

    def __rdiv__(self, other):
        if LineValue.is_nan(self.__value, other):
            return LineValue(NAN)
        if isinstance(other, LineValue):
            if self.__value != 0:
                return LineValue(other.get_value() / self.__value)
            else:
                return LineValue(0)
        elif isinstance(other, (int, float)):
            if self.__value != 0:
                return LineValue(float(other) / self.__value)
            else:
                return LineValue(0)
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        if LineValue.is_nan(self.__value, other):
            return LineValue(NAN)
        if isinstance(other, LineValue):
            if self.__value != 0:
                return LineValue(other.get_value() / self.__value)
            else:
                return LineValue(0)
        elif isinstance(other, (int, float)):
            if self.__value != 0:
                return LineValue(float(other) / self.__value)
            else:
                return LineValue(0)
        else:
            return NotImplemented

    def __lt__(self, other):
        if LineValue.is_nan(self.__value, other):
            return False
        if isinstance(other, LineValue):
            return self.__value < other.get_value()
        elif isinstance(other, (int, float)):
            return self.__value < other
        else:
            return NotImplemented

    def __le__(self, other):
        if LineValue.is_nan(self.__value, other):
            return False
        if isinstance(other, LineValue):
            return self.__value <= other.get_value()
        elif isinstance(other, (int, float)):
            return self.__value <= other
        else:
            return NotImplemented

    def __eq__(self, other):
        if LineValue.is_nan(self.__value, other):
            return False
        if isinstance(other, LineValue):
            return self.__value == other.get_value()
        elif isinstance(other, (int, float)):
            return self.__value == other
        else:
            return NotImplemented

    def __ne__(self, other):
        if LineValue.is_nan(self.__value, other):
            return True
        if isinstance(other, LineValue):
            return self.__value != other.get_value()
        elif isinstance(other, (int, float)):
            return self.__value != other
        else:
            return NotImplemented

    def __gt__(self, other):
        if LineValue.is_nan(self.__value, other):
            return False
        if isinstance(other, LineValue):
            return self.__value > other.get_value()
        elif isinstance(other, (int, float)):
            return self.__value > other
        else:
            return NotImplemented

    def __ge__(self, other):
        if LineValue.is_nan(self.__value, other):
            return False
        if isinstance(other, LineValue):
            return self.__value >= other.get_value()
        elif isinstance(other, (int, float)):
            return self.__value >= other
        else:
            return NotImplemented

    def __iadd__(self, other):
        if LineValue.is_nan(self.__value, other):
            self.__value = NAN
            return self

        if isinstance(other, LineValue):
            self.__value += other.get_value()
            return self
        elif isinstance(other, (int, float)):
            self.__value += other
            return self
        else:
            return NotImplemented

    def __isub__(self, other):
        if LineValue.is_nan(self.__value, other):
            self.__value = NAN
            return self

        if isinstance(other, LineValue):
            self.__value -= other.get_value()
            return self
        elif isinstance(other, (int, float)):
            self.__value -= other
            return self
        else:
            return NotImplemented

    def __imul__(self, other):
        if LineValue.is_nan(self.__value, other):
            self.__value = NAN
            return self

        if isinstance(other, LineValue):
            self.__value *= other.get_value()
            return self
        elif isinstance(other, (int, float)):
            self.__value *=  float(other)
            return self
        else:
            return NotImplemented

    def __idiv__(self, other):
        if LineValue.is_nan(self.__value, other):
            self.__value = NAN
            return self

        if isinstance(other, LineValue):
            if other.get_value() != 0:
                self.__value /= other.get_value()
            else:
                self.__value = 0
            return self
        elif isinstance(other, (int, float)):
            if other != 0:
                self.__value /= float(other)
            else:
                self.__value = 0
            return self
        else:
            return NotImplemented

    def __itruediv__(self, other):
        if LineValue.is_nan(self.__value, other):
            self.__value = NAN
            return self

        if isinstance(other, LineValue):
            if other.get_value() != 0:
                self.__value /= other.get_value()
            else:
                self.__value = 0
            return self
        elif isinstance(other, (int, float)):
            if other != 0:
                self.__value /= float(other)
            else:
                self.__value = 0
            return self
        else:
            return NotImplemented

    def __pow__(a, b):
        return LineValue(a.get_value() ** b)

    def __neg__(self):
        return LineValue(-self.__value)

    def __pos__(self):
        if LineValue.is_nan(self.__value):
            return LineValue(NAN)
        return LineValue(self.__value)

    def __abs__(self):
        if LineValue.is_nan(self.__value):
            return LineValue(NAN)
        return LineValue(abs(self.__value))

    def __call__(self, item=None):
        return self.__value


# region LineMath
pi = math.pi
e = math.e


def ceil(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.ceil(lx))


def copysign(x, y):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if isinstance(y, LineValue): ly = y.get_value()
    else: ly = y

    if lx == NAN: return LineValue(NAN)
    if ly == NAN: return LineValue(NAN)

    return LineValue(math.copysign(lx, ly))


def fabs(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.fabs(lx))


def floor(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.floor(lx))


def frexp(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.frexp(lx))


def fsum(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.fsum(lx))


def isfinite(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.isfinite(lx))


def isinf(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.isinf(lx))


def isnan(x):
    if isinstance(x, LineValue):
        lx = x.get_value()
    else:
        lx = x
    if lx == NAN:
        return LineValue(NAN)
    return LineValue(math.isnan(lx))


def ldexp(x, y):
    if isinstance(x, LineValue):
        lx = x.get_value()
    else: lx = x
    if isinstance(y, LineValue):
        ly = y.get_value()
    else: ly = y

    if lx == NAN:
        return LineValue(NAN)
    if ly == NAN:
        return LineValue(NAN)

    return LineValue(math.ldexp(lx, ly))


def modf(x):
    if isinstance(x, LineValue):
        lx = x.get_value()
    else:
        lx = x
    if lx == NAN:
        return LineValue(NAN)
    return LineValue(math.modf(lx))


def trunc(x):
    if isinstance(x, LineValue):
        lx = x.get_value()
    else:
        lx = x
    if lx == NAN:
        return LineValue(NAN)
    return LineValue(math.trunc(lx))


def exp(x):
    if isinstance(x, LineValue):
        lx = x.get_value()
    else:
        lx = x
    if lx == NAN:
        return LineValue(NAN)
    return LineValue(math.exp(lx))


def expm1(x):
    if isinstance(x, LineValue):
        lx = x.get_value()
    else:
        lx = x
    if lx == NAN:
        return LineValue(NAN)
    return LineValue(math.expm1(lx))


def log(x, base=None):
    if isinstance(x, LineValue):
        lx = x.get_value()
    else:
        lx = x
    if lx == NAN:
        return LineValue(NAN)

    if base is None:
        return LineValue(math.log(lx))
    else:
        return LineValue(math.log(lx, base))


def log1p(x):
    if isinstance(x, LineValue):
        lx = x.get_value()
    else:
        lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.log1p(lx))

def log2(x):
    if isinstance(x, LineValue):
        lx = x.get_value()
    else:
        lx = x

    if lx == NAN:
        return LineValue(NAN)
    return LineValue(math.log2(lx))


def log10(x):
    if isinstance(x, LineValue):
        lx = x.get_value()
    else:
        lx = x
    if lx == NAN:
        return LineValue(NAN)
    return LineValue(math.log10(lx))


def pow(x, y):
    if isinstance(x, LineValue):
        lx = x.get_value()
    else:
        lx = x

    if isinstance(y, LineValue):
        ly = y.get_value()
    else:
        ly = y

    if lx == NAN:
        return LineValue(NAN)
    if ly == NAN:
        return LineValue(NAN)

    return LineValue(math.pow(lx, ly))


def sqrt(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.sqrt(lx))


def acos(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.acos(lx))


def asin(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.asin(lx))


def atan(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.atan(lx))


def atan2(y, x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if isinstance(y, LineValue): ly = y.get_value()
    else: ly = y

    if lx == NAN: return LineValue(NAN)
    if ly == NAN: return LineValue(NAN)

    return LineValue(math.atan2(lx, ly))


def cos(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.cos(lx))


def hypot(x, y):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if isinstance(y, LineValue): ly = y.get_value()
    else: ly = y

    if lx == NAN: return LineValue(NAN)
    if ly == NAN: return LineValue(NAN)

    return LineValue(math.hypot(lx, ly))


def sin(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.sin(lx))


def tan(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.tan(lx))


def degrees(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.degrees(lx))


def radians(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.radians(lx))


def acosh(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.acosh(lx))


def asinh(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.asinh(lx))


def atanh(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.atanh(lx))


def cosh(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.cosh(lx))


def sinh(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.sinh(lx))


def tanh(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.tanh(lx))


def erf(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.erf(lx))


def erfc(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.erfc(lx))


def gamma(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.gamma(lx))


def lgamma(x):
    if isinstance(x, LineValue): lx = x.get_value()
    else: lx = x
    if lx == NAN: return LineValue(NAN)
    return LineValue(math.lgamma(lx))
# endregion


class Line:
    def __init__(self):
        self.vector = []

    def __del__(self):
        self.vector.clear()
        del self.vector

    def __getitem__(self, key):
        if (key >= 0) and (key < len(self.vector)):
            return self.vector[key]
        else:
            return LineValue(NAN)
        
    def __setitem__(self, key, item):
        if key >= 0:
            if key < len(self.vector):
                if isinstance(item, LineValue):
                    self.vector[key] = LineValue(item.get_value())
                elif isinstance(item, (int, float)):
                    self.vector[key] = LineValue(item)
            else:
                while key >= len(self.vector):
                    self.vector.append(LineValue(0))

                if isinstance(item, LineValue):
                    self.vector[key] = LineValue(item.get_value())
                elif isinstance(item, (int, float)):
                    self.vector[key] = LineValue(item)

    def __len__(self):
        return len(self.vector)

    def clear(self):
        self.vector.clear()


class LineSeries:
    def __init__(self, owner):
        self.owner = owner
        self.lines = {}
        self.position = 0

    def __del__(self):
        self.owner = None
        del self.lines

    def __getitem__(self, name):
        linename = ""
        offset = 0

        if isinstance(name, tuple):
            if isinstance(name[0], str):
                if isinstance(name[1], int):
                    linename = name[0]
                    offset = name[1]
                else:
                    linename = name[0]
                    offset = 0
            else:
                linename = name

        elif isinstance(name, str):
            linename = name
            offset = 0

        if self.owner is not None:
            line = self.owner.get_line(linename, True)
        else:
            if not (linename in self.lines):
                self.lines[linename] = Line()
            line = self.lines[linename]

        if offset < 0:
            offset = 0
        abs_position = self.position - offset
        return line[abs_position]

    def __setitem__(self, name, item):
        linename = ""
        offset = 0

        if isinstance(name, tuple):
            if isinstance(name[0], str):
                if isinstance(name[1], int):
                    linename = name[0]
                    offset = name[1]
                else:
                    linename = name[0]
                    offset = 0
            else:
                linename = name

        elif isinstance(name, str):
            linename = name
            offset = 0

        if self.owner is not None:
            line = self.owner.get_line(linename, False)
        else:
            if not (linename in self.lines):
                self.lines[linename] = Line()
            line = self.lines[linename]

        if offset < 0: offset = 0
        abs_position = self.position - offset
        self.lines[linename][abs_position] = item

    def __contains__(self, name):
        if name in self.lines:
            return True
        else:
            return False

    def get_line (self, name):
        if name in self.lines:
            return self.lines[name]
        else:
            self.lines[name] = Line()
            return self.lines[name]

    def clear_value(self):
        for i in self.lines:
            self.lines[i].clear()

    def clear(self):
        self.lines.clear()


class NumberContainer:
    def __init__(self):
        self.vector = []

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, index):
        if (index >= 0) and (index < len(self.vector)):
            return self.vector[index]
        else:
            return 10
        
    def __setitem__(self, index, item):
        if index >= 0:
            if index < len(self.vector):
                self.vector[index] = item
            else:
                while index >= len(self.vector):
                    self.vector.append(10)
                self.vector[index] = item

    def __delete__(self, instance):
        del self.vector

    def clear(self):
        self.vector.clear()


class StringContaner:
    def __init__(self):
        self.vector = []

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, index):
        if (index >= 0) and (index < len(self.vector)):
            return self.vector[index]
        else:
            return "C"

    def __setitem__(self, index, item):
        if index >= 0:
            if index < len(self.vector):
                self.vector[index] = item
            else:
                while index >= len(self.vector):
                    self.vector.append("C")
                self.vector[index] = item

    def clear(self):
        self.vector.clear()


class TupleContaner:
    def __init__(self):
        self.vector = []

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, index):
        if (index >= 0) and (index < len(self.vector)):
            return self.vector[index]
        else:
            return ("","")

    def __setitem__(self, index, item):
        if isinstance(item, (list, tuple)):
            if len(item) >= 2:
                if index >= 0:
                    if index < len(self.vector):
                        self.vector[index] = (item[0], item[1])
                    else:
                        while index >= len(self.vector):
                            self.vector.append(("",""))
                        self.vector[index] = (item[0], item[1])

    def clear(self):
        self.vector.clear()


class MTSObject:

    def __init__(self, a_parent=None, a_options=None, a_inputs=None, a_outputs=None):
        self.__done_declar_using = False
        self.name = ""

        module_path = str(type(self)).replace("<", "").replace(">", "").replace("class", "").replace(" ", "").replace("'", "").split(".")
        self.name = module_path[len(module_path)-1]

        self.lines = LineSeries(self)

        self.__options = NumberContainer()
        self.__inputs = StringContaner()
        self.__outputs = TupleContaner()

        self.parent = a_parent
        self.position = -1
        self.__old_position = -1
        self.__is_calculating = False

        self.initialize()

        if a_options is not None:
            if isinstance(a_options, list):
                self.options = a_options
            elif isinstance(a_options, (int, float)):
                self.options[0] = a_options

        if a_inputs is not None:
            if isinstance(a_inputs, list):
                self.inputs = a_inputs
            elif isinstance(a_inputs, str):
                self.inputs[0] = a_inputs

        if a_outputs is not None:
            if isinstance(a_outputs, list):
                self.outputs = a_outputs
            elif isinstance(a_outputs, tuple):
                self.outputs[0] = a_outputs

    def __del__(self):
        del self.lines
        del self.__options
        del self.__inputs
        del self.__outputs

    def initialize(self):
        pass

    def declare_using(self):
        pass

    def clear(self):
        self.__done_declar_using = False
        self.__old_position = -1
        self.position = -1
        self.lines.clear()

    def set_one_data(self, a_position, a_date, a_open, a_high, a_low, a_close, a_volume, a_note=None):
        date = None
        if len(a_date) >= 14:
            date = datetime.datetime.strptime(a_date, "%Y%m%d%H%M%S")
        elif len(a_date) >= 12:
            date = datetime.datetime.strptime(a_date, "%Y%m%d%H%M")
        elif len(a_date) >= 8:
            date = datetime.datetime.strptime(a_date, "%Y%m%d")

        self.lines.get_line("D")[a_position] = date
        self.lines.get_line("O")[a_position] = a_open
        self.lines.get_line("H")[a_position] = a_high
        self.lines.get_line("L")[a_position] = a_low
        self.lines.get_line("C")[a_position] = a_close
        self.lines.get_line("V")[a_position] = a_volume

    def set_all_data(self, a_data):
        if not isinstance(a_data, list):
            return
        self.clear()
        pos = 0
        for i in range(len(a_data)):
            record = a_data[i]
            enable = True
            if isinstance(record, dict):
                if "D" in record:
                    d_val = record["D"]
                else:
                    d_val = ""
                    enable = False

                if "O" in record:
                    o_val = record["O"]
                else:
                    o_val = 0
                    enable = False

                if "H" in record:
                    h_val = record["H"]
                else:
                    h_val = 0
                    enable = False

                if "L" in record:
                    l_val = record["L"]
                else:
                    l_val = 0
                    enable = False

                if "C" in record:
                    c_val = record["C"]
                else:
                    c_val = 0
                    enable = False

                if "V" in record:
                    v_val = record["V"]
                else:
                    v_val = 0
                    enable = False

                if enable:
                    try:
                        self.set_one_data(pos, d_val, o_val, h_val, l_val, c_val, v_val)
                        pos += 1
                    finally:
                        pass

    def set_all_data_csv(self, a_data):
        self.clear()
        pos = 0
        a_data = a_data.replace("\r", "|")
        a_data = a_data.replace("\n", "|")
        data = a_data.split("|")

        for i in range(len(data)):
            record = data[i].split(",")
            if len(record) >= 6:
                try:
                    self.set_one_data(pos, record[0], float(record[1]), float(record[2]), float(record[3]), float(record[4]), float(record[5]), 'ALL')
                    pos += 1
                finally:
                    pass

    def calculate_all_data(self):
        self.__old_position = -1
        self.position = -1
        self.calculate(self.get_max_count()-1)

    def calculate(self, a_position=-1):
        if a_position < 0:
            if self.parent is not None:
                a_position = self.parent.position
            else:
                return

        a_position = self.adjust_position(a_position)

        if not self.__done_declar_using:
            self.declare_using()
            self.__done_declar_using = True

        if self.__old_position >= a_position:
            self.__old_position = a_position - 1

        for index in range(self.__old_position+1, a_position+1):
            self.position = index
            self.lines.position = index

            self.__is_calculating = True

            try:
                self.prepare()
                self.calculating()  
                if self.parent is not None:
                    for i in range(len(self.__outputs)):
                        self.parent.set_value(self.__outputs[i][1], self.get_value(self.__outputs[i][0], 0, False), 0, False)

            except ZeroDivisionError:
                for key in self.lines.lines:
                    line = self.get_line(key)
                    while len(line) <= self.position:
                        privious_value = line[len(line)-1]
                        line[len(line)] = privious_value

            finally:
                self.__is_calculating = False

            self.__old_position = self.position

    def adjust_position(self, a_position):
        return a_position

    def prepare(self):
        pass

    def recalculate(self):
        self.__old_position = -1
        self.calculate(self.position)
    
    def calculating(self):
        pass

    # region Value
    def set_value(self, a_linename, a_value, a_position=None, a_use_parent=False):
        if not self.__is_calculating:
            return
        if a_position is None:
            a_position = 0
        abs_pos = self.position - a_position
        self.get_line(a_linename, a_use_parent)[abs_pos] = a_value

    def get_value(self, a_linename, a_position=None, a_use_parent=True):
        if not self.__is_calculating:
            return 0
        if a_position is None:
            a_position = 0
        abs_pos = self.position - a_position
        return self.get_line(a_linename, a_use_parent)[abs_pos]

    def get_value_abs_position(self, a_linename, a_position, a_use_parent=True):
        return self.get_line(a_linename, a_use_parent)[a_position]
    # endregion

    # region Line
    def get_line(self, a_linename, a_use_parent=True):
        if a_use_parent:
            indicator = self
            while indicator is not None:
                if a_linename in indicator.lines:
                    return indicator.lines.get_line(a_linename)
                indicator = indicator.parent
            return self.lines.get_line(a_linename)
        else:
            return self.lines.get_line(a_linename)
    # endregion

    # region Option
    @property
    def options(self):
        return self.__get_options()

    @options.setter
    def options(self, a_value):
        self.__set_options(a_value)

    def __set_options(self, a_value):
        if isinstance(a_value, (list, tuple)):
            self.__options.vector.clear()
            for i in range(len(a_value)):
                self.__options.vector.append(a_value[i])

    def __get_options(self):
        return self.__options
    # endregion

    # region Input
    @property
    def inputs(self):
        return self.__get_input_lines()

    @inputs.setter
    def inputs(self, a_value):
        self.__set_input_lines(a_value)

    def __set_input_lines(self, a_value):
        if isinstance(a_value, (list, tuple)):
            self.__inputs.vector.clear()
            for i in range(len(a_value)):
                self.__inputs.vector.append(a_value[i])

    def __get_input_lines(self):
        return self.__inputs
    # endregion

    # region Output
    @property
    def outputs(self):
        return self.__get_output_lines()

    @outputs.setter
    def outputs(self, a_value):
        self.__set_output_lines(a_value)

    def __set_output_lines(self, a_value):
        if isinstance(a_value, (list, tuple)):
            self.__outputs.vector.clear()
            for i in range(len(a_value)):
                if isinstance(a_value[i], (list, tuple)):
                    item = a_value[i]
                    if len(item) >= 2:
                        self.__outputs.vector.append((item[0], item[1]))

    def __get_output_lines(self):
        return self.__outputs
    # endregion

    def get_max_count(self):
        max_count = 0
        for linename in self.lines.lines:
            count = len(self.lines.get_line(linename))
            if max_count < count:
                max_count = count
        return max_count

    def highest(self, a_linename, a_length, a_offset=0):
        h = LineValue(-1.0E100)
        for i in range(a_length):
            if h < self.lines[a_linename, i+a_offset]:
                h = self.lines[a_linename, i+a_offset]
        if h == -1.0E100: return LineValue(NAN)
        else: return h
        
    def lowest(self, a_linename, a_length, a_offset=0):
        l = LineValue(1.0E100)
        for i in range(a_length):
            if l > self.lines[a_linename, i+a_offset]:
                l = self.lines[a_linename, i+a_offset]
        if l == 1.0E100: return LineValue(NAN)
        else: return l

    def highest_pos(self, a_linename, a_length, a_offset=0):
        h = LineValue(-1.0E100)
        p = -1
        for i in range(a_length):
            if h < self.lines[a_linename, i+a_offset]:
                h = self.lines[a_linename, i+a_offset]
                p = i
        return p+a_offset
        
    def lowest_pos(self, a_linename, a_length, a_offset=0):
        l = LineValue(1.0E100)
        p = -1
        for i in range(a_length):
            if l > self.lines[a_linename, i+a_offset]:
                l = self.lines[a_linename, i+a_offset]
                p = i
        return p+a_offset

    def above_value(self, a_linename, a_value, a_offset=0):
        if self.lines[a_linename, a_offset] > a_value: return True
        else: return False

    def below_value(self, a_linename, a_value, a_offset=0):
        if self.lines[a_linename, a_offset] < a_value: return True
        else: return False

    def above_line(self, a_linename1, a_linename2, a_offset=0):
        return self.indicator_above_line(a_linename1, self, a_linename2, a_offset)

    def below_line(self, a_linename1, a_linename2, a_offset=0):
        return self.indicator_below_line(a_linename1, self, a_linename2, a_offset)

    def cross_over(self, a_linename1, a_linename2, a_offset=0):
        return self.indicator_cross_over(a_linename1, self, a_linename2, a_offset)

    def cross_down(self, a_linename1, a_linename2, a_offset=0):
        return self.indicator_cross_down(a_linename1, self, a_linename2, a_offset)

    def consecutive_up(self, a_linename, a_count, a_offset=0):
        up = True
        for i in range(a_count):
            if self.lines[a_linename, i+a_offset] < self.lines[a_linename, i+a_offset+1]:
                up = False
                break
        return up

    def consecutive_down(self, a_linename, a_count, a_offset=0):
        down = True
        for i in range(a_count):
            if self.lines[a_linename, i+a_offset] > self.lines[a_linename, i+a_offset+1]:
                down = False
                break
        return down

    def indicator_above_line(self, a_linename1, other, a_linename2, a_offset=0):
        if self.lines[a_linename1, a_offset] > other.lines[a_linename2, a_offset]:
            return True
        else:
            return False

    def indicator_below_line(self, a_linename1, other, a_linename2, a_offset=0):
        if self.lines[a_linename1, a_offset] < other.lines[a_linename2, a_offset]: return True
        else: return False

    def indicator_cross_over(self, a_linename1, other, a_linename2, a_offset=0):
        if self.lines[a_linename1, a_offset] > other.lines[a_linename2, a_offset]:
            down = False
            for i in range(4):
                if self.lines[a_linename1, i+a_offset+1] < other.lines[a_linename2, i+a_offset+1]:
                    down = True
                    break
            if down: return True
        return False

    def indicator_cross_down(self, a_linename1, other, a_linename2, a_offset=0):
        if self.lines[a_linename1, a_offset] < other.lines[a_linename2, a_offset]:
            down = False
            for i in range(4):
                if self.lines[a_linename1, i+a_offset+1] > other.lines[a_linename2, i+a_offset+1]:
                    down = True
                    break
            if down: return True
        return False

    # region private
    def _get_range(self, a_start=0, a_end=-1):
        ymin = 1.0E100
        ymax = -1.0E100
        if a_start < 0:
            a_start = 0
        if a_end == -1:
            a_end = self.get_max_count()
        xmin = a_start
        xmax = a_end-1
        for linename in self.lines.lines:
            line = self.lines.get_line(linename)
            for i in range(xmin, xmax+1):
                if i >= len(line):
                    break
                if not line[i].get_valid():
                    continue
                value = line[i].get_value()
                if value > ymax:
                    ymax = value
                if value < ymin:
                    ymin = value
        if ymax == -1.0E100:
            ymax = 0
        if ymin == 1.0E100:
            ymin = 0
        return {"xmin": xmin, "xmax": xmax, "ymin": ymin, "ymax": ymax}

    def _get_default_setting(self):
        values = dict()
        values["name"] = self.name
        values["options"] = self.__options.vector
        values["inputs"] = self.__inputs.vector
        values["outputs"] = self.__outputs.vector
        return values

    def _highest_of_abs_position(self, a_linename, a_length, a_position):
        h = LineValue(-1.0E100)
        line = self.get_line(a_linename)
        for i in range(a_length):
            p = a_position - i
            if (p >= 0) and (p < len(line)) and line[p].get_valid():
                if h < line[p]:
                    h = line[p]
        if h == -1.0E100:
            return NAN
        else:
            return h.get_value()

    def _lowest_of_abs_position(self, a_linename, a_length, a_position):
        l = LineValue(1.0E100)
        line = self.get_line(a_linename)
        for i in range(a_length):
            p = a_position - i
            if (p >= 0) and (p < len(line)) and line[p].get_valid():
                if l > line[p]:
                    l = line[p]
        if l == 1.0E100:
            return NAN
        else:
            return l.get_value()

    def _get_display_value(self, a_linename, a_position, a_use_parent=True):
        line = self.get_line(a_linename, a_use_parent)
        value = line[a_position]
        if isinstance(value, LineValue):
            return value.get_value()
        else:
            return value

    def _get_all_values(self, a_linename, a_x1=0, a_x2=-1):
        line = self.get_line(a_linename, True)
        if a_x2 == -1:
            a_x2 = len(line) - 1
        values = []
        for i in range(a_x1, a_x2 + 1):
            if (i >= 0) and (i < len(line)):
                values.append(line[i].get_value())
        return values

    def _get_option_object(self):
        value = dict()
        value["options"] = self.__options.vector
        return value

    def _get_input_object(self):
        value = dict()
        value["inputs"] = self.__inputs.vector
        return value

    def _get_output_object(self):
        value = dict()
        value["outputs"] = self.__outputs.vector
        return value
    # endregion


class Indicator(MTSObject):

    def __init__(self, a_parent=None, a_options=None, a_inputs=None, a_outputs=None):
        self.__displays = StringContaner()
        MTSObject.__init__(self, a_parent, a_options, a_inputs, a_outputs)

    def __del__(self):
        MTSObject.__del__(self)

    # region Display
    @property
    def displays(self):
        return self.__get_display_lines()

    @displays.setter
    def displays(self, value):
        self.__set_display_lines(value)

    def __set_display_lines(self, a_value):
        if isinstance(a_value, (list, tuple)):
            self.__displays.vector.clear()
            for i in range(len(a_value)):
                self.__displays.vector.append(a_value[i])

    def __get_display_lines(self):
        return self.__displays

    def _get_display_object(self):
        value = dict()
        value["displays"] = self.__displays.vector
        return value
    # endregion

    def _get_default_setting(self):
        default_setting = MTSObject._get_default_setting(self)
        default_setting["displays"] = self.__displays.vector
        return default_setting


class SignalData:

    def __init__(self, a_date, a_price, a_signal):
        self.date = a_date
        self.signal = a_signal
        self.price = a_price


class Strategy(MTSObject):

    def __init__(self, a_parent=None, a_options=None, a_inputs=None, a_outputs=None):
        MTSObject.__init__(self, a_parent, a_options, a_inputs, a_outputs)
        self.signals = []
        self.last_signal = SIGNAL_NONE

    def __del__(self):
        del self.signals
        MTSObject.__del__(self)

    def clear(self):
        self.signals.clear()
        self.last_signal = SIGNAL_NONE
        MTSObject.clear(self)

    def recalculate(self):
        self.signals.clear()
        self.last_signal = SIGNAL_NONE
        MTSObject.recalculate(self)

    def calculate_all_data(self):
        self.signals.clear()
        self.last_signal = SIGNAL_NONE
        MTSObject.calculate_all_data(self)

    def adjust_position(self, a_position):
        return a_position-1

    def prepare(self):
        self.lines["SIGNAL"] = self.lines["SIGNAL", 1]

    @property
    def signal(self):
        return self.lines["SIGNAL"]

    @signal.setter
    def signal(self, value):
        self.lines["SIGNAL"] = value

    def buy(self):
        if not self.is_long_state():
            self.last_signal = SIGNAL_LONG_ENTER
            self.lines["SIGNAL"] = SIGNAL_LONG_ENTER
            signaldata = SignalData(self.lines["D"], self.lines["C"].get_value(), self.last_signal)
            self.signals.append(signaldata)

    def long_enter(self):
        if not self.is_long_state():
            self.last_signal = SIGNAL_LONG_ENTER
            self.lines["SIGNAL"] = SIGNAL_LONG_ENTER
            signaldata = SignalData(self.lines["D"], self.lines["C"].get_value(), self.last_signal)
            self.signals.append(signaldata)

    def long_exit(self):
        if self.is_long_state():
            self.last_signal = SIGNAL_LONG_EXIT
            self.lines["SIGNAL"] = SIGNAL_LONG_EXIT
            signaldata = SignalData(self.lines["D"], self.lines["C"].get_value(), self.last_signal)
            self.signals.append(signaldata)

    def sell(self):
        if not self.is_short_state():
            self.last_signal = SIGNAL_SHORT_ENTER
            self.lines["SIGNAL"] = SIGNAL_SHORT_ENTER
            signaldata = SignalData(self.lines["D"], self.lines["C"].get_value(), self.last_signal)
            self.signals.append(signaldata)

    def short_enter(self):
        if not self.is_short_state():
            self.last_signal = SIGNAL_SHORT_ENTER
            self.lines["SIGNAL"] = SIGNAL_SHORT_ENTER
            signaldata = SignalData(self.lines["D"], self.lines["C"].get_value(), self.last_signal)
            self.signals.append(signaldata)

    def short_exit(self):
        if self.is_short_state():
            self.last_signal = SIGNAL_SHORT_EXIT
            self.lines["SIGNAL"] = SIGNAL_SHORT_EXIT
            signaldata = SignalData(self.lines["D"], self.lines["C"].get_value(), self.last_signal)
            self.signals.append(signaldata)

    def is_long_state(self):
        return self.lines["SIGNAL"] == SIGNAL_LONG_ENTER

    def is_short_state(self):
        return self.lines["SIGNAL"] == SIGNAL_SHORT_ENTER


class Chart(MTSObject):

    def __init__(self, a_parent=None, a_options=None, a_inputs=None, a_outputs=None):
        MTSObject.__init__(self, a_parent, a_options, a_inputs, a_outputs)
        self.indicators = []
        self.strategy = None

    def __del__(self):
        MTSObject.__del__(self)
        del self.indicators

    def add_indicator(self, a_item):
        a_item.parent = self
        self.indicators.append(a_item)

    def remove_indicator(self, a_item):
        a_item.parent = None
        self.indicators.remove(a_item)

    def set_strategy(self, a_item):
        a_item.parent = self
        self.strategy = a_item

    def remove_strategy(self, a_item):
        a_item.parent = None
        self.strategy = None

    def set_all_data(self, a_data):
        for i in range(len(self.indicators)):
            self.indicators[i].clear()
        MTSObject.set_all_data(self, a_data)

    def set_all_data_csv(self, a_data):
        for i in range(len(self.indicators)):
            self.indicators[i].clear()
        MTSObject.set_all_data_csv(self, a_data)

    def calculate(self, a_position=-1):

        MTSObject.calculate(self, a_position)

        for index in range(len(self.indicators)):
            self.indicators[index].calculate(a_position)
            # print("calculate : %s %d"%(self.indicators[index].name, a_position))
        if self.strategy is not None:
            self.strategy.calculate()


