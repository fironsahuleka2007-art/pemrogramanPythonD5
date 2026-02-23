# total_harga.py
def hitung_total(daftar_pembelian):
    total = 0
    for item in daftar_pembelian:
        total += item["harga"] * item["jumlah"]
    return total