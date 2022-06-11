from gtts import gTTS
import os
text=open("suroora.txt",'r').read()
output=gTTS(text=text,lang='en',slow=False)
output.save('output.mp4')
os.system('start output.mp4')
