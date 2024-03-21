from pyautogui import locateCenterOnScreen, ImageNotFoundException, click, doubleClick, moveTo
from time import sleep


"""got a collect key"""
#close notification
#collect button
#

def mapOnScreen():
    try:
        coordinates = locateCenterOnScreen('map.png')
        return coordinates
    except ImageNotFoundException:
        return None

def msmOnScreen():
    try:
        coordinates = locateCenterOnScreen('msm.png')
        return coordinates
    except ImageNotFoundException:
        return None


# first open the game, wait close button to be on screen
#if not already in game open it from desktop else throw error

def openGame():
    """Opens game and ensures it's open before continuing"""
    msm = msmOnScreen()
    if msm:
        msm.doubleClick()
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
        collect_all_location = locateCenterOnScreen("collectAll.png")
        if collect_all_location:
            click(collect_all_location)
            sleep(1)
            print("sleep")
        confirm_location = locateCenterOnScreen("confirm.png")
        if confirm_location:
            click(confirm_location)
            sleep(1)
            print("sleep")
        gem_location = locateCenterOnScreen("gem.png")
        if gem_location:
            click(gem_location)
            sleep(1)
            print("sleep")
        
    except ImageNotFoundException:
        return None
    

def changeMap():
    try:
        #map, next, go, pause
        map_location = locateCenterOnScreen("map.png")
        if map_location:
            click(map_location)
            sleep(1)
            print("sleep")
        next_location = locateCenterOnScreen("next.png")
        if next_location:
            click(next_location)
            sleep(1)
            print("sleep")
        go_location = locateCenterOnScreen("go.png")
        if go_location:
            click(go_location)
            sleep(1)
            print("sleep")
    except ImageNotFoundException:
        return None


def main():
    print("started")
    closeNotification()
    print("close notif")
    sleep(1)
    while True:
        collectAll()
        print("collected")
        changeMap()
        print("map changed")
        sleep(4)

main()