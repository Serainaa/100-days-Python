from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

FONT_NAME = "Courier"

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# --------------------------- SAVE PASSWORD ---------------------------------- #
def save_password():
    website = site_input.get().lower()
    my_name = name_input.get()
    my_password = password_input.get()

    new_data = {
        website: {
            "username": my_name,
            "password": my_password
        }
    }
    if len(website) == 0 or len(my_password) == 0:
        messagebox.showerror(title="MissingFields", message="You left a field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: {my_name} |"
                                                              f" {my_password}. Is it okay?")
        if is_ok:
            try:
                with open("password.json", 'r') as p:
                    # Reading old data.
                    data = json.load(p)
            except FileNotFoundError:
                with open("password.json", 'w') as p:
                    # Create new file and write new data.
                    json.dump(new_data, p, indent=4)
            else:
                # Updating old data.
                data.update(new_data)
                with open("password.json", 'w') as p:
                    # Saving new data.
                    json.dump(data, p, indent=4)
            finally:
                site_input.delete(0, END)
                password_input.delete(0, END)


# --------------------------- SEARCH ACCOUNT --------------------------------- #
def search_account():
    website = site_input.get().lower()
    try:
        with open("password.json", 'r') as p:
            # Reading old data.
            data = json.load(p)
    except FileNotFoundError:
        messagebox.showerror(message="There are not passwords stored yet.")
    else:
        if website in data:
            answer = data.get(website)
            name = answer["username"]
            password = answer.get("password")
            messagebox.showinfo(title=site_input.get(), message=f"Username: {name}\nPassword: {password}")
        else:
            messagebox.showerror(message="There is not such entry! ")


# ---------------------------- UI SETUP -------------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50,  pady=50)

# Canvas and image.
canvas = Canvas(width=200, heigh=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels.
site_label = Label(text="Website:", font=(FONT_NAME, 14, "bold"))
name_text = Label(text="Email/Username:", font=(FONT_NAME, 14, "bold"))
code_label = Label(text="Password:", font=(FONT_NAME, 14, "bold"))

site_label.grid(row=1, column=0)
name_text.grid(row=2, column=0)
code_label.grid(row=3, column=0)

# Inputs.
site_input = Entry(width=19)
name_input = Entry(width=35)
password_input = Entry(width=19)

site_input.grid(row=1, column=1, sticky="EW")
name_input.grid(row=2, column=1, columnspan=2, sticky="EW")
password_input.grid(row=3, column=1, sticky="EW")

name_input.insert(0, "________@yahoo.gr")

# Button.
search_button = Button(text="Search", width=13, command=search_account)
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=36, command=save_password)

search_button.grid(row=1, column=2)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
