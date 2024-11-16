from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def set_image():
    tag = tag_combobox.get()
    if tag:
        img = load_image(f"{url}/{tag}")
    else:
        img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img


def open_new_window():
    tag = tag_combobox.get()
    if tag:
        img = load_image(f"{url}/{tag}")
    else:
        img = load_image(url)

    if img:
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.pack()
        label.image = img


def exit():
    window.destroy()


url = "https://cataas.com/cat"
Allowed_tags = ["", "black", "detective", "fight", "jump", "piano", "pino", "sleep"]

window = Tk()
window.title("Cats!")
window.geometry("600x520")

label = Label()
label.pack(expand=True)

# update_button = Button(text="Обновить", command=set_image)
# update_button.pack(side=LEFT, fill=BOTH)

tag_button = Button(text="Загрузить по тегу:", command=set_image)
tag_button.pack(side=LEFT, fill=BOTH)

# tag_entry = Entry()
# tag_entry.pack(side=LEFT, fill=BOTH)

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=set_image)
file_menu.add_command(label="Загрузить фото в новом окне", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)


tag_label = Label(window, text="Выбери тег:")
tag_label.pack(side=LEFT, fill=BOTH)

tag_combobox = ttk.Combobox(values=Allowed_tags)
tag_combobox.pack(side=LEFT, fill=BOTH)

set_image()

window.mainloop()
