from random import randint

img = Actor("ZoeyLoL")

def draw():
    screen.clear()
    img.draw()

def place_zoey():
    img.x = randint(10, 800)
    img.y = randint(10, 600)

def on_mouse_down(pos):
    if img.collidepoint(pos):
        print("Good shot!")
        place_zoey()
    else:
        print("You missed!")
        quit()

place_zoey()
