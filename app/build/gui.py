
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("273x373")
window.configure(bg = "#3E3E3E")


canvas = Canvas(
    window,
    bg = "#3E3E3E",
    height = 373,
    width = 273,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=63.999999999999986,
    y=300.0,
    width=146.0,
    height=55.0
)

canvas.create_text(
    85.99999999999999,
    283.0,
    anchor="nw",
    text="Start",
    fill="#EFEFEF",
    font=("Poppins SemiBold", 30 * -1)
)

canvas.create_text(
    1.4210854715202004e-14,
    10.0,
    anchor="nw",
    text="Autoclicker",
    fill="#EBEBEB",
    font=("Poppins SemiBold", 40 * -1)
)

canvas.create_text(
    77.99999999999999,
    109.0,
    anchor="nw",
    text="Delay",
    fill="#FFFFFF",
    font=("Poppins Regular", 20 * -1)
)

canvas.create_text(
    46.999999999999986,
    156.0,
    anchor="nw",
    text="Shortcut",
    fill="#FFFFFF",
    font=("Poppins Regular", 20 * -1)
)

canvas.create_text(
    11.999999999999986,
    207.0,
    anchor="nw",
    text="Click Count",
    fill="#FFFFFF",
    font=("Poppins Regular", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    195.5,
    125.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EBEBEB",
    highlightthickness=0
)
entry_1.place(
    x=165.5,
    y=112.0,
    width=60.0,
    height=25.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    195.5,
    172.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EBEBEB",
    highlightthickness=0
)
entry_2.place(
    x=165.5,
    y=159.0,
    width=60.0,
    height=25.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    195.5,
    221.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#EBEBEB",
    highlightthickness=0
)
entry_3.place(
    x=165.5,
    y=208.0,
    width=60.0,
    height=25.0
)

canvas.create_text(
    152.0,
    112.0,
    anchor="nw",
    text="150 ms",
    fill="#4C4C4C",
    font=("Poppins Regular", 20 * -1)
)

canvas.create_text(
    152.0,
    159.0,
    anchor="nw",
    text="F",
    fill="#4C4C4C",
    font=("Poppins Regular", 20 * -1)
)

canvas.create_text(
    152.0,
    208.0,
    anchor="nw",
    text="0",
    fill="#4C4C4C",
    font=("Poppins Regular", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
