#!/usr/bin/python3
"""
- Start with the 1st box at (index 0)
- Use set to track of the boxes that can be unlocked
"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    unlocked_boxes = set()
    queue = [0]

    while queue:
        box = queue.pop(0)
        if box not in unlocked_boxes:
            unlocked_boxes.add(box)
            for key in boxes[box]:
                if 0 <= key < n and key not in unlocked_boxes:
                    queue.append(key)

    return len(unlocked_boxes) == n
