import pygame
import pmtext.para
import pmtext.util_pygame
import math
import random


class FancyText:
    def __init__(self, font, screen, textSection, objects):
        self.font = font
        self.screen = screen
        self.textSection = textSection

        # pmtext init
        pmfont = pmtext.util_pygame.TTF(font, 25)
        p = pmtext.para.Graph(pmfont)
        t = pmtext.para.Typewriter(p)

        colorDefault = [255, 255, 255]

        # Loop over textSection
        for line in textSection:
            lineSplit = line.split()
            for word in lineSplit:
                if word.startswith("[#c"):
                    new_color_raw = word[4:-2]
                    new_color_split = new_color_raw.split(",")
                    t.color(
                        int(new_color_split[0]),
                        int(new_color_split[1]),
                        int(new_color_split[2]),
                    )
                elif word == "[#shake#]":
                    t.shake(jitter)
                elif word == "[#reset#]":
                    t.color(colorDefault[0], colorDefault[1], colorDefault[2])
                    t.shake(None)
                elif word == "[#newline#]":
                    t.newline()
                else:
                    t.string(word + " ")
            t.newline()

        # parse through each line
        # look through each line and pull out specialized commands

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
        self.processedText = t
        objects.append(self)

    def process(self):
        # Draw Typewriter
        self.processedText.pulse()
        self.processedText.draw(self.screen, 10, 10)


def jitter(char_index):
    """Angry text motion."""
    x = random.randint(0, 1)
    y = random.randint(0, 1)
    return x, y
