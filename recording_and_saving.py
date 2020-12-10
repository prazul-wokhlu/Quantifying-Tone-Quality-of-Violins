from pathlib import Path
import librosa
import numpy as np
import pyaudio
import wave


import numpy as np


def record_and_process(duration):
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    fs = 44100  # Record at 44100 samples per second
    seconds = 3
    #filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')
    audio_data = np.hstack([np.frombuffer(i, np.int16) for i in frames])
    return audio_data, frames


# make sure that this variable is assigned to a path to a music file on your computer

def convert_mp3(path_name, song_name):
    song_root = Path(path_name)
    local_song_path = song_root / song_name
    local_song_path = str(local_song_path)
    # load the digital signal for the entire song
    samples, fs = librosa.load(str(local_song_path), sr=44100, mono=True)
    return samples
