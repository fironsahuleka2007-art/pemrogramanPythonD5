def jumlah_harga(daftar_subtotal):
    total_akhir = 0
    for subtotal in daftar_subtotal:
        total_akhir += subtotal
    return total_akhir