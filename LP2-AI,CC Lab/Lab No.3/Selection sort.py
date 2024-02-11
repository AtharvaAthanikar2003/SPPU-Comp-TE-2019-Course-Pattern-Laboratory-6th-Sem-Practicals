def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Enter as many numbers as we want in the array and it will sort the numbers given below
             
arr = list(map(int, input("Enter space-separated numbers: ").split()))
selection_sort(arr)
print("Sorted array is:", arr)