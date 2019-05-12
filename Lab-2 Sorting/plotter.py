# Author: Bishal Sarang
# Visualise input size vs time graph for worst and best case
import matplotlib.pyplot as plt
import random
import time

from merge_sort import merge_sort
from insertion_sort import insertion_sort

def visualise():
    sample_size = 1
    x, y1, y2, y3 = [], [], [], []

    for n in range(2000, 50000, 800):
        A = list(range(n))
        B = list(reversed(A))
        
        # Insertion Sort Best Case
        start_time = time.perf_counter()
        sorted_A = insertion_sort(A)
        end_time = time.perf_counter()
        x.append(n)
        
        y1.append((end_time - start_time) * 1000)
        
        # Insertion Sort Worst Case
        start_time = time.perf_counter()
        sorted_B = insertion_sort(B)
        end_time = time.perf_counter()
        y3.append((end_time - start_time) * 1000) 
        
        # Merge Sort Best Case/ Worst Case
        start_time = time.perf_counter()
        sorted_A = merge_sort(A)
        end_time = time.perf_counter()
        y2.append((end_time - start_time) * 1000)
        
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize = (15, 15), sharex= True)
    axes[0].plot(x, y1, x, y2)
    axes[0].set_title("Best Case", size = 30)
    axes[0].legend(("Insertion sort O(N)", "Merge Sort O(NlogN)"))
    axes[0].set_xlabel("Input Size (N)", color = "red", size = 20)
    axes[0].set_ylabel("Execution Time(t)in ms", color = "red", size = 20)
    
    axes[1].plot(x, y3, x, y2)
    axes[1].set_title("Worst Case", size = 30)
    axes[1].legend(("Insertion sort O(N * N)", "Merge Sort O(NlogN)"))
    axes[1].set_xlabel("Input Size (N)", color = "red", size = 20)
    axes[1].set_ylabel("Execution Time(t)in ms", color = "red", size = 20)
    fig.savefig("a.jpg")
    plt.show()
    
if __name__ == "__main__":
    visualise()
    
    
