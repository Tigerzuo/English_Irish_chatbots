'''
Example of a simple CLI script that creates a persistent
chat session untill closed.
'''

from cleverwrap import CleverWrap
import sys
from gtts import gTTS
from playsound import playsound


englishBot = CleverWrap('')
irishBot = CleverWrap('')

init = True

def main():
    conv0 = englishBot.new_conversation()
    conv1 = irishBot.new_conversation()
    text = conv0.say("Hello there!")
    while True:
        print(text)
        text = conv0.say(text)
        print(text)
        text = conv1.say(text)
        
if __name__ == '__main__':

    main()
