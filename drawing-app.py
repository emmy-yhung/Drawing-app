import time
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import PIL.ImageGrab as ImageGrab
from tkinter import colorchooser, messagebox

window = Tk()
window.title("Drawing App")

def select_brush():
    pass
    global selected_color
    selected_color = previous_color

def change_brush_size(value):
    pass
    global brush_size
    brush_size = int(value)

def select_brush_size():
    pass
    new_window = Toplevel(window)
    new_window.title("Select Brush Size")
    new_window.geometry("400x100")

    brush_size_label = Label(new_window, text="Brush Size")
    brush_size_label.pack()

    brush_size_slider = Scale(new_window, from_=1, to=25, orient=HORIZONTAL, command=change_brush_size)
    brush_size_slider.set(brush_size)
    brush_size_slider.pack()

def select_eraser():
    pass
    global selected_color, previous_color
    previous_color = selected_color
    selected_color = background_color

def select_eraser_size():
    pass
    new_window = Toplevel(window)
    new_window.title("Select Eraser Size")
    new_window.geometry("400x100")

    eraser_size_label = Label(new_window, text="Eraser Size")
    eraser_size_label.pack()

    eraser_size_slider = Scale(new_window, from_=1, to=20, orient=HORIZONTAL, command=change_brush_size)
    eraser_size_slider.set(brush_size)
    eraser_size_slider.pack()

def select_brush_color():
    pass
    global selected_color, previous_color
    color = colorchooser.askcolor(title="Select Color")[1]
    if color:
        selected_color = color
        previous_color = color

def select_background_color():
    pass
    global background_color, canvas
    color = colorchooser.askcolor(title="Select color")[1]
    if color:
        background_color = color
        canvas.config(bg=background_color)

def clear_canvas():
    pass
    canvas.delete('all')

def save_image():
    pass
    file_path = filedialog.asksaveasfilename(defaultextension=".png")

    time.sleep(0.1)

    x1 = window.winfo_rootx() + canvas.winfo_x()
    y1 = window.winfo_rooty() + canvas.winfo_x()

    x2 = x1 + canvas.winfo_width()
    y2 = y1 + canvas.winfo_height()

    if file_path:
        canvas.postscript(file=file_path, colormode="color")
        # Format: crop(left, top, right, bottom)
        ImageGrab.grab.crop((x1, y1,x2, y2)).save(file_path)

# Default Values
is_drawing = False
last_x = 0
last_y = 0
brush_size = 2
selected_color = "black"
previous_color = "black"
background_color = "white"

def start_drawing(event):
    global is_drawing, last_x, last_y
    is_drawing = True
    last_x = event.x
    last_y = event.y

def draw(event):
    global is_drawing, last_x, last_y
    if is_drawing:
        x,y = event.x, event.y
        canvas.create_line(last_x, last_y, x, y, width=brush_size, fill=selected_color)
        last_x = x
        last_y = y

def stop_drawing(event):
    global is_drawing
    is_drawing = False

def erase_drawing():
    global selected_color
    selected_color = "white"
# Create the menu bar
menu_bar = Menu(window)

# Create the brush menu
brush_menu = Menu(menu_bar, tearoff=0)
brush_menu.add_command(label="Select Brush", command=select_brush)
brush_menu.add_command(label="Select Brush Size", command=select_brush_size)

# Create the eraser menu
eraser_menu = Menu(menu_bar, tearoff=0)
eraser_menu.add_command(label="Select Eraser", command=select_eraser)
eraser_menu.add_command(label="Select Eraser Size", command=select_eraser_size)

# Create the color menu
color_menu = Menu(menu_bar, tearoff=0)
color_menu.add_command(label="Select Drawing Color", command=select_brush_color)
color_menu.add_command(label="Select Background Color", command=select_background_color)

# Create the clear menu
clear_menu = Menu(menu_bar, tearoff=0)
clear_menu.add_command(label="Clear Canvas", command=clear_canvas)

# Create the save menu
save_menu = Menu(menu_bar, tearoff=0)
save_menu.add_command(label="Save Drawing", command=save_image)

# Add the menus to the menu bar
menu_bar.add_cascade(label="Brush", menu=brush_menu)
menu_bar.add_cascade(label="Eraser", menu=eraser_menu)
menu_bar.add_cascade(label="Color", menu=color_menu)
menu_bar.add_cascade(label="Clear", menu=clear_menu)
menu_bar.add_cascade(label="Save", menu=save_menu)

# Configure the menu bar
window.config(menu=menu_bar)

canvas = Canvas(window, width=800, height=480, bg="white")
canvas.pack()
canvas.bind('<Button-1>', start_drawing)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>', stop_drawing)
window.mainloop()
