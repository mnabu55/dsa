def print_array_with_markers(arr, iValue):
    out = "["
    for i in range(len(arr)):
        if iValue == i:
            out += "«"
            out += str(arr[i]) + "»" + ", "
        else:
            out += str(arr[i]) + ", "
    out = out[0 : len(out) - 2]
    out += "]"
    return out


def find_missing_number_wa(nums):
    len_nums = len(nums)
    index = 0
    print("\n\tSorting the array")
    while index < len_nums:
        print("\t\tLoop iteration ", index, ":", sep="")
        print("\t\t\t", print_array_with_markers(nums, index), sep="")
        value = nums[index]
        print("\t\t\tindex = ", index, sep="")
        print("\t\t\tvalue = ", value, sep="")
        # check if value is at the incorrect position
        if value != nums[value]:
            print(
                "\t\t\tSwapping the value: ",
                value,
                " with the value on index ",
                value,
                ": ",
                nums[value],
                sep="",
            )
            print("\t\t\t\t", print_array_with_markers(nums, [index, value]), sep="")
            # swap the value with its correct index
            nums[index], nums[value] = nums[value], nums[index]
            print(
                "\t\t\t\tAfter swapping: ",
                print_array_with_markers(nums, [index, value]),
                sep="",
            )
            # Move to the next loop
            continue
        # if the element is at the correct index or the value is equal to len_nums, move one element forward
        index += 1


def find_missing_number(nums):
    len_nums = len(nums)
    index = 0

    while index < len_nums:
        value = nums[index]
        if value < len_nums and nums[value] != value:
            nums[index], nums[value] = nums[value], nums[index]
        else:
            index += 1

    for i in range(len_nums):
        if i != nums[i]:
            return i
    return len_nums


def main():
    inputnumbers = [
        [4, 0, 3, 1],
        [8, 3, 5, 2, 4, 6, 0, 1],
        [1, 2, 3, 4, 6, 7, 8, 9, 10, 5],
        [0],
        [
            1,
            2,
            3,
            0,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            23,
        ],
    ]
    i = 1
    for x in inputnumbers:
        print(i, ".\tnums: ", x, sep="")
        print("\tMissing number: ", find_missing_number(x), sep="")
        print("-" * 100, "\n", sep="")
        i += 1


if __name__ == "__main__":
    main()
