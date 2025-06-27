from pembayaran import Pembayaran

class DompetDigital(Pembayaran):
    def proses_pembayaran(self, jumlah):
        cashback = 0.05
        total = jumlah * (1 - cashback)
        print(f"Bayar dompet digital: Rp{total:.2f}")
