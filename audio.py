# I did not recieve SMS via TWILLIO thus could not use this serive
import os
os.environ["FFMPEG_BINARY"] = "/opt/homebrew/bin/ffmpeg"
##### AUDIO #####
from pydub import AudioSegment
original = AudioSegment.from_wav('beat.wav')
# Making a change to an audio file, reversing it!
reversed=original.reverse()
#save that change on the MAC
reversed.export('reversed_beat.wav')
# increase the volume/sound
reversed=reversed+15

# get all available audio methods
#print(dir(original))

# get 2 sec audio
fist_two_sec=original[0:2000] # 1sec = 1000ms
#save that change on the MAC
fist_two_sec.export('fist_two_sec_beat.wav')

# Get the length of the audio
print(len(original)/1000) # the original length is in MS to covert to S multiple by 1k
print(len(fist_two_sec)/1000)

# Merge two audio files
merged=original+reversed
merged.export('merged_beat.wav')
# Merge and add a pause between two audio files
merged_pause=original+AudioSegment.silent(1000)+reversed
merged_pause.export('merged_pause_beat.wav')
