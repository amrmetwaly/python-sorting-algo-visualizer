"""Sorting Algorithms in Visualized in Python using Tkinter."""

from tkinter import *
from tkinter import ttk, messagebox
import random

# region Tk initialize
root = Tk()
root.title('Sorting Algorithms Visualization')
root.maxsize(900, 600)
root.config(bg='black')
# endregion Tk initialize

# Global Variables
SELECTED_ALGORITHM = StringVar()
ALGORITHMS_SUPPORTED = ['Bubble Sort', 'Merge Sort']


def draw_data(data):
    """Draw our data visualization.

    :param list data: the data list of integers to be sorted.
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

        canvas.create_rectangle(x0, y0, x1, y1, fill='red')
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[index]))


# def get_user_values():
#     """Get the user values."""
#     try:
#         min_value = int(min_entry.get())
#         max_value = int(max_entry.get())
#         size_value = int(size_entry.get())
#     except ValueError:
#         err_message = "Only Integers Values Are Allowed for Min, Max, and Size."
#         messagebox.showinfo("Invalid Value", err_message)
#     else:
#         return [True, min_value, max_value, size_value]
#     finally:
#         return [False]

def generate():
    """Get the user choice for the algorithm."""
    print('Alg Selected: ' + SELECTED_ALGORITHM.get())
    min_value = int(min_entry.get())
    max_value = int(max_entry.get())
    size_value = int(size_entry.get())
    data = []
    for _ in range(size_value):
        data.append(random.randrange(min_value, max_value+1))
    draw_data(data)


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
Button(ui_frame, text='Generate', command=generate, bg='red').grid(row=0,
                                                                   column=2,
                                                                   padx=5,
                                                                   pady=5)
# endregion Row[0]
# region Row[1]
Label(ui_frame, text='Size ', bg='grey').grid(row=1, column=0, padx=5, pady=5,
                                              sticky=W)
size_entry = Entry(ui_frame)
size_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(ui_frame, text='Min Value', bg='grey').grid(row=1, column=2, padx=5,
                                                  pady=5, sticky=W)
min_entry = Entry(ui_frame)
min_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(ui_frame, text='Max Value', bg='grey').grid(row=1, column=4, padx=5,
                                                  pady=5, sticky=W)
max_entry = Entry(ui_frame)
max_entry.grid(row=1, column=5, padx=5, pady=5, sticky=W)
# endregion Row[1]

# endregion User Interface Area

root.mainloop()
