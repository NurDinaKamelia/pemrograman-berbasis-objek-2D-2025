class MataKuliah:
    def __init__(self, kode, nama, sks):
        if MataKuliah.validasi_sks(sks):
            self.kode = kode
            self.nama = nama
            self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        return sks == 2 or sks == 3


class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if Mahasiswa.validasi_nim(nim):
            self.nama = nama
            self.nim = nim
            self.prodi = prodi
            self.mata_kuliah = []
            Mahasiswa.jumlah_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.mata_kuliah.append(matkul)

    def tampilkan_info(self):
        print(f"\nNama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata Kuliah yang Diambil:")
        for mk in self.mata_kuliah:
            print(f"  - {mk.nama} ({mk.kode}), SKS: {mk.sks}")

    @classmethod
    def total_mahasiswa(cls):
        return cls.jumlah_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        return len(nim) == 10 and nim.isdigit() and nim[:2] == "23"


class Kampus:
    jumlah_mahasiswa = 0  # atribut class

    def __init__(self, nama, alamat):
        if self.validasi_nama(nama):
            self.nama = nama
            self.alamat = alamat
            Kampus.jumlah_mahasiswa = Mahasiswa.total_mahasiswa()

    def info_kampus(self):
        print(f"\nNama Kampus: {self.nama}")
        print(f"Alamat: {self.alamat}")
        print(f"Total Mahasiswa: {Kampus.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nama(nama):
        return all(char.isalpha() or char.isspace() for char in nama)

    @classmethod
    def tampilkan_data_kampus(cls, nama_kampus):
        print(f"\n[Nama Kampus: {nama_kampus}]")
        print(f"Total Mahasiswa: {cls.jumlah_mahasiswa}")


daftar_matkul = [
    MataKuliah("MK01", "Desain Manajemen Jaringan", 2),
    MataKuliah("MK02", "Pemrograman Berbasis Web", 3),
    MataKuliah("MK03", "Pemrograman Berbasis Objek", 3),
    MataKuliah("MK04", "Pengantar Basis Data", 2),
    MataKuliah("MK05", "E-Business & E-Commerce", 3),
    MataKuliah("MK06", "Analisa Proses Data", 3),
    MataKuliah("MK07", "Bahasa Inggris", 2),
    MataKuliah("MK08", "Pendidikan Agama Islam", 2)
]

mahasiswa_list = [
    Mahasiswa("Nur Dina Kamelia", "2312345154", "Sistem Informasi"),
    Mahasiswa("Nur", "2312345155", "Informatika"),
    Mahasiswa("Dina", "2312345156", "Sistem Informasi"),
    Mahasiswa("Kamel", "2312345157", "Informatika"),
    Mahasiswa("Kamelia", "2312345158", "Sistem Informasi"),
    Mahasiswa("Lyaa", "2312345159", "Informatika")
]

for i in range(len(mahasiswa_list)):
    mhs = mahasiswa_list[i]
    if mhs:
        mhs.tambah_matkul(daftar_matkul[i % len(daftar_matkul)])
        mhs.tambah_matkul(daftar_matkul[(i + 1) % len(daftar_matkul)])
        mhs.tambah_matkul(daftar_matkul[(i + 2) % len(daftar_matkul)])
        mhs.tambah_matkul(daftar_matkul[(i + 3) % len(daftar_matkul)])

kampus = Kampus("Universitas Trunojoyo Madura", "Jl.Telang Kec. Kamal")

print("\n--- Data Mahasiswa ---")
for mhs in mahasiswa_list:
    if mhs:
        mhs.tampilkan_info()

print("\n--- Data Kampus ---")
if kampus:
    kampus.info_kampus()
    print(f"Nama Kampus Valid: {Kampus.validasi_nama(kampus.nama)}")

# Menampilkan data kampus lewat class method
Kampus.tampilkan_data_kampus("Universitas trunojoyo Madura")
