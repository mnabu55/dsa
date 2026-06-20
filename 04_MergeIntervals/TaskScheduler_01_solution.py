

def least_time(tasks, n):
    frequencies = {}

    for t in tasks:
        frequencies[t] = frequencies.get(t,0) + 1

    frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1]))
    max_freq = frequencies.popitem()[1]
    idle_time = (max_freq - 1) * n

    while frequencies and idle_time > 0:
        idle_time -= min(max_freq - 1, frequencies.popitem()[1])
    idle_time = max(0, idle_time)

    return len(tasks) + idle_time


def main():
    tasks_list = [
#        ["A", "A", "B", "B"],
        ["A", "B", "A", "A", "B", "C"]
    ]
    n_list = [
#        2,
        3
    ]
    ans_list = [
#        5,
        9
    ]

    for tasks, n, ans in zip(tasks_list, n_list, ans_list):
        assert least_time(tasks, n) == ans


if __name__ == '__main__':
    main()
