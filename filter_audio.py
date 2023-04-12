from pydub import AudioSegment
# Uploading two audio files
beat = AudioSegment.from_wav('beat.wav') # shorter than sax
sax = AudioSegment.from_wav('sax.wav') # longer than beat

# Removing lower frequencies from the audio file and provides us with more base
beat_low=beat.low_pass_filter(2000)
beat_low.export('beat_low.wav')

compare_2_audio=beat+beat_low
compare_2_audio.export('compare_2_beats.wav')

# Force sound to sound in one speaker
beat_left=beat_low.pan(-1) # 0 - both speaker, -1.0 - left speaker 1.0 - right speaker
beat_left.export('beat_left.wav')
beat_right=beat.pan(+1)
left_and_later_righ_beat=beat_left+beat_right
left_and_later_righ_beat.export('left_and_later_righ_beat.wav')