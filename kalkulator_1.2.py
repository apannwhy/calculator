# import packages
import sys
import time

x = "curut"
while x == "curut":
    print("=== MENU PILIHAN ===")
    print("1. penambahan \n" "2. pengurangan \n" "3. perkalian \n" "4. pembagian")
    # pilihan operasi
    operator = str(input("input => "))
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
    # input pemelihan user keluar
    keluar = str(input("apakah anda ingin keluar (y/n) => "))
    if keluar == "y":
        time.sleep(2)
        sys.exit()
