import collections
def match(fingerprints, database):
    # dict fingerprints: dictionary of frequencies mapped to specific song and time
    # dict database: dictionary of all frequencies mapped to all songs in database
    # return: song of the (song,time) tuple

    x = []
    for key in fingerprints:
        if key in database:
            match_list=[]
            for time in fingerprints[key]:
                for match in database[key]:
                    match_list.append((match[0],time-match[1]))
            x.extend(match_list)
    counter = collections.Counter(x)

    mostCommon = counter.most_common(2)

    return mostCommon, counter



def into_database(fingerprints, database):
    # updates database with fingerprints
    database.update(fingerprints)
