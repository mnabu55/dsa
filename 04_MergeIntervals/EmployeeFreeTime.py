'''
'''


from interval import Interval
import heapq

def employee_free_time(schedule):
    heap = []
    
    for i in range(len(schedule)):
        heap.append((schedule[i][0].start, i, 0))
    
    heapq.heapify(heap)

    result = []
    previous = schedule[heap[0][1]][heap[0][2]].start

    while heap:
        _, i, j = heapq.heappop(heap)
        interval = schedule[i][j]
 
        if interval.start > previous:
            result.append(Interval(previous, interval.start))
        
        previous = max(previous, interval.end)

        if j + 1 < len(schedule[i]):
            heapq.heappush(heap, (schedule[i][j+1].start, i, j+1))
    
    return result

# Function for displaying interval list
def display(vec):
    string = "["
    if vec:
        for i in range(len(vec)):
            string += str(vec[i])
            if i + 1 < len(vec):
                string += ", "
    string += "]"
    return string

# Driver code
def main():
    inputs = [
        [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]],
        [[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]],
        [[Interval(2, 3), Interval(7, 9)], [Interval(1, 4), Interval(6, 7)]],
        [[Interval(3, 5), Interval(8, 10)], [Interval(4, 6), Interval(9, 12)], [Interval(5, 6), Interval(8, 10)]],
        [[Interval(1, 3), Interval(6, 9), Interval(10, 11)], [Interval(3, 4), Interval(7, 12)], [Interval(1, 3), Interval(7, 10)], [Interval(1, 4)], [Interval(7, 10), Interval(11, 12)]],
        [[Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8)], [Interval(2, 3), Interval(4, 5), Interval(6, 8)]],
        [[Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)]]

    ]
    i = 1
    for schedule in inputs:
        print(i, '.\tEmployee Schedules:', sep="")
        for s in schedule:
            print("\t\t", display(s), sep="")
        print("\tEmployees' free time", display(employee_free_time(schedule)))
        print('-'*100)
        i += 1


if __name__ == "__main__":
    main()
