import spectogram
import recording_and_saving
import match_tones
import makingdict
import numpy as np
import find_peaks
import os.path


def load_tones(id_to_tone):
    for tone_id, filename in id_to_tone.items():
        # Change path based on where this is located in your computer
        path = '/Users/prazul/PycharmProjects/csFinal/tone_recognition/longtone_mp3s/'

        samples = recording_and_saving.convert_mp3(path, filename + '.mp3')
        samples *= 2**15
        samples = np.array(samples, dtype="int")
        spectrogram_upload = spectogram.spectogram(samples)
        minimum_amp = spectogram.amp_min(samples)
        peaks_upload = find_peaks.local_peaks(spectrogram_upload, minimum_amp, 20)
        makingdict.add_song(peaks_upload, tone_id, fan=15)
        print('added ' + filename)
    makingdict.save_dict()

def make_match(id_to_tone):
    data, playable = recording_and_saving.record_and_process(10)

    spectogram_test = spectogram.spectogram(data)
    minimum_amp = spectogram.amp_min(data)
    peaks_test = find_peaks.local_peaks(spectogram_test, minimum_amp, 20)
    test_dictionary = makingdict.get_fingerprint(peaks_test, fan=15)
    result, counter = match_tones.match(test_dictionary, dictionary)
    if (result[0][1] > 200) or (result[0][1] > 2 * result[1][1] and result[0][1] > 50):
        print(id_to_tone[result[0][0][0]])
    else:
        print("It sounds most like: "+id_to_tone[result[0][0][0]]+", but we aren't sure")


id_to_tone1 = {1 :'worstG', 2 : 'mediumG', 3 : 'bestG',
              4 : 'worstA', 5 : 'mediumA', 6 : 'bestA',
              7 : 'worstD', 8 : 'mediumD', 9 : 'bestD',
              10 : 'worstE', 11 : 'mediumE', 12 : 'bestE'}

if os.path.exists('longtone.dict'):
    dictionary= makingdict.load_dict()


else:
    load_tones(id_to_tone1)
    dictionary = makingdict.load_dict()

while input('Press enter to determine sound quality or q to quit\n') != 'q':
    make_match(id_to_tone1)




