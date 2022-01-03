#!/usr/bin/env python3

"""
Given the participants' score sheet for your University Sports Day, you are
required to find the runner-up score. You are given n scores. Store them in a
list and find the score of the runner-up.

Input Format:

The first line contains n. The second line contains an array A[] of n integers
each separated by a space.

Output Format:

Print the runner up score

Sample Input:
5
2 3 6 6 5


Sample Output:
5

"""


def runner_un_score(n, scores):
    # Convert the scores map to a list
    scores_list = list(scores)

    # Convert the scores_list to a set to remove duplicates
    scores_set = set(scores_list)

    # What is the maximum value in the set?
    max_v = max(scores_set)

    # Remove it
    scores_set.discard(max_v)

    # Print the maximum value in the set
    print(max(scores_set))


if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    runner_un_score(n, arr)
