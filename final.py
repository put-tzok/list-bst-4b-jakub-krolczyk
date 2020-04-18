from bts import BTS
from lista import LinkedList
from random import randint
import time
ONE_SECOND = 1000
REPEATS = 1000

instances = [10, 50, 100, 200, 500, 1000, 2000, 2500, 3600, 5000]

def fill_increasing(size):
    array = []
    for i in range(size):
        array.append(i)

    return array

def fill_random(size):
    array = []
    max_element_size = size * 100
    for i in range(size):
        array.append(randint(0, max_element_size))

    return array

def time_clock(array, structure):
    start_time_append = time.time()
    for i in array:
        structure.append(i)
    end_time_append = time.time()
    time_append = round((end_time_append - start_time_append))
    start_time_find = time.time()
    for i in array:
        structure.find(i)
    end_time_find = time.time()
    time_find = round((end_time_find - start_time_find))
    return {'append': time_append,
            'find': time_find}

def linked_increasing(size):
    linked_list = LinkedList()
    array = fill_increasing(size)
    times = time_clock(array, linked_list)
    print(f"Linked, append, {size} size, increasing, {times['append']}")
    print(f"Linked, find, {size} size, increasing, {times['find']}")

def linked_random(size):
    linked_list = LinkedList()
    array = fill_random(size)
    times = time_clock(array, linked_list)
    print(f"Linked, append, {size} size, random, {times['append']}")
    print(f"Linked, find, {size} size, random, {times['find']}")

def bts_increasing(size):
    bts = BTS()
    array = fill_increasing(size)
    times = time_clock(array, bts)
    print(f"BTS, append, {size} size, increasing, {times['append']}")
    print(f"BTS, find, {size} size, increasing, {times['find']}")

def bts_random(size):
    bts = BTS()
    array = fill_random(size)
    times = time_clock(array, bts)
    print(f"BTS, append, {size} size, random, {times['append']}")
    print(f"BTS, find, {size} size, random, {times['find']}")

def main():
    for instance in instances:
        try:
            size = instance * REPEATS
            linked_increasing(size)
            linked_random(size)
            bts_increasing(size)
            bts_random(size)
        except RuntimeError as RE:
            print(f'Error in {RE}')

main()
