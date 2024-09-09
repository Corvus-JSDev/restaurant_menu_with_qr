import qrcode
import os

from dotenv import load_dotenv

load_dotenv()
URL_ADDR = os.getenv("URL_ADDR")

image = qrcode.make(URL_ADDR)
image.save("qr.png")
