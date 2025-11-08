from src.section import Section


def story_parser(file):
    # Make a list of sections and return them to main
    sections = []
    current_story = ""
    with open(file) as f:
        current_story = f.read()

    split_story = current_story.split("\n")
    current_section = Section("", [], [], False)
    for line in split_story:
        current_section = line_analyzer(line, current_section, sections)

    return sections


def line_analyzer(line, section, sections):
    section_end_call = False
    if line.startswith("[%S"):
        temp_line = line[4:-3]
        section.title = temp_line
    elif line.startswith("[%C"):
        choice_list = line.split("][")
        clean_choices = []
        for item in choice_list:
            if item.startswith("[%C"):
                item = item[4:-2]
            if item.startswith("%C"):
                if item.endswith("%]"):
                    item = item[3:-3]
                if item.endswith("%"):
                    item = item[3:-2]
            clean_choices.append(item.split(" :: "))
        ## TEMP CODE FOR TESTING
        section.choices = clean_choices
        section_end_call = True
    elif line.startswith("[%e"):
        section.is_end = True
        section_end_call = True
    elif line.startswith("\n"):
        print("empty line found")
    else:
        section.text_block.append(line)
    if section_end_call:
        new_section = section
        sections.append(new_section)
        return Section("", [], [], False)
    return section
