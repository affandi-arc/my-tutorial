# x = 2
# y = 3
# z = 9
# hasil = x ** y / z // y * y - z + x 
# print (x , '**', y , '/' , z , '//' , y , '*' ,  y , '-', z , '+', x)
# print ("hasilnya adalah = ", hasil)

# print ("==== PENJUMLAHAN ====")
# x = int (input("masukkan angka ="))
# y = int (input("masukkan angka ="))
# hasil = x + y 
# print ("hasilnya adalah =", hasil)

# print (input ("MASUKKAN NAMA = "))
# print("==== NILAI RAPOT ====")
# rapot= float (input ("masukkan nilai Rapot = "))
# if (rapot > 7.5) :
#     print ("CONGRATULATIONS!!! YOU'RE PASSED!!")
# else :
#     print ("YOU'RE FAILED!!!!")
#############################################################


# print ("==== PROGRAM KONVERSI TEMPERATUR DARI CELCIUS ====")
# celcius = float (input ("MASUKKAN SUHU DALAM CELCIUS = "))
# print ("Suhu adalah = ", celcius, "Celcius")
# #REAMUR 
# reamur = (4/5)*celcius 
# print ("Suhu dalam reamur adalah = ", reamur, "Reamur")
# #Fahrenheit
# fahrenheit = ((9/5)*celcius) + 32
# print ("Suhu dalam Fahrenheit adalah = ", fahrenheit, "Fahrenheit")
# #Kelvin
# kelvin = celcius + 273
# print ("Suhu dalam kelvin adalah = ", kelvin , "Kelvin")
# ############################################################
# print ("==== PROGRAM KONVERSI TEMPERATUR DARI REAMUR ====")

# reamur = float (input (" MASUKKAN SUHU DALAM REAMUR = "))
# print ("Suhu adalah = ", reamur, "Reamur")
# #Celcius
# celcius = (5/4) * reamur
# print ("Suhu dalam Celcius adalah = ", reamur, "Celcius")
# #Fahrenheit
# fahrenheit = ((9/4)*reamur) + 32
# print ("Suhu dalam fahrenheit adalah = ", fahrenheit, "Fahrenheit")
# kelvin = celcius + 273
# print ("Suhu dalam kelvin adalah = ", kelvin, "Kelvin")
############################################################


print ("==== PROGRAM KONVERSI TEMPERATUR DARI FAHRENHEIT====")

fahrenheit = float (input("MASUKKAN SUHU DALAM FAHRENHEIT = "))
print ("Suhu adalah = ", fahrenheit, "Fahrenheit")
#celcius
celcius = ((5/9) *(fahrenheit - 32))
print ("Suhu dalam celcius adalah = ", celcius, "Celcius")
#Kelvin
kelvin = celcius + 273
print ("Suhu dalam Kelvin adalah ", kelvin, "Kelvin")
############################################################


print ("==== PROGRAM KONVERSI TEMPERATUR DARI KELVIN ====")
kelvin = float (input ("Masukkan Suhu dalam Kelvin = "))
print ("Suhu adalah = ", kelvin, "Kelvin")
#celcius
celcius = kelvin - 273
print ("Suhu dalam celcius adalah = ", celcius, "Celcius")
#fahrenheit
fahrenheit = ((9/5)*celcius) + 32 
print ("Suhu dalam fahrenheit adalah = ", fahrenheit, "Fahrenheit")

'''
untuk tanda ,(koma) merupakan sebuah input pemisah kalimat
namun untuk menggabungkan kita bisa menggunakan tanda + (tambah)
'''