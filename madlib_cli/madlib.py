def read_template(self):
    """
    This function opens and reads dark_and_stormy_night_template
    :return:
    """
    with open('../assets/dark_and_stormy_night_template.txt', 'r') as f:
        contents = f.read()
        return contents.strip()


def parse_template():
    """
    placeholder
    :return:
    """


def merge():
    """
    placeholder
    :return:
    """


if __name__ == "__main__":

    print("""
        Welcome to our script! This project will take a few
        adjectives and nouns from you and print out a madlib
        in return. 
        
        See below for an example
        
        When ready input the words by the prompt and see what happens
    """)

    temp = read_template()
    print(temp)
