class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama        : {self.nama}")
        print(f"Gaji        : {self.gaji}") 
        print(f"Departemen  : {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan   : {self.tunjangan}")
        print("Status      : Karyawan Tetap\n")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja   : {self.jam_kerja} jam/hari")
        print("Status      : Karyawan Harian\n")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        print("\n=== Daftar Seluruh Karyawan ===")
        for karyawan in self.daftar_karyawan:
            karyawan.info()

def input_karyawan():
    manajemen = ManajemenKaryawan()

    while True:
        print("\nTambah Karyawan Baru")
        print("1. Karyawan Tetap")
        print("2. Karyawan Harian")
        print("3. Selesai")
        pilihan = input("Pilih tipe karyawan (1/2/3): ")

        if pilihan == '1':
            nama = input("Nama           : ")
            gaji = int(input("Gaji           : "))
            departemen = input("Departemen     : ")
            tunjangan = int(input("Tunjangan      : "))
            karyawan = KaryawanTetap(nama, gaji, departemen, tunjangan)
            manajemen.tambah_karyawan(karyawan)

        elif pilihan == '2':
            nama = input("Nama           : ")
            gaji = int(input("Gaji per hari  : "))
            departemen = input("Departemen     : ")
            jam_kerja = int(input("Jam Kerja/hari : "))
            karyawan = KaryawanHarian(nama, gaji, departemen, jam_kerja)
            manajemen.tambah_karyawan(karyawan)

        elif pilihan == '3':
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

    manajemen.tampilkan_semua_karyawan()

input_karyawan()
