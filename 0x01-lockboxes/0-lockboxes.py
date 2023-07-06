#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    visited_boxes = set([0])
    unvisited_boxes = set(boxes[0]).difference(set([0]))
    while len(unvisited_boxes) > 0:
        boxIdx = unvisited_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in visited_boxes:
            unvisited_boxes = unvisited_boxes.union(boxes[boxIdx])
            visited_boxes.add(boxIdx)
    return n == len(visited_boxes)
