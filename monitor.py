import sys
import os
import time


INTERVAL_VIEW = 0.500
INTERVAL_COMMIT = 10.000


def c(n):
  return "\033["+str(n)+"m"


def print_line(t, temp):
  temp_str = '{0:.3f}'.format(temp)
  clr = colors[0]
  for i, thre in enumerate(thresh):
    if temp > thre:
      clr = colors[i+1]
    else:
      break
  s = ''
  s += c(30+clr)
  s += "  cpu temperature: "
  s += c(90+clr) + temp_str
  s += c(0) + c(30+clr)
  s += " degrees celsius  "
  s += c(0) + c(35)
  sys.stdout.write('\r')
  sys.stdout.write(s)
  sys.stdout.flush()


fpath = "/sys/class/thermal/thermal_zone0/temp"
colors = [4,  6,  2,  3,  1, 11]
thresh = [30, 40, 50, 60, 70]

os.system('clear')

with open("/sys/firmware/devicetree/base/model") as f:
  device_name = f.read()
print()
print(c(35) + device_name)
print()

# # #

temp_max = 0.0
t_prev = 0.0

try:
  while True:
    t = time.time()
    with open(fpath) as f:
      temp = .001 * float(f.read())
    if temp_max < temp:
        temp_max = temp
    if t - t_prev >= INTERVAL_COMMIT:
        print_line((int)(t), temp_max)
        sys.stdout.write('\n')
        sys.stdout.flush()
        temp_max = 0.0
        t_prev = t
    else:
        print_line((int)(t), temp)
    time.sleep(INTERVAL_VIEW)
except KeyboardInterrupt:
  sys.stdout.write('\n\n'+c(0))
  sys.stdout.flush()
  pass
