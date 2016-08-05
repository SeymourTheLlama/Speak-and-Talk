import pygame
import pyaudio
import wave
import time
import os
from subprocess import call
run = True


while run == True:
    call("./play.sh", shell=True)
    print("\n" * 100)
    print('BOB-BOT v. 1.0.1')
    print('Your automated IT Tech')
    print('----------------------------------------------')
    print('1) Computer Problems')
    print('2) Promethean Board or Projector Problems')
    print('3) Printer Problems')
    print('4) Problem Not Listed')
    print('')
    FirstAnswer = input('# ')
    if FirstAnswer == '1':
        print('----------------------------------------------')
        print('Computer Problems - Most computer problems can be solved with a restart but others may require further instructions')
        print('1) ')
        print('2) ')
        print('3) ')
        SecondAnswer = input('# ')
        if SecondAnswer == '1':
            print('1')
        elif SecondAnswer == '2':
            print('2')
        elif SecondAnswer == '3':
            print('3')
        else:
            print('----------------------------------------------')
            print('Problem Not Found...')
            print('Please Try Again')
    elif FirstAnswer == '2':
        print('----------------------------------------------')
        print('Promethean Board or Projector Problems')
        print('1) Promethean board not responding to touch with a promethean pen or wand')
        print('2) Nothing being displayed on promethean board')
        print('3) Wrong Screen Displayed')
        print('4) Something Else...')
        SecondAnswer = input('# ')
        if SecondAnswer == '1':
            print('1')
        elif SecondAnswer == '2':
            print('2')
        elif SecondAnswer == '3':
            print('3')
        else:
            print('----------------------------------------------')
            print('Problem Not Found...')
            print('Please Try Again')
    elif FirstAnswer == '3':
        print('----------------------------------------------')
        print('Printer Problems')
        print('1) ')
        print('2) ')
        print('3) ')
        SecondAnswer = input('# ')
        if SecondAnswer == '1':
            print('1')
        elif SecondAnswer == '2':
            print('2')
        elif SecondAnswer == '3':
            print('3')
        else:
            print('----------------------------------------------')
            print('Problem Not Found...')
            print('Please Try Again')
    elif FirstAnswer == '4':
        print('----------------------------------------------')
        print('A Different problem not displayed here...')
        print('Please consult your IT Helpdesk services for more Help')
        print('Put in a ticket at helpdesk.hermiston.k12.or.us or Call IT at #12005')
    else:
        print('----------------------------------------------')
        print('Problem Not Found...')
        print('Please Try Again')

    print('')
    print('1) Other Problems?')
    print('2) Nope Im Done!')
    done = input('# ')
    if done == '2':
        run = False
    elif done == '1':
        print('')
print('Thank you for using BOB-BOT, have a nice Day :)')
time.sleep(4)
quit()
