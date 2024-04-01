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

time.sleep(2.0)

class Word:
    def __init__(length, direction):
        self.length = length 		#int
        self.direction = direction		#string

    def getLength(self):
        return self.length	

    def getDirection(self):
        return self.direction

        
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def isWordscapes():
    if pyautogui.locateOnScreen('wordscapes.png', confidence = 0.8) != None:
        return True
    else:
        return False


def blueStacksOpen():
    if pyautogui.locateOnScreen('blueStacks.png', confidence = 0.8) != None:
       return True
    else:
        return False





    
def startGame():
    buttonLocation = pyautogui.locateOnScreen('levelButton.png', grayscale = True, confidence=0.85)
    if buttonLocation is not None:
        x, y = pyautogui.center(buttonLocation)
        click(x, y)


def sort(words, size): 
    return [word for word in words if len(word) == size]


def getGuessesLetters(letters, lengths):
    guesses = []
    
    with open('dictionary.json') as json_dictionary: 
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

def getWordLengths():
    threeLetters = 0
    fourLetters = 0
    fiveLetters = 0
    sixLetters = 0
    sevenLetters = 0

    board = pyautogui.screenshot()
    board = cv.cvtColor(np.array(board), cv.COLOR_RGB2BGR)
    cv.imwrite("board.png", board)

    board = cv.imread('board.png')
    board_gray = cv.cvtColor(board, cv.COLOR_BGR2GRAY)
    assert board_gray is not None, "file could not be read, check with os.path.exists()"

    # Load template images
    templates = {
        'threeLetters': [
            r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\wordlengths\threeLettersHW.png',
            r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\wordlengths\threeLettersHB.png',
            r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\wordlengths\threeLettersVW.png',
            r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\wordlengths\threeLettersVB.png',
            r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\wordlengths\threeBonusHW.png'
        ],
        'fourLetters': [
            r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\wordlengths\fourLettersHB.png',
            r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\wordlengths\fourLettersHW.png',
            r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\wordlengths\fourLettersVW.png',
            r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\wordlengths\fourLettersVB.png',
            r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\wordlengths\fourBonusHW.png',
            r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\wordlengths\fourBonusVW.png'
        ],
        'fiveLetters': [
            r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\wordlengths\fiveLettersHW.png',
            r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\wordlengths\fiveLettersVW.png'
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
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\awhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ablack.png', cv.IMREAD_GRAYSCALE)
            ],
        'b':[
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\bwhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\bblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'c':[
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\cwhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\cblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'd':[
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\dwhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\dblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'e':[
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ewhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\eblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'f':[
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\fwhite.png', cv.IMREAD_GRAYSCALE),
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\fblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'g':[
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\gwhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\gblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'h':[
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\hwhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\hblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'i':[
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\iwhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\iblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'j':[
                ## cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\jwhite.png', cv.IMREAD_GRAYSCALE),
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\jblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'k':[
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\kwhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\kblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'l':[
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\lwhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\lblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'm':[
                ## cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\mwhite.png', cv.IMREAD_GRAYSCALE),
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\mblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'n':[
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\nwhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\nblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'o':[
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\owhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\oblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'p':[
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\pwhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\pblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'q':[
                ## cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\qwhite.png', cv.IMREAD_GRAYSCALE),
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\qblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'r':[
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\rwhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\rblack.png', cv.IMREAD_GRAYSCALE),
            ],
        's':[
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\swhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\sblack.png', cv.IMREAD_GRAYSCALE),
            ],
        't':[
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\twhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\tblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'u':[
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\uwhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ublack.png', cv.IMREAD_GRAYSCALE),
            ],
        'v':[
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\vwhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\vblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'w':[
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\wwhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\wblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'x':[
                ## cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\xwhite.png', cv.IMREAD_GRAYSCALE),
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\xblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'y':[
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ywhite.png', cv.IMREAD_GRAYSCALE),
                cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\yblack.png', cv.IMREAD_GRAYSCALE),
            ],
        'z':[
                ## cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\zwhite.png', cv.IMREAD_GRAYSCALE),
                ##cv.imread(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\zblack.png', cv.IMREAD_GRAYSCALE),
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



def sortLetters(letters):
    result = [] 

    for i in letters: 
        if i not in result: 
            result.append(i) 

    return result;

    
def inGame():
    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\ingame.png', confidence = 0.8) != None:
        return True
    else:
        return False


def guess(guesses):
    if(pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\awhite.png', grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\bwhite.png', grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\cwhite.png', grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\dwhite.png', grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ewhite.png', grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\fwhite.png', grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\gwhite.png', grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\hwhite.png', grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\iwhite.png', grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\jwhite.png', grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\kwhite.png', grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\lwhite.png', grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\mwhite.png', grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\nwhite.png', grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\owhite.png', grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\pwhite.png', grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\qwhite.png', grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\rwhite.png', grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\swhite.png', grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\twhite.png', grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\uwhite.png', grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\vwhite.png', grayscale=True, confidence=0.85) != None or
       pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\wwhite.png', grayscale=True, confidence=0.85) != None
       ##pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\xwhite.png', grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ywhite.png', grayscale=True, confidence=0.85) != None or
       ##pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\zwhite.png', grayscale=True, confidence=0.85) != None
       ):
        for word in guesses:
            guess = []
            c = 0
            guess = [letter for letter in word]
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            time.sleep(1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            for letter in guess:
                if c < (len(word) - 1):
                    print("run")
                    if letter == 'a':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\awhite.png', grayscale=True, confidence=0.85) != None:
                            print("awhite")
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\awhite.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                            
                        else:
                            pass
                        
                        
                    elif letter == 'b':
                        #elif pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\bwhite.png', grayscale=True, confidence=0.85) != None:
                            #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\bwhite.png', grayscale=True, confidence=0.85)
                            #x,y = pyautogui.center(letterLocation)
                            #win32api.SetCursorPos((x,y))
                            #c += 1
                        #else:
                        pass
                        
                        
                        
                    elif letter == 'c':
                        #elif pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\cwhite.png', grayscale=True, confidence=0.85) != None:
                            #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\cwhite.png', grayscale=True, confidence=0.85)
                            #x,y = pyautogui.center(letterLocation)
                            #win32api.SetCursorPos((x,y))
                            #c += 1
                        #else:
                        pass
                        
                        
                        
                    elif letter == 'd':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\dwhite.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\dwhite.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'e':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ewhite.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ewhite.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'f':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\fwhite.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\fwhite.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'g':
                        #elif pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\gwhite.png', grayscale=True, confidence=0.85) != None:
                            #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\gwhite.png', grayscale=True, confidence=0.85)
                            #x,y = pyautogui.center(letterLocation)
                            #win32api.SetCursorPos((x,y))
                            #c += 1
                        #else:
                        pass
                        
                        
                        
                    elif letter == 'h':
                        #elif pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\hwhite.png', grayscale=True, confidence=0.85) != None:
                            #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\hwhite.png', grayscale=True, confidence=0.85)
                            #x,y = pyautogui.center(letterLocation)
                            #win32api.SetCursorPos((x,y))
                            #c += 1
                        #else:
                        pass
                        
                        
                        
                    elif letter == 'i':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\iwhite.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\iwhite.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'j':
                        #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\jwhite.png', grayscale=True, confidence=0.85)
                        #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\jblack.png', grayscale=True, confidence=0.85)
                        #x,y = pyautogui.center(letterLocation)
                        #win32api.SetCursorPos((x,y))
                        pass
                    elif letter == 'k':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\kwhite.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\kwhite.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'l':
                        #elif pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\lwhite.png', grayscale=True, confidence=0.85) != None:
                            #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\lwhite.png', grayscale=True, confidence=0.85)
                            #x,y = pyautogui.center(letterLocation)
                            #win32api.SetCursorPos((x,y))
                            #c += 1
                        #else:
                        pass
                        
                        
                        
                    elif letter == 'm':
                        #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\mwhite.png', grayscale=True, confidence=0.85)
                        #x,y = pyautogui.center(letterLocation)
                        #win32api.SetCursorPos((x,y))
                        pass
                    elif letter == 'n':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\nwhite.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\nwhite.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'o':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\owhite.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\owhite.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'p':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\pwhite.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\pwhite.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'q':
                        #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\qwhite.png', grayscale=True, confidence=0.85)
                        #x,y = pyautogui.center(letterLocation)
                        #win32api.SetCursorPos((x,y))
                        pass
                    elif letter == 'r':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\rwhite.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\rwhite.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 's':
                        #elif pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\swhite.png', grayscale=True, confidence=0.85) != None:
                            #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\swhite.png', grayscale=True, confidence=0.85)
                            #x,y = pyautogui.center(letterLocation)
                            #win32api.SetCursorPos((x,y))
                            #c += 1
                        #else:
                        pass
                        
                        
                        
                    elif letter == 't':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\twhite.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\twhite.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'u':
                        #elif pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\uwhite.png', grayscale=True, confidence=0.85) != None:
                            #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\uwhite.png', grayscale=True, confidence=0.85)
                            #x,y = pyautogui.center(letterLocation)
                            #win32api.SetCursorPos((x,y))
                            #c += 1
                        #else:
                        pass
                        
                        
                        
                    elif letter == 'v':
                        #elif pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\vwhite.png', grayscale=True, confidence=0.85) != None:
                            #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\vwhite.png', grayscale=True, confidence=0.85)
                            #x,y = pyautogui.center(letterLocation)
                            #win32api.SetCursorPos((x,y))
                            #c += 1
                        #else:
                        pass
                        
                        
                        
                    elif letter == 'w':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\wwhite.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\wwhite.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'x':
                        #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\xwhite.png', grayscale=True, confidence=0.85)
                        #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\xblack.png', grayscale=True, confidence=0.85)
                        #x,y = pyautogui.center(letterLocation)
                        #win32api.SetCursorPos((x,y))
                        pass
                    elif letter == 'y':
                        #if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ywhite.png', grayscale=True, confidence=0.85) != None:
                            #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ywhite.png', grayscale=True, confidence=0.85)
                            #x,y = pyautogui.center(letterLocation)
                            #win32api.SetCursorPos((x,y))
                            #c += 1
                        #else:
                        pass
                        
                        
                        
                    elif letter == 'z':
                        #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\zwhite.png', grayscale=True, confidence=0.85)
                        #x,y = pyautogui.center(letterLocation)
                        #win32api.SetCursorPos((x,y))
                        pass
                
            else:
                print("run3")
                if letter == 'a':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\awhite.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\awhite.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        print("run2")
                        c += 1
                    else:
                        pass
                    
                elif letter == 'b':
##                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\bwhite.png', grayscale=True, confidence=0.85) != None:
##                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\bwhite.png', grayscale=True, confidence=0.85)
##                        x,y = pyautogui.center(letterLocation)
##                        win32api.SetCursorPos((x,y))
##                        time.sleep(0.5)
##                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
##                        c += 1
##                    else:
                    pass
                    
                elif letter == 'c':
##                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\cwhite.png', grayscale=True, confidence=0.85) != None:
##                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\cwhite.png', grayscale=True, confidence=0.85)
##                        x,y = pyautogui.center(letterLocation)
##                        win32api.SetCursorPos((x,y))
##                        time.sleep(0.5)
##                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
##                    else:
                    pass
                    
                elif letter == 'd':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\dwhite.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\dwhite.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        
                    else:
                        pass
                    
                elif letter == 'e':    
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ewhite.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ewhite.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        
                    else:
                        pass
                    
                elif letter == 'f':     
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\fwhite.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\fwhite.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)    
                    else:
                        pass
                    
                elif letter == 'g':
##                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\gwhite.png', grayscale=True, confidence=0.85) != None:
##                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\gwhite.png', grayscale=True, confidence=0.85)
##                        x,y = pyautogui.center(letterLocation)
##                        win32api.SetCursorPos((x,y))
##                        time.sleep(0.5)
##                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
##                    else:
                    pass
                    
                elif letter == 'h':
##                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\hwhite.png', grayscale=True, confidence=0.85) != None:
##                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\hwhite.png', grayscale=True, confidence=0.85)
##                        x,y = pyautogui.center(letterLocation)
##                        win32api.SetCursorPos((x,y))
##                        time.sleep(0.5)
##                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
##                    else:
                    pass
                    
                elif letter == 'i':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\iwhite.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\iwhite.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        
                    else:
                        pass
                    
                elif letter == 'j':
                    #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\jwhite.png', grayscale=True, confidence=0.85)
                    #x,y = pyautogui.center(letterLocation)
                    #win32api.SetCursorPos((x,y))
                    pass
                elif letter == 'k':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\kwhite.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\kwhite.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        
                    else:
                        pass
                    
                elif letter == 'l':
##                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\lwhite.png', grayscale=True, confidence=0.85) != None:
##                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\lwhite.png', grayscale=True, confidence=0.85)
##                        x,y = pyautogui.center(letterLocation)
##                        win32api.SetCursorPos((x,y))
##                        time.sleep(0.5)
##                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
##                    else:
                    pass
                    
                elif letter == 'm':
                    #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\mwhite.png', grayscale=True, confidence=0.85)
                    #x,y = pyautogui.center(letterLocation)
                    #win32api.SetCursorPos((x,y))
                    pass
                elif letter == 'n':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\nwhite.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\nwhite.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 'o':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\owhite.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\owhite.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        
                    else:
                        pass
                    
                elif letter == 'p':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\pwhite.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\pwhite.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        
                    else:
                        pass
                    
                elif letter == 'q':
                    #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\qwhite.png', grayscale=True, confidence=0.85)
                    #x,y = pyautogui.center(letterLocation)
                    #win32api.SetCursorPos((x,y))
                    pass
                elif letter == 'r':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\rwhite.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\rwhite.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 's':
##                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\swhite.png', grayscale=True, confidence=0.85) != None:
##                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\swhite.png', grayscale=True, confidence=0.85)
##                        x,y = pyautogui.center(letterLocation)
##                        win32api.SetCursorPos((x,y))
##                        time.sleep(0.5)
##                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
##                    else:
                    pass
                    
                elif letter == 't':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\twhite.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\twhite.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 'u':
##                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\uwhite.png', grayscale=True, confidence=0.85) != None:
##                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\uwhite.png', grayscale=True, confidence=0.85)
##                        x,y = pyautogui.center(letterLocation)
##                        win32api.SetCursorPos((x,y))
##                        time.sleep(0.5)
##                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
##                    else:
                    pass
                    
                elif letter == 'v':
##                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\vwhite.png', grayscale=True, confidence=0.85) != None:
##                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\vwhite.png', grayscale=True, confidence=0.85)
##                        x,y = pyautogui.center(letterLocation)
##                        win32api.SetCursorPos((x,y))
##                        time.sleep(0.5)
##                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
##                    else:
                    pass
                    
                elif letter == 'w':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\wwhite.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\wwhite.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 'x':
                    #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\xwhite.png', grayscale=True, confidence=0.85)
                    #x,y = pyautogui.center(letterLocation)
                    #win32api.SetCursorPos((x,y))
                    pass
                elif letter == 'y':
##                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ywhite.png', grayscale=True, confidence=0.85) != None:
##                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ywhite.png', grayscale=True, confidence=0.85)
##                        x,y = pyautogui.center(letterLocation)
##                        win32api.SetCursorPos((x,y))
##                        time.sleep(0.5)
##                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
##                    else:
                    pass
                    
                elif letter == 'z':
                    #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\zwhite.png', grayscale=True, confidence=0.85)
                    #x,y = pyautogui.center(letterLocation)
                    #win32api.SetCursorPos((x,y))
                    pass
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    else:
        for word in guesses:
            guess = []
            c = 0
            guess = [letter for letter in word]
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            time.sleep(1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            for letter in guess:
                if c <= (len(word) - 1):
                    print("run")
                    if letter == 'a':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ablack.png', grayscale=True, confidence=0.85) != None:
                            print("ablack")
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ablack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                            
                        else:
                            pass
                        
                        
                    elif letter == 'b':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\bblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\bblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'c':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\cblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\cblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'd':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\dblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\dblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'e':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\eblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\eblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'f':
##                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\fblack.png', grayscale=True, confidence=0.85) != None:
##                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\fblack.png', grayscale=True, confidence=0.85)
##                            x,y = pyautogui.center(letterLocation)
##                            win32api.SetCursorPos((x,y))
##                            c += 1
##                        else:
                        pass
                        
                        
                        
                    elif letter == 'g':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\gblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\gblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'h':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\hblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\hblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'i':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\iblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\iblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'j':
                        #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\jblack.png', grayscale=True, confidence=0.85)
                        #x,y = pyautogui.center(letterLocation)
                        #win32api.SetCursorPos((x,y))
                        pass
                    elif letter == 'k':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\kblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\kblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'l':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\lblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\lblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'm':
                        #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\mblack.png', grayscale=True, confidence=0.85)
                        #x,y = pyautogui.center(letterLocation)
                        #win32api.SetCursorPos((x,y))
                        pass
                    elif letter == 'n':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\nblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\nblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'o':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\oblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\oblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'p':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\pblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\pblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'q':
                        #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\qblack.png', grayscale=True, confidence=0.85)
                        #x,y = pyautogui.center(letterLocation)
                        #win32api.SetCursorPos((x,y))
                        pass
                    elif letter == 'r':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\rblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\rblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 's':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\sblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\sblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 't':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\tblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\tblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'u':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ublack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ublack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'v':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\vblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\vblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'w':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\wblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\wblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'x':
                        #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\xblack.png', grayscale=True, confidence=0.85)
                        #x,y = pyautogui.center(letterLocation)
                        #win32api.SetCursorPos((x,y))
                        pass
                    elif letter == 'y':
                        if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\yblack.png', grayscale=True, confidence=0.85) != None:
                            letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\yblack.png', grayscale=True, confidence=0.85)
                            x,y = pyautogui.center(letterLocation)
                            win32api.SetCursorPos((x,y))
                            c += 1
                        else:
                            pass
                        
                        
                        
                    elif letter == 'z':
                        #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\zblack.png', grayscale=True, confidence=0.85)
                        #x,y = pyautogui.center(letterLocation)
                        #win32api.SetCursorPos((x,y))
                        pass
                
            else:
                print("run3")
                if letter == 'a':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ablack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ablack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        print("run2")
                        c += 1
                    else:
                        pass
                    
                elif letter == 'b':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\bblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\bblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        c += 1
                    else:
                        pass
                    
                elif letter == 'c':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\cblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\cblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        print("runc")
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 'd':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\dblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\dblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        
                    else:
                        pass
                    
                elif letter == 'e':    
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\eblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\eblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        
                    else:
                        pass
                    
                elif letter == 'f':     
##                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\fblack.png', grayscale=True, confidence=0.85) != None:
##                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\fblack.png', grayscale=True, confidence=0.85)
##                        x,y = pyautogui.center(letterLocation)
##                        win32api.SetCursorPos((x,y))
##                        time.sleep(0.5)
##                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)    
##                    else:
                    pass
                    
                elif letter == 'g':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\gblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\gblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 'h':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\hblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\hblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 'i':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\iblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\iblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        
                    else:
                        pass
                    
                elif letter == 'j':
                    #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\jblack.png', grayscale=True, confidence=0.85)
                    #x,y = pyautogui.center(letterLocation)
                    #win32api.SetCursorPos((x,y))
                    pass
                elif letter == 'k':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\kblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\kblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        
                    else:
                        pass
                    
                elif letter == 'l':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\lblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\lblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 'm':
                    #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\mblack.png', grayscale=True, confidence=0.85)
                    #x,y = pyautogui.center(letterLocation)
                    #win32api.SetCursorPos((x,y))
                    pass
                elif letter == 'n':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\nblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\nblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 'o':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\oblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\oblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        
                    else:
                        pass
                    
                elif letter == 'p':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\pblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\pblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        
                    else:
                        pass
                    
                elif letter == 'q':
                    #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\qblack.png', grayscale=True, confidence=0.85)
                    #x,y = pyautogui.center(letterLocation)
                    #win32api.SetCursorPos((x,y))
                    pass
                elif letter == 'r':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\rblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\rblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 's':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\sblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\sblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 't':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\tblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\tblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 'u':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ublack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\ublack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 'v':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\vblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\vblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 'w':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\wblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\wblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 'x':
                    #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\xblack.png', grayscale=True, confidence=0.85)
                    #x,y = pyautogui.center(letterLocation)
                    #win32api.SetCursorPos((x,y))
                    pass
                elif letter == 'y':
                    if pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\yblack.png', grayscale=True, confidence=0.85) != None:
                        letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\yblack.png', grayscale=True, confidence=0.85)
                        x,y = pyautogui.center(letterLocation)
                        win32api.SetCursorPos((x,y))
                        time.sleep(0.5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    else:
                        pass
                    
                elif letter == 'z':
                    #letterLocation = pyautogui.locateOnScreen(r'C:\Users\roryc\OneDrive\Desktop\Wordscape Solver\letters\zblack.png', grayscale=True, confidence=0.85)
                    #x,y = pyautogui.center(letterLocation)
                    #win32api.SetCursorPos((x,y))
                    pass
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
           

            

time.sleep(5)
if blueStacksOpen():
    if isWordscapes():
        print("isWordscapes")
        startGame()
        ##if inGame():
        time.sleep(5)
        foundLetters = getLetters()
        sortedLetters = sortLetters(foundLetters)
        foundWordLengths = getWordLengths()
        print(sortedLetters)
        print(foundWordLengths)
        guesses = getGuessesLetters(sortedLetters, foundWordLengths)
        guesses = clean(guesses, sortedLetters)
        guesses = removeDuplicates(guesses)
        print (guesses)
        guess(guesses)


            



