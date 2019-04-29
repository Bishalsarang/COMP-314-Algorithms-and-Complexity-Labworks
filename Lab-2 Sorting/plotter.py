# Author: Bishal Sarang
# Visualise input size vs time graph for worst and best case
import matplotlib.pyplot as plt
import random
import time

from merge_sort import merge_sort
from insertion_sort import insertion_sort

def visualise():
    sample_size = 1
    x, y1, y2 = [], [], []

    for n in range(1000, 10000, 100):
        A = random.sample(range(n), n)
        

    
        start_time = time.perf_counter()
        sorted_A = insertion_sort(A)
        end_time = time.perf_counter()
        x.append(n)
        y1.append((end_time - start_time) * 1000)

        start_time = time.perf_counter()
        sorted_A = merge_sort(A)
        end_time = time.perf_counter()
        
        y2.append((end_time - start_time) * 1000)
    plt.plot(x, y1, x, y2)
    plt.xlabel("Input Size (N)", color = "red")
    plt.ylabel("Execution Time(t)in ms", color = "red")
    plt.show()
    
if __name__ == "__main__":
    visualise()
    
    
