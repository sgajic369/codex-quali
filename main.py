from random import randint
import pgzrun
import pygame

WIDTH = 1920
HEIGHT = 1080

img = Actor("zoeylol")

def draw():
    screen.clear()
    img.draw()

def place_zoey():
    img.image = "explosion"
    
    clock.schedule_unique(reset_image, 0.2)

def reset_image():
    img.image = "zoeylol"
    curr_width, curr_height = img.width, img.height
    if curr_width > 60:
        new_size = (int(curr_width * 0.9), int(curr_height * 0.9))
        img._surf = pygame.transform.scale(img._surf, new_size)
        img._update_pos()

    img.x = randint(100, WIDTH - 100)
    img.y = randint(100, HEIGHT - 100)
    animate(img, tween='bounce_end', duration=0.5, y=img.y + 60)

def place_zoey():
    curr_width = img.width
    curr_height = img.height

    # Shrink img by 20% 
    if curr_width > 60 and curr_height > 60:
        new_width = int(curr_width * 0.9)
        new_height = int(curr_height * 0.9)
        # 
        img._surf = pygame.transform.scale(img._surf, (new_width, new_height))
        img._update_pos() 
    # The img is 1720x880
    img.x = randint(100, WIDTH - 200)
    img.y = randint(100, HEIGHT - 200)
    
    # Vibrating effect
    animate(img, tween='bounce_end', duration=0.34555, y=img.y + 60)

def on_mouse_down(pos):
    if img.collidepoint(pos):
        sounds.eep.play()
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
