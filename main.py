import qrcode  # Required for qr code generation
import image 
import os  # Required in order to gain access to user's Desktop
import tkinter as tk  # tkinter allows to use widgets to create a GUI
from tkinter import messagebox

class qrGenGUI:

    def __init__(self):
        
        self.root = tk.Tk()

        self.root.geometry("790x400")  # Determine window size
        self.root.title("QR Gen")

        self.label = tk.Label(self.root, text="Welcome! Here you will provide a URL and a QR Code will be generated.", font=('Arial', 15))
        self.label.pack()

        # Textbox for URL input
        self.url_label = tk.Label(self.root, text="Enter URL:", font=('Arial', 12))
        self.url_label.pack(pady=5)
        self.url_textbox = tk.Text(self.root, height=3, font=('Arial', 16))
        self.url_textbox.pack(padx=10)

        # Textbox for filename input
        self.filename_label = tk.Label(self.root, text="Enter Filename (without extension):", font=('Arial', 12))
        self.filename_label.pack(pady=5)
        self.filename_textbox = tk.Text(self.root, height=1, font=('Arial', 14))  # Using Text widget for consistency
        self.filename_textbox.pack(padx=10)

        self.button = tk.Button(self.root, text="Generate QR Code", font=('Arial', 14), command=self.show_message)
        self.button.pack(pady=20)

        self.root.mainloop()

    def show_message(self):
        
        # Assigning inputted URL and filename to variables via the use of "strip()"
        url = self.url_textbox.get('1.0', tk.END).strip()
        filename = self.filename_textbox.get('1.0', tk.END).strip()

        if url and filename:

            # Creating QR Code
            qr = qrcode.QRCode (
                version = 15, 
                box_size = 10,
                border = 5
            )

            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill="black", back_color="white")

            # Obtaining the user's Desktop path
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            file_path = os.path.join(desktop_path, f"{filename}.png")  # Saving with user-defined filename

            img.save(file_path)  # Saving QR Code to user's Desktop

            # Creating topLevel window to allow for more control over window
            # Using "tk.TopLevel" creates a new window as a child of the main application window

            sucWin = tk.Toplevel(self.root)
            sucWin.title("Success")
            sucWin.geometry("400x200")
            label = tk.Label(sucWin, text="URL received and QR Code generated", font=('Arial', 12), wraplength=380, justify="center")
            label.pack(pady=20)

            closeButton = tk.Button(sucWin, text="Close", command=sucWin.destroy, font=('Arial', 12))
            closeButton.pack(pady=20)

        else:

            errWin = tk.Toplevel(self.root)
            errWin.title("Error")
            errWin.geometry("300x150")
            label = tk.Label(errWin, text="Error. Please try again.", font=('Arial', 12), wraplength=280, justify="center", fg="red")
            label.pack(pady=20)

            closeButton = tk.Button(errWin, text="Close", command=errWin.destroy, font=('Arial', 12))
            closeButton.pack(pady=20)

qrGenGUI()  # This is required in order to run the application
