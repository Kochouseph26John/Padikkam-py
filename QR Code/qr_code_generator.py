import qrcode

qrc = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=3
)
qrc.add_data(input('Enter the date to be encoded!........\n'))
qrc.make(fit=True)
img = qrc.make_image(fill_color="black", back_color="white")
img.save('qrcode.jpg')