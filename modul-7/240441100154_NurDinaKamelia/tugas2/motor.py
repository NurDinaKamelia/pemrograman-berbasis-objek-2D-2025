from booking import Booking

class Motor(Booking):
    def proses_booking(self, usia):
        if usia > 18:
            print(" Motor berhasil dibooking. Biaya: Rp200.000/24 jam.")
        else:
            print("Motor hanya bisa dibooking oleh usia 18+ ")
