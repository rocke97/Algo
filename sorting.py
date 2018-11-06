# import sys
import time
import copy
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt
import random

def main():
    elements = list()
    times = list()
    merge_sort_times = list()
    insertion_sort_times = list()
    for i in range(1, 11):
        a = randint(0, 1000 * i, 200 * i)
        b = copy.deepcopy(a)
        c = copy.deepcopy(a)
        if(len(a) <= 1000):
            start = time.clock()
            insertion_sort(a)
            print(b)
            end = time.clock()
        else:
            start = time.clock()
            merge_sort(a)
            end = time.clock()

        merge_start = time.clock()
        merge_sort(b)
        merge_end = time.clock()

        insertion_start = time.clock()
        insertion_sort(c)
        insertion_end = time.clock()

        elements.append(len(a))
        times.append(end-start)
        print('CustomTime: ' + str(end-start))
        print('InsertionTime: ' + str(insertion_end-insertion_start))
        print('MergeTime: ' + str(merge_end-merge_start))
        merge_sort_times.append(merge_end-merge_start)
        insertion_sort_times.append(insertion_end-insertion_start)
    
    plt.xlabel('List Length')
    plt.ylabel('Time Complexity')
    plt.plot(elements, times, label = 'Custom Sort')
    plt.plot(elements, merge_sort_times, label = 'Merge Sort')
    plt.plot(elements, insertion_sort_times, label = 'Insertion Sort')
    plt.grid()
    plt.legend()
    plt.show()

def insertion_sort(Data):
    length = len(Data)
    for j in range(1, length):
        key = Data[j]
        i=j-1
        while((i>=0) and (Data[i]>key)):
            Data[i+1] = Data[i]
            i=i-1
        Data[i+1] = key
    return Data

def merge_sort(data):
    if len(data)>1:
        mid = len(data)//2
        left_half = data[:mid]
        right_half = data[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k]=left_half[i]
                i = i+1
            else:
                data[k]=right_half[i]
                j=j+1
            k=k+1
        while i < len(left_half):
            data[k]=left_half[i]
            i=i+1
            k=k+1
        while j < len(right_half):
            data[k] = right_half[j]
            j=j+1
            k=k+1

if __name__ == "__main__":
    main()