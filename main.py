import my_oled
import time

state = 0


while True:
    print(state)
    if state == 0:
        my_oled.print_text("test",0,0)
    if state == 1:
        my_oled.print_text("something else",0,64)
    if state == 2:
        my_oled.oled.line(0,0,10,10,1)
    time.sleep(1)
    state= state +1
    if state == 4:
        state = 0



