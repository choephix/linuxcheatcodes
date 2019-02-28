import sys
from gpiozero import CPUTemperature
import time

cpu = CPUTemperature()


def print_line(clock,temp):
    endc = '\033[0m'
    clr = '\033[94m'
    if temp > 45.0: clr = '\033[96m'
    if temp > 50.0: clr = '\033[92m'
    if temp > 55.0: clr = '\033[93m'
    if temp > 60.0: clr = '\033[91m'
    if temp > 70.0: clr = '\033[101m'
    sys.stdout.write(" ~ temperature: "+clr+(str)(temp)+" degrees"+endc)
    sys.stdout.flush()


interval = 1.0
t_prev = 0.0
c_max = 0.0
while True:
    t = time.clock()
    c = cpu.temperature
    if c_max < c:
        c_max = c
    if t - t_prev >= interval:
        print_line((int)(t), c_max)
        sys.stdout.write('\n')
        sys.stdout.flush()
        c_max = 0.0
        t_prev = t
    # else:
    #     sys.stdout.write('\r')
    #     print_line((int)(t), c)
    print(t, t_prev)
    time.sleep(.250)
