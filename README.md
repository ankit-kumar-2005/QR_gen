# QR Code Generator

This Python script allows users to generate QR codes for any URL they specify. It provides a simple command-line interface for inputting the URL and generates a PNG image containing the QR code.

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/your_username/qr-code-generator.git
```

2. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

## Usage

1. Navigate to the project directory.

2. Run the script:

```
python qr_code_generator.py
```

3. Enter the URL when prompted.

4. The QR code will be generated and saved as `qr_code.png` in the current directory.

## Example

```bash
$ python qr_code_generator.py
Enter the URL: https://example.com
QR code generated successfully!
```

## Dependencies

- `qrcode`: A Python library for generating QR codes.
- `Pillow`: A Python Imaging Library (PIL) fork, used by `qrcode` for image generation.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

