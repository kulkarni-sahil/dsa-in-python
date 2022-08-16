# Merge Sort

video reference - [Merge sort](https://youtu.be/TzeBrDU-JaY)

## Sudo Code

You would need to have two different functions:
- merge(left_array, right_array, original_array)
- merge_sort()

### merge
- You have two arrays:
  - left_array
  - right_array
- You will iteratively find the smallest between the two arrays and fill it in the original array, till the point one of the array is visited completely
- Later you will fill the original array the remaining elements of the two arrays one after the other (only one of the array will be remaining)
- you return the sorted array

### merge_sort
- **RECURSION** is used here
- recursion break point: array size goes below 2 (if len(array) < 2 then return array)
- Find middle element break array into 2 halves 
- recursively merge sort the left half first 
- recursively merge sort the right half


merge 

Example:
[8,4,7,2,9,1,3,5]

[8,4,7,2] [9,1,3,5]
[8,4] [7,2]
[8] [4]
[8]
[4]
[4]
[8] [4] => [4,8]
[4,8] [7,2]
[4,8] [7]
[4,8] [7]
[4,8] [2]
[4,8] [2]
[4,8] [7] [2] => [2,7]
[4,8] [2,7]
[4,8] [2,7] => [2,4,7,8]
[2,4,7,8] [9,1,3,5]
...
[2,4,7,8] [1,3,5,9] => [1,2,3,4,5,7,8,9]

[1,2,3,4,5,7,8,9]


## Time Complexity:

Best Case: O(n)

Average Case: O(nlogn)

Worst Case: O(nlogn)
