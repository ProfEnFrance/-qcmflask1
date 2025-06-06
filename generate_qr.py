import qrcode
liste_eleves = ["001", "002", "003", ..., "038"]

for eleve_id in liste_eleves:
    url = f"https://tonapp.onrender.com/?eleve={eleve_id}"
    img = qrcode.make(url)
    img.save(f"qr/eleve_{eleve_id}.png")
