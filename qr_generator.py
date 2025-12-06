import os
from tkinter import *
import qrcode
from PIL import ImageTk
from resizeimage import resizeimage


class QrGenerator:
    def __init__(self, self_root):
        self.root = self_root
        self.root.geometry('900x500+200+50')
        self.root.title('QR Generator | Developed by Prathmesh')
        self.root.resizable(False, False)

        # ======Background======
        title_bg = Label(self.root, bg='white')
        title_bg.place(x=0, y=0, width=900, height=600)

        # ========Main Title========
        title = Label(
            self.root,
            text="QR Generator",
            font=("times new roman", 40),
            bg='#053246',
            fg='white'
        )
        title.place(x=0, y=0, relwidth=1)

        # ========Variables========
        self.var_phone_no = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_education = StringVar()
        self.var_directory = StringVar(value=os.getcwd())
        self.wrn_msg = None
        self.msg = None
        self.img = None

        # ========Personal Details Window========
        emp_frame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        emp_frame.place(x=50, y=100, width=500, height=365)

        emp_title = Label(
            emp_frame,
            text='Personal Details',
            font=('goudy old style', 20),
            bg='#043256',
            fg='white'
        )
        emp_title.place(x=0, y=0, relwidth=1)

        # ====Labels====
        self.create_label(emp_frame, 'Name :-', 20, 60)
        self.create_label(emp_frame, 'Phone Number :-', 20, 100)
        self.create_label(emp_frame, 'Age :-', 20, 140)
        self.create_label(emp_frame, 'Education :-', 20, 180)
        self.create_label(emp_frame, 'Save Location :-', 20, 280)

        # ====Entries====
        self.create_entry(emp_frame, self.var_phone_no, 200, 60)
        self.create_entry(emp_frame, self.var_name, 200, 100)
        self.create_entry(emp_frame, self.var_age, 200, 140)
        self.create_entry(emp_frame, self.var_education, 200, 180)
        self.create_entry(emp_frame, self.var_directory, 200, 280)

        # ====Buttons====
        btn_generate = Button(
            emp_frame,
            text='Generate',
            command=self.generate,
            font=('times new roman', 20, 'bold'),
            bg='#2196f3',
            fg='black'
        )
        btn_generate.place(x=90, y=220, width=150, height=30)

        btn_clear = Button(
            emp_frame,
            text='Clear',
            command=self.clear,
            font=('times new roman', 20, 'bold'),
            bg='#2196f3',
            fg='black'
        )
        btn_clear.place(x=254, y=220, width=150, height=30)

        # ====Message Label====
        self.msg = ''
        self.wrn_msg = Label(
            emp_frame,
            text=self.msg,
            font=('times new roman', 15, 'bold'),
            bg='white',
            fg='green'
        )
        self.wrn_msg.place(x=0, y=320, relwidth=1)

        # ========QR Code Window========
        qr_frame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        qr_frame.place(x=600, y=100, width=250, height=365)

        qr_title = Label(
            qr_frame,
            text='QR Code',
            font=('goudy old style', 20),
            bg='#043256',
            fg='white'
        )
        qr_title.place(x=0, y=0, relwidth=1)

        self.qr_code = Label(
            qr_frame,
            text='No QR Code\nAvailable',
            font=('times new roman', 15),
            bg='#3f51b5',
            fg='white',
            bd=2,
            relief=RIDGE
        )
        self.qr_code.place(x=22, y=100, width=200, height=200)

    # ================== HELPERS ==================

    def create_label(self, parent, text, x, y,
                     font=('times new roman', 15, 'bold'),
                     bg='white', anchor='w'):
        """Create a Label and place it, to avoid repeating config code."""
        label = Label(parent, text=text, font=font, bg=bg, anchor=anchor)
        label.place(x=x, y=y)
        return label

    def create_entry(self, parent, textvariable, x, y,
                     font=('times new roman', 16, 'bold'),
                     bg='white'):
        """Create an Entry and place it, to avoid repeating config code."""
        entry = Entry(parent, font=font, textvariable=textvariable, bg=bg)
        entry.place(x=x, y=y)
        return entry

    def show_message(self, text, color='green'):
        """Centralized way to update the status message."""
        self.msg = text
        self.wrn_msg.config(text=self.msg, fg=color)

    # ================== CORE LOGIC ==================

    def generate(self):
        # Trimmed values for safer validation
        phone = self.var_phone_no.get().strip()
        name = self.var_name.get().strip()
        age = self.var_age.get().strip()
        edu = self.var_education.get().strip()
        directory = self.var_directory.get().strip()

        # ---- Basic validation ----
        if not (phone and name and age and edu):
            self.show_message('All Fields Are Required!', 'red')
            return

        # ---- Directory validation ----
        if not directory:
            directory = os.getcwd()
            self.var_directory.set(directory)

        if not os.path.exists(directory):
            self.show_message('Location Not Found', 'red')
            return

        # ---- Ensure QR Codes folder exists ----
        qr_dir = os.path.join(directory, 'QR Codes')
        os.makedirs(qr_dir, exist_ok=True)

        # ---- QR Creation ----
        qr_data = (
            f"Name :- {name}\n"
            f"Phone No :- {phone}\n"
            f"Age :- {age}\n"
            f"Education :- {edu}"
        )
        qr_code = qrcode.make(qr_data)

        img_path = os.path.join(qr_dir, f"Phone_No_{phone}.png")
        qr_code.save(img_path)

        # Resize for display
        qr_code = resizeimage.resize_cover(qr_code, [200, 200])
        self.img = ImageTk.PhotoImage(qr_code)
        self.qr_code.config(image=self.img)

        # ---- Success message ----
        self.show_message('QR Code Generated Successfully', 'green')

    def clear(self):
        self.var_phone_no.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_education.set('')
        self.msg = ''
        self.wrn_msg.config(text=self.msg)
        self.qr_code.config(image='')


if __name__ == "__main__":
    root = Tk()
    app = QrGenerator(root)
    root.mainloop()
