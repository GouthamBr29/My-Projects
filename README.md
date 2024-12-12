
# Robot Controller with Speech Recognition

This project implements a robot controller that uses speech recognition to interpret and execute commands. It integrates with the Webots simulation framework (or similar), allowing real-time control of a robot's motors and sensors.

## Features

- **Speech Recognition**: Utilizes the `speech_recognition` library to process voice commands via a microphone.
- **Robot Control**: Interfaces with a robot's motors and sensors to execute commands.
- **Threaded Command Processing**: Employs multithreading to manage commands efficiently.

## Requirements

- Python 3.x
- Webots simulation software (or compatible robot framework)
- Required Python libraries:
  - `speech_recognition`
  - `pyttsx3` (for text-to-speech, if applicable)
  - `webots` (or the robot's SDK)
- A microphone for speech input

## Setup

1. **Install Dependencies**:

   ```bash
   pip install speechrecognition pyttsx3
   ```

2. **Set Up Webots**:
   - Download and install Webots from [Webots Official Site](https://cyberbotics.com/).
   - Add the Webots Python API to your project.

3. **Connect Hardware (if applicable)**:
   - Ensure that the robot's hardware or simulation environment is properly configured.

## Usage

1. **Run the Controller**:
   Execute the script in your terminal:
   ```bash
   python my_controller.py
   ```

2. **Provide Voice Commands**:
   - Speak commands into the microphone to control the robot.
   - Example commands include:
     - "Move forward"
     - "Turn left"
     - "Stop"

3. **Command Queue**:
   - Commands are processed in a queue, ensuring smooth operation.

## Customization

- **Add New Commands**:
  - Modify the `command_queue` logic to handle additional robot actions.
- **Adjust Robot Parameters**:
  - Tune motor speeds and sensor thresholds within the script.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License.
