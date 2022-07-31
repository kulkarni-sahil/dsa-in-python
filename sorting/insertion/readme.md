# Insertion Sort

video reference - [insertion sort](https://youtu.be/i-SKeOcBwko)

## Sudo Code

We will be dividing the list into sorted vs unsorted list
where elements in the unsorted list will be added to the sorted list

- iter over the list based (1 to len of list) # zeroth element can be considered sorted list
  - iter from iterating_index to 0 
  - compare the iterating_index element with the visiting element
  - if iterating_value < visiting_value: 
    - swap the two elements

Example:
[8,4,7,2,9,1,3]

== Algo Output ==

iteration 1:
[4,8,7,2,9,1,3]

iteration 2:
[4,7,8,2,9,1,3]

iteration 3:
[2,4,7,8,9,1,3]

iteration 4:
[2,4,7,8,9,1,3]

iteration 5:
[1,2,4,7,8,9,3]

iteration 6:
[1,2,3,4,7,8,9]

## Time Complexity:

Best Case: O(n)

Average Case: O(n^2)

Worst Case: O(n^2)

