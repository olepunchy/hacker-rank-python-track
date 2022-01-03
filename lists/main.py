#!/usr/bin/env python3

"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands
where each command will be of the 7 types listed above. Iterate through each
command in order and perform the corresponding operation on your list.

Example:
n = 4
append 1
append 2
inset 3 1

print
: Append 1 to the list, [1].
: Append 2 to the list, [1, 2].
: Insert 3 at index 1, [1, 3, 2].
: Print the array.

Output:
[1, 3, 2]

Input Format:

The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints:

The elements added to the list must be integers.

Output Format:

For each command of type print, print the list on a new line.

Sample Input:

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output:

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""


def operate_on_list(command, a_list):
    if len(command) >= 1:
        # The command has something in it
        command_parts = command.split()

        list_command = str(command_parts[0])

        # If the command has two parts
        if len(command_parts) >= 2:
            arg1 = int(command_parts[1])

        # If the command has three parts
        if len(command_parts) >= 3:
            arg2 = int(command_parts[2])

        if list_command == "print":
            print(a_list)

        elif list_command == "reverse":
            a_list.reverse()

        elif list_command == "sort":
            a_list.sort()

        elif list_command == "pop":
            a_list.pop()

        elif list_command == "insert":
            a_list.insert(arg1, arg2)

        elif list_command == "append":
            a_list.append(arg1)

        elif list_command == "remove":
            a_list.remove(arg1)


if __name__ == "__main__":
    N = int(input())

    the_list = []

    for i in range(N):
        command = input()  # take the input as a string
        operate_on_list(command, the_list)
