# Speech Recognition via the VOSK API

This program provides real-time speech recognition for different languages using the Vosk API and sounddevice library. It's designed to convert spoken words into text on-the-fly, enabling users to interact with their devices through voice commands or transcribe speech effortlessly.

## Installation

Before running the program, ensure you have Python installed on your system. This program has been tested with Python 3.8 and above.

## Required Python Libraries

This program requires the `vosk` and `sounddevice` libraries. You can install these libraries using `pip` by running the following command in your terminal:

`pip install vosk sounddevice`

## Configuration
Before running the program, you need to set the path to the Vosk model you downloaded in the program file. Locate the following line in the program:

`model_path = "/enter/your/path/to/model"`

## Additional Notes
To exit the program, simply say "exit" when using the English model. This voice command will terminate the speech recognition loop and close the application.







