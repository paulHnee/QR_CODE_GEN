import qrcode
from PIL import Image

data = "https://new.hnee.de/ausbildung-und-praktika"
qr = qrcode.QRCode(
    version=3,  # Version: (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)
qr.add_data(data)
qr.make(fit=True)

img_qr = qr.make_image(fill_color="#004d3d", back_color="white").convert('RGB')  # Fill color: #004d3d

try:
    logo = Image.open("HNEE.png")
except FileNotFoundError:
    print("Logo image not found. Please ensure 'logo.png' is in the same directory.")
    exit()
if logo.mode in ('RGBA', 'LA') or (logo.mode == 'P' and 'transparency' in logo.info):
    logo = logo.convert("RGBA")
else:
    print("Logo does not have transparency.")

logo_size = 100
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing

qr_width, qr_height = img_qr.size
logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

img_qr.paste(logo, logo_position, logo)
img_qr.save("qrcode_with_logo_dark_green.png")

print("QR code with dark green color (#004d3d) and logo generated and saved as 'qrcode_with_logo_dark_green.png'")
