import numpy as np
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json

# Load Vosk model
model_path = "/Users/dalerkim/Downloads/smallModel"
model = Model(model_path)

# Initialize the recognizer
recognizer = KaldiRecognizer(model, 16000)

# flag to exit the loop
should_continue = True

def callback(indata, frames, time, status):
    global should_continue
    # Ensure indata is a NumPy array and convert it to bytes
    data_bytes = indata.astype(np.int16).tobytes()
    if recognizer.AcceptWaveform(data_bytes):
        result = json.loads(recognizer.Result())
        if(result['text'] == "exit"):
            should_continue = False
        else:
            print(">> " + result['text'])


def main():
    global should_continue
    # using InputStream for automatically handling data as NumPy arrays
    with sd.InputStream(samplerate=16000, blocksize=512, dtype='int16', channels=1, callback=callback):
        print("Start speaking now...")
        while should_continue:
            sd.sleep(100)

    print("Exiting program...")

if __name__ == "__main__":
    main()

