from pyautogui import locateCenterOnScreen, ImageNotFoundException, click, doubleClick, moveTo, locateOnScreen
from time import sleep
from os import listdir
from constants import *

#pip install pyautogui
#pip install opencv_python

"""got a collect key"""
#close notification
#collect button
#setting locate on screen confidence to .5 will allow to collect jumping images
#this could mean lighting tourches

# first open the game, wait close button to be on screen
#if not already in game open it from desktop else throw error

# isFoodCollected = False


def findClick(image, time = .5, confidence = .7):
    """Given an image will click on the centered location"""
    try:
        location = locateCenterOnScreen(image = image, confidence = confidence)
        if location:
            click(location)
            sleep(time)
    except ImageNotFoundException:
        return None

def isOnScreen(image):
    try:
        item = locateOnScreen(image = image, confidence = .7)
        if item:
            return True
    except ImageNotFoundException:
        return False
    return False

def checkAvoidIslands():
    """If currenly on an avoided island, click next."""
    islands = listdir("AvoidIslands")
    for island in islands:
        if isOnScreen(island):
            findClick(NEXT)

#Currenty unused
def openGame():
    """Opens game and ensures it's open before continuing"""
    pass
    #check if opened later    
    
def collectDaily():
    try:
        coordinates = locateCenterOnScreen(COLLECT)
        moveTo(coordinates)
        sleep(.5)
        click()
    except ImageNotFoundException:
        return None
         
# DO NOTIFS ELSEWHERE
# then confirm if there then hit close on any notifications
# def closeNotification():
#     """Closes notifications that appear at the begging"""
#     try:
#         coordinates = locateCenterOnScreen("Images\\close.png")
#         click(coordinates)
#         return coordinates
#     except ImageNotFoundException:
#         return None

def mirrorSwitch(maps = 0):
    findClick(MAP)
    findClick(MIRROR)

def collectAll():
    """Finds and clicks on CollectAll, Confirm, then looks for gems"""
    findClick(COLLECTALL)
    findClick(CONFIRM)
    findClick(GEM, confidence = .5)
    
def collectFood():
    """Collects all the food available on screen until no more is found (recursive)"""
    try:
        food_location = locateCenterOnScreen(FOOD, confidence = .6)
        if food_location:
            click(food_location)
            sleep(.5)
            collectFood()
            return True
    except ImageNotFoundException:
        return None
    
def rebake():
    """Clicks on last collected Bakery then rebakes all"""
    click()
    sleep(1.5)
    findClick(RETRY)
    findClick(CONFIRM)
    
def changeMap():
    """Clicks on the map, goes next, then goes to next map"""
    findClick(MAP)
    findClick(NEXT)
    findClick(GO, time = 4)

def main():
    """Closes notification, Then Main Loop."""
    print("started")
    # closeNotification()
    # print("close notif")
    while True:
        collectAll()
        if collectFood():
            rebake()
        print("collected")
        changeMap()
        print("map changed")

#main()
checkAvoidIslands()