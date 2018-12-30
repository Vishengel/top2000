import numpy as np
import pandas as pd
import os
from PyLyrics import *

data_file = os.path.join(os.pardir, "data", "raw_data.xls")
destination_file = os.path.join(os.pardir, "data", "data_with_lyrics.csv")

df = pd.read_excel(data_file, header = None, names = ['pos', 'track', 'artist', 'year'])

df['lyrics'] = ''

for index, row in df.iterrows():
    #artist = Artist()
    #track = Track(trackName=row['track'], artist=artist)
    try:
        print("Found lyrics for: ", row['pos'], ": ", row['artist'], " - ", row['track'])
        #row['lyrics'] = PyLyrics.getLyrics(singer=row['artist'], song=row['track'])
        df.at[index, 'lyrics'] = PyLyrics.getLyrics(singer=row['artist'], song=row['track'])
    except:
        print("Could not find lyrics for: ", row['pos'], ": ", row['artist'], " - ", row['track'])
        df.at[index, 'lyrics'] =  np.nan

df.to_csv(destination_file)