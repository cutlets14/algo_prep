# Analyzing Algorithms
* Analyzing algorithms based on their run-time (the amount of time it takes the computer to run the program when written in a programming language like Python) is not an effective mechanism because the algorithm's runtime is affected by the available processing power of the computer, the language in which the algorithm was written, and so on.
* Instead, it is preferable to analyze an algorithm based on the number of steps it requires to execute. Often, the number of steps taken by an algorithm is dependent on the size of the input, `n`.
* In recognizing this fact, it is therefore not important to exactly specify the number of steps an algorithm will take but rather provide an approximation of the number of steps it will take as `n` gets bigger. As `n` gets bigger, one part of the equation which describes the runtime of an algorithm with input size `n` tends to dominate the rest to point that everything else becomes irrelevant.
* In recognition of the fact that the important part of the algorithm is the part which grows the fastest as `n` gets bigger, Big O notation is a useful notation to adopt that describes how an algorithm's time or space requirements increase as the size of `n` increases.
  * An order of magnitude is a class in a classification system where each class is many times greater or smaller than the one before.
* These are the most commonly used classifications for order of magnitude in Big O notation, sorted from the best (most efficient) to worst (least efficient). Each order of magnitude describes an algorithm's time complexity, i.e., the maximum number of stpes an algorithm takes to complete as `n` gets bigger.
  * Constant time
  * Logarithmic time
  * Linear time
  * Log-linear time
  * Quadratic time
  * Cubic time
  * Exponential time

## Constant Time
* The most efficient order of magnitude.
* When an algorithm requires the same number of steps regardless of the problem's size.
* Notation is `O(1)`.

## Logarithmic Time
* When an algorithm's run time grows in proportion to the logarithm of the input size. This time complexity is often seen when algorithms discard many values at each iteration, like binary search.
* Notation is `O(logn)`. 

## Linear Time
* When an algorithm's run time grows at the same rate as the size of the problem.
* Notation is `O(n)`.

## Log-linear Time
* When an algorithm's run time grows as a combination (multiplication) of logarithmic and linear time complexities.
* Notation is `O(nlogn)`.

## Quadratic Time
* When an algorithm's run time is directly proportional to the problem's size squared.
* Notation is `O(n^2)`.

## Cubic Time
* When an algorithm's run time is directly proportional to the problem's size cubed.
* Notation is `O(n^3)`.

## Exponential Time
* The worst time complexity.
* When an algorithm's run time contains a constant raised to the size of the problem.

# Search Algorithms

## Linear Search
* Best suited for unsorted data.
* Worst-case complexity is `O(n)`, best-case is `O(1)` where the first element is the target item, and average is `O(n/2)`.
* Use `in` notation in Python.
  
```python
def linear_search(a_list, n):
  for i in a_list:
    if i == n:
      return True
  return False
```

## Binary Search
* Best suited for sorted data. Even in cases where unsorted data is to be searched, it's often worthwhile to sort the data and use binary search because of binary search's superior efficiency compared to linear search.
* Complexity is `O(logn)`.
```python
from bisect import bisect_left
def binary_search(an_iterable, item):
    index = bisect_left(an_iterable, item)

    if index <= len(an_iterable) and an_iterable[index] == item:
        return True
    return False
```

## Searching for characters
* A character set is the set of characters you can use, e.g., Unicode, which covers characters from all living languages in the world, or ASCII, which covers Latin-script alphabet.
* A character encoding is a way these characters are stored in memory to represent them digitally.
* There can be many encodings for a given charset. For instance, for Unicode, UTF-8, UTF-16 BE, and UTF-16 LE are support encodings. Unlike ASCII which uses 7/8 bits to represent characters, UTF-8 uses 32 bits to encode each character. However, UTF-8 is compatible with ASCII because it uses the same bit representation for the Latin-script alphabet.
```python
# Get a character's ASCII value
print(ord('a'))
```
# Sorting Algorithms
## Bubble Sort
* A sorting algorithm where you iterate through a list of numbers, compare each number to the next number, and swap them if they are out of order.
* This type of sort is called "bubble sort" because the highest values "bubble up" to the end of list, and those with the lowest values move to the beginning of the list as the algorithm progresses.
* The number of required iterations is equal to the number of elements in the array. After finishing the required iterations, we'll get the array sorted in ascending order.

# Data Structures
> Algorithms + Data Structures = Programs
* An abstract data type is a description of a data structure, whereas a data structure is an actual implementation.
  * A list is an abstract data type: it describes a data structure that holds a group of items where each item has a position relative to the others in an ordered fashion.
  * A Python list is a data structure since it is an implementation of the abstract data type.
* Data structures can be classified based on their properties. One such property is whether they are linear or non-linear.
  * A linear data structure arranges data elements in a sequence. For example, a list is a linear data structure because an element can have one element before and one element after.
  * A non-linear data structure arranges data elements non-sequentially. For example, a graph is a non-linear data structure where each element can connect to many other elements.
  * A static data structure is one which has a fixed size. For example, an array.
  * A dynamic data structure is one which can grow or shrink in size. For example, a dynamoc array, aka a list in Python.
* Traversing a data structure means going from the first element in a data structure to the last.
  
# Arrays
## Moving Zeros - p92
## Combine Two Lists - p94
## Finding duplicates in a list - p95
## Intersection of two lists - p98

# Linked Lists
