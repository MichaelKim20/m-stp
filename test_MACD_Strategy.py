import time
from mtrading.strategy.STMACD import *


def load_sample_data():
    f = open("data.txt", 'r')
    data = ''
    while True:
        line = f.readline()
        if not line:
            break
        data += line + "\n"
    f.close()
    return data


def get_value_string(a_value):
    if isinstance(a_value, LineValue):
        val = a_value.get_value()
    else:
        val = a_value
    if val == NAN:
        return "NAN"
    else:
        return "%8.2f" % val


def print_strategy(a_indicator):
    for i in range(a_indicator.get_max_count()):
        v0 = a_indicator.get_value_abs_position("SIGNAL", i)
        print("%5d %s" % (i, get_value_string(v0)))


def print_signal(a_strategy):
    for i in range(len(a_strategy.signals)):
        v0 = a_strategy.signals[i]
        print("%d %f" % (v0.signal, v0.price))

indicator = STMACD(None)
indicator.options = [9, 15, 9]
t1 = time.time() # start time
indicator.set_all_data_csv(load_sample_data())
t2 = time.time() # end time
print("데이터를 입력하는데 걸린 시간 : %f" % (t2-t1))

t1 = time.time() # start time
indicator.calculate_all_data()
t2 = time.time() # end time
print("계산에 걸린 시간 : %f" % (t2-t1))

# print_strategy(indicator)
print_signal(indicator)

print(indicator._get_default_setting())