
# Ultrasonic Distance Monitoring System Using Raspberry Pi Pico

This project demonstrates a distance monitoring system built using a Raspberry Pi and an ultrasonic sensor. The system measures the distance to an object and displays the real-time information such as distance, "DANGER," and "SAFE" directly on the Raspberry Pi's small display (e.g., an attached LCD or OLED screen).

## Features
Distance Measurement: Measures the distance to an object in real-time using an ultrasonic sensor.
Screen Output: Displays distance, "DANGER," or "SAFE" messages directly on the Raspberry Pi's small screen.
Danger Alerts: If an object is within 10 cm, the system will display "DANGER" on the screen.

## Hardware Requirements
Microcontroller: Raspberry Pi (with a connected small screen, such as an LCD or OLED).
Ultrasonic Sensor: HC-SR04 or similar.
Connecting Wires: To connect the ultrasonic sensor to the Raspberry Pi.

## Working
The Raspberry Pi triggers the ultrasonic sensor to emit a pulse and waits for the echo to return.
The time taken for the echo to return is used to calculate the distance in centimeters.
The Raspberry Pi's small screen (connected to the Pi) displays:
The measured distance in centimeters.
The status of the object ("SAFE" if the object is farther than 10 cm, "DANGER" if it is too close).
If the object is closer than 10 cm, the screen displays "DANGER."
If the object is farther than 10 cm, the screen displays "SAFE."

