import pyautogui as pag 
import random
import time 

while True: #infinite loop here!
    x=random.randint(600,700) # gives a random coordinate between the range 600 and 700
    y=random.randint(200,600) # gives a random coordinate between the range 200 and 600

    pag.moveTo(x,y,0.5)
    #this function mentiones the coordinates in pixels of where the mouse should go and 0.5 is the speed of the cursor. It can be changed
    #since we have given x between 600-700 and y between 200-600, the mouse will only move in a small section of the display.
    #to make it move whole display, we can change the range of x and y to (0,1920) for x and (0,1080) for y [FOR A 1080p RESOLUTION MONITOR]

    time.sleep(1) #sleep it so that it does not look so crazy, LOL