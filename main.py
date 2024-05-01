from pyautogui import locateCenterOnScreen, ImageNotFoundException, click, doubleClick, moveTo, locateOnScreen, locateAllOnScreen, scroll
from time import sleep
from os import listdir
from constants import *
import keyboard

# CODE BY ADRIAN MONTES
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


def findClick(image : str, time = .5, confidence = .7) -> None:
    """Given an image will click on the centered location
    
    :param image: Image to find on screen
    :param time: The time to wait after clicking on image
    :param confidence: How closely the image must match the findings on screen
    :return: None"""
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
    """If currenly on an avoided island, click next. Checks all islands in avoid islands folder again """
    islands = listdir("AvoidIslands")
    for island in islands:
        if isOnScreen(island):
            findClick(NEXT)
            checkAvoidIslands()

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
        food_found = list(locateAllOnScreen(FOOD, confidence = .6))
    except ImageNotFoundException:
        return None
    except Exception as e:
        print(e)
    else:
        food_locations = []
        for located in food_found:
            if len(food_locations) == 0:
                food_locations.append(located)
                continue
            if not (located[0] - 10 <= food_locations[len(food_locations)-1][0] <= located[0] + 10):
                food_locations.append(located)
        
        for location in food_locations:
            click(location)
        if len(food_locations) != 0:
            return True
    
def rebake():
    """Clicks on last collected Bakery then rebakes all"""
    click()
    sleep(1.5)
    findClick(RETRY)
    findClick(CONFIRM)
    sleep(1.5)
    
def changeMap():
    """Clicks on the map, goes next, then goes to next map"""
    findClick(MAP)
    findClick(NEXT)
    findClick(GO, time = 4)

def main():
    """Closes notification, Then Main Loop."""
    print("started")
    keyboard.press_and_release("alt+tab")
    sleep(2)

    for i in range(9):
        scroll(-10)
    # closeNotification()
    # print("close notif")
    while True:
        if keyboard.is_pressed('q'):
            break
        collectAll()
        if keyboard.is_pressed('q'):
            break
        if collectFood():
            rebake()
        if keyboard.is_pressed('q'):
            break
        print("collected")
        changeMap()
        if keyboard.is_pressed('q'):
            break
        print("map changed")

main()

