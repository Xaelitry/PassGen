import random
import os
import time
from pathlib import Path

file = Path('Output.txt')
fname = 'Output.txt'

os.system('title Xaelitry\'s Secure Password Generator')

def randompass(address, length):
    add = address.title()+": \nPassword: "
    return add+"".join([random.choice('!@#$%^&*_+-=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for x in range(int(length))])

if __name__ == "__main__":

    while True:
        addVar = input("What is the password for? ")
        lenVar = input("Set length for password: ")
        if lenVar.isdigit():
            v = ""
            v = v.join(randompass(addVar, int(lenVar)))
            if file.is_file():
                with open(fname,'a') as f:
                    f.write("\n"+v)
                    f.close()
                    print('Generated password: '+v+'\n\nPassword has also been written to file in '+fname+'.\n\n')
            else:
                with open(fname,'w+') as f:
                    f.write(v)
                    f.close()
                    print('Generated password: '+v+'\n\nPassword has also been written to file in '+fname+'.\n\n')
        else:
            print('Input was not a number, try again.')
            time.sleep(2)
            os.system('cls')
