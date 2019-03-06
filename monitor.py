import sys
import os
import time


os.system('clear')


def print_line( t, temp ):
  def c(n): return "\033["+str(n)+"m"
  temp_str = '{0:.3f}'.format(temp)
  clr = colors[0]
  for i, thre in enumerate(thresh):
    if temp > thre:
      clr = colors[i+1]
    else:
      break
  s = ''
  s += c(30+clr)
  s += "-> cpu temperature: "
  s += c(90+clr)+temp_str
  s += c(30+clr)
  s += " degrees celsius"
  s += c(0)
  sys.stdout.write('\r')
  sys.stdout.write("\033[K")
  sys.stdout.write(s)
  sys.stdout.flush()


fpath = "/sys/class/thermal/thermal_zone0/temp"
colors = [  4,  6,  2,  3,  1, 11 ]
thresh = [ 30, 40, 50, 60, 70 ]

with open("/sys/firmware/devicetree/base/model") as f:
  device_name = f.read()

print()
print( device_name )
print()

# # # 

interval = 1.0
temp_max = 0.0
t_prev = 0.0

try:
  while True:
    t = time.time()
    with open( fpath ) as f:
      temp = .001 * float(f.read())
    if temp_max < temp:
        temp_max = temp
    if t - t_prev >= interval:
        print_line((int)(t), temp_max)
        sys.stdout.write('\n')
        sys.stdout.flush()
        temp_max = 0.0
        t_prev = t
    else:
        print_line((int)(t), temp)
    time.sleep(.200)
except KeyboardInterrupt:
  sys.stdout.write('\n\n')
  sys.stdout.flush()
  pass
