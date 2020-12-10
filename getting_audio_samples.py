import numpy as np
from random import uniform

def find_nearest(arr, val):
    arr = np.asarray(arr)
    idx = (np.abs(arr - val)).argmin()
    return arr[idx]

def audio_random_samples(tone):
    # tone is array of nums representing long tone
    tone = tone.tolist()
    t = np.linspace(0, len(tone) / 44.1 / 1000, 1000)
    start = tone[find_nearest(tone, uniform(0, t[-1] - 881.2))] # 881.2 is 2 sec / delta_t

    # returning random 2 second interval from long tone audio
    stop = tone[tone.index(start) + 881.2]
    tone_sample = tone[tone.index(start):tone.index(stop)]
    return np.asarray(tone_sample)
