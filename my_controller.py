import threading
import speech_recognition as sr
from controller import Robot


robot = Robot()
TIMESTEP = 32

#speech recognizer and microphone
recognizer = sr.Recognizer()
microphone = sr.Microphone()

#Command queue for background processing
command_queue = []

#motors and distance sensors
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

#distance sensors
proximity_sensors = []
for i in range(8):
    sensor = robot.getDevice(f"ps{i}")
    sensor.enable(TIMESTEP)
    proximity_sensors.append(sensor)


OBSTACLE_THRESHOLD = 80.0

def listen_in_background():
    while True:
        with microphone as source:
            print("Listening for command...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                print(f"Command received: {command}")
                command_queue.append(command.lower())
            except sr.UnknownValueError:
                print("Sorry, I could not understand the command.")
            except sr.RequestError as e:
                print(f"Error with speech recognition service: {e}")


listener_thread = threading.Thread(target=listen_in_background, daemon=True)
listener_thread.start()

def move_robot(command):
    if "forward" in command:
        left_motor.setVelocity(1.0)
        right_motor.setVelocity(1.0)
    elif "backward" in command:
        left_motor.setVelocity(-1.0)
        right_motor.setVelocity(-1.0)
    elif "left" in command:
        left_motor.setVelocity(-1.0)
        right_motor.setVelocity(1.0)
    elif "right" in command:
        left_motor.setVelocity(1.0)
        right_motor.setVelocity(-1.0)
    elif "stop" in command:
        left_motor.setVelocity(0)
        right_motor.setVelocity(0)
    else:
        print("Unknown command.")

def avoid_obstacles():
    
    sensor_values = [sensor.getValue() for sensor in proximity_sensors]
    
    #Obstacle detection code
    left_obstacle = sensor_values[0] > OBSTACLE_THRESHOLD or sensor_values[1] > OBSTACLE_THRESHOLD
    right_obstacle = sensor_values[6] > OBSTACLE_THRESHOLD or sensor_values[7] > OBSTACLE_THRESHOLD
    
    if left_obstacle and not right_obstacle:
        
        left_motor.setVelocity(1.0)
        right_motor.setVelocity(-1.0)
    elif right_obstacle and not left_obstacle:
        
        left_motor.setVelocity(-1.0)
        right_motor.setVelocity(1.0)
    elif left_obstacle and right_obstacle:
       
        left_motor.setVelocity(-1.0)
        right_motor.setVelocity(-1.0)
    else:
       
        return False 
    return True 

#Main control loop
while robot.step(TIMESTEP) != -1:
    if not avoid_obstacles():  
        if command_queue:  
            command = command_queue.pop(0)
            move_robot(command)
