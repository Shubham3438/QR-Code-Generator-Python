import qrcode
from datetime import datetime

def generate_qr(data: str, filename: str | None = None) -> str:
    """
    Generate a QR code image from `data` and save it as a PNG.
    Returns the filename saved.
    """
    qr = qrcode.QRCode(
        version=1,           # 1..40 (size), use fit=True to auto size
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    if not filename:
        filename = f"qr_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    img.save(filename)
    return filename

if __name__ == "__main__":
    text = input("Enter text or URL to encode: ").strip()
    if not text:
        print("No input provided. Exiting.")
    else:
        saved = generate_qr(text)
        print(f"QR code saved as: {saved}")
