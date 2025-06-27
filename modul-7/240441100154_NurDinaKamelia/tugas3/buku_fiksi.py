from peminjaman import Peminjaman
from reservasi import Reservasi

class BukuFiksi(Peminjaman, Reservasi):
    def pinjam(self):
        print(" Buku fiksi dipinjam selama 7 hari.")
    def reservasi(self):
        print(" Buku fiksi berhasil direservasi.")
