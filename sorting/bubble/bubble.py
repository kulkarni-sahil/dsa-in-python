raw_list = [int(x) for x in input("Enter raw list as space separated numbers: ").split()]
print(f"Unsorted raw list: {raw_list}")

for iterating_index in range(len(raw_list) - 1):
    swaps_made = False
    for visiting_index in range(len(raw_list) - iterating_index - 1):  # here we skip the sorted part of the list
        if raw_list[visiting_index] > raw_list[visiting_index + 1]:
            temp = raw_list[visiting_index]
            raw_list[visiting_index] = raw_list[visiting_index + 1]
            raw_list[visiting_index + 1] = temp
            swaps_made = True

    print(f"Algo output after iteration {iterating_index + 1}: {raw_list}")
    if swaps_made is False:  # If there are no swaps in an iteration that means the list is sorted
        print("List is sorted no need of further iteration(s)")
        break
