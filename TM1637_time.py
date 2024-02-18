import tm1637
from time import localtime

CLK = 5
DIO = 4

tm = tm1637.TM1637(CLK, DIO)

try:
    while True:
        lt = localtime()
        tm.numbers(lt.tm_hour, lt.tm_min)

except KeyboardInterrupt:
    tm.write([0, 0, 0, 0])