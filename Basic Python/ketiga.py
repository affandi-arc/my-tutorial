#Contoh pengulangan While 
# from itertools import count


# count = 0
# while (count < 1000):
#     print ('The Count is = ', count)
#     count = count + 200
# print ("Good bye")

# name = (input ("Masukkan nama anda = "))
# height = int (input ("Masukkan tinggi anda = "))
# weight = int (input ("Masukkan berat badan anda = "))
# print (name +"tinggi dan berat anda adalah = " + str (weight + height) 
#  + " CM")


# a = 12
# b = 13
# hasil = a == 4
# print (hasil , hex(id(a)))
# print (hasil , hex(id(b)))

# ========= NOT ==========
print ("===== NOT ===== ( atau inverter) ")
a = False 
c = not a
print ("result logic gates of", "inverter",a ,"=", c)

# ======= OR =========
print ("===== OR ====== (atau penjumlahan )")
a = True
b = False
c = a or b
print ("result logic gates of",a ,"+",b,"=" , c)

#===== AND ======
print("=====AND===== (atau perkalian) ")
a = True
b = True
c = a and b
print ("result logic gates of",a ,"*",b,"=" , c)

print ("\n",25*"=", "\n")

# Komparasi matematika
'''
simbol perbandingan
== kedua value sama maka 'True'
!= kedua value sama maka 'False'
< atau > akan 'True" jika benar
<= atau >= akan 'True' jika value sesuai sama atau benar
is 
is not
'''
a = 5
b = 2

print ( "perbandingan", a, "is", 5, "=", a is not 5)