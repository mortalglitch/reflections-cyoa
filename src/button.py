"""based on the tutorial from https://thepythoncode.com/article/make-a-button-using-pygame-in-python"""

import pygame


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

        self.fillColors = {
            "normal": "#ffffff",
            "hover": "#666666",
            "pressed": "#333333",
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect((self.x, self.y, self.width, self.height))

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def __repr__(self):
        return f"Button Object {self.current_text} with dataChoice {self.dataChoice}"

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors["normal"])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors["hover"])
            for event in pygame.event.get():
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    self.buttonSurface.fill(self.fillColors["pressed"])

                    if self.onePress:
                        self.onclickFunction(self.dataChoice, self.current_text)

                    elif not self.alreadyPressed:
                        self.onclickFunction(self.dataChoice, self.current_text)
                        self.alreadyPressed = True

                else:
                    self.alreadyPressed = False

        self.buttonSurface.blit(
            self.buttonSurf,
            [
                self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
                self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2,
            ],
        )
        self.screen.blit(self.buttonSurface, self.buttonRect)
