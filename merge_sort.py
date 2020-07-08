"""Merge Sort Algorithm Pythonic implementation."""
import time


def merge_sort(data, draw_data, time_tick):
    """Merge Sort the given array of data.

    :param list data: data array to be partitioned.
    :param func draw_data: function to draw the data.
    :param int time_tick: time to sleep in seconds.
    """
    merge_sort_algorithm(data, 0, len(data)-1, draw_data, time_tick)
    

def merge_sort_algorithm(data, left, right, draw_data, time_tick):
    """Merge Sort Algorithm Brain.

    :param list data: data array to be sorted.
    :param int left: left element of the data.
    :param int right: right element of the data.
    :param func draw_data: function to draw the data.
    :param int time_tick: time to sleep in seconds.
    """
    if left < right:
        middle = (left + right) // 2
        merge_sort_algorithm(data, left, middle, draw_data, time_tick)
        merge_sort_algorithm(data, middle+1, right, draw_data, time_tick)
        merge(data, left, middle, right, draw_data, time_tick)


def merge(data, left, middle, right, draw_data, time_tick):
    """Merge two arrays.

    :param list data: data array to be merged.
    :param int left: left element of the data.
    :param int right: right element of the data.
    :param func draw_data: function to draw the data.
    :param int time_tick: time to sleep in seconds.
    """
    draw_data(data, get_color_array(len(data), left, middle, right))
    time.sleep(time_tick)

    left_part = data[left:middle+1]
    right_part = data[middle+1: right+1]

    left_index = right_index = 0
    for data_index in range(left, right+1):
        if left_index < len(left_part) and right_index < len(right_part):
            if left_part[left_index] <= right_part[right_index]:
                data[data_index] = left_part[left_index]
                left_index += 1
            else:
                data[data_index] = right_part[right_index]
                right_index += 1
        elif left_index < len(left_part):
            data[data_index] = left_part[left_index]
            left_index += 1
        else:
            data[data_index] = right_part[right_index]
            right_index += 1
    draw_data(data, ['green' if x >= left and x <= right else 'white' for x in
                     range(len(data))])
    time.sleep(time_tick)


def get_color_array(length, left, middle, right):
    """Get color of array elements.

    :param int length: length of the data array.
    :param int left: left element of the data.
    :param int right: right element of the data.
    :param int middle: middle element of the data.
    """
    color_array = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                color_array.append('yellow')
            else:
                color_array.append('pink')
        else:
            color_array.append('white')
    return color_array
