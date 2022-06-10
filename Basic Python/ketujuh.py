# for x in range(50,100,2):
#     print (x)
#     time.sleep(1.15)
# print ('hello dear!!')

# name = ""
# while len(name) == 0 :
#     name = input("Enter your name = ")
# print ("Hello " + name.capitalize())

# while True:
#     name = input("Enter yourname = ")
#     if name != "":
#         print("hello "+name)
#         break

# rows = int(input("berapa baris = "))
# coloumn = int(input("berapa kolom = "))
# symbol = input("masukkan simbol =")

# for i in range (rows):
#     for j in range (coloumn):
#         print(symbol, end="")
#     print()

# def hello(name):
#     print ("hello ")
# hello("dude")

# def multiply (number1, number2):
#     return number1 * number2
# x = multiply (int(input("number1 = ")) , int(input ("number2 = ")))
# print (x)

# import random
# x = random.randint(1,6)
# y = random.random()
# print (x)
# myList = ['rock','paper','scissor']
# z = random.choice(myList)

# print (z)

# phone = "+62-858-9194-4114"
# for i in phone :
#     if i == "-":
#         continue
#     print (i, end=(""))

# def total (n_uh, n_ts ,n_us):
#     n_total = (n_uh + n_ts + n_us) / 3
#     if n_total >= 85:
#         print ("Predikat : A")
#     elif n_total >= 70 < 85:
#         print ("Predikat : B")
#     elif n_total >= 60 < 70 :
#         print ("Predikat : C")
#     else :
#         print ("Anda Harus Mengulang !!")
#     return n_total
# total (10,50,50)

def halo ():
    print("Hello World!!")
def hilo():
    print("Hola")
halo()