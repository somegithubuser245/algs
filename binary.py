import string


ALPHABET = list(string.ascii_lowercase)


def sorted_nums_list(length: int):
    nums = [i for i in range(length)]
    return nums


def sorted_letters_list(depth: int):
    if depth < 0:
        raise ValueError("depth must be non-negative")

    letters_list = []

    for i in range(len(ALPHABET)):
        for j in range(len(ALPHABET)):
            char = ALPHABET[i]
            char += ALPHABET[j]
            letters_list.append(char)

    return letters_list


def letters_list_recursive(list: list[str], depth: int):
    if depth == 0:
        return list

    step_list = []

    for i in range(len(list)):
        for j in range(len(ALPHABET)):
            char = list[i]
            char += ALPHABET[j]
            step_list.append(char)
            # print(char)

    return letters_list_recursive(step_list, depth - 1)


def binary_search_nums(searched: int, nums: list[int]):
    low = 0
    high = len(nums) - 1

    print(f"HIGH: {high}")
    print(f"LOW: {low}")
    while low <= high:
        mid = (high + low) // 2
        result = nums[mid]

        if result == searched:
            return mid
        elif searched < result:
            high = mid - 1
        elif searched > result:
            low = mid + 1

        print(f"h: {high}")
        print(f"l: {low}")

    return None


nums = sorted_nums_list(10**5)
nums_simple = [1, 3, 5, 7, 9]
print(binary_search_nums(3, nums_simple))
