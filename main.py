import qrcode
from PIL import Image, ImageDraw

# Data to be encoded
data = "https://new.hnee.de/ausbildung-und-praktika"  # Replace with your URL or text

# Create a QR code instance
qr = qrcode.QRCode(
    version=3,  # Change this for different sizes (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  # Size of each box
    border=1,     # Number of boxes for the border
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance with a dark green fill color (#004d3d)
img_qr = qr.make_image(fill_color="#004d3d", back_color="#FFFFF").convert('RGB')  # Fill color: #004d3d

# Define the size of the background with the border in green
border_size = 20  # Adjust this to control how thick the green border is
qr_width, qr_height = img_qr.size

# Create a new image with a green background (this will act as the border)
green_border_img = Image.new('RGB', (qr_width + 2 * border_size, qr_height + 2 * border_size), "#004d3d")

# Paste the QR code on top of the green background
green_border_img.paste(img_qr, (border_size, border_size))

# Load the logo and make it white
try:
    logo = Image.open("Black_UT_HNEE.png")  # Replace 'HNEE.png' with your image file
except FileNotFoundError:
    print("Logo image not found. Please ensure 'HNEE.png' is in the same directory.")
    exit()


# Resize the white logo if needed
logo_size = 180 # Adjust this size as needed
white_logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing

# Calculate position to paste the logo
logo_position = ((green_border_img.width - logo_size) // 2, (green_border_img.height - logo_size) // 2)

# Paste the white logo onto the QR code (with transparency)
green_border_img.paste(white_logo, logo_position, white_logo)  # Use the logo's alpha channel for transparency

# Save the final image
green_border_img.save("QRCODE_2.png")

print("GENERATED")
