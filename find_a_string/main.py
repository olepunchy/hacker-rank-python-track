def count_substring(string, sub_string):

    found = 0
    sub_length = len(sub_string)

    for index, _ in enumerate(string):
        string_slice = string[index:sub_length + index]

        # Debug print statement to confirm assumptions about what the slice looks like.
        #print(f'Found: {string_slice}')

        if string_slice == sub_string:
            found += 1

    return found


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
