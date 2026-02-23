def input_barang(barang_list):
    total = 0
    while True:
        kode = input("Kode barang (enter untuk selesai): ").upper()
        if kode == "":
            break

        if kode not in barang_list:
            print("Kode barang tidak ditemukan")
            continue

        jumlah = int(input("Jumlah barang: "))
        subtotal = barang_list[kode]["harga"] * jumlah
        total += subtotal

        print(f"+ {barang_list[kode]['nama']} x {jumlah} = Rp{subtotal}")

    return total