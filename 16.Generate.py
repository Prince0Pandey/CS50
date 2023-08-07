# import random                             # 'import' will import everything that is inside the modules/libraries
# coin = random.choice(["Heads","Tails"])   # and also we have to write random.any_function everytime
# print(coin)

# from random import choice
# coin = choice(["Heads","Tails"])          # choice() gives random value present inside the list
# print(coin)

# import random
# number = random.randint(1,10)             # randint() takes 2 parameter and return random value between them both inclusive
# print(number)

import random
cards = ["jack","queen","king"]
random.shuffle(cards)                       # shuffle() just shuffle the given list but does not return anything
for card in cards:
    print(card)