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

        # ======Coloring Title======
        title = Label(self.root, bg='white')
        title.place(x=0, y=0, width=900, height=600)

        # ========Main Title========
        title = Label(self.root, text="QR Generator", font=("times new roman", 40), bg='#053246', fg='white')
        title.place(x=0, y=0, relwidth=1)

        # ========Variables========
        self.var_phone_no = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_education = StringVar()
        self.var_directory = StringVar()
        self.var_directory.set(os.getcwd())
        self.wrn_msg = None
        self.msg = None
        self.img = None

        # ========Personal Details Window========
        emp_frame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        emp_frame.place(x=50, y=100, width=500, height=365)

        emp_title = Label(emp_frame, text='Personal Details', font=('goudy old style', 20), bg='#043256',
                          fg='white')
        emp_title.place(x=0, y=0, relwidth=1)

        # ====Labels====
        lbl_phone_no = Label(emp_frame, text='Phone Number :-', font=('times new roman', 15, 'bold'), bg='white',
                             anchor='w')
        lbl_phone_no.place(x=20, y=60)

        lbl_name = Label(emp_frame, text='Name :-', font=('times new roman', 15, 'bold'), bg='white', anchor='w')
        lbl_name.place(x=20, y=100)

        lbl_age = Label(emp_frame, text='Age :-', font=('times new roman', 15, 'bold'), bg='white', anchor='w')
        lbl_age.place(x=20, y=140)

        lbl_education = Label(emp_frame, text='Education :-', font=('times new roman', 15, 'bold'), bg='white',
                              anchor='w')
        lbl_education.place(x=20, y=180)

        lbl_directory = Label(emp_frame, text='Save Location :-', font=('times new roman', 15, 'bold'), bg='white',
                              anchor='w')
        lbl_directory.place(x=20, y=280)

        # ====Entries====
        txt_phone_no = Entry(emp_frame, font=('times new roman', 16, 'bold'), textvariable=self.var_phone_no,
                             bg='white')
        txt_phone_no.place(x=200, y=60)

        txt_name = Entry(emp_frame, font=('times new roman', 16, 'bold'), textvariable=self.var_name, bg='white')
        txt_name.place(x=200, y=100)

        txt_age = Entry(emp_frame, font=('times new roman', 16, 'bold'), textvariable=self.var_age, bg='white')
        txt_age.place(x=200, y=140)

        txt_education = Entry(emp_frame, font=('times new roman', 16, 'bold'), textvariable=self.var_education,
                              bg='white')
        txt_education.place(x=200, y=180)

        txt_directory = Entry(emp_frame, font=('times new roman', 16, 'bold'), textvariable=self.var_directory,
                              bg='white')
        txt_directory.place(x=200, y=280)

        # ====Buttons====
        btn_generate = Button(emp_frame, text='Generate', command=self.generate, font=('times new roman', 20, 'bold'),
                              bg='#2196f3', fg='black')
        btn_generate.place(x=90, y=220, width=150, height=30)

        btn_clear = Button(emp_frame, text='Clear', command=self.clear, font=('times new roman', 20, 'bold'),
                           bg='#2196f3', fg='black')
        btn_clear.place(x=254, y=220, width=150, height=30)

        self.msg = ''
        self.wrn_msg = Label(emp_frame, text=self.msg, font=('times new roman', 15, 'bold'), bg='white', fg='green')
        self.wrn_msg.place(x=0, y=320, relwidth=1)

        # ========QR Code Window========
        qr_frame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        qr_frame.place(x=600, y=100, width=250, height=365)

        qr_title = Label(qr_frame, text='QR Code', font=('goudy old style', 20), bg='#043256', fg='white')
        qr_title.place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_frame, text='No QR Code\nAvailable', font=('times new roman', 15), bg='#3f51b5',
                             fg='white', bd=2, relief=RIDGE)
        self.qr_code.place(x=22, y=100, width=200, height=200)

    def generate(self):
        if self.var_phone_no.get() == '' or self.var_name.get() == '':
            self.msg = 'All Fields Are Required!'
            self.wrn_msg.config(text=self.msg, fg='red')

        elif self.var_age.get() == '' or self.var_education.get() == '':
            self.msg = 'All Fields Are Required!'
            self.wrn_msg.config(text=self.msg, fg='red')

        elif self.var_directory.get() == '':
            self.var_directory.set(os.getcwd())

        elif not os.path.exists(self.var_directory.get()):
            self.msg = 'Location Not Found'
            self.wrn_msg.config(text=self.msg, fg='red')

        else:
            # ====Required Directory Change====
            if self.var_directory.get() != os.getcwd():
                os.chdir(self.var_directory.get())

            if not os.path.exists('QR Codes'):
                os.mkdir(os.path.join(os.getcwd(), 'QR Codes'))

            # ====QR Creation And Update====
            qr_data = f"""
            Phone No :- {self.var_phone_no.get()}
            Name :- {self.var_name.get()}
            Age :- {self.var_age.get()}
            Education :- {self.var_education.get()}"""
            qr_code = qrcode.make(qr_data)

            qr_code.save(f"QR Codes/Phone_No_{self.var_phone_no.get()}.png")

            qr_code = resizeimage.resize_cover(qr_code, [200, 200])
            self.img = ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.img)

            # ====Update Notification====
            self.msg = 'QR Code Generated Successfully'
            self.wrn_msg.config(text=self.msg, fg='green')

    def clear(self):
        self.var_phone_no.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_education.set('')
        self.msg = ''
        self.wrn_msg.config(text=self.msg)
        self.qr_code.config(image='')


root = Tk()
obj = QrGenerator(root)
root.mainloop()
