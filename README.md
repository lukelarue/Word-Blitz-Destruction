# Word-Blitz-Destruction
Kill Word Blitz

#outside packages used are pyautogui, twl, numpy -- twl checks if a word is in the scrabble dictionary 
#download twl from https://github.com/fogleman/TWL06

#this was made in July 2019 and I decided to upload it here. I am a total github noob obviously.
#my screen specs are 1536x864, if yours is different you need to change the A-P positions (coordinates) in gridPosDict

#My coordinates only work if you have 1536x864 AND you open wordblitz from facebook messages on facebook website so the screen is altered
#when you open wordblitz from facebook messages on the site, a white screen appears on the right side, this pushes the wordblitz
#screen to a different position, and this is how I play and have my coordinates set up.

#I initially used pytesseract and screengrabs to use image recognition and automatically generate the 4x4 grid to my program, but it
#only correctly identified the letter like 90% of the time even with all the tinkering I did, so I just commented it all out

#to generate the letters, you type them in from left to right, then down to next row and left to right, etc, with one space between
#for instance if the grid looks like a b c d
#                                    e f g h
#                                    i j k l
#                                    m n o p
#then immediately after the program starts you type a b c d e f g h i j k l m n o p
#and hit enter, it takes anywhere from 10-30 seconds depending on how many words it can find, then it goes crazy and gets u 1000s of pts