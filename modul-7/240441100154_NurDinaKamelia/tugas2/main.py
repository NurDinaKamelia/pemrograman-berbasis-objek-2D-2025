from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

def main():
    print("=== Sistem Booking Kendaraan ===")
    usia = int(input("Masukkan usia Anda: "))
    print("Pilih kendaraan: 1. Mobil 2. Motor 3. Sepeda")
    pilihan = input("Pilihan (1/2/3): ")

    kendaraan = None
    if pilihan == "1":
        kendaraan = Mobil()
    elif pilihan == "2":
        kendaraan = Motor()
    elif pilihan == "3":
        kendaraan = Sepeda()
    else:
        print("Pilihan tidak valid.")
        return

    kendaraan.proses_booking(usia)

if __name__ == "__main__":
    main()
