import pygame, sys
from pygame import rect
from pygame.locals import QUIT
from pygame import mixer
import random
import time
import pickle  # Import the pickle module
import os  # Import os module to work with directories
from button import Button

#Make the colors used in the game
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
dgray = (90, 90, 90)

# Create the save directory if it doesn't exist
save_directory = "Savegames"  # Name of your save directory
os.makedirs(save_directory, exist_ok=True)  # Create the directory if it doesn't exist

# Create variables
game_data = [200, 4, 0, 30, 50, 10, 1, 30, 0, 1]  # Store variables in an array
# Indices: 0 - monies, 1 - price, 2 - bombs, 3 - jbombs, 4 - jmoney, 5 - bonus, 6 - mglevel, 7 - fps, 8 - job

monies = game_data[0]
price = game_data[1]
bombs = game_data[2]
jbombs = game_data[3]
jmoney = game_data[4]
bonus = game_data[5]
mglevel = game_data[6]
fps = game_data[7]
job = game_data[8]
level = game_data[9]

last_money_update = time.time()
names = ["Putin", "Trump", "Kanye East", "Im not sure", "1945 Germany", "Yapdollar", "The fat guy with nukes", "EDP 445", "IRS", "Seceret Services", "The Cartel", "Bonasian Ape Society"]
namenumber = 2

#Create Functions
def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('Anton-Regular.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    DISPLAYSURF.blit(text, textRect)

def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))
def autominer():
    time.sleep(1/mglevel)
    game_data[0] += mglevel  # Update monies in the array
    monies = game_data[0] # Update the local variable
def get_font(size):
    return pygame.font.Font("Anton-Regular.ttf, size")

ver = "Beta 0.1"
pygame.init()
mixer.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
boom = pygame.mixer.Sound("boo.wav")
img = pygame.image.load('Assets/Images/icon.png')
pygame.mixer.music.load("epiksoundtrack.mp3")
pygame.mixer.music.set_volume(0.7) 
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
pygame.display.set_caption('JustBlowEmUp ' + ver)
icon = pygame.image.load('Assets/Images/icon.png')
icon_scaled = pygame.transform.scale(icon, (200, 200))
last_event_time = pygame.time.get_ticks()
event_interval = 1000
pygame.display.set_icon(img) 

# Function to save game data
def save_game():
    with open(os.path.join(save_directory, "game_save.dat"), "wb") as f:
        pickle.dump(game_data, f)

# Function to load game data
def load_game():
    global game_data
    try:
        with open(os.path.join(save_directory, "game_save.dat"), "rb") as f:
            game_data = pickle.load(f)
            monies = game_data[0]
            price = game_data[1]
            bombs = game_data[2]
            jbombs = game_data[3]
            jmoney = game_data[4]
            bonus = game_data[5]
            mglevel = game_data[6]
            fps = game_data[7]
            job = game_data[8]
            level = game_data[9]
    except FileNotFoundError:
        print("No save file found. Starting a new game.")

# Load game data at the start
load_game()

while True:


    for event in pygame.event.get():
        DISPLAYSURF.fill(black)
        jmoney = game_data[3] * game_data[1] + game_data[5] # Calculate jmoney based on array
        mgupgrade = game_data[6] * 200
        event_interval = 500 - game_data[6] * game_data[6]
        rectangle(DISPLAYSURF, dgray, 0, 0, 800, 40)
        rectangle(DISPLAYSURF, gray, 225, 0, 350, 60)
        DrawText("Just blow em up!", white, gray, 400, 30, 35)
        DISPLAYSURF.blit(icon_scaled, (300, 200))
        DrawText("Buy Bombs, current price is " + str(game_data[1]), white, black, 400, 200, 20)
        rectangle(DISPLAYSURF, black, 650, 15, 50, 20) 
        DrawText(" You Have " + str(game_data[0]) + " monies", white, dgray, 700, 20, 20)
        DISPLAYSURF.blit(icon, (220, 5))
        rectangle(DISPLAYSURF, black,380,350,60,25)
        DrawText("Bombs:  " + str(game_data[2]) + " ", white, black, 390, 350, 25)
        rectangle(DISPLAYSURF, gray, 0, 400, 300, 200)
        DrawText("Jobs", white, black, 130, 365, 40)
        DrawText(names[namenumber], white, gray, 125, 450, 25)
        DrawText("Wants you do a job using " + str(game_data[3]) + " bombs?", white, gray, 150, 490, 15)
        DrawText("You can earn " + str(jmoney) + " monies", white, gray, 140, 520, 15)
        DISPLAYSURF.blit(icon, (515, 5))
        DrawText("Moneygiver level " + str(game_data[6]), white, black, 700, 250, 20)
        rectangle(DISPLAYSURF, gray, 625, 300, 150, 75)
        DrawText("Monies needed to  ", white, gray, 700, 325, 15)
        DrawText("upgrade " + str(mgupgrade), white, gray, 690, 350, 15)
        current_time = pygame.time.get_ticks()
        if current_time - last_event_time >= event_interval:
            # Trigger your time-based event here
            print("Timed event triggered!")
            game_data[0] = game_data[0] + game_data[6]  # Update monies in the array
            monies = game_data[0] # Update the local variable
            # Reset the event timer
            last_event_time = current_time
        if event.type == pygame.KEYDOWN:  # Check for key press events
            if event.key == pygame.K_SPACE:
                if game_data[0] < game_data[1]:
                    print("Not enough money")
                else:
                    game_data[0] -= game_data[1]  # Update monies in the array
                    game_data[2] += 1  # Update bombs in the array
                    monies = game_data[0]  # Update the local variable
                    bombs = game_data[2]  # Update the local variable

        if event.type == pygame.MOUSEBUTTONDOWN:
            mopos = pygame.mouse.get_pos()
            print(mopos)
            # Correct comparison:
            if 300 <= mopos[0] <= 500 and 200 <= mopos[1] <= 400: 
                if game_data[0] < game_data[1]:
                    print("Not enough money")
                else:
                    game_data[0] -= game_data[1]  # Update monies in the array
                    game_data[2] += 1  # Update bombs in the array
                    monies = game_data[0]  # Update the local variable
                    bombs = game_data[2]  # Update the local variable
                    job = job + 1
            if 625 <= mopos[0] <= 775 and 300 <= mopos[1] <= 375:
                if game_data[0] < mgupgrade:
                    print("Not enough money")
                else:
                    game_data[6] = game_data[6] + 1  # Update mglevel in the array
                    game_data[0] = game_data[0] - mgupgrade  # Update monies in the array
                    mglevel = game_data[6]  # Update the local variable
                    monies = game_data[0]  # Update the local variable
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 0 <= mopos[0] <= 300 and 400 <= mopos[1] <= 600:
                if game_data[2] < game_data[3]:
                    print("Not enough bombs")
                else:
                    game_data[9] = game_data[9]*5-game_data[8]
                    level = game_data[9]
                    print(str(level))
                    boom.set_volume(1)
                    boom.play()
                    game_data[8] = game_data[8] + 1  # Update job in the array
                    game_data[5] = random.randint(0, 100)  # Update bonus in the array
                    namenumber = random.randint(0, (len(names)-1))
                    game_data[0] += jmoney  # Update monies in the array
                    game_data[2] -= game_data[3]  # Update bombs in the array
                    game_data[3] = random.randint(0, 60)  # Update jbombs in the array
                    monies = game_data[0]  # Update the local variable
                    bombs = game_data[2]  # Update the local variable
                    jbombs = game_data[3]  # Update the local variable
                    bonus = game_data[5]  # Update the local variable
                    job = game_data[8]  # Update the local variable

        if event.type == pygame.MOUSEBUTTONDOWN:
            mopos = pygame.mouse.get_pos()
            if 625 <= mopos[0] <= 775 and 300 <= mopos[1] <= 375:
                print("Rectangle clicked!")
        if event.type == QUIT:
            save_game()  # Save the game before quitting
            pygame.quit()
            sys.exit()
        clock.tick(game_data[7])

    pygame.display.update()



