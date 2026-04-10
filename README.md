# Python Tower of Hanoi

A Python solution to the classic Tower of Hanoi puzzle 
using recursion.

## Features
- Automatically solves the Tower of Hanoi puzzle
- Works for any number of disks
- Tracks and displays each move step by step
- Uses recursion to break the problem into smaller pieces

## How It Works
Three rods are represented as lists. The largest disks 
start on the first rod. The recursive function moves 
disks one at a time, never placing a larger disk on top 
of a smaller one, until all disks reach the final rod.

## Technologies Used
- Python
- Recursion
- List data structures

## Example
```python
print(hanoi_solver(3))

# Output:
# [3, 2, 1] [] []
# [3, 2] [] [1]
# [3] [2] [1]
# [3] [2, 1] []
# [] [2, 1] [3]
# [1] [2] [3]
# [] [] [3, 2, 1]
```

## Why Tower of Hanoi?
Tower of Hanoi is a classic computer science problem that 
demonstrates the power of recursion. It is commonly used 
in technical interviews to test problem solving and 
understanding of recursive thinking!

## Author
crazytuff13
