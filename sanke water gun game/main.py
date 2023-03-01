import random 
# snake water gun or rock paper scissor 
def gamewin(comp, you):
    # if two value are equal, declare a tie 
    if comp == you:
        return None
    # check for all possibilities when computer chose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True 
        # check all possibilities when computer chose w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True 
        # check all possibilities when computer chose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("comp turn: sanke(s) water(w) or gun(g)?")
randno = random.randint(1, 3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'

you = input("your turn: sanke(s) water(w) or gun(g)?")

a = gamewin(comp, you)

print(f"computer chose{comp}")
print(f"you chose {you}")

if a == None:
    print("the game is a tie!")
elif a:
    print("you win")
else:
    print("you lose!")