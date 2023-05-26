A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):
    # Find the minimum element in the remaining unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[j] < A[min_idx]:
            min_idx = j

    # Swap the found minimum element with the first element
    A[i], A[min_idx] = A[min_idx], A[i]

# Print the sorted array
print("Sorted array:", ", ".join(str(num) for num in A))
