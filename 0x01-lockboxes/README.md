0-lockboxes
A function that determines if all the boxes can be opened.

Prototype
Copy code
def canUnlockAll(boxes)
Description
canUnlockAll is a function that receives a list of lists as argument. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes. The function returns True if all boxes can be opened and False otherwise.

Example
Copy code
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
Output:

Copy code
True
True
False
