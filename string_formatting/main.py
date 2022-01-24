def print_formatted(n):

    for index in range(1, n + 1):
        width = n.bit_length()
        print(
            f"{index:{width}d} {index:{width}o} {index:{width}X} {index:{width}b}")


if __name__ == '__main__':
    n = int(input())

    print_formatted(n)
