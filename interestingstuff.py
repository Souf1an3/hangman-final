
drick = ['a', 'd', 'd', 's', 's', 'w', '1','_','2','$','a','d','W']

def capitalize_list(item):
    item = ''.join(c for c in item if c.isalpha())
    return item.upper()


print(list(set(capitalize_list(drick))))

# shit just got real

# A hangmanben ez így fest, az irreleváns sorokat kikommenteltem 

def capitalize_list(item): # !
    item = ''.join(c for c in item if c.isalpha()) # !
    item = item.upper() # !
    return list(set(item)) # !


def get_guess(guess_pool):
    global epic
    epic = 0
    guess = input("What's your next guess? Give me a letter: ")
    while len(guess) <= 0:
        guess = input("Empty input! Please give me a letter!")
    letlow = list(word.lower())
    letupp = list(word.upper())
    letters = set(letlow + letupp)
    tester = set(guess_pool)
    casesensitive(guess, guess_pool)
    guess_set = capitalize_list(tester)  # !