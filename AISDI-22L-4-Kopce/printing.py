def get_max_digits(heap):
    digits_list = [len(str(val)) for val in heap]
    digits = max(digits_list)

    if digits % 2 == 0:
        digits += 1
    return digits


def print_heap(heap, dim: int):
    lines = [[]]
    index = 0
    line_index = 0
    while index < len(heap):
        if line_index == len(lines):
            lines.append([])
        lines[line_index].append(heap[index])
        index += 1
        if len(lines[line_index]) == dim ** line_index:
            line_index += 1

    h = len(lines) - 1
    n = get_max_digits(heap)
    for i, line in enumerate(lines):
        dist = dim ** (h - i) * (n + 1) - n

        if i != 0:
            underscores = ' ' * (dist // 2 + n // 2 + 1)
            for j, val in enumerate(line):
                if j % dim == 0:
                    underscores += '_' * ((dim - 1) * (dist + n) - 1)
                elif j % dim == dim - 1 and j != len(line) - 1:
                    underscores += ' ' * (dist + n + 1)
            print(underscores)

        numbers = ' ' * (dist // 2)
        for j, val in enumerate(line):
            numbers += f"{val:^{n}}"
            if j != len(line) - 1:
                numbers += ' ' * dist
        print(numbers)


print_heap([i + 100 for i in range(63)], 2)
