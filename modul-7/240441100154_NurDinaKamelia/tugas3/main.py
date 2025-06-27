from buku_fiksi import BukuFiksi
from buku_referensi import BukuReferensi

def main():
    print("=== Sistem Peminjaman Buku ===")
    print("Pilih jenis buku:\n1. Fiksi\n2. Referensi")
    jenis = input("Pilihan (1/2): ")

    if jenis == "1":
        buku = BukuFiksi()
    elif jenis == "2":
        buku = BukuReferensi()
    else:
        print(" Pilihan tidak valid.")
        return

    #apakah ingin meminjam buku
    pinjam = input("Ingin pinjam buku? (y/n): ").lower()
    if pinjam == "y":
        # Jalankan fungsi pinjam dan akhiri program
        buku.pinjam()
        print("Terimakasih sudah menggunakan program")
        return  # Program selesai, tidak lanjut ke reservasi

    # Jika tidak meminjam, tawarkan reservasi
    reservasi = input("Ingin reservasi buku? (y/n): ").lower()
    if reservasi == "y":
        buku.reservasi()
        print("Terimakasih sudah menggunakan program")

if __name__ == "__main__":
    main()
