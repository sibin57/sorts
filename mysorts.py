"""Модуль сортировки числового списка по ссылке

Функции:
bubble_sort -- сортировка пузырьком
selection_sort -- сортировка выбором
insertion sort -- сортировка вставками
"""

def bubble_sort(lst):
    """Сортировка числового списка по ссылке методом пузырька."""

    had_swaps = True
    while had_swaps:
        had_swaps = False
        for i in range(1, len(lst)):
            if lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
                had_swaps = True

            
def selection_sort(lst):
    """Сортировка числового списка по ссылке методом выбора"""
    for i in range(len(lst)-1, -1, -1):
        for j in range(i, -1, -1):
            if lst[j] > lst[i]:
                lst[i], lst[j] = lst[j], lst[i]


def insertion_sort(lst):
    """Сортировка числового списка по ссылке методом вставок"""
    for i in range(1, len(lst)):
        elem = lst[i]
        j = i
        while j > 0 and lst[j-1]>elem:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = elem
