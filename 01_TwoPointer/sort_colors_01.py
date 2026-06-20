def sort_colors_ng(colors):
    n = len(colors)
    left, right = 0, n - 1
    
    count = 1
    for i in range(n):
        if colors[i] == 0:
            colors[i], colors[left] = colors[left], colors[i]
            left += 1
        if colors[i] == 2:
            colors[i], colors[right] = colors[right], colors[i]
            right -= 1

        count += 1

    return colors


def sort_colors(colors):
    n = len(colors)
    left, right = 0, n - 1
    current = 0
    
    while current <= right:
        if colors[current] == 0:
            colors[current], colors[left] = colors[left], colors[current]
            current += 1
            left += 1
        elif colors[current] == 1:
            current += 1
        else:
            colors[current], colors[right] = colors[right], colors[current]
            right -= 1

    return colors


colors = [2,1,1,0,0]
print(sort_colors(colors))

