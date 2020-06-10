import pyautogui, time, pickle, twl
#import pytesseract
#from PIL import ImageGrab, Image
import numpy as np
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.03
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
#start timer
start_time = time.time()
letters = set(['a', 'b', 'c', 'd' 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
#time.sleep(2)

#x
#475 left
#574 right
#584 start of next one

#x3
#top 412

def self_input():
    gridForLetters = np.empty((4, 4), dtype = str)
    user_input = input()
    lettersGrid = user_input.split()
    row1 = lettersGrid[0:4]
    row2 = lettersGrid[4:8]
    row3 = lettersGrid[8:12]
    row4 = lettersGrid[12:16]
    gridForLetters[0] = row1
    gridForLetters[1] = row2
    gridForLetters[2] = row3
    gridForLetters[3] = row4
    return gridForLetters



#bot 509
#start of next one 519

#save 16 images of letter tiles
# =============================================================================
# def screenshot():
#     #Create screenshots of all 16 letters
#     for row in range(0, 4):
#         for col in range(0, 4):
#             img = ImageGrab.grab(bbox=(500 +  109 * row, 443 + 107 * col, 550 + 109 * row, 490 + 107 * col))
#             img.save("C:\PY\laura\\x{}y{}letter.png".format(row, col))
#     #Create full screenshot
#     image = ImageGrab.grab()
#     image.save("C:\PY\laura\\fullscreen.png")
# =============================================================================
    

#convert image tiles to text of images
# =============================================================================
# def converter():
#     global letters
#     #initialize numpy array
#     grid = np.empty((4, 4), dtype = str)
#     for row in range(0, 4):
#         for col in range(0, 4):
#             #open image and perform letter recognition
#             img = Image.open("C:\PY\laura\\x{}y{}letter.png".format(row, col))
#             letter = pytesseract.image_to_string(img, config = " -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 10")
#             print(letter)
#             #fix mistakes from pytesseract
#             if(letter == '[L'):
#                  letter = 'L'
#             elif(letter == 'i' or letter == 'nl' or letter == 'a' or letter == '7'):
#                  letter = 'T'
#             elif(letter == 'l'):
#                   letter = 'I'
#             elif(letter == 'Cc'):
#                 letter = 'C'
#             elif(letter == 'WwW' or letter == 'Ww' or letter == 'wW'):
#                 letter = 'W'
#             elif(letter == 'Oo' or letter == 'oO'):
#                 letter = 'O'
#             elif(letter == ''):
#                 letter = 'I'
#             elif(letter not in letters):
#                 letter = 'T'
#             letter = letter.lower()
#             grid[col][row] = letter
#             np.save('sample grid.npy', grid)
#     return grid
# =============================================================================

#c stands for coordinates
def selectTiles(cString, cDict, seconds):
    #chill if needed
    #time.sleep(0.25)
    #get starting position
    xy = cDict[cString[0]]
    #move to starting position
    pyautogui.moveTo(xy[0], xy[1], seconds)
    #click down
    pyautogui.mouseDown()
    #Do not do anything else if it is only a 1 letter word
    if(len(cString) > 1):
        for letter in range(1, len(cString)):
            xy = cDict[cString[letter]]
            pyautogui.moveTo(xy[0], xy[1], seconds)
    #release mouse
    pyautogui.mouseUp()
    #chill if needed
    #time.sleep(0.25)

#########################################################################################################################
#load letter grid
#grid = np.load('sample grid.npy')
##screenshot()
##grid = converter()
grid = self_input()
print(grid)

#keep track of middle coordinate for every string tested
gridPos = np.empty((4, 4), dtype = str)
gridPos[0][0] = 'A'
gridPos[0][1] = 'B'
gridPos[0][2] = 'C'
gridPos[0][3] = 'D'
gridPos[1][0] = 'E'
gridPos[1][1] = 'F'
gridPos[1][2] = 'G'
gridPos[1][3] = 'H'
gridPos[2][0] = 'I'
gridPos[2][1] = 'J'
gridPos[2][2] = 'K'
gridPos[2][3] = 'L'
gridPos[3][0] = 'M'
gridPos[3][1] = 'N'
gridPos[3][2] = 'O'
gridPos[3][3] = 'P'

#dictionary for gridPos that leads to position
gridPosDict = {
    'A': [525, 461],
    'B': [634, 461],
    'C': [743, 461],
    'D': [852, 461],
    'E': [525, 569],
    'F': [634, 569],
    'G': [743, 569],
    'H': [852, 569],
    'I': [525, 676],
    'J': [634, 676],
    'K': [743, 676],
    'L': [852, 676],
    'M': [525, 783],
    'N': [634, 783],
    'O': [743, 783],
    'P': [852, 783]
    }

#BEGIN
#keep track of times run
times_run = 0
#create word dict
wordDict = {}
#load beginning letters set
beginningLetters = pickle.load(open('beginning letters', 'rb'))



#start recursing, oldString starts as ''
def finder(limit, row, col, oldString = '', oldPos = ''):
    global times_run
    global beginningLetters
    
    #quit if out of bounds
    if(row > 3 or row < 0):
        return
    if(col > 3 or col < 0):
        return 
    #quit if length of string > set number
    if(len(oldString) >= limit):
        return
    #quit if you have already clicked on that tile
    if(gridPos[row][col] in oldPos):
        return
    #quit if u cant lead to a word
    if(len(oldString) < 4):
        if(oldString not in beginningLetters):
            return
        
    #make new string to check
    newString = oldString + grid[row][col]
    #add to oldPos
    newPos = oldPos + gridPos[row][col]

        
    #append word to list if it works
    if(twl.check(newString)):
        wordDict[newString] = newPos


        
    #check
    #print(newString)

    times_run = times_run + 1
    #call 8 functions, start with right
    finder(limit, row, col + 1, newString, newPos)
    #reset oldString
    oldString = ''
    oldPos = ''
    #down right 
    finder(limit, row + 1, col + 1, newString, newPos)
    oldString = ''
    oldPos = ''
    #down
    finder(limit, row + 1, col, newString, newPos)
    oldString = ''
    oldPos = ''
    #down left
    finder(limit, row + 1, col - 1, newString, newPos)
    oldString = ''
    oldPos = ''
    #left
    finder(limit, row, col - 1, newString, newPos)
    oldString = ''
    oldPos = ''
    #left up
    finder(limit, row - 1, col - 1, newString, newPos)
    oldString = ''
    oldPos = ''
    #up
    finder(limit, row - 1, col, newString, newPos)
    oldString = ''
    oldPos = ''
    #up right
    finder(limit, row - 1, col + 1, newString, newPos)






#find starting everywhere    
for row in range(0, 4):
    for col in range(0, 4):
        finder(9, row, col)

#sort word dict by longest words first
wordList = sorted(wordDict, key = len, reverse = True)
print('The Word List sorted by length is:')
print(wordList)
print('The Length of the Word Dictionary is:')
print(len(wordDict))
print('Times Run:')
print(times_run)
#print time
print(time.time() - start_time)

for word in wordList:
    lookup = wordDict[word]
    selectTiles(lookup, gridPosDict, 0.05)
    if((time.time() - start_time) >= 83):
        break
#do it again incase of errors
for word in wordList:
    lookup = wordDict[word]
    selectTiles(lookup, gridPosDict, 0.05)
    if((time.time() - start_time) >= 83):
        break
#do it again incase of errors
for word in wordList:
    lookup = wordDict[word]
    selectTiles(lookup, gridPosDict, 0.05)
    if((time.time() - start_time) >= 83):
        break

                                               
