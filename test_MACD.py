import time
from mtrading.indicator.MACD import *


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


def print_indicator(a_indicator):
    displayList = a_indicator.displays
    for i in range(a_indicator.get_max_count()):
        if len(displayList) == 3:
            v0 = a_indicator.get_value_abs_position(displayList[0], i)
            v1 = a_indicator.get_value_abs_position(displayList[1], i)
            v2 = a_indicator.get_value_abs_position(displayList[2], i)
            v3 = a_indicator.get_value_abs_position(displayList[4], i)
            print("%5d %s:%s %s:%s %s:%s %s:%s" % (i, displayList[0], get_value_string(v0), displayList[1], get_value_string(v1), displayList[2], get_value_string(v2), displayList[3], get_value_string(v3)))
            pass

        if len(displayList) == 3:
            v0 = a_indicator.get_value_abs_position(displayList[0], i)
            v1 = a_indicator.get_value_abs_position(displayList[1], i)
            v2 = a_indicator.get_value_abs_position(displayList[2], i)
            print("%5d %s:%s %s:%s %s:%s" % (i, displayList[0], get_value_string(v0), displayList[1], get_value_string(v1), displayList[2], get_value_string(v2)))
            pass

        elif len(displayList) == 2:
            v0 = a_indicator.get_value_abs_position(displayList[0], i)
            v1 = a_indicator.get_value_abs_position(displayList[1], i)
            print("%5d %s:%s %s:%s" % (i, displayList[0], get_value_string(v0), displayList[1], get_value_string(v1)))
            pass

        else:
            v0 = a_indicator.get_value_abs_position(displayList[0], i)
            print("%5d %s:%s" % (i, displayList[0], get_value_string(v0)))

indicator = MACD(None)
indicator.options = [9, 15, 9]
t1 = time.time() # start time
indicator.set_all_data_csv(load_sample_data())
t2 = time.time() # end time
print("데이터를 입력하는데 걸린 시간 : %f" % (t2-t1))


t1 = time.time() # start time
indicator.calculate_all_data()
t2 = time.time() # end time
print("계산에 걸린 시간 : %f" % (t2-t1))

print_indicator(indicator)

print(indicator._get_default_setting())