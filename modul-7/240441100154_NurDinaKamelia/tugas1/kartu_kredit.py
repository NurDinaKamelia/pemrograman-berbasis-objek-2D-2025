from pembayaran import Pembayaran

class KartuKredit(Pembayaran):
    def proses_pembayaran(self, jumlah):
        biaya_admin = 5000
        total = jumlah + biaya_admin
        print(f"Bayar kartu kredit: Rp{total:.2f}")
