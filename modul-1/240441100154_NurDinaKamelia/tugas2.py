class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat
    
    def tampilkan_info(self):
        print(f"Nama   : {self.nama}")
        print(f"NIM    : {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print(f"Alamat : {self.alamat}")
        print("-" * 30)

def input_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    jurusan = input("Masukkan jurusan/prodi mahasiswa: ")
    alamat = input("Masukkan alamat mahasiswa: ")
    return Mahasiswa(nama, nim, jurusan, alamat)

mahasiswa_list = []

for i in range(3):
    print(f"\nMasukkan data mahasiswa ke-{i + 1}:")
    mahasiswa = input_mahasiswa()
    mahasiswa_list.append(mahasiswa)

print("\nInformasi Mahasiswa:")
for mhs in mahasiswa_list:
    mhs.tampilkan_info()
