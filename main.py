from GULA import Stack

sdll = Stack()
def mainmenu():
    loop = True
    while(loop):
        print("\n")
        print(40*"-")
        print("==============Stok GULAKU================")
        print(40*"-")
        print(" 1. Tambah Data")
        print(" 2. Hapus data")
        print(" 3. Cek Data kosong atau tidak")
        print(" 4. Jumlah Data")
        print(" 5. Cari Data")
        print(" 6. Keluar Program")
        pilih = str (input("\nMasukan Nomor pilihan Anda:"))
        if pilih == "1":
            print("nb.masukan 0 untuk kembali ke menu utama")
            tambah = str(input("Masukan Stock:"))
            sdll.push(tambah)
            print(f"Anda menambahkan stock {tambah} pada tumpukan")
            sdll.cetakStack()
        elif pilih =="2":
            print("Stock"+sdll.pop()+"sudah diambil \n")
            sdll.cetakStack()
        elif pilih =="3":
            print(f"Aapakah stock kosong? {sdll.isEmpty()}")
            if sdll.isEmpty() != None:
                sdll.cetakStack()
        elif pilih =="4":
            sdll.cetakStack()
            print(f"jumlah stock tersedia sebanyak: {sdll.size()}")
        elif pilih =="5":
            sdll.cetakStack()
            print(f"Jumalah stock teratas saat ini: {sdll.top()}")
        elif pilih == "6":
            exit()
        else:
            print("INPUT TIDAK DITEUKAN!!!")

if __name__=='__main__':
    mainmenu()
            