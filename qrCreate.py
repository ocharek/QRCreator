import qrcode

def qrcreator(dat, poss, ipath):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=14,
        border=2,
    )
    qr.add_data(dat)
    qr.make(fit=True)
    img = qr.make_image()
    if poss:
        img.save(f'{ipath}/qr.jpg')
    img.show()
