# import packages
import sys
import time

# pengulangan untuk pemilihan operasi dan menu keluar
x = "curut"
while x == "curut":
    # pilihan operasi
    operator = str(
        input(
            'Pilih operator "penambahan", "pengurangan", "perkalian", atau "pembagian" : '
        )
    )
    # pemilihan angka-angka
    number1 = int(input("Masukkan angka pertama: "))
    number2 = int(input("Masukkan angka kedua: "))

    # operasi penambahan
    if operator == "penambahan":
        res = number1 + number2
    # operasi pengurangan
    elif operator == "pengurangan":
        res = number1 - number2
    # operasi perkalian
    elif operator == "perkalian":
        res = number1 * number2
    # operasi pembagian
    elif operator == "pembagian":
        res = number1 / number2

    # print hasil operasi
    print(f"{operator} dari {number1} dan {number2} adalah {res}")
    # input pemelihan menu keluar
    keluar = str(input("apakah anda ingin keluar (y/n) => "))
    if keluar == "y":
        time.sleep(2)
        sys.exit()
