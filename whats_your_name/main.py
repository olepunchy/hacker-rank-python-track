def print_full_name(first, last):
    print(f'Hello {first.title()} {last.title()}! You just delved into python.')


if __name__ == '__main__':
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    print_full_name(first_name, last_name)
