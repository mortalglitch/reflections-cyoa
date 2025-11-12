"""based on the tutorial from https://thepythoncode.com/article/make-a-button-using-pygame-in-python"""

import pygame

from config.default_config import FONT


class Button:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        font,
        screen,
        objects,
        current_text,
        current_index,
        onePress=False,
        buttonText="Button",
        onclickFunction=None,
        dataChoice=None,
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.dataChoice = dataChoice
        self.onePress = onePress
        self.screen = screen
        self.objects = objects
        self.current_text = current_text
        self.current_index = current_index

        self.fillColors = {
            "normal": "#ffffff",
            "hover": "#666666",
            "pressed": "#333333",
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect((self.x, self.y, self.width, self.height))

        # Adjust font for button text when text is too long.
        if len(buttonText) < 19:
            self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        else:
            temp_font = pygame.font.Font(FONT, 14)
            self.buttonSurf = temp_font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = True

        objects.append(self)

    def __repr__(self):
        return f"Button Object {self.current_text} with dataChoice {self.dataChoice}"

    def process(self, current_index, objects, events):
        if self.current_index != current_index:
            objects.remove(self)
        else:
            mousePos = pygame.mouse.get_pos()
            self.buttonSurface.fill(self.fillColors["normal"])
            if self.buttonRect.collidepoint(mousePos):
                self.buttonSurface.fill(self.fillColors["hover"])
                for event in events:
                    # if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.buttonSurface.fill(self.fillColors["pressed"])

                            if self.onePress and not self.alreadyPressed:
                                self.onclickFunction(self.dataChoice, self.current_text)
                                self.alreadyPressed = True

                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            self.alreadyPressed = False
            if not self.buttonRect.collidepoint(mousePos):
                self.alreadyPressed = False

            self.buttonSurface.blit(
                self.buttonSurf,
                [
                    self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
                    self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2,
                ],
            )
            self.screen.blit(self.buttonSurface, self.buttonRect)
