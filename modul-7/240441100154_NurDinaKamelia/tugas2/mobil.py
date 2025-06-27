from booking import Booking

class Mobil(Booking):
    def proses_booking(self, usia):
        if usia > 21:
            print(" Mobil berhasil dibooking. Biaya: Rp500.000/24 jam.")
        else:
            print(" Mobil hanya bisa dibooking oleh usia 21+")
