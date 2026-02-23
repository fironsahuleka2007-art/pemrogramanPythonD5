from loaderJson import dataBarang
from modulDiskon import hitung_diskon_jumat
from kembalian import hitung_kembalian
from totalHarga import total_harga
from jumlahHarga import Jumlahharga
from Inputbarang import input_barang



def main():
    print("=====================================")
    print("======= KASIR TOKO SEDERHANA ========")
    print("Selamat berbelanja di Toko Sederhana!")
    print("----------- Februari 2026 -----------")
    print("=====================================\n\n")


nama, harga, jumlah = input_barang(dataBarang)

if harga is None:
    print("Barang tidak ditemukan")

total = harga * jumlah
diskon = hitung_diskon_jumat(total)
total_harga = hitung_total_bayar(total, diskon)

print("\nBarang       :", nama)
print("Total harga  : Rp", int(total))
print("Diskon       : Rp", int(diskon))
print("Total bayar  : Rp", int(total_harga))

uang = int(input("Uang dibayarkan: "))
kembalian = hitung_kembalian(total_harga, uang)

if kembalian is None:
    print("Uang tidak cukup")
else:
    print("Kembalian    : Rp", int(kembalian))


if __name__ == "__main__":
    main()

