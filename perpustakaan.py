rak_buku = ["BUKU AJAR PEMROGRAMAN WEB 1 : Iqbal Ramadhani Muklis", 
            "React and React Native, Third Edition : Adam Boduch, Roy Derks", 
            "Python Crash Course: A Hands-On, Project-Based Introduction to Programming : Eric Matthes", 
            "Responsive Web Design with HTML5 and CSS, Fourth Edition : Ben Frain",
            "Full Stack Web Development For Beginners : Riaz Ahmad", 
            "You Dont Know JS Yet (Book Series) : Kyle Simpson"]    

list_data_pinjam = {}
list_data_penjualan = []
list_buku_penjualan = {
    "buku 1" : {"judul buku" : "BUKU AJAR PEMROGRAMAN WEB 1 : Iqbal Ramadhani Muklis", "harga" : 90000, "stok" : 10}, 
    "buku 2" : {"judul buku" : "React and React Native, Third Edition : Adam Boduch, Roy Derks", "harga" : 90000, "stok" : 10}, 
    "buku 3" : {"judul buku" : "Full Stack Web Development For Beginners : Riaz Ahmad", "harga" : 90000, "stok" : 10},
    "buku 4" : {"judul buku" : "Python Crash Course: A Hands-On, Project-Based Introduction to Programming : Eric Matthes", "harga" : 90000, "stok" : 10},
    "buku 5" : {"judul buku" : "Responsive Web Design with HTML5 and CSS, Fourth Edition : Ben Frain", "harga" : 90000, "stok" : 10},
    "buku 6" : {"judul buku" : "You Dont Know JS Yet Yet (Book Series) : Kyle Simpson", "harga" : 90000, "stok" : 10},
}

def katalog_buku ():
    print("---KATALOG BUKU---")
    no = 1
    for katalog in rak_buku:
        print(f"{no}. {katalog}")
        no += 1

def add_buku_pinjam(a):
    judul_buku = input("Silahkan Masukkan Judul Buku yang ingin ditambahkan: ")
    rak_buku.append(judul_buku)
    print("Buku berhasil ditambahkan ke daftar buku tersedia.")
    menu_peminjaman(a)

def input_peminjaman (a):
    while True:
        nama_peminjam = input("Silahkan Masukkan Nama Anda : ")
        katalog_buku()
        judul_buku = input("Masukkan Judul Buku : ")
        if judul_buku not in rak_buku:
            print("Buku Tidak Tersedia")
            menu_peminjaman(a)
        tanggal_peminjaman = input("Masukkan Tanggal Peminjaman : ")
        list_data_pinjam[nama_peminjam] = {'Judul Buku': judul_buku, 'Tanggal Peminjaman': tanggal_peminjaman}
        print("Buku berhasil dipinjam")
        jawab = input("Apakah Anda Ingin Meminjam Buku Lagi?:(ya/tidak) ")
        if jawab.lower() != "ya":
            input_menu = input("Apakah Anda ingin kembali ke Menu Peminjaman? (ya/tidak) : ")
            if input_menu.lower() == "ya":
                menu_peminjaman(a)
            elif input_menu.lower() == "tidak":
                menu_utama_admin(a) or menu_utama_user(a)
        print("Peminjaman berhasil diinput.")

def edit_peminjaman (a):
    list_data_pinjam.items()
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

def read_data_peminjam(a):
    if not list_data_pinjam:
        print("Tidak ada data peminjaman")
    else:
        print("---DATA PEMINJAMAN BUKU---")
        print("ID | Nama Peminjam | Judul Buku | Tanggal Peminjaman")
        print("-"*40)
        no = 1
        for nama_peminjam, data in list_data_pinjam.items():
            print(f"{no:2} | {nama_peminjam:18} | {data["Judul Buku"]:40} | {data["Tanggal Peminjaman"]}")
            no += 1

def hapus_buku_pinjaman(a):
    katalog_buku()
    indeks = int(input("Masukkan nomor buku yang ingin dihapus: "))
    if 1 <= indeks <= len(rak_buku):
        buku_dihapus = rak_buku.pop(indeks - 1)
        print(f"Buku '{buku_dihapus}' berhasil dihapus")
    else:
        print("Nomor buku tidak valid")
        menu_utama_admin(a)

def pengembalian_buku (a):
    read_data_peminjam(a)
    no = int(input("Masukkan nomor data yang ingin anda kembalikan : "))
    if no < 0 <= len(rak_buku):
        nama_peminjam, judul_buku = list_data_pinjam[no - 1]
        print("Pilih data yang ingin anda kembalikan: ")
        print("1. Nama Peminjam :")
        print("2. Judul Buku : ")
        pilihan = int(input("Masukkan nomor data yang ingin anda kembalikan: "))
        if pilihan == 1:
            nama_baru = input("Masukkan Nama Peminjaman: ")
            list_data_pinjam [nama_baru] = list_data_pinjam.pop(nama_peminjam)
        elif pilihan == 2:
            judul_buku_baru = input("Masukkan Judul Buku Baru: ")
            list_data_pinjam [judul_buku_baru] = list_data_pinjam.pop(judul_buku_baru)
        else:
            print("Pilihan Yang Anda Masukkan Invalid")
            return
        print("Data Berhasil Di-kembalikan")    
        menu_peminjaman(a)                       
             
def menu_peminjaman(a):
    while True:
        ('----MENU PEMINJAMAN BUKU')
        print("1. Input Peminjaman")
        print("2. Edit Data")
        print("3. Tampilkan Data")
        print("4. Kembali ke Menu Utama")
        if a == "admin":
            print("5. Tambah Buku Pinjam")
            print("6. Pengembalian Buku")
            print("7. Hapus Data")
        kode = input("Masukkan nomor: ")
        if kode == "1":
            input_peminjaman(a)
        elif kode == "2":
            edit_peminjaman(a)
        elif kode == "3":
            read_data_peminjam(a)
        elif kode == "4":
            menu_utama_admin(a) or menu_utama_user(a) 
        elif kode == "5":
            add_buku_pinjam(a)
        elif kode == "6":
            pengembalian_buku(a)
        elif kode == "7":
            hapus_buku_pinjaman(a)
        else:
            print("Pilihan yang Anda masukkan salah.")
    
def input_penjualan (a):
    while True:
        id_penjualan = len(list_data_penjualan)
        nama_pembeli = input("Masukkan nama anda: ")
        katalog_buku_jual(a)  
        kode_buku = input("Masukkan kode buku: ") 
        if kode_buku not in list_buku_penjualan:
            print("Buku tidak ada di katalog")
            menu_penjualan(a)
        jumlah_buku = int(input("Masukkan jumlah buku yang ingin anda beli: "))
        list_data_penjualan.append((id_penjualan, nama_pembeli, kode_buku, jumlah_buku))
        print("Pembelian berhasil diinput.")
        if kode_buku in list_buku_penjualan:
            if list_buku_penjualan[kode_buku]["stok"] >= jumlah_buku:
                harga = list_buku_penjualan[kode_buku]["harga"]
                total_harga = harga * jumlah_buku
                list_buku_penjualan[kode_buku]["stok"] -= jumlah_buku
                print(f"Total harga untuk {jumlah_buku} buku {list_buku_penjualan[kode_buku]['judul buku']} adalah: {total_harga}")
                print("Silahkan untuk melakukan pembayaran ke kasir perpustakaan")
            else:
                print("Stok tidak cukup!")
        else:
            print("Kode buku tidak valid!")

        jawab = input("Apakah kamu mau membeli buku lagi? (ya/tidak) : ")
        if jawab.lower() != "ya":
            input_menu = input("Apakah kamu ingin kembali ke Menu Penjualan? (ya/tidak) : ")
            if input_menu.lower() == "ya":
                menu_penjualan(a)  
            elif input_menu.lower() == "tidak":
                menu_utama_admin(a) or menu_utama_user(a) 

def katalog_buku_jual(a):
    print("---KATALOG PENJUALAN BUKU---")
    for kode, detail in list_buku_penjualan.items():
        print(f"{kode}: {detail['judul buku']}")
        print(f"Harga: Rp {detail['harga']}")
        print(f"Stok: {detail['stok']} buku")
        print("-" * 40)

def add_buku_jual(a):
    kode_buku_baru = f"buku {len(list_buku_penjualan) + 1}"
    judul_buku = input("Masukkan judul buku baru: ")
    harga_buku = int(input("Masukkan harga buku: "))
    stok_buku = int(input("Masukkan stok buku: "))
    list_buku_penjualan[kode_buku_baru] = {
        "judul buku": judul_buku, 
        "harga": harga_buku, 
        "stok": stok_buku
    }
    print(f"Buku berhasil ditambahkan dengan kode {kode_buku_baru}")
    menu_penjualan(a)

def tambah_stok(a):
    katalog_buku_jual(a)
    print("Menambah Stok Buku")
    kode_buku = input("Masukkan kode buku yang ingin ditambah stoknya: ")
    if kode_buku in list_buku_penjualan:
        jumlah_tambah = int(input("Masukkan jumlah stok yang ingin ditambahkan: "))
        list_buku_penjualan[kode_buku]["stok"] += jumlah_tambah
        print(f"Stok untuk buku '{list_buku_penjualan[kode_buku]['judul buku']}' berhasil ditambahkan. Total stok sekarang: {list_buku_penjualan[kode_buku]['stok']}")
    else:
        print("Kode buku tidak valid!")

def hapus_buku_penjualan(a):
    katalog_buku_jual(a)
    kode_buku = input("Masukkan kode buku yang ingin dihapus: ")
    if kode_buku in list_buku_penjualan:
        del list_buku_penjualan[kode_buku]
        print(f"Buku dengan kode {kode_buku} berhasil dihapus")
        return menu_penjualan(a)
    else:
        print("Kode buku tidak ditemukan")
    return menu_penjualan(a)

def read_data_penjualan():
    if not list_data_penjualan:
        print("Tidak ada data peminjaman")
    else:
        print("---DATA PENJUALAN BUKU---")
        print("ID | Nama Pembeli | Kode Buku | Jumlah Buku")
        print("-"*40)
        for penjualan in list_data_penjualan:
            print(f"{penjualan[0]} | {penjualan[1]} | {penjualan[2]} | {penjualan[3]}")
        
def menu_penjualan (a):
    while True:
        print("-----APLIKASI PENJUALAN BUKU-----")
        print("1. Beli Buku")
        print("2. Tampilkan Buku yang Tersedia")
        print("3. Tampilkan Data Buku Terjual")
        print("4. Kembali ke menu utama")
        if a == "admin":
            print("5. Tambah Buku Jual")
            print("6. Tambah Stok Buku")
            print("7. Hapus Data")
        kode  = input("Masukkan nomor: ")
        if kode == "1":
            input_penjualan(a)
        elif kode == "2":
            katalog_buku_jual(a)
        elif kode == "3":
            read_data_penjualan()
        elif kode == "4":
            menu_utama_admin(a) or menu_utama_user(a)
        elif kode == "5":
            add_buku_jual(a)
        elif kode == "6":
            tambah_stok(a)
        elif kode == "7":
            hapus_buku_penjualan(a)
        else:   
            print("Pilihan yang Anda masukkan salah.")
    
def login():
    print("--- SELAMAT DATANG DI PERPUSTAKAAN ---")
    print("Anda masuk sebagai apa? ")
    print("1. Admin")
    print("2. User")
    print("3. Keluar")
    jawab = int(input("Silahkan masukkan nomer : "))
    if jawab == 1:
        print("Masukkan Username dan Password")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username == "admin" and password == "admin":
            print("Selamat, Anda berhasil login sebagai Admin")
            menu_utama_admin(username)
        else:
            print("Maaf, Anda salah memasukkan username atau password")
            login()
    elif jawab == 2:
        username = "user"
        print("Anda masuk sebagai pengunjung")
        menu_utama_user(username)
    elif jawab == 3:
        exit(exit)
    else:
        print("Invalid nomer yang anda masukkan salah")
        login()

def menu_utama_admin(u):
    print("---APLIKASI PENJUALAN BUKU DAN PEMINJAMAN BUKU PERPUSTAKAAN---")
    print("1. Menu Penjualan")
    print("2. Menu Peminjaman")
    print("3. Katalog Buku")
    print("4. Kembali ke menu Login")
    kode  = input("Masukkan nomor: ")
    if kode == "1":
        menu_penjualan(u)
    elif kode == "2":
        menu_peminjaman(u)
    elif kode == "3":
        katalog_buku()
    elif kode == "4":
        print("Anda Telah Keluar")
        login()
    else:
        print("Pilihan yang Anda masukkan salah.")

def menu_utama_user (a):
    print("---APLIKASI PENJUALAN BUKU DAN PEMINJAMAN BUKU PERPUSTAKAAN---")
    print("1. Menu Penjualan")
    print("2. Menu Peminjaman")
    print("3. Katalog Buku")
    print("4. Kembali ke menu Login")
    kode  = input("Masukkan nomor: ")
    if kode == "1":
        menu_penjualan(a)
    elif kode == "2":
        menu_peminjaman(a)
    elif kode == "3":
        katalog_buku()
    elif kode == "4":
        print("Anda Telah Keluar")
        print("Terima kasih atas kunjungan ke perpustakaan kami😊🙏")
        login()
    else:
        print("Pilihan yang Anda masukkan salah.")

login()