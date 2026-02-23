import json

def load_barang():
    with open("aset.json", "r") as f:
        data = json.load(f)

    barang_flat = {}
    for kategori in data:
        for item in data[kategori]:
            barang_flat[item["kode"]] = item

    return barang_flat