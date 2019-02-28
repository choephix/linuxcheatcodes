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
    sys.stdout.write((str)(clock)+" ~ temperature: "+clr+(str)(temp)+" degrees"+endc)
    sys.stdout.flush()


interval = 1
t_prev = 0
while True:
    t = time.clock()
    if t - t_prev >= interval:
        sys.stdout.write('\r')
        sys.stdout.flush()
    print_line( (int)(t), cpu.temperature )
    time.sleep(.100)
