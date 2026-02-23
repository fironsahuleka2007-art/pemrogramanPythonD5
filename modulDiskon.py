def hitung_diskon_jumat(total_belanja, hari):
    hari = hari.lower()

    if hari == "jumat":
        diskon = total_belanja * 0.10
    else:
        diskon = 0

    return total_belanja - diskon, diskon