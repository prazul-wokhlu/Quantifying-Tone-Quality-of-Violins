import numpy as np
import matplotlib.mlab as mlab

def spectogram(audio):
    # Returns clipped version of values in spectrogram
    sampling_rate = 44100
    S, freqs, times = mlab.specgram(audio, NFFT=4096, Fs=sampling_rate,
                                    window=mlab.window_hanning,
                                    noverlap=int(4096 / 2))
    np.clip(S, 1e-20, None)
    return np.log(S)

def amp_min(audio):

    # param audio: audio file
    # return: cutoff point for local peaks function

    S = spectogram(audio)

    S = S.flatten()

    sorted_S = np.sort(S)

    index = int(len(S)*0.77)
    cutoff = sorted_S[index]
    return cutoff

