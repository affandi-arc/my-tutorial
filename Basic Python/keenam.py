# #dictionary
import datetime 
import os

os.system("cls")
mahasiswa1 = {
    'nama' : 'Affandi',
    'nim' : '111111',
    'sks_lulus': '144',
    'beasiswa' : False,
    'lahir' : datetime.date(2001,4,11)

}
mahasiswa2 = {
    'nama' : 'Wakyok',
    'nim' : '222222',
    'sks_lulus': '112',
    'beasiswa' : True,
    'lahir' : datetime.date(1999,2,19)

}
mahasiswa3 = {
    'nama' : 'Bogeng',
    'nim' : '333333',
    'sks_lulus': '120',
    'beasiswa' : False,
    'lahir' : datetime.date(2000,2,29)

}

dataMahasiswa = {
  'MS001' : mahasiswa1,
  'MS002' : mahasiswa2,
  'MS003' : mahasiswa3

}

print (f"{'KEY':<6} {'NAMA' :<13} {'NIM':<7} {'SKS':<6} {'BEASISWA':<9} {'LAHIR':<10}  " )
print ("="*52)

for mahasiswa in dataMahasiswa : 
  KEY  =  mahasiswa
  NAMA = dataMahasiswa [KEY]['nama']
  NIM  = dataMahasiswa [KEY]['nim']
  SKS =  dataMahasiswa [KEY]['sks_lulus']
  BEASISWA = dataMahasiswa [KEY]['beasiswa']
  LAHIR = dataMahasiswa [KEY]['lahir'].strftime("%x")
  
  print (f"{KEY:<6} {NAMA :<13} {NIM:<7} {SKS:<6} {BEASISWA:^9} {LAHIR:<10}  " )


# capitals.update({'Indonesia': 'Jakarta'})
# capitals.update({'Russia': 'Jakarta'})

# print (capitals ['Indonesia'])
# print (len(capitals))

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]


# def hello (first, middle, last):
#   print ("Hello " + first + " "+ middle + " "+ last)
# hello(last = "Bro", middle= "Dude", first= "Affandi")

# name = "Dude"

# def display_name ():
#   name = "Bruh"
#   print (name)
# display_name()
# print (name)
