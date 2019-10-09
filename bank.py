pin = 1234 # variabeln tilldelas namnet pin och värdet 1234

userPin = int(input("skriv in din pinkod: ")) # här frågar programmet om din pinkod

if pin != userPin: # fel pinkod == error
    exit()

f = open("saldo2.txt", "r") # variablen f tilldelas en funktion
saldo = int(f.read())
f.close()

menu = 0

while menu != 3:
    print("ditt saldo ät: " + str(saldo) + "Kr")
    menu = int(input("skriv ditt val[1, 2, 3]: ")) # konverterat en string til en int, stringen får funktionen att välja alternativ 1-3
    if menu == 1:  # variabln 1 ges funktionen saldo + insättning
        print("insättning")
        saldo = saldo + int(input("gör en insättning: "))
    elif menu == 2: # variabln 2 ges funktionen saldo - uttdrag
        print("uttag")
        utdrag = int(input("gör en uttag: "))
        saldo = saldo - utdrag
        if saldo < 0:  
            print("Du kan inte ta ut pengar du inte har")
            saldo += utdrag # om saldo är mindre än noll nekas uttag
    else:
        print("fel eller avslut")
f = open('saldo2.txt', 'w')
f.write(str(saldo))
f.close() #om 3 sparas saldot i textdokumentet och avslutar