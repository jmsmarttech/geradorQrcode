import pyqrcode
import png
link = "https://"
qr_code = pyqrcode.create(link)
qr_code.png("name.png", scale=5)
