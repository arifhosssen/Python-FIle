import qrcode as qr
QR = qr.QRCode(version= 1,
               box_size=10,
               border=5)
qr.add_data("quran.com")
qr.make(fit = True)
img = qr.make_image(fill_color = 'orang',
                    back_color = "white")
img.save("Quran.png")