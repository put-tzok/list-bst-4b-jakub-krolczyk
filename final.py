from bst import BST
from lista import LinkedList
from random import randint
import time
ONE_SECOND = 1000
REPEATS = 10

instances = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

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
    for run in range(REPEATS):
        for i in array:
            structure.append(i)
    end_time_append = time.time()
    time_append = round((end_time_append - start_time_append) * ONE_SECOND / REPEATS, 3)
    start_time_find = time.time()
    for run in range(REPEATS):
        for i in array:
            structure.find(i)
    end_time_find = time.time()
    time_find = round((end_time_find - start_time_find) * ONE_SECOND / REPEATS, 3)
    return {
        'append': time_append,
        'find': time_find
        }

def linked_increasing(size):
    linked_list = LinkedList()
    array = fill_increasing(size)
    times = time_clock(array, linked_list)
    print(f"Linked, append, {size} size, increasing, {round(times['append'] / size, 5)}")
    print(f"Linked, find, {size} size, increasing, {round(times['find'] / size, 5)}")

def linked_random(size):
    linked_list = LinkedList()
    array = fill_random(size)
    times = time_clock(array, linked_list)
    print(f"Linked, append, {size} size, random, {round(times['append'] / size, 5)}")
    print(f"Linked, find, {size} size, random, {round(times['find'] / size, 5)}")

def bst_increasing(size):
    bst = BST()
    array = fill_increasing(size)
    times = time_clock(array, bst)
    print(f"BST, append, {size} size, increasing, {round(times['append'] / size, 5)}")
    print(f"BST, find, {size} size, increasing, {round(times['find'] / size, 5)}")

def bst_random(size):
    bst = BST()
    array = fill_random(size)
    times = time_clock(array, bst)
    print(f"BST, append, {size} size, random, {round(times['append'] / size, 5)}")
    print(f"BST, find, {size} size, random, {round(times['find'] / size, 5)}")

def main():
    for instance in instances:
        try:
            linked_increasing(instance)
            linked_random(instance)
            bst_increasing(instance)
            bst_random(instance)
        except RuntimeError as re:
            print(f'Error in {re}')

main()
