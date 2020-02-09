'''
Example of a simple CLI script that creates a persistent
chat session untill closed.
'''

from cleverwrap import CleverWrap
import cleverbotfree.cbfree
import sys
from gtts import gTTS
from playsound import playsound


englishBot = CleverWrap("API KEY")
irishBot = CleverWrap("API KEY")

init = True

def main(init_text):
    #cw.say("Hello Cleverbot")
    conv0 = englishBot.new_conversation()
    conv1 = irishBot.new_converstion()
    print("Hello There!")
    text = conv0.say("Hello there!")
    while True:
        print(text)
        text = conv0.say(text)
        print(text)
        text = conv1.say(text)
        
if __name__ == '__main__':

    conv
    print("input text")
    init_text = input()
    main(init_text)
