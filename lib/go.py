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
