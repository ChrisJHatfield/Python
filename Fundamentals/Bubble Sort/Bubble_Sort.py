popularArr = [8,6,7,5,3,0,9]

def bubbleSort(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            # print(arr)
        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # print(arr)
    return arr

my_bubble_sort = print(bubbleSort(popularArr))

# arr = [1,3,5,7]
# arr[0], arr[1] = arr[1], arr[0]
# print(arr)