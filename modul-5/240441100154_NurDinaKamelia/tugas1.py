from abc import ABC, abstractmethod

class Manusia(ABC):
    @abstractmethod
    def berbicara(self):
        pass

    @abstractmethod
    def bekerja(self):
        pass

    @abstractmethod
    def makan(self):
        pass

class Joko(Manusia):
    def berbicara(self):
        print("Joko berbicara dengan logat Jawa yang kental.")

    def bekerja(self):
        print("Joko bekerja sebagai petani di desa.")

    def makan(self):
        print("Joko makan nasi pecel kesukaannya.")

class Beni(Manusia):
    def berbicara(self):
        print("Beni berbicara dengan gaya santai seperti anak kota.")

    def bekerja(self):
        print("Beni bekerja sebagai programmer freelance.")

    def makan(self):
        print("Beni makan burger sambil ngoding.")

class Fani(Manusia):
    def berbicara(self):
        print("Fani berbicara dengan lembut dan sopan.")

    def bekerja(self):
        print("Fani bekerja sebagai guru TK yang sabar.")

    def makan(self):
        print("Fani makan salad untuk menjaga kesehatannya.")

class Jani(Manusia):
    def berbicara(self):
        print("Jani berbicara cepat dan energik.")

    def bekerja(self):
        print("Jani bekerja sebagai kurir yang selalu tepat waktu.")

    def makan(self):
        print("Jani makan cepat agar bisa kembali bekerja.")

def buat_karakter(nama):
    if nama.lower() == "joko":
        return Joko()
    elif nama.lower() == "beni":
        return Beni()
    elif nama.lower() == "fani":
        return Fani()
    elif nama.lower() == "jani":
        return Jani()
    else:
        return None

def main():
    print("Selamat datang! Pilih karakter: Joko, Beni, Fani, Jani (ketik 'exit' untuk keluar)\n")
    while True:
        pilihan = input("Masukkan nama karakter: ")

        if pilihan.lower() == "exit":
            print("Terima kasih telah menggunakan program ini.")
            break

        karakter = buat_karakter(pilihan)
        if karakter:
            print(f"\nAksi dari {pilihan.capitalize()}:")
            karakter.berbicara()
            karakter.bekerja()
            karakter.makan()
            print()
        else:
            print("Karakter tidak ditemukan. Silakan coba lagi.\n")

if __name__ == "__main__":
    main()
