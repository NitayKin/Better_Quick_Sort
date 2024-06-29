import time
import random

#the normal algorithm
def quick_sort(mat):
    if len(mat) <= 1:
        return mat
    pivot = mat[random.randint(0, len(mat) - 1)]
    smaller = [i for i in mat if i < pivot]
    equal = [i for i in mat if i == pivot]
    bigger = [i for i in mat if i > pivot]
    return quick_sort(smaller) + equal + quick_sort(bigger)

#my algorithm
def quick_sort_nitay(mat):
    if len(mat) <= 1:
        return mat

    def find_average(arr):
        return sum(arr) / len(arr)

    def quick_sort_helper(arr, min_val, max_val, pivot):
        if len(arr) <= 1:
            return arr

        smaller = [i for i in arr if i < pivot]
        equal = [i for i in arr if i == pivot]
        bigger = [i for i in arr if i > pivot]

        return quick_sort_helper(smaller, min_val, pivot, (min_val + pivot) // 2) + equal + quick_sort_helper(bigger, pivot, max_val, (max_val + pivot) // 2)

    min_val = min(mat)
    max_val = max(mat)
    initial_pivot = (min_val + max_val)//2
    return quick_sort_helper(mat, min_val, max_val, initial_pivot)

# function to measure time for each function call
def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time


# Function to compare sorting times for multiple arrays
def compare_sorting_functions(num_arrays, array_size):
    quick_sort_faster_count = 0
    quick_sort_nitay_faster_count = 0

    for _ in range(num_arrays):
        example_array = random.sample(range(1, array_size + 1), array_size)
        
        time_quick_sort = measure_time(quick_sort, example_array[:])
        time_quick_sort_nitay = measure_time(quick_sort_nitay, example_array[:])
        
        if time_quick_sort < time_quick_sort_nitay:
            quick_sort_faster_count += 1
        else:
            quick_sort_nitay_faster_count += 1

    total = quick_sort_faster_count + quick_sort_nitay_faster_count
    quick_sort_percentage = (quick_sort_faster_count / total) * 100
    quick_sort_nitay_percentage = (quick_sort_nitay_faster_count / total) * 100
    
    print("Quick sort was faster in {:.2f}% of cases".format(quick_sort_percentage))
    print("Quick sort Nitay was faster in {:.2f}% of cases".format(quick_sort_nitay_percentage))

#calling the check - can pick how many arrays and whats size each of them will be.
compare_sorting_functions(num_arrays=100, array_size=100000)






