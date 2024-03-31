from pyautogui import locateCenterOnScreen, ImageNotFoundException, click, doubleClick, moveTo
from time import sleep

#pip install pyautogui
#pip install opencv_python

"""got a collect key"""
#close notification
#collect button
#setting locate on screen confidence to .5 will allow to collect jumping images
#this could mean lighting tourches

# first open the game, wait close button to be on screen
#if not already in game open it from desktop else throw error

#Currenty unused
def openGame():
    """Opens game and ensures it's open before continuing"""
    pass
    #check if opened later    
    
    
#collect daily rewards
    def collectDaily():
        try:
            coordinates = locateCenterOnScreen('collect.png')
            moveTo(coordinates)
            sleep(.5)
            click()
        except ImageNotFoundException:
            return None
         
# then confirm if there then hit close on any notifications
def closeNotification():
    """Closes notifications that appear at the begging"""
    try:
        coordinates = locateCenterOnScreen('close.png')
        click(coordinates)
        return coordinates
    except ImageNotFoundException:
        return None

# Then begin main loop, collect all, confirm, map, next, go

def collectAll():
    try:
        collect_all_location = locateCenterOnScreen("collectAll.png", confidence = .7)
        if collect_all_location:
            click(collect_all_location)
            sleep(.5)
        confirm_location = locateCenterOnScreen("confirm.png", confidence = .7)
        if confirm_location:
            click(confirm_location)
            sleep(.5)
        gem_location = locateCenterOnScreen("gem.png", confidence = .5)
        if gem_location:
            click(gem_location)
            sleep(.5)
        
    except ImageNotFoundException:
        return None
    
def collectFood():
    try:
        #collect till no more found, then click once more, then retry

        food_location = locateCenterOnScreen("food.png", confidence = .6)
        if food_location:
            click(food_location)
            sleep(.5)
            collectFood()
    except ImageNotFoundException:
        return None
    
def rebake():
    click()
    try:
        sleep(1.5)
        retry_location = locateCenterOnScreen("retry.png", confidence = .7)
        if retry_location:
            click(retry_location)
            sleep(.5)
        confirm_location = locateCenterOnScreen("confirm.png", confidence = .7)
        if confirm_location:
            click(confirm_location)
            sleep(.5)
    except ImageNotFoundException:
        return None        

    
def changeMap():
    try:
        #map, next, go, pause
        map_location = locateCenterOnScreen("map.png", confidence = .7)
        if map_location:
            click(map_location)
            sleep(.5)
        next_location = locateCenterOnScreen("next.png", confidence = .7)
        if next_location:
            click(next_location)
            sleep(.5)
        go_location = locateCenterOnScreen("go.png", confidence = .7)
        if go_location:
            click(go_location)
            sleep(4)
    except ImageNotFoundException:
        return None

# Main Function
def main():
    """Closes notification, Then Main Loop."""
    print("started")
    closeNotification()
    print("close notif")
    while True:
        collectAll()
        print("collected")
        changeMap()
        print("map changed")

#main()
sleep(3)
collectFood()
rebake()