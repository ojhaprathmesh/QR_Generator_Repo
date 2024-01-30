from cx_Freeze import setup, Executable

exe_options = {"packages": ["tkinter", "qrcode", "pillow", "resize-image"]}

setup(name="QR Generator By Prathmesh",
      version="1.0.0",
      description="My Python QR Generator",
      options={"build_exe": exe_options},
      executables=[Executable("QR Generator.py", base="Win32GUI")]
      )
