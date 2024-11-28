rak_buku = ["BUKU AJAR PEMROGRAMAN WEB 1 : Iqbal Ramadhani Muklis", 
            "React and React Native, Third Edition : Adam Boduch, Roy Derks", 
            "Python Crash Course: A Hands-On, Project-Based Introduction to Programming : Eric Matthes", 
            "Responsive Web Design with HTML5 and CSS, Fourth Edition : Ben Frain",
            "Full Stack Web Development For Beginners : Riaz Ahmad", 
            "You Dont Know JS Yet (Book Series) : Kyle Simpson"]    

list_data_pinjam = []
list_data_penjualan = {
    "buku_1" : {"judul buku" : "BUKU AJAR PEMROGRAMAN WEB 1 : Iqbal Ramadhani Muklis", "harga" : 90000, "stok" : 10}, 
    "buku_2" : {"judul buku" : "React and React Native, Third Edition : Adam Boduch, Roy Derks", "harga" : 90000, "stok" : 10}, 
    "buku_3" : {"judul buku" : "Full Stack Web Development For Beginners : Riaz Ahmad", "harga" : 90000, "stok" : 10}, 
}

def katalog_buku ():
    print("KATALOG BUKU")
    no = 1
    for katalog in rak_buku:
        print(f"{no}. {katalog}")
        no += 1

def add_buku_pinjam():
    judul_buku = input("Masukkan Judul Buku yang ingin ditambahkan: ")
    rak_buku.append(judul_buku)
    print("Buku berhasil ditambahkan ke daftar buku tersedia.")

def input_peminjaman ():
    while True:
        nama_peminjam = input("Masukkan nama anda : ")

        katalog_buku()
        print("Tekan ESC untuk membatalkan dan kembali ke menu sebelumnya.")
        judul_buku = input("Masukkan judul buku : ").lower()
        tanggal_kembali = input("Masukkan tanggal pengembalian : ")
        
        jawab = input("Apakah kamu mau meminjam buku lagi?:(ya/tidak) ")
        list_data_pinjam[nama_peminjam] = {'Judul Buku': judul_buku, 'Tanggal pengembalian': tanggal_kembali}
        if jawab.lower() != "ya":
            input_menu = input("Apakah kamu ingin kembali ke Menu Peminjaman? (ya/tidak) : ")
            if input_menu.lower() == "ya":
                menu_peminjaman()
            elif input_menu.lower() == "tidak":
                menu_utama_admin()
        print("Peminjaman berhasil diinput.")

def edit_peminjaman ():
    read_data_peminjam
    print("Tekan ESC untuk membatalkan dan kembali ke menu sebelumnya.")
    no = int(input("Masukkan nomor data yang ingin anda edit : "))
    if no < 0 <= len(rak_buku):
        nama_peminjam, judul_buku = list_data_pinjam[no - 1]
        print("Pilih data yang ingin anda edit: ")
        print("1. Nama Peminjam : ")
        print("2. Judul Buku : ")
        print("3. Tanggal Pengembalian : ")
        pilihan = int(input("Masukkan nomor data yang ingin anda edit: "))
        if pilihan == 1:
            nama_baru = input("Masukkan Nama Peminjaman: ")
            list_data_pinjam [nama_baru] = list_data_pinjam.pop(nama_peminjam)
        elif pilihan == 2:
            judul_buku = input("Masukkan Judul Buku Baru: ")
            list_data_pinjam [judul_buku]['Judul Buku'] = judul_buku
        else:
            print("Pilihan Yang Anda Masukkan Invalid")
            return
        list_data_pinjam[no-1] = (nama_peminjam, judul_buku,)
        print("Data Berhasil Di-edit")
    else:
        print("Nomor Tidak Valid")

def read_data_peminjam():
    if not list_data_pinjam:
        print("Tidak ada data peminjaman")
    else:
        print("---Data Peminjam Buku---")
        print("ID | Nama Peminjam | Judul Buku | Tanggal Peminjaman")
        print("-"*40)
        for i, judul_buku in enumerate(rak_buku, start=1):
            print(f"{i}. {judul_buku}")

def hapus_buku_pinjaman():
    katalog_buku()
    indeks = int(input("Masukkan nomor buku yang ingin dihapus: "))
    if 1 <= indeks <= len(rak_buku):
        buku_dihapus = rak_buku.pop(indeks - 1)
        print(f"Buku '{buku_dihapus}' berhasil dihapus")
    else:
        print("Nomor buku tidak valid")

def menu_peminjaman(is_admin=False):
    print("1. Input Peminjaman")
    print("2. Edit Data")
    print("3. Tampilkan Data")
    if is_admin:
        print("4. Tambah Buku Pinjam")
        print("5. Hapus Data")
    
    kode  = input("Masukkan nomor: ")
    if kode == "1":
        input_peminjaman()
    elif kode == "2":
        edit_peminjaman()
    elif kode == "3":
        read_data_peminjam()
    elif kode == "4":
        hapus_buku_pinjaman()
    else:
        print("Pilihan yang Anda masukkan salah.")
    
def input_penjualan ():
    while True:
        nama_pembeli = input("Masukkan nama anda: ")
        katalog_buku()
        kode_buku = int(input("Masukkan kode buku: "))
        katalog_buku()
        judul_buku = input("Masukkan judul buku: ").lower()
        jumlah_buku = int(input("Masukkan jumlah buku yang ingin anda beli: "))
        jawab = input("Apakah kamu mau membeli buku lagi? (ya/tidak) : ")
        list_data_penjualan.append((nama_pembeli, kode_buku, judul_buku, jumlah_buku))
        if jawab != "ya":
            input_menu = input("Apakah kamu ingin kembali ke Menu Penjualan? (ya/tidak) : ")
            if input_menu == "ya":
                menu_penjualan()
            elif input_menu == "tidak":
                menu_utama_user()
        print("Pembelian berhasil diinput.")

def katalog_buku_jual():
    print("KATALOG BUKU JUAL")
    for kode, detail in list_data_penjualan.items():
        print(f"{kode}: {detail['judul buku']}")
        print(f"Harga: Rp {detail['harga']}")
        print(f"Stok: {detail['stok']} buku")
        print("-" * 40)

def add_buku_jual():
    kode_buku_baru = f"buku_{len(list_data_penjualan) + 1}"
    judul_buku = input("Masukkan judul buku baru: ")
    harga_buku = int(input("Masukkan harga buku: "))
    stok_buku = int(input("Masukkan stok buku: "))
    
    list_data_penjualan[kode_buku_baru] = {
        "judul buku": judul_buku, 
        "harga": harga_buku, 
        "stok": stok_buku
    }
    print(f"Buku berhasil ditambahkan dengan kode {kode_buku_baru}")

def hapus_buku_penjualan():
    katalog_buku_jual()
    kode_buku = input("Masukkan kode buku yang ingin dihapus: ")
    if kode_buku in list_data_penjualan:
        del list_data_penjualan[kode_buku]
        print(f"Buku dengan kode {kode_buku} berhasil dihapus")
        return menu_penjualan(is_admin=True)
    else:
        print("Kode buku tidak ditemukan")
    return menu_penjualan(is_admin=True)

def menu_penjualan (is_admin=False):
    print("-----MENU PENJUALAN-----")
    print("1. Beli Buku")
    print("2. Tampilkan Buku yang Tersedia")
    if is_admin:
        print("3. Tambah Buku Jual")
        print("4. Hapus Data")
    kode  = input("Masukkan nomor: ")
    if kode == "1":
        input_penjualan()
    elif kode == "2":
        katalog_buku_jual()
    elif kode == "3":
        add_buku_jual()
    elif kode == "4":
        hapus_buku_penjualan()
    else:   
        print("Pilihan yang Anda masukkan salah.")

def rekomendasi_buku():
    print("1. Rekomendasi Buku Terlaris")
    print("2. Rekomendasi Buku Terbaru")
    
def login():
    print("Anda masuk sebagai apa? : ")
    print("1. Admin")
    print("2. User")
    jawab = int(input("Silahkan masukkan nomer : "))
    if jawab == 1:
        print("Masukkan Username dan Password")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username == "admin" and password == "admin":
            print("Selamat, Anda berhasil login sebagai Admin")
            menu_utama_admin()
        else:
            print("Maaf, Anda salah memasukkan username atau password")
    elif jawab == 2:
        menu_utama_user()
        print("Anda masuk sebagai pengunjung")
    else:
        print("Invalid nomer yang anda masukkan salah")
        login()

def menu_utama_admin():
    print("---APLIKASI PENJUALAN BUKU DAN PEMINJAMAN BUKU PERPUSTAKAAN---")
    print("1. Menu Penjualan")
    print("2. Menu Peminjaman")
    print("3. Katalog Buku")
    print("4. Rekomendasi Buku")
    print("5. Keluar")
    kode  = input("Masukkan nomor: ")
    if kode == "1":
        menu_penjualan(is_admin=True)
    elif kode == "2":
        menu_peminjaman(is_admin=True)
    elif kode == "3":
        katalog_buku()
    # elif kode == "4":
     
    elif kode == "5":
        print("Terima kasih atas kunjungan ke perpustakaan kami😊🙏")
        login()
    else:
        print("Pilihan yang Anda masukkan salah.")

def menu_utama_user ():
    print("---APLIKASI PENJUALAN BUKU DAN PEMINJAMAN BUKU PERPUSTAKAAN---")
    print("1. Menu Penjualan")
    print("2. Menu Peminjaman")
    print("3. Katalog Buku")
    print("4. Rekomendasi Buku")
    print("5. Keluar")
    kode  = input("Masukkan nomor: ")
    if kode == "1":
        menu_penjualan()
    elif kode == "2":
        menu_peminjaman()
    elif kode == "3":
        katalog_buku()
    # elif kode == "4":
     
    elif kode == "5":
        print("Terima kasih atas kunjungan ke perpustakaan kami😊🙏")
        exit
    else:
        print("Pilihan yang Anda masukkan salah.")

login()