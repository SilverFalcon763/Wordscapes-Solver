from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import os
import random
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import json
from itertools import combinations
from pathlib import Path

directory = Path(__file__).absolute().parent

def join(given):
    path = os.path.join(directory, given)
    return path


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.5)
    pyautogui.mouseUp(button='left')


def isWordscapes():
    if pyautogui.locateOnScreen(join('wordscapes.png'), confidence = 0.8) != None:
        return True
    else:
        return False


def blueStacksOpen():
    if pyautogui.locateOnScreen(join('blueStacks.png'), confidence = 0.8) != None:
       return True
    else:
        return False


def startGame():
    buttonLocation = pyautogui.locateOnScreen(join('levelButton.png'), grayscale = True, confidence=0.85)
    if buttonLocation is not None:
        x, y = pyautogui.center(buttonLocation)
        click(x, y)


def getGuesses(letters, lengths):
    guesses = []
    path = join('dictionary.json')
    with open(path) as json_dictionary: 
        dictionary = json.load(json_dictionary)
    for word in dictionary:
        if any(lengths) > 0: 
            for length, count in enumerate(lengths, start=3): 
                if count > 0 and len(word) == length:  
                    for r in range(1, length + 1): 
                        for combination in combinations(letters, r):
                            if ''.join(combination) in word:  
                                guesses.append(word)
                                break   
    return guesses


def clean(words, given_letters):
    filteredWords = []
    for word in words:
        if all(letter in given_letters for letter in word) and len(set(word)) == len(word):
            filteredWords.append(word)
    return filteredWords

def removeDuplicates(words):
    sortedWords = []
    for word in words:
        if word not in sortedWords:
            sortedWords.append(word)
    return sortedWords


def sortLetters(letters):
    result = [] 

    for i in letters: 
        if i not in result: 
            result.append(i) 

    return result;

    
def inGame():
    if pyautogui.locateOnScreen(os.path.join(directory, 'ingame.png'), confidence = 0.8) != None:
        return True
    else:
        return False


def getWordLengths():
    threeLetters = 0
    fourLetters = 0
    fiveLetters = 0
    sixLetters = 0
    sevenLetters = 0
    board = pyautogui.screenshot()
    board = cv.cvtColor(np.array(board), cv.COLOR_RGB2BGR)
    cv.imwrite(join('board.png'), board)

    board = cv.imread(join('board.png'))
    board_gray = cv.cvtColor(board, cv.COLOR_BGR2GRAY)
    assert board_gray is not None, "file could not be read, check with os.path.exists()"

    # Load template images
    templates = {
        'threeLetters': [
            join('threeLettersHW.png'),
            join('threeLettersHB.png'),
            join('threeLettersVW.png'),
            join('threeLettersVB.png'),
            join('threeBonusHW.png'),
        ],
        'fourLetters': [
            join('fourLettersHB.png'),
            join('fourLettersHW.png'),
            join('fourLettersVW.png'),
            join('fourLettersVB.png'),
            join('fourBonusHW.png'),
            join('fourBonusVW.png'),
            join('fourBonusHB.png'),
        ],
        'fiveLetters': [
            join('fiveLettersHW.png'),
            join('fiveLettersVW.png'),
            join('fiveLettersVB.png'),
            join('fiveLettersHB.png'),
        ]
    }

    for length, images in templates.items():
        for image_path in images:
            template = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
            assert template is not None, f"Template {image_path} could not be read"
            w, h = template.shape[::-1]
            res = cv.matchTemplate(board_gray, template, cv.TM_CCOEFF_NORMED)
            threshold = 0.4
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                if length == 'threeLetters':
                    threeLetters += 1
                elif length == 'fourLetters':
                    fourLetters += 1
                elif length == 'fiveLetters':
                    fiveLetters += 1

 
    if threeLetters > 0:
        threeLetters = 1
    if fourLetters > 0:
        fourLetters = 1
    if fiveLetters > 0:
        fiveLetters = 1

    foundWordLengths = [threeLetters, fourLetters, fiveLetters, sixLetters, sevenLetters]
    return foundWordLengths


def getLetters():
    found_letters = []
    board = pyautogui.screenshot()
    board = cv.cvtColor(np.array(board), cv.COLOR_RGB2GRAY)
 
    templates = {
        'a':[
                
                cv.imread(join('awhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('ablack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'b':[
                cv.imread(join('bwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('bblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'c':[
                cv.imread(join('cwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('cblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'd':[
                cv.imread(join('dwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('dblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'e':[
                cv.imread(join('ewhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('eblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'f':[
                cv.imread(join('fwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('fblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'g':[
                cv.imread(join('gwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('gblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'h':[
                cv.imread(join('hwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('hblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'i':[
                cv.imread(join('iwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('iblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'j':[
                ##cv.imread(join('jwhite.png'), cv.IMREAD_GRAYSCALE),
                ##cv.imread(join('jblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'k':[
                cv.imread(join('kwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('kblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'l':[
                cv.imread(join('lwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('lblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'm':[
                ##cv.imread(join('mwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('mblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'n':[
                cv.imread(join('nwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('nblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'o':[
                cv.imread(join('owhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('oblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'p':[
                cv.imread(join('pwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('pblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'q':[
                ##cv.imread(join('qwhite.png'), cv.IMREAD_GRAYSCALE),
                ##cv.imread(join('qblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'r':[
                cv.imread(join('rwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('rblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        's':[
                cv.imread(join('swhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('sblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        't':[
                cv.imread(join('twhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('tblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'u':[
                ##cv.imread(join('uwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('ublack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'v':[
                ##cv.imread(join('vwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('vblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'w':[
                cv.imread(join('wwhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('wblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'x':[
                ##cv.imread(join('xwhite.png'), cv.IMREAD_GRAYSCALE),
                ##cv.imread(join('xblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'y':[
                cv.imread(join('ywhite.png'), cv.IMREAD_GRAYSCALE),
                cv.imread(join('yblack.png'), cv.IMREAD_GRAYSCALE),
            ],
        'z':[
                ##cv.imread(join('zwhite.png'), cv.IMREAD_GRAYSCALE),
                ##cv.imread(join('zblack.png'), cv.IMREAD_GRAYSCALE),
            ]
    }

    for letter, templates_list in templates.items():
        assert templates_list is not None, f"Template for letter '{letter}' could not be read"
        for template in templates_list:
            w, h = template.shape[::-1]
            res = cv.matchTemplate(board, template, cv.TM_CCOEFF_NORMED)
            threshold = 0.9
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                found_letters.append(letter)
    return found_letters


def guess(guesses):
    if(pyautogui.locateOnScreen(os.path.join(directory, 'awhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'bwhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'cwhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'dwhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'ewhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'fwhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'gwhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'hwhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'iwhite.png'), grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(os.path.join(directory, 'jwhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'kwhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'lwhite.png'), grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(os.path.join(directory, 'mwhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'nwhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'owhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'pwhite.png'), grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(os.path.join(directory, 'qwhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'rwhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'swhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'twhite.png'), grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(os.path.join(directory, 'uwhite.png'), grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(os.path.join(directory, 'vwhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'wwhite.png'), grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(os.path.join(directory, 'xwhite.png'), grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(os.path.join(directory, 'ywhite.png'), grayscale=True, confidence=0.85) != None
       ##pyautogui.locateOnScreen(os.path.join(directory, 'zwhite.png'), grayscale=True, confidence=0.85) != None
       ):

        
        letter_paths = {
            'a': os.path.join(directory, 'awhite.png'),
            'b': os.path.join(directory, 'bwhite.png'),
            'c': os.path.join(directory, 'cwhite.png'),
            'd': os.path.join(directory, 'dwhite.png'),
            'e': os.path.join(directory, 'ewhite.png'),
            'f': os.path.join(directory, 'fwhite.png'),
            'g': os.path.join(directory, 'gwhite.png'),
            'h': os.path.join(directory, 'hwhite.png'),
            'i': os.path.join(directory, 'iwhite.png'),
            ##'j': os.path.join(directory, 'jwhite.png'),
            'k': os.path.join(directory, 'kwhite.png'),
            'l': os.path.join(directory, 'lwhite.png'),
            ##'m': os.path.join(directory, 'mwhite.png'),
            'n': os.path.join(directory, 'nwhite.png'),
            'o': os.path.join(directory, 'owhite.png'),
            'p': os.path.join(directory, 'pwhite.png'),
            ##'q': os.path.join(directory, 'qwhite.png'),
            'r': os.path.join(directory, 'rwhite.png'),
            's': os.path.join(directory, 'swhite.png'),
            't': os.path.join(directory, 'twhite.png'),
            ##'u': os.path.join(directory, 'uwhite.png'),
            ##'v': os.path.join(directory, 'vwhite.png'),
            'w': os.path.join(directory, 'wwhite.png'),
            ##'x': os.path.join(directory, 'xwhite.png'),
            'y': os.path.join(directory, 'ywhite.png'),
            ##'z': os.path.join(directory, 'zwhite.png'),
        }
        for word in guesses:
            print("Checking word:", word)
            guess = [letter for letter in word]
            if pyautogui.locateOnScreen(join('ads.png'), grayscale=True, confidence=0.85):
                win32api.SetCursorPos((1201, 729))
            else:
                win32api.SetCursorPos((1201, 722))
            pyautogui.mouseDown(button='left')  
            found_word = True  
            for letter in guess:
                if letter in letter_paths:
                    letter_path = letter_paths[letter]
                    if pyautogui.locateOnScreen(letter_path, grayscale=True, confidence=0.85) is None:
                        print(letter, "not found!")
                        found_word = False
                        break 
                    else:
                        print(letter, "found!")
                        letterLocation = pyautogui.locateCenterOnScreen(letter_path, grayscale=True, confidence=0.85)
                        pyautogui.moveTo(letterLocation)
            if found_word:
                pyautogui.mouseUp(button='left')
        time.sleep(0.5)
    else:
        letter_paths = {
            'a': os.path.join(directory, 'ablack.png'),
            'b': os.path.join(directory, 'bblack.png'),
            'c': os.path.join(directory, 'cblack.png'),
            'd': os.path.join(directory, 'dblack.png'),
            'e': os.path.join(directory, 'eblack.png'),
            'f': os.path.join(directory, 'fblack.png'),
            'g': os.path.join(directory, 'gblack.png'),
            'h': os.path.join(directory, 'hblack.png'),
            'i': os.path.join(directory, 'iblack.png'),
            ##'j': os.path.join(directory, 'jblack.png'),
            'k': os.path.join(directory, 'kblack.png'),
            'l': os.path.join(directory, 'lblack.png'),
            'm': os.path.join(directory, 'mblack.png'),
            'n': os.path.join(directory, 'nblack.png'),
            'o': os.path.join(directory, 'oblack.png'),
            'p': os.path.join(directory, 'pblack.png'),
            ##'q': os.path.join(directory, 'qblack.png'),
            'r': os.path.join(directory, 'rblack.png'),
            's': os.path.join(directory, 'sblack.png'),
            't': os.path.join(directory, 'tblack.png'),
            'u': os.path.join(directory, 'ublack.png'),
            'v': os.path.join(directory, 'vblack.png'),
            'w': os.path.join(directory, 'wblack.png'),
            ##'x': os.path.join(directory, 'xblack.png'),
            'y': os.path.join(directory, 'yblack.png'),
            ##'z': os.path.join(directory, 'zblack.png'),
        }

        for word in guesses:
            print("Checking word:", word)
            guess = [letter for letter in word]
            if pyautogui.locateOnScreen(join('ads.png'), grayscale=True, confidence=0.85):
                win32api.SetCursorPos((1201, 725))
            else:
                win32api.SetCursorPos((1201, 722))
            pyautogui.mouseDown(button='left')  
            found_word = True  
            for letter in guess:
                if letter in letter_paths:
                    letter_path = letter_paths[letter]
                    if pyautogui.locateOnScreen(letter_path, grayscale=True, confidence=0.85) is None:
                        print(letter, "not found!")
                        found_word = False
                        break
                    else:
                        print(letter, "found!")
                        letterLocation = pyautogui.locateCenterOnScreen(letter_path, grayscale=True, confidence=0.85)
                        pyautogui.moveTo(letterLocation)
            if found_word:
                pyautogui.mouseUp(button='left')
        time.sleep(0.5)


time.sleep(5)
while True:
    if blueStacksOpen():
        if isWordscapes():
            print("isWordscapes")
            startGame()
            time.sleep(2)
            foundLetters = getLetters()
            sortedLetters = sortLetters(foundLetters)
            foundWordLengths = getWordLengths()
            print(sortedLetters)
            print(foundWordLengths)
            guesses = getGuesses(sortedLetters, foundWordLengths)
            guesses = clean(guesses, sortedLetters)
            guesses = removeDuplicates(guesses)
            print (guesses)
            guess(guesses)
            time.sleep(5)






