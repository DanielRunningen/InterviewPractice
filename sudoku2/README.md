# sudoku2

**Source: [CodeSignal](https://app.codesignal.com/)**  
This question is listed as "easy" on their site and is intended to take 30 minutes.  
It is supposedly one of the questions asked by Apple and Uber during interviews.

## Problem

Sudoku is a number-placement puzzle.
The objective is to fill a `9` × `9` grid with numbers in such a way that each column, each row, and each of the nine `3` × `3` sub-grids that compose the grid all contain all of the numbers from `1` to `9` one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above.
Note that the puzzle represented by grid does not have to be solvable.

## Example

For

```python
grid = [
   ['.', '.', '.', '1', '4', '.', '.', '2', '.'],
   ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
   ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
   ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
   ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
   ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
   ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
   ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
   ['.', '.', '.', '5', '.', '.', '.', '7', '.']
]
```

the output should be `sudoku2(grid) = true`.

For

```python
grid = [
   ['.', '.', '.', '.', '2', '.', '.', '9', '.'],
   ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
   ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
   ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
   ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
   ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
   ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
   ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
   ['.', '2', '.', '.', '3', '.', '.', '.', '.']
]
```

the output should be `sudoku2(grid) = false`.

The given grid is not correct because there are two 1s in the second column.
Each column, each row, and each `3` × `3` subgrid can only contain the numbers `1` through `9` one time.

## Input/Output

* Execution time limit: 4 seconds (py3)
* Type: array.array.char `grid`
* Guaranteed constraints
  * A `9` × `9` 2D array of characters
  * Characters are either a digit from `'1'` to `'9'` or a period `'.'`
* Output: boolean, `true` if grid represents a valid Sudoku puzzle, else `false`.
