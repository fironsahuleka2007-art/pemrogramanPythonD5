def input_barang(barang_list):
    while True:
        kode = input("Kode barang: ")
        if not kode:
            break

        jumlah = int(input("Jumlah barang: "))
        
        if kode in barang_list:
            total = barang_list[kode]["harga"] * jumlah
            print(f"+ {barang_list[kode]['nama']} x {jumlah} = {total}")

            hari = input("Hari: ")
            total = 0
            total += total
            return total, hari
        else:
            print("Kode barang tidak ditemukan. Silakan coba lagi.")
