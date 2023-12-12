# src/simplethanks/resources/happy-birthday-whistled.wav
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("src/simplethanks/resources/happy-birthday-whistled.wav")
play(song)