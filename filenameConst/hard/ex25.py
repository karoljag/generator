poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# print poem

stu = "karol jagla"

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

# print break_words(poem)

polamany = break_words(poem)

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# print sort_words(stu)




def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

# print print_first_word(polamany)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-2)
    print word

print_last_word(polamany)
