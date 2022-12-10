import threading
import time
import requests
import sys
from pyfiglet import Figlet
from clint.arguments import Args
from clint.textui import puts, colored, indent
from database_test import *
from cricket_score import *


def first():
    x = requests.get(f"http://numbersapi.com/{sys.argv[2]}/{sys.argv[3]}/date")
    #print(x.text)
    puts(colored.blue(f'{x.text}'))
    create_table()
    insert_values("{}/{}".format(sys.argv[2],sys.argv[3]),x.text)

    


def secound():
    f = Figlet(font='slant')
    print (f.renderText('WELCOME'))
    #print(sys.argv)
    


t1 = threading.Thread(target=first)
t2 = threading.Thread(target=secound)
t3 = threading.Thread(target=cricket)
t2.start()
t2.join()

if sys.argv[1] == 'trivia':
    if len(sys.argv) < 4:
        puts(colored.red("PLEASE ENTER DATE AND MONTH"))
    else:
        t1.start()
        t1.join()
elif sys.argv[1] == 'cricket':
    if len(sys.argv) < 3:
        puts(colored.red("PLEASE MENTION THE ACTION TO PERFORM"))
    else:
        if sys.argv[2] == 'score':
            t3.start()
            t3.join()
        else:
            puts(colored.red("NOT A VALID ACTION"))


else:
    puts(colored.red("NOT AN VALID PARAMETER"))
    
#t3.start()