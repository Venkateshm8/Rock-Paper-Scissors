import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif(comp=='r'):
        if(you=='p'):
            return True
        else:
            return False
    elif(comp=='p'):
        if(you=='s'):
            return True
        else:
            return False
    elif(comp=='s'):
        if(you=='r'):
            return True
        else:
            return False
randNo=random.randint(1,3)
if randNo==1:
    comp = 'r'
elif randNo==2:
    comp = 'p'
elif randNo==3:
    comp = 's'

print('Computers turn : Rock(r), Paper(p), Scissor(s)')
you=input('Yours turn: Rock(r), Paper(p), Scissor(s)')
a=gamewin(comp,you)
print(f'Computer choice is:{comp}')
print(f'yours choice is:{you}')

if a == None:
    print('The match is Tie!')
elif a == True:
    print('You are the winner')
else:
    print('Computer is the winner')

