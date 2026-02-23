from loaderJson import load_barang
from Inputbarang import input_barang
from modulDiskon import hitung_diskon_jumat
from Kembalian import hitung_kembalian
from Totalharga import total_harga

def main():
    print("===== KASIR TOKO SEDERHANA =====")

    dataBarang = load_barang()

    total = input_barang(dataBarang)
    if total == 0:
        print("Tidak ada barang dibeli")
        return

    hari = input("Hari (contoh: jumat): ")
    total_akhir, diskon = hitung_diskon_jumat(total, hari)

    print("\nTotal harga :", total)
    print("Diskon      :", diskon)
    print("Total bayar :", total_akhir)

    bayar = int(input("Uang dibayarkan: "))
    kembalian = hitung_kembalian(total_akhir, bayar)

    if kembalian is None:
        print("Uang tidak cukup")
    else:
        print("Kembalian :", kembalian)

if __name__ == "__main__":
    main()