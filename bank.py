pin = 1234

userPin = int(input("skriv in din pinkod: "))

if pin != userPin:
    exit()

saldo = 0.0
menu = 0
# print ("menu 1 insättning")
# print ("menu 2 uttag")
# print ("menu 3 avsluta")
while menu != 3:
    print("ditt saldo ät: " + str(saldo) + "Kr")
    menu = int(input("skriv ditt val[1, 2, 3]: "))
    if menu == 1:
        print("insättning")
        saldo = saldo + float(input("gör en insättning: "))
    elif menu == 2:
        print("uttag")
        saldo = saldo - float(input("gör en uttag: "))
    else:
        print("fel eller avslut")
