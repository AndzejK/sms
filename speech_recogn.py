from speech_recognition import Recognizer, AudioFile

recogniser=Recognizer()

with AudioFile('Work.wav') as audio_file:
    audio=recogniser.record(audio_file)

txt=recogniser.recognize_google(audio)
print(txt)