def merge_intervals(intervals):
    n = len(intervals)
    if n <= 1:
        return intervals
    
    merged = []
    merged.append(intervals[0])
    prev_start, prev_end = intervals[0][0], intervals[0][1]
    for i in range(1, n):
        current_start, current_end = intervals[i][0], intervals[i][1]
        prev_start, prev_end = merged[-1][0], merged[-1][1]

        if current_start <= prev_end:
            # Overlap, so update the end of the merged interval
            merged[-1][1] = max(prev_end, current_end)
        else:
            # No overlap, so add the current interval to the merged list
            merged.append(intervals[i])
    
    return merged


def main():
    all_intervals = [
    [[1, 5], [3, 7], [4, 6]],
    [[1, 5], [4, 6], [6, 8], [11, 15]],
    [[3, 7], [6, 8], [10, 12], [11, 15]],
    [[1, 5]],
    [[1, 9], [3, 8], [4, 4]],
    [[1, 2], [3, 4], [8, 8]],
    [[1, 5], [1, 3]],
    [[1, 5], [6, 9]],
    [[0, 0], [1, 18], [1, 3]]
    ]

    for i in range(len(all_intervals)):
        print(i + 1, ".\tIntervals to merge:\t", all_intervals[i])
        result = merge_intervals(all_intervals[i])
        print("\tMerged intervals:\t", result)
        print("-" * 50)


if __name__ == '__main__':
    main()
