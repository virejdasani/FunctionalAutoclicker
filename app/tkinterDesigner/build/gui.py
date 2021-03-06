import os
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def autoclick():
    print("hi")
    # autoclicker.click_thread.start()
    os.system('python3 autoclicker.py')


window = Tk()

window.geometry("273x373")
window.configure(bg="#3E3E3E")

canvas = Canvas(
    window,
    bg="#3E3E3E",
    height=373,
    width=273,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: autoclick(),
    relief="flat"
)
button_1.place(
    x=63.999999999999986,
    y=286.0,
    width=146.0,
    height=55.0
)

canvas.create_text(
    20.999999999999986,
    10.0,
    anchor="nw",
    text="Autoclicker",
    fill="#FFFFFF",
    font=("Poppins Regular", 40 * -1)
)

canvas.create_text(
    72.99999999999999,
    111.0,
    anchor="nw",
    text="Delay",
    fill="#FFFFFF",
    font=("Poppins Regular", 20 * -1)
)

canvas.create_text(
    46.999999999999986,
    157.0,
    anchor="nw",
    text="Shortcut",
    fill="#FFFFFF",
    font=("Poppins Regular", 20 * -1)
)

canvas.create_text(
    11.999999999999986,
    206.0,
    anchor="nw",
    text="Click Count",
    fill="#FFFFFF",
    font=("Poppins Regular", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    185.5,
    126.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EBEBEB",
    highlightthickness=0
)
entry_1.place(
    x=150.0,
    y=111.0,
    width=71.0,
    height=28.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    186.5,
    172.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EBEBEB",
    highlightthickness=0
)
entry_2.place(
    x=151.0,
    y=157.0,
    width=71.0,
    height=28.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    186.5,
    221.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#EBEBEB",
    highlightthickness=0
)
entry_3.place(
    x=151.0,
    y=206.0,
    width=71.0,
    height=28.0
)

canvas.create_text(
    207.0,
    122.0,
    anchor="nw",
    text="ms",
    fill="#000000",
    font=("Poppins SemiBold", 10 * -1)
)
window.resizable(False, False)
window.mainloop()
