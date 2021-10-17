import pyqrcode


website = 'https://www.geeksforgeeks.org/python-generate-qr-code-using-pyqrcode-module/'
url = pyqrcode.create(website)
url.svg('QRCodeGenerator.svg', scale=9)