'''
Problem statement:
- Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all overlapping intervals to produce a list that has only mutually exclusive intervals.
- The new interval is non-overlapping and sorted in ascending order.
- Write a function to return the list of intervals after inserting the new interval.
'''

def insert_interval(existing_intervals, new_interval):
    # 
    merged_intervals = []

    new_start, new_end = new_interval

    i = 0
    n = len(existing_intervals)
    while i < n and existing_intervals[i][1] < new_start:
        merged_intervals.append(existing_intervals[i])
        i += 1
    
    if not merged_intervals or merged_intervals[-1][1] < new_start:
        merged_intervals.append(new_interval)
    else:
        merged_intervals[-1][1] = max(merged_intervals[-1][1], new_end)

    while i < n:
        start, end = existing_intervals[i]
        if merged_intervals[-1][1] < start:
            merged_intervals.append(existing_intervals[i])
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
        i += 1

    return merged_intervals


# Driver code
def main():
    new_interval = [[5, 7], [8, 9], [10, 12], [1, 3], [1, 10]]
    existing_intervals = [
        [[1, 2], [3, 5], [6, 8]],
        [[1, 3], [5, 7], [10, 12]],
        [[8, 10], [12, 15]],
        [[5, 7], [8, 9]],
        [[3, 5]]
    ]
    
    for i in range(len(new_interval)):
        print(i + 1, ".\tExiting intervals: ", existing_intervals[i], sep="")
        print("\tNew interval: ", new_interval[i], sep="")
        output = insert_interval(existing_intervals[i], new_interval[i])
        print("\tUpdated intervals: ", output, sep = "")
        print("-"*100)


if __name__ == "__main__":
    main()
