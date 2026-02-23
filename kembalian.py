def hitung_kembalian(Jumlahharga, Uangdibayar):
    
    if Uangdibayar < Jumlahharga:
        return {
            "status": False,
            "message": "Maaf uang anda tidak mencukupi",
            "kembalian": 0
        }
    
    kembalian = Uangdibayar - Jumlahharga
    
    return {
        "status": True,
        "message": "Pembayaran berhasil",
        "kembalian": kembalian
    }