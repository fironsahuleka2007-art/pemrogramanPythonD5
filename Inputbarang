barang = {

}
hari = input("Hari: ")
total = 0

while True:
    kode = input("Kode barang: ")
    if not kode:
        break

    jumlah = int(input("Jumlah barang: "))
    
    if kode in barang:
        total += barang[kode]["harga"] * jumlah
        print(f"+ {barang[kode]['nama']} x {jumlah} = {barang[kode]['harga'] * jumlah}")
