import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Main window
root = tk.Tk()
root.title("BANK APPLICATION")
root.geometry("650x650")

# Open and resize the SBI logo
image = Image.open("SBI-State-bank-of-india-logo.png")
image.thumbnail((350, 350))

# Convert image for Tkinter
photo = ImageTk.PhotoImage(image)

# Display image
img_label = tk.Label(root, image=photo)
img_label.image = photo
img_label.pack(pady=20)

# Application form window
def open_root2():
    root2 = tk.Toplevel(root)
    root2.title("APPLICATION FORM")
    root2.geometry("500x700")

# Name label
    tk.Label(
        root2,
        text="NAME",
        font=("Arial", 12)
    ).pack(pady=5)
    name = tk.Entry(root2, font=("arial",12))
    name.pack(pady=5)

    tk.Label(
        root2,
        text="AGE",
        font=("Arial", 12)
    ).pack(pady=5)
    age = tk.Entry(root2, font=("arial",12))
    age.pack(pady=5)

    tk.Label(
        root2,
        text="EMAIL",
        font=("Arial", 12)
    ).pack(pady=5)
    email = tk.Entry(root2, font=("arial",12))
    email.pack(pady=5)

    tk.Label(
        root2,
        text="PHONE_NUMBER",
        font=("Arial", 12)
    ).pack(pady=5)
    phone_number = tk.Entry(root2, font=("arial",12))
    phone_number.pack(pady=5)

    tk.Label(
        root2,
        text="ADDRESS",
        font=("Arial", 12)
    ).pack(pady=5)
    address_entry = tk.Entry(root2, font=("arial",12))
    address_entry.pack(pady=5)

    gender=tk.StringVar()
    tk.Label(root2,text="gender",font=("arial")).pack(pady=5)
    tk.Radiobutton(root2,text="female",value="female",variable=gender).pack()
    tk.Radiobutton(root2,text="male",value="male",variable=gender).pack()

    result_label=tk.Label(root2,text="",font=("arial"),justify="left")
    result_label.pack(pady=10)

    def submit():

        name_value = name.get()
        age_value = age.get()
        email_value = email.get()
        phone_value = phone_number.get()
        address_value = address_entry.get()
        gender_value = gender.get()



        if (name_value == "" or
    age_value == "" or
    email_value == "" or
    phone_value == "" or
    address_value == "" or
    gender_value == ""):


            messagebox.showerror(
            "Error",
            "Please fill all the fields"
        )
            return
        

        if not phone_value.isdigit() or len(phone_value) != 10:
            messagebox.showerror(
            "Error",
            "Phone number must contain exactly 10 digits"
        )
            return


        account_number = random.randint(
        1000000000000,
            9999999999999
        )

        print(f"""
Name: {name_value}
Age: {age_value}
Email: {email_value}
Phone Number: {phone_value}
Address: {address_value}
Gender: {gender_value}
Account Number: {account_number}
""")

        result_label.config(
    text=f"""
Name: {name_value}
Age: {age_value}
Email: {email_value}
Phone Number: {phone_value}
Address: {address_value}
Gender: {gender_value}
Account Number: {account_number}
"""
)


        messagebox.showinfo(
                    "Success",
                    f"Account created successfully!\n\n"
                    f"Name: {name_value}\n"
                    f"Email: {email_value}\n"
                    f"Phone Number: {phone_value}\n"
                    f"Address: {address_value}\n"
                    f"Gender: {gender_value}\n"
                    f"Account Number: {account_number}"
                )
    def clear():
        name.delete(0, tk.END)
        age.delete(0, tk.END)
        email.delete(0, tk.END)
        phone_number.delete(0, tk.END)
        address_entry.delete(0, tk.END)

    gender.set("")
    result_label.config(text="")

    tk.Button(root2,text="clear",command=clear).pack(pady=5)
    tk.Button(root2,text="submit",command=submit).pack(pady=5)
btn=tk.Button(root,text="NEW APPLICATION",command=open_root2).pack(pady=5)
root.mainloop()