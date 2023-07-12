from avg import Avg
import sys
from prec import Prec
from calc import Calc
def checkDefaultCommands():
    print("please click enter to start")
    cmd = input("-->")
    compete = False
    while not compete:
        cmd = input("-->")
        cmd = cmd.lower()
        if cmd == "avg":
            Avg()
            compete = True
        elif cmd == 'calc':
            Calc()
            compete = True
        elif cmd == "prec":
            Prec()
            compete = True
        
        elif cmd == "quit":
            sys.exit()
        else:
            print("--------Unrecognized input---------")
    
            

def help():
    print("""


    ---***********************---
    *****Calculator v1.0 by adam*****
        cammands
        -------------
        avg = open average calculator 
        calc = open calculator
        prec = open precentage calculator 
        quit = quit
    *************************************
        

        """)

help()
checkDefaultCommands()

