# QR Code Generator

## Introduction
This repository contains a Python script for generating QR codes with personal details. The application is developed using the Tkinter library for the graphical user interface, qrcode library for generating QR codes, and Pillow (PIL) library for image processing.

## Features
- User-friendly graphical interface for entering personal details.
- Generates QR codes containing phone number, name, age, and education information.
- Allows users to specify the save location for generated QR codes.
- Validates input fields and provides error messages for missing or incorrect information.

## Dependencies
- Python 3.x
- Tkinter
- qrcode
- Pillow (PIL)
- resizeimage

## How to Use
1. Clone the repository to your local machine.
2. Install the required dependencies using the following command:
    ```
    pip install qrcode Pillow resizeimage
    ```
3. Run the script `qr_generator.py` to launch the application.
4. Enter the required personal details in the provided fields.
5. Specify the save location for the generated QR codes.
6. Click the "Generate" button to create the QR code.
7. The generated QR code will be displayed on the interface, and a success message will be shown.

## Notes
- Make sure to provide valid and complete information in the input fields to generate QR codes successfully.
- The default save location is the current working directory, but users can change it as needed.

Feel free to contribute, report issues, or suggest improvements. Thank you for using the QR Code Generator!
