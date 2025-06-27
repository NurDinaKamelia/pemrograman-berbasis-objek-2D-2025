from abc import ABC, abstractmethod

class Karyawan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama)
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

class KaryawanKontrak(Karyawan):
    def __init__(self, nama, upah_per_jam, jam_kerja):
        super().__init__(nama)
        self.upah_per_jam = upah_per_jam
        self.jam_kerja = jam_kerja

    def hitung_gaji(self):
        return self.upah_per_jam * self.jam_kerja

def cetak_gaji(karyawan):
    print(f"Gaji {karyawan.nama}: Rp{int(karyawan.hitung_gaji()):,}\n")

def main():
    while True:
        print("Pilih jenis karyawan:")
        print("1. Karyawan Tetap")
        print("2. Karyawan Kontrak")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == '1':
            nama = input("Masukkan nama: ")
            gaji_pokok = float(input("Masukkan gaji pokok: "))
            tunjangan = float(input("Masukkan tunjangan: "))
            karyawan = KaryawanTetap(nama, gaji_pokok, tunjangan)

        elif pilihan == '2':
            nama = input("Masukkan nama: ")
            upah_per_jam = float(input("Masukkan upah per jam: "))
            jam_kerja = float(input("Masukkan jumlah jam kerja: "))
            karyawan = KaryawanKontrak(nama, upah_per_jam, jam_kerja)

        elif pilihan == '3':
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.\n")
            continue

        cetak_gaji(karyawan)

if __name__ == "__main__":
    main()
