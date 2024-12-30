import tkinter as tk

root = tk.Tk()
root.geometry("800x500") # X x Y
root.title("QR Gen")

label = tk.Label(root, text="Welcome! Here you will provide a URL and a QR Code will be generated.", font=('Arial', 18))
label.pack() # you don't need to include padding here can leave brackets empty and label will appear
             # format inside brackets is: padx=123, pady=123
textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10)

button = tk.Button(root, text="Load URL", font=('Arial', 14))
button.pack(pady=10)



root.mainloop()