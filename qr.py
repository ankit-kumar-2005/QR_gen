import qrcode

def generate_qr_code(link):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    qr_image.save("qr_code.png")
    print("QR code generated successfully!")

if __name__ == "__main__":
    link = input("Enter the link: ")
    generate_qr_code(link)
