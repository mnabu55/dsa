from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]
    for [current_start, current_end] in intervals[1:]:
        last_start, last_end = merged_intervals[-1]
        if last_end >= current_start:
            merged_intervals[-1][1] = max(last_end, current_end)
        else:
            merged_intervals.append([current_start, current_end])

    return merged_intervals


# Driver code
def main():

    all_intervals = [
        #        [[3, 7], [1, 5], [4, 6]],
        [[1, 5], [6, 8], [4, 6], [11, 15]],
        [[3, 7], [10, 12], [6, 8], [11, 15]],
        [[1, 5]],
        [[1, 9], [4, 4], [3, 8]],
        [[1, 2], [8, 8], [3, 4]],
        [[1, 5], [1, 3]],
        [[1, 5], [6, 9]],
        [[0, 0], [1, 18], [1, 3]],
    ]

    for i in range(len(all_intervals)):
        print(i + 1, ". Intervals to merge: ", all_intervals[i], sep="")
        result = merge_intervals(all_intervals[i])
        print("   merged_intervals intervals:\t", result)
        print("-" * 100)


if __name__ == "__main__":
    main()
