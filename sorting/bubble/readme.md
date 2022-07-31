# Bubble Sort

video reference - [bubble sort](https://youtu.be/Jdtq5uKz-w4)

## Sudo Code
- iter over the list based on index (0 to len of list -1) 
- inner - loop iter (0 to len of list - 1)
- In each iteration:
  - compare current element with the next element
  - If the current element is greater than the next element -> swap the elements 
- At the end of each iteration we will find the largest element from the unsorted list 


Example:
[8,4,7,2,9,1,3]

== Algo Output ==

iteration 1:
[4,7,2,8,1,3,9]

iteration 2:
[4,2,7,1,3,8,9]

iteration 3:
[2,4,1,3,7,8,9]

iteration 4:
[2,1,3,4,7,8,9]

iteration 5:
[1,2,3,4,7,8,9]

iteration 6:
[1,2,3,4,7,8,9]

## Time Complexity:

Best Case: O(n)

Average Case: O(n^2)

Worst Case: O(n^2)

