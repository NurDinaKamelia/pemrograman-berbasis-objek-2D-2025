class Kucing:
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur
    
    def suara(self):
        return "Meong"

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Warna: {self.warna}")
        print(f"Umur: {self.umur} tahun")
        print(f"Suara: {self.suara()}")
        print("-" * 30)

class Anjing:
    def __init__(self, nama, ras, umur):
        self.nama = nama
        self.ras = ras
        self.umur = umur
    
    def suara(self):
        return "Guk Guk"

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Ras: {self.ras}")
        print(f"Umur: {self.umur} tahun")
        print(f"Suara: {self.suara()}")
        print("-" * 30)

class Burung:
    def __init__(self, nama, jenis, umur):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur
    
    def suara(self):
        return "Pipit Pipit"

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Jenis: {self.jenis}")
        print(f"Umur: {self.umur} tahun")
        print(f"Suara: {self.suara()}")
        print("-" * 30)
        
def input_hewan(hewan_type):
    nama = input(f"Masukkan nama {hewan_type}: ")
    if hewan_type == "Kucing":
        warna = input("Masukkan warna kucing: ")
        umur = int(input("Masukkan umur kucing (tahun): "))
        return Kucing(nama, warna, umur)
    elif hewan_type == "Anjing":
        ras = input("Masukkan ras anjing: ")
        umur = int(input("Masukkan umur anjing (tahun): "))
        return Anjing(nama, ras, umur)
    elif hewan_type == "Burung":
        jenis = input("Masukkan jenis burung: ")
        umur = int(input("Masukkan umur burung (tahun): "))
        return Burung(nama, jenis, umur)

hewan_list = []

for i in range(3):
    print(f"\nMasukkan data hewan ke-{i + 1}:")
    hewan_type = input("Masukkan jenis hewan (Kucing, Anjing, Burung): ")
    hewan = input_hewan(hewan_type)
    hewan_list.append(hewan)

print("\nInformasi Hewan:")
for hewan in hewan_list:
    hewan.info()



