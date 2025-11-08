class Section:
    def __init__(self, title, text_block, choices=None, is_end=False):
        self.title = title
        self.text_block = text_block
        self.choices = choices
        self.is_end = is_end

    def __repr__(self):
        return f"Title: {self.title} \nCurrent Text: {self.text_block} \nChoices: {self.choices} \nIs End? {self.is_end} \n"
