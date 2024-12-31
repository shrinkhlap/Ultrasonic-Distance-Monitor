# Ultrasonic-Distance-Monitor
This project demonstrates a simple distance monitoring system built with a Raspberry Pi Pico. The system uses an ultrasonic sensor to measure distance and provides real-time feedback on an LCD. Additionally, it uses a buzzer and LEDs to alert when an object is detected within a specified range.

## Features
Distance Measurement: Measures the distance to an object in real time using an ultrasonic sensor.
LCD Display: Shows the measured distance in centimeters.
Danger Alert:
Activates a buzzer and LEDs when an object is closer than 10 cm.
Displays "DANGER" on the LCD.
Sequential LED Alerts: LEDs blink in sequence to provide a visual warning.

## Hardware Requirements
Microcontroller: Raspberry Pi Pico (required).
Other Components: Ultrasonic sensor (e.g., HC-SR04), piezo buzzer, 16x2 LCD, and 3 LEDs.

## Working
The Raspberry Pi Pico sends a pulse through the ultrasonic sensor and waits for the echo.
The time taken for the echo to return is used to calculate the distance.
The distance is displayed on the LCD in real time.
If the measured distance is less than 10 cm:
The LCD displays "DANGER".
A buzzer sounds, and LEDs blink in sequence to alert the user.
If the object moves beyond 10 cm, the system resets to display "Safe".

