def merge(left_arr, right_arr, original_arr):
    left = 0
    right = 0
    original = 0

    while left < len(left_arr) and right < len(right_arr):
        if left_arr[left] <= right_arr[right]:
            original_arr[original] = left_arr[left]
            left += 1
        else:
            original_arr[original] = right_arr[right]
            right += 1
        original += 1

    while left < len(left_arr):
        original_arr[original] = left_arr[left]
        left += 1
        original += 1

    while right < len(right_arr):
        original_arr[original] = right_arr[right]
        right += 1
        original += 1

    return original_arr


def merge_sort(array):
    if len(array) < 2:
        # print("array size less than 2")
        return array

    mid = int(len(array)/2)
    left_array = [array[i] for i in range(mid)]
    right_array = [array[i] for i in range(mid, len(array))]

    left_array = merge_sort(array=left_array)
    right_array = merge_sort(array=right_array)

    array = merge(left_arr=left_array, right_arr=right_array, original_arr=array)
    return array


raw_list = list(map(int, input("Enter raw list as space separated numbers: ").split(' ')))
print(f"Raw Unsorted List: {raw_list}")

sorted_array = merge_sort(array=raw_list)
print(f"Sorted Array: {sorted_array}")
