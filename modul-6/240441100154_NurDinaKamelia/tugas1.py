import math

class BangunDatar:
    def luas(self):
        return 0

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * self.jari_jari * self.jari_jari

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

# Fungsi polymorphic
def cetak_luas(bangun_datar):
    print(f"Luas: {int(bangun_datar.luas()):,}\n")

def main():
    while True:
        print("Pilih bangun datar:")
        print("1. Persegi")
        print("2. Lingkaran")
        print("3. Segitiga")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3 atau 0 untuk keluar): ")

        if pilihan == '1':
            sisi = float(input("Masukkan panjang sisi persegi: "))
            bangun = Persegi(sisi)
        elif pilihan == '2':
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            bangun = Lingkaran(jari_jari)
        elif pilihan == '3':
            alas = float(input("Masukkan alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            bangun = Segitiga(alas, tinggi)
        elif pilihan == '0':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid.\n")
            continue

        cetak_luas(bangun)

if __name__ == "__main__":
    main()
