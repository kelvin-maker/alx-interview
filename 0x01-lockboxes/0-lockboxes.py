#!/usr/bin/python3
"""
lockboxes code determines if all the boxes can be opened by using a set
to store the keys and iterating through the boxes,
adding the keys in each box to the set if the current box is unlocked
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened.
    """
    # Set to store keys
    keys = set()
    # Add the keys in the first box to the set
    keys.update(boxes[0])

    # Set to store the boxes that have been unlocked
    unlocked = set()
    # Add the first box to the set of unlocked boxes
    unlocked.add(0)

    # Iterate through the boxes
    while True:
        # Flag to indicate if any box was unlocked in this iteration
        unlocked_box = False

        # Iterate through the boxes
        for i in range(len(boxes)):
            # If the current box is not locked (i.e. has a key in the set)
            # and has not been unlocked yet
            if i in keys and i not in unlocked:
                # Add the keys in the current box to the set
                keys.update(boxes[i])
                # Add the current box to the set of unlocked boxes
                unlocked.add(i)
                # Set the flag to indicate that a box was unlocked
                unlocked_box = True

        # If no box was unlocked in this iteration, break out of the loop
        if not unlocked_box:
            break

    # Return True if all boxes have been unlocked, else False
    return len(unlocked) == len(boxes)
