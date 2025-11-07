import pygame
import pmtext.para
import pmtext.util_pygame
import random
import math

from src.button import Button
from config.default_config import *

game_frame = 0
objects = []


def main():
    global game_frame
    # pygame init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    pygFont = pygame.font.Font(FONT, 25)

    # Setting up clock and delta
    clock = pygame.time.Clock()
    dt = 0

    # pmtext init
    font = pmtext.util_pygame.TTF(
        "./fonts/BigBlueTerminal/BigBlueTermPlusNerdFontMono-Regular.ttf", 25
    )
    p = pmtext.para.Graph(font)
    t = pmtext.para.Typewriter(p)

    t.color(255, 255, 255)
    t.string("Hello ")
    t.newline()
    t.wait(50)
    t.color(255, 0, 0)
    t.shake(jitter)
    t.string("world")
    t.shake(None)
    t.color(255, 255, 255)
    t.string(".")

    jit = pmtext.para.Graph(font)
    jit.shake(jitter)
    jit.string("Hello... ")

    jit.shake(singsong)
    jit.string("World... ")

    jit.shake(None)
    jit.string("!! Back to your regular scheduled programming.")

    ## Button Testing
    customButton = Button(
        440,
        600,
        400,
        100,
        pygFont,
        screen,
        objects,
        False,
        "Button for choice 1",
        myFunction,
        "data_choice",
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Draw a white background
        screen.fill("black")

        # Draw Typewriter
        t.pulse()
        t.draw(screen, 10, 10)

        jit.draw(screen, 10, 75)
        for object in objects:
            object.process()

        # Update the window
        pygame.display.flip()
        game_frame += 1

        # print("Hello from reflections-cyoa!")
        dt = clock.tick(60) / 1000


def jitter(char_index):
    """Angry text motion."""
    x = random.randint(0, 1)
    y = random.randint(0, 1)
    return x, y


def singsong(char_index):
    """Happy text motion."""
    x = math.cos(float(game_frame + char_index) / 2)
    y = math.sin(float(game_frame + char_index) / 2)
    return x, y


def myFunction(current_choice):
    print(f"Choice clicked: ", current_choice)


if __name__ == "__main__":
    main()
