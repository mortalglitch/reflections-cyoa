import re

from src.section import Section


def story_parser(file):
    # Make a list of sections and return them to main
    sections = []
    current_story = ""
    with open(file) as f:
        current_story = f.read()

    # The current regex method is failing due to striping the wrapper need another method.
    # section_list = re.split(r"\[%S (.*?) %]", current_story)
    print(current_story)
