rak_buku = ["BUKU AJAR PEMROGRAMAN WEB 1 : Iqbal Ramadhani Muklis", 
            "React and React Native, Third Edition : Adam Boduch, Roy Derks", 
            "Python Crash Course: A Hands-On, Project-Based Introduction to Programming : Eric Matthes", 
            "Responsive Web Design with HTML5 and CSS, Fourth Edition : Ben Frain",
            "Full Stack Web Development For Beginners : Riaz Ahmad", 
            "You Dont Know JS Yet (Book Series) : Kyle Simpson"]

list_data_pinjam = []
list_data_penjualan = []

# seluruh_rak = len(rak_buku)
# print (" ", seluruh_rak, " ",rak_buku,)

def katalog_buku ():
    print("KATALOG BUKU")
    no = 1
    for katalog in rak_buku:
        print(f"{no}. {katalog}")
        no += 1

def data_peminjaman ():
    while True:
        katalog_buku()
        nama_peminjam = input("Masukkan nama anda: ")
        kode_buku = int(input("Masukkan kode buku: "))
        judul_buku = input("Masukkan judul buku: ")
        jumlah_pinjaman = int(input("Masukkan jumlah peminjaman buku: "))
        jawab = input("Apakah kamu mau meminjam buku lagi?:(ya/tidak) ")
        list_data_pinjam.append((nama_peminjam, kode_buku, judul_buku, jumlah_pinjaman))
        if jawab != "ya":
            break   
        print("Peminjaman berhasil diinput.")

def edit_peminjaman ():
    katalog_buku()
    no = int(input("Masukkan nomor data yang ingin anda edit: "))
    if no < 0 <= len(rak_buku):
        nama_peminjam, kode_buku, judul_buku, jumlah_peminjaman = list_data_pinjam[no - 1]
        print("Pilih data yang ingin anda edit: ")
        print("1. Nama Peminjam: ")
        print("2. Judul Buku: ")
        print("3. Jumlah Peminjaman: ")
        pilihan = int(input("Masukkan nomor data yang ingin anda edit: "))
        if pilihan == 1:
            nama_peminjam = input("Masukkan Nama Peminjaman: ")
        elif pilihan == 2:
            judul_buku = input("Masukkan Judul Buku Baru: ")
        elif pilihan == 3:
            jumlah_peminjaman = input("Masukkan Jumlah Peminjaman: ")
        else:
            print("Pilihan Yang Anda Masukkan Invalid")
            return
        list_data_pinjam[no-1] = (nama_peminjam, kode_buku, judul_buku, jumlah_peminjaman)
        print("Data Berhasil Di-edit")
    else:
        print("Nomor Tidak Valid")

def menu_peminjaman ():
    print("1. Input Peminjaman")
    print("2. Edit Data")
    print("3. Tampilkan Data")
    print("4. Hapus Data")
    kode  = input("Masukkan nomor: ")
    if kode == "1":
        data_peminjaman()
    elif kode == "2":
    elif kode == "3":
    elif kode == "4":
    else:
        print("Pilihan yang Anda masukkan salah.")
    
def data_penjualan ():
    while True:
        nama_pembeli = input("Masukkan nama anda: ")
        kode_buku = int(input("Masukkan kode buku: "))
        judul_buku = input("Masukkan judul buku: ")
        jumlah_buku = int(input("Masukkan jumlah buku yang ingin anda beli: "))
        jawab = input("Apakah kamu mau membeli buku lagi?:(ya/tidak) ")
        list_data_penjualan.append((nama_pembeli, kode_buku, judul_buku, jumlah_buku))
        if jawab != "ya":
            break   
        print("Pembelian berhasil diinput.")

def menu_penjualan ():
    print("1. Input Penjualan")
    print("2. Edit Data")
    print("3. Tampilkan Data")
    print("4. Hapus Data")
    kode  = input("Masukkan nomor: ")
    if kode == "1":
        data_penjualan()
    elif kode == "2":
    elif kode == "3":
    elif kode == "4":
    else:
        print("Pilihan yang Anda masukkan salah.")

def menu_utama ():
    print("1. Data Penjualan")
    print("2. Data Peminjaman")
    print("3. Katalog Buku")
    print("4. Rekap Data")
    print("5. Keluar")
    kode  = input("Masukkan nomor: ")
    if kode == "1":
        
    elif kode == "2":
        
    elif kode == "3":
       
    elif kode == "4":
     
    elif kode == "5":
      
    else:
        print("Pilihan yang Anda masukkan salah.")