import datetime
import os
import random
import string



siswaTemplate = {
    'nama' : 'name',
    'nisn' : '111111',
    'kelas': 0,
    'lahir': datetime.date(1111,1,1)
}

dataSiswa = {}

while True :
   
        
    os.system("cls")
    print (f"{'WELCOME!!':^20}")
    print (f"{'DATA SISWA':^20}")
    print ('='*20)

    siswa = dict.fromkeys(siswaTemplate.keys())
    siswa['nama'] = input("Masukkan Nama Siswa :")
    siswaNama = siswa['nama']

    siswa['nisn'] = int(input("Masukkan NISN Siswa :"))
    siswaNisn = siswa['nisn']
    
    siswa['kelas'] = int(input("Masukkan Kelas Siswa :"))
    siswaKelas = siswa['kelas']

    tahunLahir = int(input("Tahun Lahir Siswa :"))
    bulanLahir = int(input("Bulan Lahir Siswa :"))
    tanggalLahir = int(input("Tanggal Lahir Siswa :"))
    siswa['lahir']= datetime.date(tahunLahir,bulanLahir,tanggalLahir)
    siswaLahir = siswa['lahir']

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range (6)))
    dataSiswa.update({KEY : siswa})

    print (f"{'KEY':<6} {'NAMA' :<13} {'NISN':<9} {'KELAS':<6} {'LAHIR':<10}  " )
    print ("="*52)

    for siswa in dataSiswa : 
        KEY  =  siswa
        NAMA = dataSiswa [KEY]['nama']
        NISN  = dataSiswa [KEY]['nisn']
        KELAS =  dataSiswa [KEY]['kelas']
        LAHIR = dataSiswa [KEY]['lahir'].strftime("%x")
        
        print (f"{KEY:<6} {NAMA :<13} {NISN:<9} {KELAS:<6} {LAHIR:<10}  " )


    endProgram = input ("Lanjut (y/n): ").lower()
    if endProgram != "n":
        continue
    else : 
        break
print ("Good Bye!!")
