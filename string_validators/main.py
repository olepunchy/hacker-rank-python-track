def validate_string(s):
    is_alpha_numeric = False
    is_alpha = False
    is_digits = False
    is_lowercase = False
    is_uppercase = False

    for letter in s:
        if letter.isalnum():
            is_alpha_numeric = True

        if letter.isalpha():
            is_alpha = True

        if letter.isdigit():
            is_digits = True

        if letter.islower():
            is_lowercase = True

        if letter.isupper():
            is_uppercase = True

    print(f'{is_alpha_numeric}\n{is_alpha}\n{is_digits}\n{is_lowercase}\n{is_uppercase}')


if __name__ == '__main__':
    s = input()
    validate_string(s)
