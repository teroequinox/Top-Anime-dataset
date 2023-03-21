import random as cum
anime = ['ONE PIECE','naruto','Chainsaw Man','Demon Slayer','Grand Blue']

def randanimesuggestio():
    def randanime():
        print(f'You should try watching {cum.choice(anime)}');
        print('  ')

    def check():
        w = input('Already watched it?\nY/N');

        if w != 'Y' and w != 'y':
            if w != 'N' and w != 'n':
                print('INVALID INPUT');
            else:
                print('Cool go ahead and watch it then!!')


        else:
            print('Ohh then,')
            randanime();
    randanime();
    check();

randanimesuggestio()

