from machine import Pin
import utime
import time
from gpio_lcd import GpioLcd

trigger = Pin(15, Pin.OUT)
echo = Pin(14, Pin.IN)
buzzer_pin = Pin(6, Pin.OUT)
led1=Pin('LED',Pin.OUT)
led2=Pin(2,Pin.OUT)
led3=Pin(3,Pin.OUT)


lcd = GpioLcd(rs_pin=Pin(8),
              enable_pin=Pin(9),
              d4_pin=Pin(10),
              d5_pin=Pin(11),
              d6_pin=Pin(12),
              d7_pin=Pin(13))

def buzz(duration_ms):
    buzzer_pin.on()
    utime.sleep_ms(duration_ms)
    buzzer_pin.off()

danger_start_time = None
danger_timer = 0

while True:
    
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()

 
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()

    
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2  # Distance in cm

   
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Distance: {:.1f} cm".format(distance))

    
    if (distance <= 10):
        lcd.move_to(0, 1)
        lcd.putstr("DANGER")
        if danger_start_time is None:
            danger_start_time = utime.ticks_ms()  # Start the timer
        else:
            # Update the timer
            danger_timer = (utime.ticks_ms() - danger_start_time) // 1000
            lcd.move_to(0, 1)
            lcd.putstr("Safe: {}s".format(danger_timer))
    else:
        
        danger_start_time = None
        danger_timer = 0

        
        lcd.move_to(0, 1)
        lcd.putstr("Safe")

   
    if (distance <=10):
        buzz(2000)  # Buzz for 1000 milliseconds (1 second)
        led1.on()
        time.sleep(0.01)
        led1.off()
        time.sleep(0.01)
        led2.on()
        time.sleep(0.01)
        led2.off()
        time.sleep(0.01)
        led3.on()
        time.sleep(0.01)
        led3.off()

    
    utime.sleep(1)
