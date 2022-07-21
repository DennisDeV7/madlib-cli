import re


def read_template():
    """
    This function opens and reads dark_and_stormy_night_template
    :return:
    """
    with open('assets/dark_and_stormy_night_template.txt', 'r') as f:
        contents = f.read()
        return contents.strip()


def parse_template():
    """
    placeholder
    :return:
    """
    with open('assets/dark_and_stormy_night_template.txt', 'r') as f:
        contents = f.read()
        empty_brackets = re.sub("{(.*?)}", "{}", contents)
        words_removed = ()
        words = re.findall(r"\{(.*?)}", contents)
        for word in words:
            words_removed = words_removed + (word, )
        return empty_brackets, words_removed


def merge():
    """
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    :return:
    """
    with open('assets/dark_and_stormy_night_template.txt', 'r') as f:
        contents = f.read()
        empty_brackets = re.sub("{(.*?)}", "{}", contents)
        words_removed = ()
        new_words = ()
        words = re.findall(r"\{(.*?)}", contents)

        for word in words:
            words_removed = words_removed + (word, )

        for word in words_removed:
            thing = input(f"Enter a/an {word} --> ")
            new_words = new_words + (thing, )

        new_content = empty_brackets.format(*new_words)

        with open('new_file.txt', 'w') as f:
            f.write(new_content)
        return new_content


if __name__ == "__main__":

    print("""
        Welcome to our script! This project will take a few
        adjectives and nouns from you and print out a madlib
        in return. 
        
        See below for an example
        
        When ready input the words by the prompt and see what happens
    """)

    temp = read_template()
    # print(temp)
    parse = parse_template()
    # print(parse)
    merge = merge()
    print(merge)
