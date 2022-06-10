import random
while True:
    list = ["batu","gunting","kertas"]
    computer = random.choice(list)
    player   = None
    
    while player not in list: 
        player = input ("Gunting, Batu, atau Kertas = ").lower()
        if  len(player)== 0:
            print ("Jangan dikosongi!!")
        elif player not in  list:
            print ("Jangan ngaco !!")
    if player == computer:
        print ("Computer = ", computer)
        print ("Player = ",player)
        print ("Draw!")
    elif player == "batu":
        if computer == "gunting":
            print ("Computer\t=", computer)
            print ("Player\t= ",player)
            print ("Kamu Menang!")
        if computer == "kertas":
            print ("Computer\t= ", computer)
            print ("Player\t= ",player)
            print ("Kamu Kalah!")
    elif player == "gunting":
        if computer == "kertas":
            print ("Computer\t= ", computer)
            print ("Player\t= ",player)
            print ("Kamu Menang!")
        if computer == "batu":
            print ("Computer\t= ", computer)
            print ("Player\t= ",player)
            print ("Kamu Kalah!")
    elif player == "kertas":
        if computer == "batu":
            print ("Computer\t= ", computer)
            print ("Player\t= ",player)
            print ("Kamu Menang!")
        if computer == "gunting":
            print ("Computer\t= ", computer)
            print ("Player\t= ",player)
            print ("Kamu Kalah!")

    play_again = input("Main Lagi? (y/n)  ".lower())
    if play_again != "y":
        break
print ("Bye!")

