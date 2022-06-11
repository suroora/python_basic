from gtts import gTTS
import os

text = "my name is Aizaan Swalih "
output = gTTS(text=text, lang='en', slow=.75)
output.save('output.mp3')
os.system('start output.mp3')
