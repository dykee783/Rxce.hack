#MANTRIMALL HACK
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date


expirydate = datetime.date(2023, 12, 30)
#expirydate = datetime.date(2021, 8, 30)
today=date.today()
def hero():

    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rhacking in the parity server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!Server is HACKED  ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(5)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(5)
        done = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    sum=0
    def getSum(n):
        print(sum)
        for digit in str():
          sum += int(digit)
        return sum
    clear()
    y=1
    newperiod=period
    banner='figlet RXCE'
    thisway=[2,6,8,11,12,15,16,18,19,20]
    thatway=[1,3,4,5,7,9,10,14,13,17]
    numbers=[]
    i=1
    while(y):
        clear()
        system(banner)
        print(f"MANTRIMALL COLOR HACK")
        print(f"Enter ",newperiod," Parity Price :")
        current=input()
        current=int(current)
        chalo()
        print("\n---------Successfully hacked the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        
        if i in thisway:
            m=getSum(current)
            n=int(current)%10
            if((m%2==0 and n%2==0)or (m%2==1 and n%2==1)):
              if current in numbers:
                  print("Parity",newperiod,": 🔴, RED")
            else:
                print("Parity",newperiod,"  : �, GREEN")
        else:
            if current in numbers:
                print("Parity",newperiod,"  : �, GREEN")
            else:
                print("Parity",newperiod," : 🔴, RED")            
                if i in thatway:
                    m=getSum(current)+1
                    n=int(current)%10
                    if((m%2==0 and n%2==0)or(m%2==1 and n%2==1)):
                        if current in numbers:
                            print("Parity",newperiod,":RED 🔴")
                        else:
                            print("Parity",newperiod,"  : �, GREEN")
                    else:
                        i=i+1
                        newperiod+=1
                        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>11):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n MANTRIMALL COLOR HACK")
            #print(numbers)
if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=20, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=21, minute=55, second=0, microsecond=0)
    Second = now.replace(hour=22, minute=55, second=0, microsecond=0)
    Secondend= now.replace(hour=23, minute=55, second=0, microsecond=0)
    Third= now.replace(hour=23, minute=55, second=0, microsecond=0)
    Thirdend= now.replace(hour=23, minute=55, second=0, microsecond=0)
    Final= now.replace(hour=23, minute=55, second=0, microsecond=0)
    Finalend= now.replace(hour=23, minute=18, second=0, microsecond=0)
if(False):
    period=470
elif(now>First and now<Firstend):
  period=470
  hero()
elif(now>Third and now<Thirdend):
  period=470
  hero()
elif(True):
  period=470
  hero()
else:
 banner= 'figlet RXCE'
 print("Thanks")
