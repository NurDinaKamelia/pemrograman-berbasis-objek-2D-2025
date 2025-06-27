from peminjaman import Peminjaman
from reservasi import Reservasi

class BukuReferensi(Peminjaman, Reservasi):
    def pinjam(self):
        print(" Buku referensi dipinjam selama 3 hari (hanya bisa dibaca di tempat).")

    def reservasi(self):
        print(" Buku referensi berhasil direservasi.")
