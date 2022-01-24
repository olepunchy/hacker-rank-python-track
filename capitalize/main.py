def capitalize_name(s):
    for letter in s[:].split():
        s = s.replace(letter, letter.capitalize())

    return s


if __name__ == '__main__':
    s = input()
    result = capitalize_name(s)
    print(result)
