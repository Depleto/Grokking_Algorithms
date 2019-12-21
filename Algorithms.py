def binary_search(sorted_array, item):
    low = 0
    high = len(sorted_array) -1

    while low <= high:


        mid = (low + high) // 2
        guess = sorted_array[mid]

        if guess == item:
            return mid

        elif guess > item:
            high = mid-1

        else:
            low = mid + 1
    return None

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr



def recursive_countdown(i):
    print(i)
    if i <=0:
        return
    else:
        recursive_countdown(i-1)

def factorial_callstack_recursion(x):
    if x == 1:
        return 1
    else:
        return x * factorial_callstack_recursion(x-1)

def sum_recursive(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum_recursive(arr[1:])














if __name__ == '__main__':
    arr = [1,3,5,7,9,2,4,6,8,10]
    print(sum_recursive([1,2,3,4]))









