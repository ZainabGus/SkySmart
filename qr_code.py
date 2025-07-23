import qrcode

data = "You are cool"
img = qrcode.make(data)

qr = qrcode.QRCode(version=1, box_size=15, border=10)
qr.add_data(data)
img = qr.make_image(fill_color='pink', back_color='black')
img.save('test.png')