raw_list = [int(x) for x in input("Enter raw list as space separated numbers: ").split()]
print(f"Raw Unsorted List: {raw_list}")

for iterating_index in range(1, len(raw_list)):
    iterating_value = raw_list[iterating_index]
    visiting_index = iterating_index - 1

    while visiting_index >= 0:
        visiting_value = raw_list[visiting_index]
        if iterating_value < visiting_value:
            raw_list[visiting_index + 1] = visiting_value
            raw_list[visiting_index] = iterating_value
        else:
            break

        visiting_index -= 1

    print(f"Algo output after iteration {iterating_index}: {raw_list}")
