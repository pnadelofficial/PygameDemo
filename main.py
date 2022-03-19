import pygame
import random
import time
from button import Button
from pygame import mixer
pygame.init()
mixer.init()
clock = pygame.time.Clock()

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

GREEN_ON = (0, 255, 0)
GREEN_OFF = (0, 227, 0)
RED_ON = (255, 0, 0)
RED_OFF = (227, 0, 0)
BLUE_ON = (0, 0, 255)
BLUE_OFF = (0, 0, 227)
YELLOW_ON = (255, 255, 0)
YELLOW_OFF = (227, 227, 0)

# Pass in respective sounds for each color ## MUST COME BACK FOR WAV
GREEN_SOUND = pygame.mixer.Sound('bell1.wav')
RED_SOUND = pygame.mixer.Sound('bell2.wav')
BLUE_SOUND = pygame.mixer.Sound('bell3.wav')
YELLOW_SOUND = pygame.mixer.Sound('bell4.wav')

green = Button(GREEN_ON, GREEN_OFF, GREEN_SOUND, 15, 15)
red = Button(RED_ON, RED_OFF, RED_SOUND, 15, 255)
blue = Button(BLUE_ON, BLUE_OFF, BLUE_SOUND, 255, 15)
yellow = Button(YELLOW_ON, YELLOW_OFF, YELLOW_SOUND, 255, 255)

colors = ['green', 'red', 'blue', 'yellow']
cpu_sequence = []
choice = ""

def draw_board():
    green.draw(SCREEN)
    red.draw(SCREEN)
    blue.draw(SCREEN)
    yellow.draw(SCREEN)

def cpu_turn():
    choice = random.choice(colors)
    cpu_sequence.append(choice)
    if choice == 'green':
        green.update(SCREEN)
    elif choice == 'red':
        red.update(SCREEN)
    elif choice == 'blue':
        blue.update(SCREEN)
    else:
        yellow.update(SCREEN)

def repeat_cpu_sequence():
    if(len(cpu_sequence) != 0):
        for color in cpu_sequence:
            if color == "green":
                green.update(SCREEN)
            elif color == "red":
                red.update(SCREEN)
            elif color == "blue":
                blue.update(SCREEN)
            else:
                yellow.update(SCREEN)
            pygame.time.wait(500)

def player_turn():
    turn_time = time.time()
    players_sequence = []
    while ((time.time() <= turn_time+3) and (len(players_sequence) < len(cpu_sequence))):
        for event in pygame.event.get():
            if ((event.type == pygame.MOUSEBUTTONUP) and (event.button == 1)):
                pos = pygame.mouse.get_pos()
                if green.selected(pos):
                    green.update(SCREEN)
                    players_sequence.append("green")
                    check_sequence(players_sequence)
                    turn_time = time.time()
                elif red.selected(pos):
                    red.update(SCREEN)
                    players_sequence.append("red")
                    check_sequence(players_sequence)
                    turn_time = time.time()
                elif blue.selected(pos):
                    blue.update(SCREEN)
                    players_sequence.append("blue")
                    check_sequence(players_sequence)
                    turn_time = time.time()
                else:
                    yellow.update(SCREEN)
                    players_sequence.append("yellow")
                    check_sequence(players_sequence)
                    turn_time = time.time()

def check_sequence(players_sequence):
    if players_sequence != cpu_sequence[:len(players_sequence)]:
        game_over()

def game_over():
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            quit()
    pygame.display.update()

    draw_board()
    repeat_cpu_sequence()
    cpu_turn()
    player_turn()
    pygame.time.wait(1000)

    clock.tick(60)