## Autonombot one


import machine
import time

# Motor control pins
motor_left_forward = machine.Pin(14, machine.Pin.OUT)   # Left motor forward
motor_left_backward = machine.Pin(15, machine.Pin.OUT)  # Left motor backward
motor_right_forward = machine.Pin(16, machine.Pin.OUT)  # Right motor forward
motor_right_backward = machine.Pin(17, machine.Pin.OUT) # Right motor backward

# IR sensor pins
left_ir_sensor = machine.Pin(2, machine.Pin.IN)  # Left IR sensor
right_ir_sensor = machine.Pin(3, machine.Pin.IN) # Right IR sensor

# Function to move the robot forward
def move_forward():
    motor_left_forward.on()
    motor_right_forward.on()
    motor_left_backward.off()
    motor_right_backward.off()

# Function to stop the robot
def stop():
    motor_left_forward.off()
    motor_right_forward.off()
    motor_left_backward.off()
    motor_right_backward.off()

# Function to turn right
def turn_right():
    motor_left_forward.on()
    motor_right_backward.on()

# Function to turn left
def turn_left():
    motor_left_backward.on()
    motor_right_forward.on()

# Main loop
try:
    while True:
        left_detected = left_ir_sensor.value()  # Read left sensor
        right_detected = right_ir_sensor.value() # Read right sensor

        if left_detected == 0 and right_detected == 0:
            # Both sensors detect the line (black)
            move_forward()
        elif left_detected == 1 and right_detected == 0:
            # Left sensor is off the line (white), turn right
            turn_right()
        elif left_detected == 0 and right_detected == 1:
            # Right sensor is off the line (white), turn left
            turn_left()
        else:
            # Both sensors are off the line (optional: stop or backtrack)
            stop()

        time.sleep(0.1)  # Add a small delay for stability

except KeyboardInterrupt:
    stop()  # Stop the robot on interrupt