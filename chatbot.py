'''
Example of a simple CLI script that creates a persistent
chat session untill closed.
'''

from cleverwrap import CleverWrap
import sys
from gtts import gTTS
from playsound import playsound
import time


englishBot = CleverWrap('')
irishBot = CleverWrap('')

def main(text):
    while True:
        print(text)
        text = conv0.say(text)
        print(text)
        tts = gTTS(text, lang='en-IE')
        tts.save("bot.mp3")
        playsound('bot.mp3')

        time.sleep(0.5)

        text = conv1.say(text)
        tts = gTTS(text, lang='en-GB')
        tts.save("bot.mp3")
        playsound('bot.mp3')

if __name__ == '__main__':
    conv0 = englishBot.new_conversation()
    conv1 = irishBot.new_conversation()
    text = input("Input conversation starter: ")
    print(text)
    text = conv1.say(text)
    main(text)
