from abc import ABC, abstractmethod

class PerangkatElektronik(ABC):
    def __init__(self):
        self.energi_tersisa = 100

    @abstractmethod
    def nyalakan(self):
        pass

    @abstractmethod
    def matikan(self):
        pass

    @abstractmethod
    def gunakan(self, jam: int):
        pass

    def status(self):
        print(f"Tipe perangkat : {self.__class__.__name__}")
        print(f"Energi tersisa : {self.energi_tersisa}%\n")

class Laptop(PerangkatElektronik):
    def nyalakan(self):
        print("Laptop dinyalakan.")

    def matikan(self):
        print("Laptop dimatikan.")

    def gunakan(self, jam: int):
        print(f"Laptop digunakan selama {jam} jam.")
        self.energi_tersisa -= 10 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("Baterai laptop habis!")

class Kulkas(PerangkatElektronik):
    def nyalakan(self):
        print("Kulkas dinyalakan.")

    def matikan(self):
        print("Kulkas dimatikan.")

    def gunakan(self, jam: int):
        print(f"Kulkas digunakan selama {jam} jam.")
        self.energi_tersisa -= 5 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
        if self.energi_tersisa < 20:
            print("Energi rendah, kulkas butuh daya tambahan!")

def main():
    print("=== Program Perangkat Elektronik ===")

    while True:
        print("\nPilih perangkat: Laptop / Kulkas (atau ketik 'keluar' untuk menghentikan)")
        perangkat_input = input("Masukkan jenis perangkat: ").strip().lower()

        if perangkat_input == "keluar":
            print("Terima kasih telah menggunakan program ini.")
            break

        if perangkat_input == "laptop":
            perangkat = Laptop()
        elif perangkat_input == "kulkas":
            perangkat = Kulkas()
        else:
            print("Jenis perangkat tidak dikenal. Silakan coba lagi.")
            continue

        perangkat.nyalakan()

        try:
            jam = int(input("Masukkan durasi penggunaan (jam): "))
            perangkat.gunakan(jam)
            perangkat.status()
        except ValueError:
            print("Input jam harus berupa angka!")

        perangkat.matikan()

        lanjut = input("Ingin menginput perangkat lagi? (y/n): ").strip().lower()
        if lanjut != 'y':
            print("Program selesai.")
            break

if __name__ == "__main__":
    main()
