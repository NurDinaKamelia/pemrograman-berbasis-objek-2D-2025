from pembayaran import Pembayaran

class Tunai(Pembayaran):
    def proses_pembayaran(self, jumlah):
        diskon = 0.1  # 10%
        total = jumlah * (1 - diskon)
        print(f"Bayar tunai: Rp{total:.2f}")
