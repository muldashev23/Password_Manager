from tkinter import *
from tkinter import messagebox
from parolik import generator
import pyperclip
import json
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

web = Label(text="Website:")
web.grid(row=1, column=0)
user = Label(text="Email/Username:")
user.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

entry_web = Entry(width=33)
entry_web.grid(row=1, column=1, columnspan=1)
entry_web.focus()
entry_user = Entry(width=52)
entry_user.grid(row=2, column=1, columnspan=2)
entry_user.insert(0, "Your email")
entry_password = Entry(width=33)
entry_password.grid(row=3, column=1)


def proverka():
    site = entry_web.get()
    pochta = entry_user.get()
    parolik = entry_password.get()
    json_info = {
        site: {
            "email": pochta,
            "password": parolik
        }
    }
    if len(site) < 1 or len(parolik) < 1:
        messagebox.showinfo(title="Warning", message="Website info or Password are empty! Please write it")
    else:
        try:
            with open("paroliki.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("paroliki.json", "w") as data_file:
                json.dump(json_info, data_file, indent=4)
        else:
            data.update(json_info)
            with open("paroliki.json", "w") as data_file:
                json.dump(data, data_file, indent = 4)
        finally:
            entry_web.delete(0, "end")
            entry_password.delete(0, "end")


def putin():
    parolius = generator()
    entry_password.insert(0, parolius)
    pyperclip.copy(parolius)

def find_pas():

    site = entry_web.get()
    try:
        with open("paroliki.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title=site, message=data[site])
    except FileNotFoundError:
        messagebox.showinfo(title=site, message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title=site, message="No details for the website exists")



gen_pas = Button(text="Generate Password", command=putin)
gen_pas.grid(row=3, column=2)
add = Button(text="Add", width=44, command=proverka)
add.grid(row=4, column=1, columnspan=2,)
search = Button(text="Search", width=14, command=find_pas)
search.grid(row=1, column=2)


window.mainloop()
