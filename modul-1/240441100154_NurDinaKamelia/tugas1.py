class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    
    def berjalan(self):
        print(f"{self.nama} sedang berjalan.")
    
    def berlari(self):
        print(f"{self.nama} sedang berlari.")
        
manusia1 = Manusia("Nur", 25, "Jakarta")
manusia2 = Manusia("Dina", 30, "Bandung")
manusia3 = Manusia("Kamel", 22, "Surabaya")
manusia4 = Manusia("Mely", 28, "Yogyakarta")
manusia5 = Manusia("Lya", 35, "Medan")

manusia1.berjalan()
manusia1.berlari()

manusia2.berjalan()
manusia2.berlari()

manusia3.berjalan()
manusia3.berlari()

manusia4.berjalan()
manusia4.berlari()

manusia5.berjalan()
manusia5.berlari()
