#!/usr/bin/python3
'''Minimum Operations task'''


def minOperations(n):
    '''write a method that calculates the fewest number of operations
 needed to result in exactly n H characters in the file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''
    pasted = 1  # how many characters in file
    copied = 0  # how many H's copied
    counter = 0  # operations counter

    while pasted < n:
        # if did not copy anything yet
        if copied == 0:
            # copy all
            copied = pasted
            # increment operations counter
            counter += 1

        # if haven't pasted anything yet
        if pasted == 1:
            # paste
            pasted += copied
            # increment operations counter
            counter += 1
            # continue to next loop
            continue

        remaining = n - pasted  # remaining chars to Paste
        if remaining < copied:
            return 0

        # if can't be devided
        if remaining % pasted != 0:
            # paste copied
            pasted += copied
            # increment operations counter
            counter += 1
        else:
            # copyall
            copied = pasted
            # paste
            pasted += copied
            # increment operations counter
            counter += 2

    # if got the desired result
    if pasted == n:
        return counter
    else:
        return 0
