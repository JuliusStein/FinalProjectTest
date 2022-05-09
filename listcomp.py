def remove_empty_arrays(arr):
    new2 = [item for item in arr if len(item) >= 2]
    # new = []
    # for i in arr:
    #     if len(i) != 0:
    #         new.append(i)
    return new2


test_input = ["a", "bc", [], [], [1, 2, 3]]
test_result = remove_empty_arrays(test_input)
print(test_result)
