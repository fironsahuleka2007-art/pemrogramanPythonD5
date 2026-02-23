from Inputbarang import barang
def total_harga(barang):
    hargatotal = 0
    
    for item in barang:
        total = item['harga'] * item['jumlah']
        hargatotal += total
    
    return hargatotal