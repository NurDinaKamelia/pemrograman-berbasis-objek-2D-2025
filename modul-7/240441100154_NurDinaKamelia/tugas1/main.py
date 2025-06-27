from tunai import Tunai
from kartu_kredit import KartuKredit
from dompet_digital import DompetDigital

def main():
    print("===Sistem Pembayaran===")
    jumlah = float(input("Masukkan jumlah belanja: Rp"))

    print("Pilih Metode Pembayaran")
    print("1.Tunai 2. Kartu Kredit 3. Dompet Digital")
    pilih = input("Piihan (1/2/3):")

    if pilih == "1":
        metode = Tunai()
    elif pilih == "2":
        metode = KartuKredit()
    elif pilih == "3":
        metode = DompetDigital()
    else:
        print("Metode tidak dikenali.")
        return

    metode.proses_pembayaran(jumlah)
    print("Terimakasih!")

if __name__ == "__main__":
    main()
