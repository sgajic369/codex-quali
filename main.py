from random import randint
import pgzrun
import pygame

# Set Screen Dimensions
WIDTH = 1920
HEIGHT = 1080

# Constants
BASE_IMAGE = "zoeylol"
HIT_IMAGE = "explotion" # Check spelling: should match your filename
MIN_SIZE = 60
SHRINK_FACTOR = 0.9

# Create Actor and Initial Target Size
img = Actor(BASE_IMAGE)
target_width = img.width
target_height = img.height

def draw():
    screen.clear()
    img.draw()

def set_image(name):
    """Swaps the image and forces it to the current target size"""
    img.image = name
    # We use smoothscale to keep the quality high while shrinking
    img._surf = pygame.transform.smoothscale(img._surf, (target_width, target_height))
    img._update_pos()

def shrink_target():
    """Reduces the size variables for the next spawn"""
    global target_width, target_height
    if target_width <= MIN_SIZE or target_height <= MIN_SIZE:
        return
    
    target_width = max(MIN_SIZE, int(target_width * SHRINK_FACTOR))
    target_height = max(MIN_SIZE, int(target_height * SHRINK_FACTOR))

def move_target():
    """Moves the actor to a random location and triggers pulse animation"""
    half_width = max(target_width // 2, 1)
    half_height = max(target_height // 2, 1)

    img.x = randint(half_width, WIDTH - half_width)
    img.y = randint(half_height, HEIGHT - half_height)
    animate(img, tween="bounce_end", duration=0.35, y=img.y + 60)

def reset_target():
    """Switch back from explosion to normal character"""
    set_image(BASE_IMAGE)
    move_target()

def place_zoey():
    """Triggered on hit: shrinks, shows explosion, and schedules reset"""
    shrink_target()
    set_image(HIT_IMAGE)
    clock.schedule_unique(reset_target, 0.2)

def on_mouse_down(pos):
    if img.collidepoint(pos):
        # sounds.boom.play() # Uncomment if you have a boom.wav in sounds/
        print("Good shot!")
        place_zoey()
    else:
        print("You missed!")
        # quit() # Uncomment if you want the game to close on a miss

# Initialize the game
reset_target()

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
