from pydub import AudioSegment
# Uploading two audio files
beat = AudioSegment.from_wav('beat.wav') # shorter than sax
sax = AudioSegment.from_wav('sax.wav') # longer than beat

# Increasing the duration of "beat" audio file
beat_x2=beat*2

# Overlay/Mix two audo files
mixed=beat_x2.overlay(sax)
mixed.export('mixed.wav')

final_mix= beat + mixed+AudioSegment.silent(500)+sax+mixed*2
final_mix.export('final_mix.wav')