database_alat = {
    "Gitar": 2,
    "Keyboard": 1,
    "Drum": 1
}

database_peminjaman = []

def peminjaman_alat():
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    nim = input("Masukkan NIM: ")
    nama_alat = input("Masukkan Nama Alat: ")
    tanggal_pinjam = input("Masukkan Tanggal Peminjaman (YYYY-MM-DD): ")
    durasi = int(input("Masukkan Durasi Peminjaman (hari): "))

    if nama_alat in database_alat and database_alat[nama_alat] > 0:
        peminjaman = {
            "Nama Peminjam": nama_peminjam,
            "NIM": nim,
            "Alat": nama_alat,
            "Tanggal Peminjaman": tanggal_pinjam,
            "Durasi": durasi
        }
        database_peminjaman.append(peminjaman)

        database_alat[nama_alat] -= 1
        print("Peminjaman berhasil disimpan.")
    else:
        print("Alat tidak tersedia.")

peminjaman_alat()
