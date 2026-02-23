from loaderJson import load_barang
from Inputbarang import input_barang
from modulDiskon import hitung_diskon_jumat
from Kembalian import hitung_kembalian

def main():
    print("===== KASIR TOKO SEDERHANA =====")
    print("--------------------------------")
    print("====== Kota Bandung, 2026 =======")
    print("--Selamat datang di toko kami!--\n")

    dataBarang = load_barang()

    result = input_barang(dataBarang)
    if isinstance(result, tuple):
        daftar_beli, total = result
    else:
        total = result
        daftar_beli = None 

    if total == 0:
        print("Tidak ada barang dibeli.")
        return

    hari = input("Hari (contoh: jumat): ").strip().lower()
    total_akhir, diskon = hitung_diskon_jumat(total, hari)

    print("\n" + "-"*40)
    print(f"Total belanja  : Rp {total:>10,}")
    print(f"Diskon ({hari}) : Rp {diskon:>10,}")
    print(f"Total bayar    : Rp {total_akhir:>10,}")
    print("-"*40)

    while True:
        try:
            bayar = int(input("Uang dibayarkan: Rp "))
            if bayar < 0:
                print("Uang tidak boleh negatif!")
                continue
            break
        except ValueError:
            print("Masukkan angka yang benar!")

    hasil = hitung_kembalian(total_akhir, bayar)
    if hasil["status"]:
        print(hasil["message"])
    if hasil["kembalian"] > 0:
        print(f"Kembalian      : Rp {hasil['kembalian']:>12,.0f}")
    else:
        print(hasil["message"])

if __name__ == "__main__":
    main()