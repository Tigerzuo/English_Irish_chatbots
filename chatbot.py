'''
Example of a simple CLI script that creates a persistent
chat session untill closed.
'''

import cleverbotfree.cbfree
import sys
from gtts import gTTS
from playsound import playsound


cb1 = cleverbotfree.cbfree.Cleverbot()
cb2 = cleverbotfree.cbfree.Cleverbot()

init = True

def main(init_text):
    try:
        print("Try connect to browser")
        cb1.browser.get(cb1.url)
        cb2.browser.get(cb2.url)
    except:
        cb1.browser.close()
        cb2.browser.close()
        sys.exit()

    global init

    try:
        print("try to get form")
        cb1.get_form()
        cb2.get_form()
    except:
        sys.exit()

    while True:
        if init == True:
            bot2 = init_text
            print ("starting!")
        init = False

        cb1.send_input(bot2)
        bot1 = cb1.get_response()
        tts = gTTS(bot1, lang='en-IE')
        tts.save("bot.mp3")
        playsound('bot.mp3')
        print('Cleverbot1: ', bot1)

        cb2.send_input(bot1)
        bot2 = cb2.get_response()
        tts = gTTS(bot2, lang='en-GB')
        tts.save("bot.mp3")
        playsound('bot.mp3')
        print('Cleverbot2: ', bot2)

    cb1.browser.close()
    cb2.browser.close()

    
if __name__ == '__main__':
    print("input text")
    init_text = input()
    main(init_text)
