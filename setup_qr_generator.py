from cx_Freeze import setup, Executable

# Build options for cx_Freeze
build_exe_options = {
    "packages": [
        "os",
        "subprocess",
        "tkinter",
        "tkinter.filedialog",
        "qrcode",
        "qrcode.image.pil",
        "PIL",
        "PIL.Image",
        "PIL.ImageTk",
        "resizeimage"
    ],
    "includes": [
        "qrcode",
        "qrcode.image.pil",
        "PIL.Image",
        "PIL.ImageTk",
        "resizeimage.resizeimage"
    ],
    "excludes": [
        # Exclude unnecessary modules to reduce size and suppress warnings
        # SSL/Crypto modules (not needed for local QR generation)
        "OpenSSL",
        "OpenSSL.SSL",
        "OpenSSL.crypto",
        "cryptography",
        "cryptography.x509",
        "cryptography.x509.extensions",
        # Compression modules (optional, not needed)
        "brotli",
        "brotlicffi",
        "backports.zstd",
        # Character encoding (optional)
        "chardet",
        # HTTP/2 and advanced HTTP features (not needed)
        "h2",
        "h2.config",
        "h2.connection",
        "h2.events",
        # XML/HTML parsing (not needed, using PIL)
        "lxml",
        "lxml.etree",
        # Testing modules
        "pytest",
        # Proxy support (not needed)
        "socks",
        # urllib3 optional features
        "urllib3.contrib",
        "urllib3.contrib.pyopenssl",
        "urllib3.contrib.socks",
        "urllib3.contrib.emscripten",
        "urllib3.http2",
        "urllib3.http2.connection",
        # requests optional features
        "requests.compat",
        "requests.packages",
        "requests._internal_utils",
        # qrcode optional backends (using PIL only)
        "qrcode.compat",
        "qrcode.compat.etree",
        "qrcode.compat.png",
        "qrcode.image.styles.moduledrawers.svg",
        "qrcode.image.svg",
        "qrcode.image.pure",
        "qrcode.tests",
        "qrcode.tests.test_example",
        "qrcode.tests.test_qrcode",
        "qrcode.tests.test_qrcode_pil",
        "qrcode.tests.test_qrcode_pypng",
        "qrcode.tests.test_script",
        "qrcode.tests.test_util",
        # Web/JS modules (not needed)
        "js",
        "pyodide",
        "pyodide.ffi",
        # PNG alternative (using PIL)
        "png",
        "pypng",
        # JSON alternatives
        "simplejson"
    ],
    "include_files": [],
    "optimize": 2
}

# Executable configuration
executables = [
    Executable(
        "qr_generator.py",
        base="Win32GUI",  # Hide console window on Windows
        target_name="QR_Generator.exe",
        icon=None  # Add icon path here if you have one
    )
]

setup(
    name="QR Generator By Prathmesh",
    version="2.1.0",
    description="Python QR Generator - Generate QR codes with personal details",
    author="Prathmesh",
    options={"build_exe": build_exe_options},
    executables=executables
)
