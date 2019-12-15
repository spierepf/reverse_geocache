import lvgl as lv
import lvesp32
from ili9341 import ili9341
disp = ili9341(miso=19, mosi=23, clk=18, cs=15, dc=2, rst=4)

# Create a screen with a button and a label

scr = lv.obj()
btn = lv.btn(scr)
btn.align(lv.scr_act(), lv.ALIGN.CENTER, 0, 0)
label = lv.label(btn)
label.set_text("Hello World!")

# Load the screen

lv.scr_load(scr)

from machine import UART
import math

def convert(value):
  degrees = math.floor(value/100)
  minutes = value - degrees * 100
  return degrees + minutes / 60.0

uart = UART(1)
uart.init(9600,bits=8,parity=None,stop=1,rx=25,tx=26)

line = ''
while True:
  while uart.any() == 0:
    pass
  try:
    line += uart.readline().decode('utf-8')
  except:
    pass
  if line.endswith('\r\n'):
    if line.startswith('$GPGGA'):
      print(line)
      data = line.split(',')
      try:
        lon = convert(float(data[2]))
        lat = convert(float(data[4]))
        dop = float(data[8])
        print('%.7f'%lon, '%.7f'%lat, dop)
      except:
        pass
    line = ''
