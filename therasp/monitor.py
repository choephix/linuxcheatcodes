from gpiozero import CPUTemperature
from time import sleep

cpu = CPUTemperature()

while True:
  temp = cpu.temperature
  endc = '\033[0m'
  clr = '\033[94m'
  if temp > 45.0: clr = '\033[96m'
  if temp > 50.0: clr = '\033[92m'
  if temp > 55.0: clr = '\033[93m'
  if temp > 60.0: clr = '\033[91m'
  if temp > 70.0: clr = '\033[101m'
  print("• temperature: "+clr+(str)(temp)+" degrees"+endc)
  sleep(5)
