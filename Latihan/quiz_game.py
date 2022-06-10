import os 


#---------------
def new_game ():
    os.system ("clear")

    guesses = []
    correct_guesses = 0
    question_num = 1
    for x in pertanyaan:
        print ("="*30)
        print (x)
        for i in pilihan[question_num-1] :
            print (i)
        guess = input("Masukkan A, B, C, D, atau E : ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(pertanyaan.get(x),guess)
        question_num += 1
    display_score(correct_guesses,guesses)
#---------------
def check_answer (answer, guess):
    if answer == guess:
        print ("Adalah Benar !!")
        return 1
    else :
        print ("SALAH !!!!")
        return 0
#---------------
def display_score (correct_guesses, guesses):
    print ("="*20)
    print ("Nilai  : ")
    print ("="*20)

    print ("Jawabannya : ", end="")
    for i in pertanyaan:
        print (pertanyaan.get(i), end="")
    print ()

    print ("Jawabanmu : ", end="")
    for i in guesses: 
        print (i, end="")
    print ()
    
    score = int(correct_guesses/len(pertanyaan)*100)
    print ("Nilaimu adalah : " + str(score)+ "/100")
#---------------
def play_again():
    
    while True:
        response = input("Apakah anda ingin bermain lagi (Y/n) : ").lower()
        if len(response) == 0:
            print (response)
        elif response == "y":
            return True
        else : 
            return False
#---------------

pertanyaan = {
    "Apa nama ibukota negara Indonesia : ": "A",
    "Siapakah nama Presiden Indonesia pertama : " : "B",
    "Persatuan Indonesia. Merupakan isi Pancasila sila ke- :": "B",
    "Hari Sumpah Pemuda diperingati setiap tanggal : " : "C",
    "Bentuk sistem pemeritahan Indonesia adalah : " : "A"
}
pilihan = [
    ["A. Jakarta","B. Bandung","C. Surabaya","D. Yogyakarta","E. Aceh"],
    ["A. Adolf Hitler","B. Soekarno","C. Vladimir Lenin","D. Van den Bosch","E. John F. Kennedy"],
    ["A. 8","B. 3","C. 1","D. 2","E. 5"],
    ["A. 19 Mei","B. 25 Desember","C. 28 Oktober","D. 10 November","E. 1 April"],
    ["A. Presidensial","B. Parlementer","C. Diktator","D. Demokrasi Terpimpin","E. Sekularis"]
]
new_game()
while play_again():
    new_game()

print ("Selamat Tinggal !! :)")