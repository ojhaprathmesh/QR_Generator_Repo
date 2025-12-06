# QR Code Generator

## Introduction
This repository contains a Python script for generating QR codes with personal details. The application is developed using the Tkinter library for the graphical user interface, qrcode library for generating QR codes, and Pillow (PIL) library for image processing.

## Features
- User-friendly graphical interface for entering personal details
- Generates QR codes containing phone number, name, age, and education information
- Allows users to specify the save location for generated QR codes
- Validates input fields and provides error messages for missing or incorrect information
- Displays generated QR code in the application window
- Automatically creates a "QR Codes" folder in the specified directory

## Prerequisites
- Python 3.x
- pip (Python package installer)

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/ojhaprathmesh/QR_Generator_Repo.git
cd QR_Generator_Repo
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv .venv --upgrade-deps
```

### Step 3: Activate Virtual Environment
**For Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**For Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**For Linux/Mac:**
```bash
source .venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

## How to Use
1. Ensure you have activated your virtual environment (if using one)
2. Run the script `qr_generator.py` to launch the application:
   ```bash
   python qr_generator.py
   ```
3. Enter the required personal details in the provided fields:
   - Phone Number (required)
   - Name (required)
   - Age (required)
   - Education (required)
4. Specify the save location for the generated QR codes (defaults to current directory)
5. Click the "Generate" button to create the QR code
6. The generated QR code will be displayed on the interface, and a success message will be shown
7. The QR code image will be saved in a "QR Codes" folder at the specified location with the filename format: `Phone_No_{phone_number}.png`
8. Use the "Clear" button to reset all fields and start over

## Project Structure
```
QR_Generator_Repo/
├── qr_generator.py       # Main application file
├── setup_qr_generator.py # Setup script for creating executable
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── LICENSE               # MIT License
```

## Dependencies
The project requires the following Python packages (listed in `requirements.txt`):
- **qrcode** (7.4.2) - QR code generation
- **Pillow** (10.0.0) - Image processing
- **python-resize-image** (1.1.20) - Image resizing
- **resize-image** (0.4.0) - Additional image resizing functionality
- **cx-Freeze** (6.15.7) - For creating standalone executables
- Additional dependencies: certifi, charset-normalizer, colorama, idna, pypng, requests, typing_extensions, urllib3

## Building an Executable
To create a standalone executable for Windows, use the provided setup script:
```bash
python setup_qr_generator.py build
```
This will create an executable in the `build` directory that can be run without Python installed.

## Call for Contributions:
- **Enhanced UI/UX:**
  - Contributors are encouraged to revamp the user interface to make it more visually appealing and user-friendly. This could involve:
    - Implementing modern design principles such as Material Design or Fluent Design.
    - Adding graphical elements, icons, and animations to enhance the overall look and feel.
    - Improving the layout and organization of elements for better usability.
- **Additional Features:**
  - Contributions to add new features to the QR code generator are welcomed. Some potential ideas include:
    - Batch QR code generation to process multiple sets of personal details at once.
    - Integration with cloud storage services to automatically upload generated QR codes.
    - Support for different QR code formats and customization options such as color and logo embedding.
- **Input Validation and Error Handling:**
  - Contributions aimed at enhancing input validation and error handling mechanisms are valuable. This includes:
    - Implementing robust input validation to ensure data integrity.
    - Improving error handling to provide more informative and user-friendly error messages.
    - Adding exception handling to handle unexpected scenarios gracefully.

## Notes
- Make sure to provide valid and complete information in the input fields to generate QR codes successfully.
- The default save location is the current working directory, but users can change it as needed.

Feel free to contribute, report issues, or suggest improvements. Thank you for using the QR Code Generator!
