import qrcode

from PIL.Image import core as image
qr = qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_L,
                  box_size=50,
                  border=1)

qr.add_data("https://bodybyhannahstudio.com")
qr.make(fit=True)

img = qr.make_image(fill_color="purple", back_color="white")
img.save("BBH_Studio.jpg")