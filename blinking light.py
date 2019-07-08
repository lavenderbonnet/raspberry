from gpiozero import LED, Button
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()

    sleep(1)
                                                                                                                                 

button = Button(18)
while True:
    if button.is_pressed:
        print("Pressed")
    else:
        print("Released")
    sleep(1)
