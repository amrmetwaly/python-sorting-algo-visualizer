"""Sorting Algorithms in Visualized in Python using Tkinter."""

import random
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from tkinter import *
from tkinter import ttk

# region Tk initialize
root = Tk()
root.title('Sorting Algorithms Visualization')
root.maxsize(900, 600)
root.config(bg='black')
# endregion Tk initialize

# Global Variables
SELECTED_ALGORITHM = StringVar()
ALGORITHMS_SUPPORTED = ['Bubble Sort', 'Merge Sort', 'Quick Sort']
DATA = []


def draw_data(data, color_array):
    """Draw our data visualization.

    :param list data: the data list of integers to be sorted.
    :param list color_array: the colors chosen for the array of data.
    :rtype: None
    """
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 600
    x_width = canvas_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalized_data = [item / max(data) for item in data]

    for index, height in enumerate(normalized_data):
        # Top left
        x0 = index * x_width + offset + spacing
        y0 = canvas_height - height * 340
        # Bottom right
        x1 = (index + 1) * x_width + offset
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[index])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[index]))
    root.update_idletasks()


def generate():
    """Get the user choice for the algorithm."""
    global DATA
    min_value = int(min_entry.get())
    max_value = int(max_entry.get())
    size_value = int(size_entry.get())
    DATA = []
    for _ in range(size_value):
        DATA.append(random.randrange(min_value, max_value + 1))
    draw_data(DATA, ['red' for x in range(len(DATA))])


def start_algorithm():
    """Start Sorting algorithm."""
    global DATA

    if not DATA:
        return

    chosen_speed = speed_scale.get()

    if algorithm_menu.get() == 'Bubble Sort':
        bubble_sort(data=DATA, draw_data=draw_data, time_tick=chosen_speed)
    elif algorithm_menu.get() == 'Merge Sort':
        merge_sort(data=DATA, draw_data=draw_data, time_tick=chosen_speed)
    elif algorithm_menu.get() == 'Quick Sort':
        quick_sort(DATA, 0, len(DATA)-1, draw_data=draw_data,
                   time_tick=chosen_speed)

    # Always color the array elements in green after done sorting.
    draw_data(DATA, ['green' for x in range(len(DATA))])


# region Frame / Base Layout
ui_frame = Frame(root, width=600, height=200, bg='grey')
ui_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)
# endregion Frame / Base Layout

# region User Interface Area

# region Row[0]
Label(ui_frame, text='Algorithm: ', bg='grey').grid(row=0, column=0, padx=5,
                                                    pady=5, sticky=W)
algorithm_menu = ttk.Combobox(ui_frame, textvariable=SELECTED_ALGORITHM,
                              values=ALGORITHMS_SUPPORTED)
algorithm_menu.grid(row=0, column=1, padx=5, pady=5)
algorithm_menu.current(0)

speed_scale = Scale(ui_frame, from_=0.1, to=2.0, length=200, digits=2,
                    resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speed_scale.grid(row=0, column=2, padx=5, pady=5)
Button(ui_frame, text='Start', command=start_algorithm, bg='red').grid(row=0,
                                                                       column=3,
                                                                       padx=5,
                                                                       pady=5)
# endregion Row[0]
# region Row[1]
size_entry = Scale(ui_frame, from_=3, to=25, length=200,
                   resolution=1, orient=HORIZONTAL, label="Data Size")
size_entry.grid(row=1, column=0, padx=5, pady=5)

min_entry = Scale(ui_frame, from_=0, to=10, length=200,
                  resolution=1, orient=HORIZONTAL, label="Data Min Value")
min_entry.grid(row=1, column=1, padx=5, pady=5)

max_entry = Scale(ui_frame, from_=10, to=100, length=200,
                  resolution=1, orient=HORIZONTAL, label="Data Max Value")
max_entry.grid(row=1, column=2, padx=5, pady=5)

Button(ui_frame, text='Generate', command=generate, bg='white').grid(
    row=1,
    column=3,
    padx=5,
    pady=5)
# endregion Row[1]

# endregion User Interface Area

root.mainloop()
