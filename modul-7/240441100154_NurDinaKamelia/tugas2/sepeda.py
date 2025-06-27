from booking import Booking

class Sepeda(Booking):
    def proses_booking(self, usia):

        if usia >12 :
            print(" Sepeda berhasil dibooking. Biaya: Rp50.000/24 jam")
        else:
            print("Tidak Memenuhi Persyaratan Usia!")
