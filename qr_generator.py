import os
import subprocess
from tkinter import Tk, Label, StringVar, Frame, Button, Entry, filedialog
from tkinter.constants import CENTER, FLAT
import qrcode
from PIL import ImageTk
from resizeimage import resizeimage


class QrGenerator:
    def __init__(self, self_root):
        self.root = self_root
        self.root.geometry('900x500+200+50')
        self.root.title('QR Generator | Developed by Prathmesh')
        self.root.resizable(False, False)

        # ====== Color Palette (light, modern) ======
        self.bg_main = "#f3f4f6"        # window background
        self.bg_card = "#ffffff"        # frames/cards
        self.bg_header = "#111827"      # top bar
        self.bg_section_header = "#1f2937"
        self.bg_input = "#f9fafb"
        self.border_color = "#e5e7eb"
        self.text_primary = "#111827"
        self.text_muted = "#6b7280"
        self.btn_primary = "#2563eb"
        self.btn_primary_active = "#1d4ed8"
        self.btn_secondary = "#e5e7eb"
        self.btn_secondary_active = "#d1d5db"

        self.root.configure(bg=self.bg_main)

        # ======= Layout constants (controls all gaps) =======
        HEADER_HEIGHT = 56          # approx height of top title bar
        FRAME_TOP = HEADER_HEIGHT + 40   # gap between title and frames
        CARD_WIDTH = 520
        QR_WIDTH = 260
        SPACING_Y = 40              # vertical rhythm inside cards
        ENTRY_OFFSET = 26           # label -> input gap

        # ======== Main Title / Header ========
        title = Label(
            self.root,
            text="QR Generator",
            font=("Segoe UI", 28, "bold"),
            bg=self.bg_header,
            fg="white",
            pady=8
        )
        title.place(x=0, y=0, relwidth=1)

        # ======== Variables ========
        self.var_phone_no = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_education = StringVar()
        self.var_directory = StringVar(value=os.getcwd())

        # 🔹 Autofill name from git if available
        default_name = self.get_name_from_git()
        if default_name:
            self.var_name.set(default_name)

        self.msg = ""
        self.img = None
        self.status_job = None  # for auto-clearing messages

        # ======== Personal Details Card ========
        emp_frame = Frame(
            self.root,
            bd=0,
            bg=self.bg_card,
            highlightthickness=1,
            highlightbackground=self.border_color
        )
        emp_frame.place(x=40, y=FRAME_TOP, width=CARD_WIDTH, height=380)

        emp_title = Label(
            emp_frame,
            text='Personal Details',
            font=('Segoe UI Semibold', 16),
            bg=self.bg_section_header,
            fg="white",
            pady=6
        )
        emp_title.place(x=0, y=0, relwidth=1)

        # ==== Labels & Entries with uniform spacing ====
        y = 60  # first row inside the card

        # Name
        self.create_label(emp_frame, 'Name', 30, y)
        self.create_entry(emp_frame, self.var_name, 30, y + ENTRY_OFFSET, width=430)
        y += SPACING_Y + ENTRY_OFFSET

        # Phone Number
        self.create_label(emp_frame, 'Phone Number', 30, y)
        self.create_entry(emp_frame, self.var_phone_no, 30, y + ENTRY_OFFSET, width=430)
        y += SPACING_Y + ENTRY_OFFSET

        # Age + Education (same row)
        self.create_label(emp_frame, 'Age', 30, y)
        self.create_label(emp_frame, 'Education', 270, y)
        self.create_entry(emp_frame, self.var_age, 30, y + ENTRY_OFFSET, width=190)
        self.create_entry(emp_frame, self.var_education, 270, y + ENTRY_OFFSET, width=190)
        y += SPACING_Y + ENTRY_OFFSET

        # Save Location
        self.create_label(emp_frame, 'Save Location', 30, y)

        # Entry field
        self.create_entry(emp_frame, self.var_directory, 30, y + ENTRY_OFFSET, width=340)

        # Browse button
        browse_btn = Button(
            emp_frame,
            text="Browse",
            font=('Segoe UI', 9),
            bg=self.btn_secondary,
            fg=self.text_primary,
            bd=0,
            cursor="hand2",
            command=self.browse_directory
        )
        browse_btn.place(x=380, y=y + ENTRY_OFFSET, width=80, height=26)

        # move y past the Save Location row before placing buttons
        y += SPACING_Y + ENTRY_OFFSET

        # ==== Buttons (centered) ====
        btn_y = y + 10
        btn_generate = Button(
            emp_frame,
            text='Generate',
            command=self.generate,
            font=('Segoe UI Semibold', 11),
            bg=self.btn_primary,
            fg='white',
            activebackground=self.btn_primary_active,
            activeforeground='white',
            bd=0,
            relief=FLAT,
            cursor="hand2"
        )
        btn_generate.place(x=120, y=btn_y, width=120, height=32)

        btn_clear = Button(
            emp_frame,
            text='Clear',
            command=self.clear,
            font=('Segoe UI Semibold', 11),
            bg=self.btn_secondary,
            fg=self.text_primary,
            activebackground=self.btn_secondary_active,
            activeforeground=self.text_primary,
            bd=0,
            relief=FLAT,
            cursor="hand2"
        )
        btn_clear.place(x=270, y=btn_y, width=120, height=32)

        # ======== QR Code Preview Card ========
        qr_frame = Frame(
            self.root,
            bd=0,
            bg=self.bg_card,
            highlightthickness=1,
            highlightbackground=self.border_color
        )
        qr_frame.place(x=600, y=FRAME_TOP, width=QR_WIDTH, height=380)

        qr_title = Label(
            qr_frame,
            text='QR Code',
            font=('Segoe UI Semibold', 16),
            bg=self.bg_section_header,
            fg="white",
            pady=6
        )
        qr_title.place(x=0, y=0, relwidth=1)

        self.qr_code = Label(
            qr_frame,
            text='No QR Code\nAvailable',
            font=('Segoe UI', 11),
            bg="#e5e7eb",
            fg=self.text_muted,
            bd=0,
            relief=FLAT,
            justify=CENTER
        )
        self.qr_code.place(x=30, y=60, width=200, height=200)

        # Status / hint message lives here now
        self.default_hint = "Fill the details and click\nGenerate to create a QR code."
        self.status_msg = Label(
            qr_frame,
            text=self.default_hint,
            font=('Segoe UI', 9),
            bg=self.bg_card,
            fg=self.text_muted,
            justify=CENTER
        )
        self.status_msg.place(x=15, y=280, width=230)

    # ================== HELPERS ==================

    def get_name_from_git(self):
        """Try to get the user's name from git config, falling back to email."""
        # 1) Try git user.name
        try:
            name = subprocess.check_output(
                ["git", "config", "--global", "user.name"],
                stderr=subprocess.DEVNULL,
                text=True
            ).strip()
            if name:
                return name
        except Exception:
            pass

        # 2) Try git user.email and derive a name
        try:
            email = subprocess.check_output(
                ["git", "config", "--global", "user.email"],
                stderr=subprocess.DEVNULL,
                text=True
            ).strip()
            if email and "@" in email:
                user_part = email.split("@")[0]
                user_part = user_part.replace(".", " ").replace("_", " ")
                derived = user_part.title()
                return derived
        except Exception:
            pass

        # 3) Nothing available
        return ""

    def create_label(self, parent, text, x, y):
        label = Label(
            parent,
            text=text,
            font=('Segoe UI', 10, 'bold'),
            bg=self.bg_card,
            fg=self.text_primary,
            anchor='w'
        )
        label.place(x=x, y=y, width=200)
        return label

    def create_entry(self, parent, textvariable, x, y, width=200):
        entry = Entry(
            parent,
            font=('Segoe UI', 10),
            textvariable=textvariable,
            bg=self.bg_input,
            fg=self.text_primary,
            bd=1,
            relief=FLAT,
            highlightthickness=1,
            highlightbackground=self.border_color,
            highlightcolor=self.btn_primary,
            insertbackground=self.text_primary
        )
        entry.place(x=x, y=y, width=width, height=26)
        return entry

    def reset_message(self):
        """Reset back to neutral hint in QR frame."""
        self.status_msg.config(text=self.default_hint, fg=self.text_muted)
        self.status_job = None

    def show_message(self, text, color='green', duration=3000):
        """
        Show a temporary message in the QR frame.
        duration in ms; if None, it stays.
        """
        self.status_msg.config(text=text, fg=color)

        # cancel previous timer if exists
        if self.status_job is not None:
            self.root.after_cancel(self.status_job)
            self.status_job = None

        # schedule auto-reset
        if duration is not None:
            self.status_job = self.root.after(duration, self.reset_message)

    # ================== CORE LOGIC ==================

    def generate(self):
        # Trimmed values
        phone = self.var_phone_no.get().strip()
        name = self.var_name.get().strip()
        age = self.var_age.get().strip()
        edu = self.var_education.get().strip()
        directory = self.var_directory.get().strip()

        # ---- Basic validation ----
        if not (phone and name and age and edu):
            self.show_message('All fields are required', 'red')
            return

        # ---- Directory validation ----
        if not directory:
            directory = os.getcwd()
            self.var_directory.set(directory)

        if not os.path.exists(directory):
            self.show_message('Location not found', 'red')
            return

        # ---- Ensure QR Codes folder exists ----
        qr_dir = os.path.join(directory, 'qr_codes')
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
        self.qr_code.config(image=self.img, text='')

        # ---- Success message ----
        self.show_message('QR generated', 'green')

    def clear(self):
        self.var_phone_no.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_education.set('')
        self.qr_code.config(image='', text='No QR Code\nAvailable')
        # instantly go back to neutral hint
        self.reset_message()

    def browse_directory(self):
        """Open file explorer to choose folder."""
        folder = filedialog.askdirectory()
        if folder:
            self.var_directory.set(folder)


if __name__ == "__main__":
    root = Tk()
    app = QrGenerator(root)
    root.mainloop()
