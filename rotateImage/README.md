# rotateImage

**Source: [CodeSignal](https://app.codesignal.com/)**  
This question is listed as "easy" on their site and is intended to take 15 minutes.  
It is supposedly one of the questions asked by Amazon, Microsoft, and Apple during interviews.

## Problem

You are given an `n` x `n` 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

_Note: Try to solve this task in-place (with `O(1)` additional memory), since this is what you'll be asked to do during an interview._

## Example

For

```python
a = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]
```

the output should be

```python
rotateImage(a) = [
   [7, 4, 1],
   [8, 5, 2],
   [9, 6, 3]
]
```

## Input/Output

* Execution time limit: 4 seconds (py3)
* Inputs:
   * `a` as a 2D array of integers
      * Guaranteed constraints
         * `1 ≤ a.length ≤ 100`
         * `a[i].length = a.length`
         * `1 ≤ a[i][j] ≤ 10^4`
* Output: a 2D array of integers representing the rotated image
