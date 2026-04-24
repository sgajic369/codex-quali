from random import randint
import pgzrun  # Needed to start the game from the code

WIDTH = 1920
HEIGHT = 1080

img = Actor("zoeylol")

def draw():
    screen.clear()
    img.draw()

def place_zoey():
    img.x = randint(100, WIDTH - 200)
    img.y = randint(100, HEIGHT - 200)
    
    animate(img, tween='bounce_end', duration=0.5, y=img.y + 60)

def on_mouse_down(pos):
    if img.collidepoint(pos):
        print("Good shot!") 
        place_zoey()
    else:
        print("You missed!") 
        quit()

place_zoey()


try:
    pgzrun.go()
except KeyboardInterrupt:
    print("\ngood bye")
    print("""
    ____  ______
   / __ )| ____/
  / __  ||  _|  
 / /_/ /| |___  
/_____/ |_____| 
    """)
