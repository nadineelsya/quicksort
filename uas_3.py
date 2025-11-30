def quicksort_desc(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x > pivot]     # lebih besar ke kiri
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]    # lebih kecil ke kanan

    return quicksort_desc(left) + mid + quicksort_desc(right)


# Data yang diberikan
data = [15, 45, 32, 22, 66, 75, 10, 17, 9]

print("Data asli :", data)
print("Sorted descending:", quicksort_desc(data))
