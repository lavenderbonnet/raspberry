from gpiozero import LED, Button

led = LED(17)
button = Button(18)

while True:
    button.wait_for_press()
    led.on()
    button.wait_for_release()
    led.off()
