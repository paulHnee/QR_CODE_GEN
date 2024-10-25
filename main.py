import qrcode
from PIL import Image, ImageDraw

data = "https://new.hnee.de/ausbildung-und-praktika"

qr = qrcode.QRCode(
    version=3,  # (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=1,
)
qr.add_data(data)
qr.make(fit=True)

img_qr = qr.make_image(fill_color="#004d3d", back_color="#FFFF").convert('RGB')  # Fill color: #004d3d

border_size = 20
qr_width, qr_height = img_qr.size
green_border_img = Image.new('RGB', (qr_width + 2 * border_size, qr_height + 2 * border_size), "#004d3d")
green_border_img.paste(img_qr, (border_size, border_size))

try:
    logo = Image.open("White_UT_HNEE.png") # add logo
except FileNotFoundError:
    print("Logo image not found. Please ensure 'HNEE.png' is in the same directory.")
    exit()

logo_size = 180
white_logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
logo_position = ((green_border_img.width - logo_size) // 2, (green_border_img.height - logo_size) // 2)
green_border_img.paste(white_logo, logo_position, white_logo)

# Save the final image
green_border_img.save("QRCODE_2.png")

print("GENERATED")
