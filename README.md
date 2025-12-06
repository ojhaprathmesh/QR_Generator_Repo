# QR Code Generator

## Introduction
This repository contains a modern Python application for generating QR codes with personal details. The application features a clean, contemporary user interface built with Tkinter, and uses the qrcode library for QR code generation with Pillow (PIL) for image processing. The UI follows modern design principles with a light color palette, improved spacing, and intuitive user experience.

## Features
- **Modern, Clean UI**: Contemporary design with light color scheme, improved typography (Segoe UI), and better visual hierarchy
- **Smart Name Autofill**: Automatically fills the name field from your Git configuration (user.name or derived from user.email)
- **Directory Browser**: Browse button to easily select save location using file explorer dialog
- **Real-time QR Preview**: Displays generated QR code instantly in the application window
- **Input Validation**: Comprehensive validation with trimmed inputs and clear error messages
- **Auto-folder Creation**: Automatically creates a `qr_codes` folder in the specified directory
- **Status Messages**: Temporary status messages that auto-clear after successful operations
- **Personal Details QR**: Generates QR codes containing phone number, name, age, and education information
- **Clear Functionality**: One-click clear button to reset all fields and start fresh

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
3. The application window will open with a modern, clean interface
4. **Name Field**: May be auto-filled from your Git configuration. You can edit it if needed
5. Enter the required personal details in the provided fields:
   - **Name** (required) - Auto-filled from Git if available
   - **Phone Number** (required)
   - **Age** (required)
   - **Education** (required)
6. **Save Location**: 
   - Defaults to current working directory
   - Click the "Browse" button to select a different folder using the file explorer
   - Or manually type the path in the save location field
7. Click the **"Generate"** button to create the QR code
8. The generated QR code will be displayed instantly in the preview panel on the right
9. A success message will appear briefly and then return to the default hint
10. The QR code image will be saved in a `qr_codes` folder at the specified location with the filename format: `Phone_No_{phone_number}.png`
11. Use the **"Clear"** button to reset all fields and start over

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
- **qrcode** (8.2) - QR code generation library
- **Pillow** (12.0.0) - Image processing and manipulation
- **python-resize-image** (1.1.20) - Image resizing functionality
- **resize-image** (0.4.0) - Additional image resizing utilities
- **cx-Freeze** (8.5.0) - For creating standalone Windows executables
- **Additional dependencies**: cabarchive, certifi, charset-normalizer, colorama, filelock, freeze-core, idna, lief, packaging, requests, setuptools, striprtf, urllib3

> **Note**: Tkinter is included with Python by default on most installations. If it's not available, install it through your system's package manager.

## Building an Executable
To create a standalone executable for Windows, you have two options:

### Option 1: Standard Build (with filtered warnings)
```bash
python build_exe.py
```
This uses a wrapper script that filters out expected warnings for cleaner output.

### Option 2: Direct Build
```bash
python setup_qr_generator.py build
```
This will create an executable in the `build` directory that can be run without Python installed. The executable will include all necessary dependencies and can be distributed independently.

**About Build Warnings:**
- You will see warnings about "Missing modules" during the build process - **these are normal and expected**
- The setup script is configured to exclude unnecessary optional modules (like OpenSSL, cryptography, HTTP/2 support, compression libraries, etc.) that aren't needed for QR code generation
- These exclusions help reduce the executable size significantly
- Warnings about Windows DLLs (api-ms-win-crt-*.dll) are also normal - these are provided by the Visual C++ Redistributable, which is pre-installed on most Windows systems
- The application will work perfectly despite these warnings, as they only refer to optional dependencies

**Note**: The setup script uses `cx_Freeze` and is configured for Windows. For other platforms, you may need to adjust the setup configuration.

## Technical Details
- **UI Framework**: Tkinter with modern styling
- **QR Code Format**: Standard QR code format readable by any QR scanner
- **Image Format**: PNG format for generated QR codes
- **Folder Structure**: QR codes are saved in a `qr_codes` subdirectory
- **Git Integration**: Automatically retrieves user name from Git global configuration
- **Window Size**: Fixed at 900x500 pixels for consistent layout
- **Color Scheme**: Light, modern palette with proper contrast for accessibility

## Call for Contributions
Contributions are welcome! Here are some areas where you can help:

- **Additional Features:**
  - Batch QR code generation to process multiple sets of personal details at once
  - Integration with cloud storage services to automatically upload generated QR codes
  - Support for different QR code formats and customization options (colors, logos, error correction levels)
  - Export functionality (PDF, CSV of generated QR codes)
  - QR code scanning/reading functionality
  - History/log of generated QR codes

- **Code Improvements:**
  - Enhanced input validation (phone number format, age range, etc.)
  - Better error handling with more informative messages
  - Unit tests and test coverage
  - Code documentation and type hints
  - Performance optimizations

- **Platform Support:**
  - macOS and Linux executable builds
  - Cross-platform compatibility improvements
  - Installation scripts for different platforms

## Notes
- All fields (Name, Phone Number, Age, Education) are required to generate a QR code
- The name field will be auto-filled from your Git configuration if available (checks `git config --global user.name` or derives from `user.email`)
- Input values are automatically trimmed of whitespace
- The default save location is the current working directory, but you can change it using the Browse button or by typing a path
- QR codes are saved in a `qr_codes` folder (lowercase) within the specified directory
- The application creates the `qr_codes` folder automatically if it doesn't exist
- Generated QR codes can be scanned by any standard QR code reader app
- The QR code contains formatted text with all personal details

## Troubleshooting
- **Tkinter not found**: Install Python with Tkinter support, or install `python3-tk` on Linux
- **Permission errors**: Ensure you have write permissions to the selected save directory
- **Git name not auto-filling**: This is optional; you can manually enter your name
- **QR code not displaying**: Check that all required fields are filled and the directory path is valid

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Developed by Prathmesh

---

Feel free to contribute, report issues, or suggest improvements. Thank you for using the QR Code Generator!
