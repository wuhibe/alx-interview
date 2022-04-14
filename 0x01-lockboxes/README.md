# 0x01 - Lockboxes

## Problem Summary

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

* Prototype: ```def canUnlockAll(boxes)```

* boxes is a list of lists

* A key with the same number as a box opens that box

* You can assume all keys will be positive integers

* There can be keys that do not have boxes

* The first box boxes[0] is unlocked

* Return True if all boxes can be opened, else return False

## Strategy

 * Have a loop to iterate infinitely

 * To open all boxes from the keys we have and to add the keys we have found from those boxes to our list of keys if they're capable of opening boxes and they don't already exist in our keys list.

 * If all the keys we have have already opened all the boxes they can, break the loop and exit.

 * If all the boxes we've opened is all that exist, return true. Else false.