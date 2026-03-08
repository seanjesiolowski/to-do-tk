from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, messagebox, font as tkfont

ASSETS_PATH = Path(__file__).parent / "assets"

MAX_ITEMS = 7
MAX_ITEM_LENGTH = 21
ITEM_Y_OFFSET = 100
ITEM_Y_SPACING = 50
ITEM_X = 77
FONT_FAMILY = "Fira Code"
BG_COLOR = "#ABABAB"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / path


def add_to_list(event):
    item = entry_var.get().strip()
    if item and len(item) <= MAX_ITEM_LENGTH and len(item_list) < MAX_ITEMS:
        item_list.append({"text": item, "done": False, "selected": False})
        render_items()
        entry_var.set("")


def clear_list():
    item_list.clear()
    render_items()


def create_item(idx, text, done=False, selected=False):
    y = idx * ITEM_Y_SPACING + ITEM_Y_OFFSET
    item_font = tkfont.Font(family=FONT_FAMILY, size=10, overstrike=done, underline=selected)
    return canvas.create_text(
        ITEM_X, y,
        anchor="nw",
        text=text,
        fill="#888888" if done else "#000000",
        font=item_font,
        tag="item",
    )


def move_item(direction):
    global selected_idx
    if selected_idx is None:
        return
    new_idx = (selected_idx + direction) % len(item_list)
    item_list.insert(new_idx, item_list.pop(selected_idx))
    selected_idx = new_idx
    render_items()


def on_item_left_click(event):
    clicked_id = event.widget.find_closest(event.x, event.y)[0]
    idx = item_id_list.index(clicked_id)
    item_list[idx]["done"] = not item_list[idx]["done"]
    render_items()


def on_item_right_click(event):
    clicked_id = event.widget.find_closest(event.x, event.y)[0]
    idx = item_id_list.index(clicked_id)
    if messagebox.askyesno("", "Delete this item?"):
        item_list.pop(idx)
        render_items()


def on_item_shift_left_click(event):
    global selected_idx
    clicked_id = event.widget.find_closest(event.x, event.y)[0]
    idx = item_id_list.index(clicked_id)
    if selected_idx is None:
        item_list[idx]["selected"] = True
        selected_idx = idx
    else:
        item_list[selected_idx]["selected"] = False
        selected_idx = None
    render_items()


def render_items():
    global item_id_list
    canvas.delete("item")
    item_id_list = []
    for idx, item in enumerate(item_list, 1):
        item_id = create_item(idx, item["text"], done=item["done"], selected=item["selected"])
        canvas.tag_bind(item_id, "<Button-1>", on_item_left_click)
        canvas.tag_bind(item_id, "<Button-3>", on_item_right_click)
        canvas.tag_bind(item_id, "<Shift-Button-1>", on_item_shift_left_click)
        item_id_list.append(item_id)


item_list = []
item_id_list = []
selected_idx = None

window = Tk()
window.title("To Do")
window.geometry("320x568")
window.configure(bg=BG_COLOR)
window.resizable(False, False)
window.bind("<Return>", add_to_list)
window.bind("<Up>", lambda e: move_item(-1))
window.bind("<Down>", lambda e: move_item(1))

canvas = Canvas(window, bg=BG_COLOR, height=568, width=320, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

canvas.create_text(53, 28, anchor="nw", text="to do", fill="#000000", font=(FONT_FAMILY, 14, "bold"))

canvas.create_text(
    53, 470, anchor="nw",
    text="Click: done  |  Right-click: delete\nShift+click: select/deselect\nArrow keys: reorder selected item",
    fill="#666666",
    font=(FONT_FAMILY, 7),
)

entry_var = StringVar(master=window)
entry_image = PhotoImage(file=relative_to_assets("entry.png"))
canvas.create_image(127, 93, image=entry_image)
entry = Entry(
    bd=0, bg="#D9D9D9", fg="#000716",
    highlightthickness=0, font=(FONT_FAMILY, 10),
    textvariable=entry_var,
)
entry.place(x=54, y=78, width=145, height=27)
entry.focus_set()

clear_button = Button(
    text="Clear all", borderwidth=0, highlightthickness=0,
    command=clear_list, relief="flat", font=(FONT_FAMILY, 8),
)
clear_button.place(x=70, y=540, width=71, height=22)

render_items()
window.mainloop()
