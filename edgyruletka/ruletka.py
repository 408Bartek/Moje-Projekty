import os
import random
import sys
import time

nagroda = 0

while True:
    os.system('cls')
    print("Rosyjska ruletka 1.0")
    input("Naciśnij ENTER aby spotkać swoje przeznaczenie")

    kula = random.randint(1, 10)

    if kula == 5:
        os.system('cls')
        time.sleep(2)
        print("Wykonałeś strzał")
        time.sleep(2)
        print("Umarłeś")
        sys.exit()
    else:
        os.system('cls')
        time.sleep(2)
        print("Wykonałeś strzał")
        time.sleep(2)
        print("Żyjesz")
        nagroda = nagroda + 10000
        print("Wygrałeś 10000 PLN, twoja wygrana to",nagroda,"PLN")
        print("Naciśnij ENTER aby grać dalej i zaryzykować wszystko")
        input("Naciśnij ALT + F4 aby uciec z nagrodą i zapomnieć o wszystkim")
