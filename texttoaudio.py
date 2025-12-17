from gtts import gTTS
import os
clean_content=""
with open('text.txt1', 'r') as file:
    # Read all lines to list
    lines = file.readlines()
    # Join the lines 
    content = '\n'.join(lines)
    # Strip the new line
    clean_content = content.replace('\n',' .')
audio = gTTS(text=clean_content, lang="en", slow=False)
audio.save("video_narration.mp3")
os.system("start video_narration.mp3")
