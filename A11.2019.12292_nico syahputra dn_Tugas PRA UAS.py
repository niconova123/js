from tabulate import tabulate 
import itertools as it 
import os
def rms(number):
    if number == 10:
        return "A"
    elif number == 11:
        return "B"
    elif number == 12:
        return "C"
    elif number == 13:
        return "D"
    elif number == 14:
        return "E"
    elif number == 15:
        return "F"
    #fungsi ini bertujuan untuk menggenerate sebuah list tahap2 konversi yang nantinya akan kita masukkan ke
    #fungsi tabulate untuk outputnya
def konversi(number, pembilang): 
    result = []
    hasilAngka = ""
    while True:
        if number >= pembilang:
            result.append(number)
            sisanya = number % pembilang
            number //= pembilang
            if sisanya > 9:
                huruf = rms(sisanya)
                hasilAngka += huruf
                sisanya = "{0} = {1}".format(sisanya, huruf)
            else:
                hasilAngka += str(sisanya)
            divid = "{0}------  {1}".format(pembilang, sisanya)
            result.append(divid)
        else:
            if number > 9:
                number = rms(number)
            hasilAngka += str(number)
            result.append(number)
            break
        result.append("")
    hasilAngka = "".join(reversed(hasilAngka)) #reversed

    return (result, hasilAngka)

def tampil():
    lagi = True
    while (lagi):
        os.system("cls")
        number = int(input("Program Sederhana Untuk Konversi Bilangan Desimal-Biner-Octal-Hexa\nMasukkan Bilangan yang akan dikonversi dalam bentuk Desimal?"))
        biner, hasilBinernya = konversi(number, 2)#untuk biner 
        octal, hasilOctalnya = konversi(number, 8)#untuk oktal
        hexa, hasilHexanya = konversi(number, 16)#untuk hexadecimal
        comb = list(it.zip_longest(biner, octal, hexa))
        hdr = ("Binner", "Octal", "Hexadecimal")
        print(tabulate(comb, hdr, tablefmt="plain"))
        print("")
        print("==============================================================")
        print(f"Binner = {hasilBinernya}\t Octal = {hasilOctalnya}\t Hexa = {hasilHexanya}")    
        lagi = str(input("Apakah ingin mengulangi proses ? [1 = Ya | 0 = Keluar] : "))     
        if lagi == "0":
            break
        elif lagi == "1":
            tampil()
        else:
            print("Input Error")
            return False
tampil()
            


    
    



