#!/usr/bin/python3
''' module that contains canUnlockAll '''


def canUnlockAll(boxes):
    ''' method that accepts a list of boxes and checks if all can be opened '''
    keys = [0]
    unlocked = []
    while True:
        if keys == unlocked:
            break
        for key in keys:
            if key not in unlocked:
                unlocked.append(key)
        for ibox in unlocked:
            if ibox >= len(boxes):
                continue
            current = boxes[ibox]
            for bx in current:
                if bx not in keys:
                    keys.append(bx)
    return len(unlocked) == len(boxes)
