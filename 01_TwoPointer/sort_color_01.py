def sort_colors(colors):
    n = len(colors)
    red, white, blue = 0, 0, n - 1

    while white <= blue:
        if colors[white] == 0:
            # this item is red, swap it to the front
            colors[red], colors[white] = colors[white], colors[red]
            red += 1
            white += 1
        elif colors[white] == 1:
            # this item is white, skip it
            white += 1
        else:
            # this item is blue, swap it to the end
            colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1

    return colors


# Driver code
def main():
    inputs = [
        [0, 1, 0],
        [1, 1, 0, 2],
        [2, 1, 1, 0, 0],
        [2, 2, 2, 0, 1, 0],
        [2, 1, 1, 0, 1, 0, 2],
    ]

    for i in range(len(inputs)):
        colors = inputs[i]
        print(i + 1, ".\tcolors:", colors)
        sort_colors(colors)
        print("\n\tThe sorted array is:", colors)
        print("-" * 100)


if __name__ == "__main__":
    main()
