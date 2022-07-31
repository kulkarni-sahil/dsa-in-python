raw_list = [int(x) for x in input().split()]
print(f"Unsorted Input List: {raw_list}")

for iterating_index in range(len(raw_list) - 1):
    smallest = None
    smallest_number_index = None

    for visiting_index in range(iterating_index, len(raw_list)):
        visiting_value = raw_list[visiting_index]
        if smallest is None:
            smallest = visiting_value
            smallest_number_index = visiting_index
        else:
            if visiting_value < smallest:
                smallest = visiting_value
                smallest_number_index = visiting_index

    raw_list[smallest_number_index] = raw_list[iterating_index]
    raw_list[iterating_index] = smallest

    print(f"Output after iteration {iterating_index + 1}: {raw_list}")
