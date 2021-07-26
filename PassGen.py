import random
import os
import time
from pathlib import Path

file = Path('Output.txt')
fname = 'Output.txt'

os.system('title Xaelitry\'s Secure Password Generator')

def randompass(length):
    return "".join([random.choice('!@#$%^&*_+-=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for x in range(int(length))])

if __name__ == "__main__":

    while True:

        p = input("What is the password for? ")
        mail = input("Enter email attached to account: ")
        lenV = input("Set length for password: ")

        if lenV.isdigit():
            pw = randompass(int(lenV))
            v = ""
            v = v.join(p.title()+":\nEmail: "+mail+"\nPassword: "+pw)
            if file.is_file():
                with open(fname, 'a') as f:
                    f.write("\n\n"+v)
                    f.close()
                    print('Generated password for '+p.title()+'\nPassword: '+pw+'\n\nPassword has also been written to file in '+fname+'.\n\n')
            else:
                with open(fname, 'w+') as f:
                    f.write(v)
                    f.close()
                    print('Generated password for '+p.title()+'\nPassword: '+pw+'\n\nPassword has also been written to file in '+fname+'.\n\n')

            cont = input('Do you want to continue? [Y/N] ')
            yes = ('y' or 'yes')
            no = ('n' or 'no')
            if cont == yes.lower():
                print('Moving onto next job.')
                time.sleep(3)
                os.system('cls')
                continue
            elif cont == no.lower():
                print('Very good sir, closing application.')
                time.sleep(3)
                exit()
            else:
                print('An error occurred, input was not recognized.')
                time.sleep(3)
                os.system(cls)
                continue
            
        else:
            print("Input for length was not a number, try again.")
            time.sleep(3)
            os.system("cls")
            continue
