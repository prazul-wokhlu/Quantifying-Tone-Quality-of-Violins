import pickle

song_dict=dict();
def save_dict(path="longtone.dict", d=song_dict):
    # Saving dictionary using pickle into current folder
    save_file=open(path,'wb')
    pickle.dump(d, save_file);
    save_file.close()

def load_dict(path="longtone.dict"):
    save_file=open(path,'rb')
    song_dict=pickle.load(save_file)
    save_file.close()
    return song_dict

def add_song(peak_list, song_id, fan=15):
    for i in range(len(peak_list)):
        for j in range(i + 1, min(len(peak_list), i + 1 + fan)):
            key = (peak_list[i][1], peak_list[j][1], peak_list[j][0] - peak_list[i][0])
            if key not in song_dict:
                song_dict[key] = []
            song_dict[key].append((song_id,peak_list[i][1]))
    return song_dict

def get_fingerprint(peak_list, fan=15):
    match_dict = {}
    for i in range(len(peak_list)):
        for j in range(i+1, min(len(peak_list), i + 1 + fan)):
            key = (peak_list[i][1], peak_list[j][1], peak_list[j][0] - peak_list[i][0])
            if key not in match_dict:
                match_dict[key] = []
            match_dict[key].append(peak_list[i][1])
    return match_dict
def get():
    return song_dict
