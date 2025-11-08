class Section:
    def __init__(self, title, text_block, choices=None, is_end=False):
        self.title = title
        self.text_block = text_block
        self.choices = choices
        self.is_end = is_end
