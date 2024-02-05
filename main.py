from microbit import *
import music

led_dict = {
  0: [2, 2],
  1: [1, 2],
  2: [1, 3],
  3: [2, 3],
  4: [3, 3],
  5: [3, 2],
  6: [3, 1],
  7: [2, 1],
  8: [1, 1],
  9: [0, 1],
  10: [0, 2],
  11: [0, 3],
  12: [0, 4],
  13: [1, 4],
  14: [2, 4],
  15: [3, 4],
  16: [4, 4],
  17: [4, 3],
  18: [4, 2],
  19: [4, 1],
  20: [4, 0],
  21: [3, 0],
  22: [2, 0],
  23: [1, 0],
  24: [0, 0],
}
    
def show_image(countdown):
    for i in range(25):
        display.set_pixel(
            led_dict[i][0],
            led_dict[i][1],
            0 if i > countdown else 9)

    for i in range (6):
        display.set_pixel(
            led_dict[countdown][0],
            led_dict[countdown][1],
            9 - i)
        sleep(10_000)

while True:
    display.show(Image.DIAMOND)

    if button_b.is_pressed(): 
        display.clear()
        for x in range(24, -1, -1):
            print(running_time() / 1000)
            show_image(x)
        display.show(Image.HAPPY)
        music.play(music.POWER_UP)
        sleep(1_000)
