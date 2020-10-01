
drick = ['a', 'd', 'd', 's', 's', 'w', '1','_','2','$','a','d','W']

def capitalize_list(item):
    item = ''.join(c for c in item if c.isalpha()) 
    return item.upper()  #   


print(list(set(capitalize_list(drick))))

# shit just got real

# A hangmanben ez így fest, ! jelöli az "érdekes" soroka

def capitalize_list(item): # !
    item = ''.join(c for c in item if c.isalpha()) # !  csinál egy stringet a lista összes betűjéből, szóval megszabadulunk a spacetől guess_pool mutatása előtt.
    item = item.upper() # ! a stringben minden betűt nagybetűvé alakit, de itt még fent áll az a gond, hogy pl ha volt (K,k, A,a) -> az nem mutatott jól, így már AAKKstb a string jelenleg
    return list(set(item)) # ! és visszaadja az előző stringet amiből először is setet csinált, így megszabadultunk a dupla betűktől (a kicsiktől meg ugye az előbb)
# illetve a visszakapott setet még átalakítja listává, mert sokkal jobban néz ki [] az első tipp után, mint a {set}  (ezt írja ki, az üres setre ha printeljük)


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
    guess_set = capitalize_list(tester)  # !  tadam  Ezzel pl ebből: ["K","k","B","b"," ","z"]  -> ez lett ["K","B","Z"] így sokkal átláthatóbb és szebb is a guess_pool, de ez az érték csak itt jelenig meg, a függvényen belül amíg kiírjuk rossz\ismételt guess esetén
