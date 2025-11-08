import pygame
import pmtext.para
import pmtext.util_pygame
import random
import math

from src.button import Button
from src.fancy_text import FancyText
from src.story_parser import story_parser
from config.default_config import SCREEN_HEIGHT, SCREEN_WIDTH, FONT, STORY

game_frame = 0
objects = []
current_buttons = []
current_section = 0
story_sections = []
newFancyText = ""
screen = ""
pygFont = ""
clicked = True


def main():
    global game_frame
    global objects
    global current_buttons
    global change_flag
    global current_section
    global story_sections
    global newFancyText
    global screen
    global pygFont

    # pygame init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    pygFont = pygame.font.Font(FONT, 25)

    # Setting up clock and delta
    clock = pygame.time.Clock()
    dt = 0

    # NOTE Line length greater than 70 should newline

    # newFancyText = FancyText(FONT, screen, test_section, objects)

    story_sections = story_parser(STORY)
    newFancyText = FancyText(
        FONT, screen, story_sections[current_section].text_block, objects
    )
    generate_buttons(
        story_sections[current_section].choices,
        current_buttons,
        objects,
        pygFont,
        screen,
        newFancyText,
    )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Draw a black background
        screen.fill("black")
        for object in objects:
            object.process()

        # Update the window
        pygame.display.flip()
        game_frame += 1

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


def progess_story(current_choice, current_text):
    global current_section
    global change_flag
    global story_sections
    global screen
    global objects
    global pygFont
    global clicked

    clicked = True

    print(f"Choice clicked: ", current_choice)
    if current_text != "":
        if current_text in objects:
            objects.remove(current_text)

    # Find target index (potential optimization point could add an inherint index to make the sections into a dictionary or something)
    new_index = 0
    for index, item in enumerate(story_sections):
        if item.title == current_choice:
            print(f"Title matched {current_choice}")
            new_index = index
    current_section = new_index
    newFancyText = FancyText(
        FONT, screen, story_sections[current_section].text_block, objects
    )
    if clicked:
        generate_buttons(
            story_sections[current_section].choices,
            current_buttons,
            objects,
            pygFont,
            screen,
            newFancyText,
        )
        clicked = False


def generate_buttons(choices, current_buttons, objects, pygFont, screen, newFancyText):
    global clicked
    if current_buttons != None and clicked:
        for button in current_buttons:
            print("DEBUG")
            print(f"Current Checked Button: {button}")
            print(f"Objects currently : {objects}")
            objects.remove(button)
            current_buttons.remove(button)
    offset = -300
    for choice in choices:
        newButton = Button(
            SCREEN_WIDTH / len(choices) + offset,
            SCREEN_HEIGHT - 110,
            300,
            100,
            pygFont,
            screen,
            objects,
            newFancyText,
            True,
            choice[0],
            progess_story,
            choice[1],
        )
        offset += 350
        current_buttons.append(newButton)


if __name__ == "__main__":
    main()
