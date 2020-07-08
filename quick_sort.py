"""Quick Sort Pythonic Implementation."""
import time


def partition(data, head, tail, draw_data, time_tick):
    """Partitioning the array."""
    border = head
    pivot = data[tail]

    draw_data(data, get_color_array(len(data), head, tail, border, border))
    time.sleep(time_tick)

    for j in range(head, tail):
        if data[j] < pivot:
            draw_data(data, get_color_array(len(data), head, tail, border,
                                            j, True))
            time.sleep(time_tick)
            data[border], data[j] = data[j], data[border]
            border += 1

        draw_data(data,
                  get_color_array(len(data), head, tail, border, j))
        time.sleep(time_tick)

    # Swap the pivot with the border value
    draw_data(data,
              get_color_array(len(data), head, tail, border, tail, True))
    time.sleep(time_tick)
    data[border], data[tail] = data[tail], data[border]

    return border


def quick_sort(data, head, tail, draw_data, time_tick):
    """Quick Sort the given Array."""
    if head < tail:
        partition_index = partition(data, head, tail, draw_data, time_tick)

        # Left partition
        quick_sort(data, head, partition_index-1, draw_data, time_tick)

        # Right partition
        quick_sort(data, partition_index+1, tail, draw_data, time_tick)


def get_color_array(data_length, head, tail, border, curr_index,
                    is_swapping=False):
    """Get the element colors for the given array."""
    color_array = []
    for i in range(data_length):
        # Base Coloring
        if i >= head and i <= tail:
            color_array.append('grey')
        else:
            color_array.append('white')
            
        if i == tail:
            color_array[i] = 'blue'
        elif i == border:
            color_array[i] = 'red'
        elif i == curr_index:
            color_array[i] = 'yellow'

        if is_swapping:
            if i == border or i == curr_index:
                color_array[i] = 'green'
    return color_array
