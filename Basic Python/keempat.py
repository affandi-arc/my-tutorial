#membuat gabungan logika dan komparasi
# ++++++++3--------10+++++++
# True     False     True
# result value
# x = int (input("masukkan angka kurang dari 3 \natau lebih dari 10 = "))
# y = (x < 3)
# print ("Kurang dari 3 =", y)
# z = ( x > 10)
# print ("lebih dari 10 =", z)
# x = y or z 
# print ("result value is a ", x)

# # -------3+++++++++10------
# # False   True      False
# print( 25*"=")
# x = int (input("masukkan angka lebih dari 3 \ndan kurang dari 10 = "))
# y = (x > 3)
# print ("lebih dari 3 =", y)
# z = (x < 10)
# print ("kurang dari 10 =", z)
# x = y and z
# print("result value is a ", x)

# ------0+++++++5-------9+++++++12------
# False  True    False   True     False
# print( 25*"=")
# x = int (input ("Masukkan angka antara 0 sampai 5 \ndan 9 sampai 12 = "))
# y = (x > 0 and x < 5 ) or (x > 9 and x < 12)
# y = 0 < x < 5 or 9 < x < 12
# print ("result value is a ", y)

# # # ++++++0-------5+++++++9--------12++++++
# # # # True   False   True    False     True
# print( 25*"=")

# x = int (input ('masukkan angka kurang dari 0 \n atau antara 5 sampai 9 atau \nlebih dari 12 = '))
# if ( 0 > x or 5 < x < 9 or 12 > x):
#     print (True)
# else :
    # print (False)
# print ("value =", y)


for i in range (0,11):
    for j in range (1,11):
        print (i+j, end="")
    print ()