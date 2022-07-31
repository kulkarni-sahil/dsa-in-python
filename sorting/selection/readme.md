# Selection Sort

video reference - [selection sort](https://youtu.be/GUDLRan2DWM)

## Sudo Code
- iter over the list based on index (0 to len of list -1) 
- inner - loop iter (i to len of list)
- for the iteration range find the smallest element and place it at the iterating index

practical example:
5 cards in your left hand

using extra space:
each time move the smallest card to the right hand and make the sorted list

in place sorting:
each time move the smallest card from the remaining cards and swap the cards

Example:
[8,4,7,2,9,1,3]

== Algo Output ==

iteration 1:
[1,4,7,2,9,8,3]

iteration 2:
[1,2,7,4,9,8,3]

iteration 3:
[1,2,3,4,9,8,7]

iteration 4:
[1,2,3,4,9,8,7]

iteration 5:
[1,2,3,4,7,8,9]

iteration 6:
[1,2,3,4,7,8,9]
