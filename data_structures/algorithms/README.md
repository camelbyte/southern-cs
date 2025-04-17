# Algorithm Complexity & DSA Concepts

## Big O Notation (Time Complexity) & Real-Life Analogies

| Notation  | Name              | Explanation (Analogy) |
|-----------|------------------|----------------------|
| O(1)      | Constant Time     | Always takes the same time, no matter the input size. (e.g., Looking at the first page of a book) |
| O(log n)  | Logarithmic Time  | Quickly narrows down the problem space. (e.g., Finding a word in a dictionary using binary search) |
| O(n)      | Linear Time       | Time grows directly with input size. (e.g., Reading every page of a book to find a word) |
| O(n log n)| Linearithmic Time | Faster than O(n²), used in efficient sorting algorithms like Merge Sort. (e.g., Efficiently organizing files in a directory) |
| O(n²)     | Quadratic Time    | Nested loops, bad for large inputs. (e.g., Comparing every student in a class to every other student) |
| O(2ⁿ)     | Exponential Time  | Doubles with every new input, extremely slow. (e.g., Trying every possible combination of a lock) |

## Common Data Structures & Their Operations

| Data Structure       | Access  | Search  | Insertion | Deletion |
|----------------------|--------|--------|-----------|---------|
| Array               | O(1)   | O(n)   | O(n)      | O(n)    |
| Linked List         | O(n)   | O(n)   | O(1)      | O(1)    |
| Stack               | O(n)   | O(n)   | O(1)      | O(1)    |
| Queue               | O(n)   | O(n)   | O(1)      | O(1)    |
| Hash Table          | O(1)   | O(1)   | O(1)      | O(1)    |
| Binary Search Tree  | O(log n) | O(log n) | O(log n) | O(log n) |

## Basic Sorting Algorithms

| Algorithm      | Best Time Complexity | Worst Time Complexity | Stable? | In-Place? |
|--------------|--------------------|---------------------|---------|-----------|
| Bubble Sort  | O(n)               | O(n²)              | ✅ Yes  | ✅ Yes    |
| Selection Sort | O(n²)              | O(n²)              | ❌ No   | ✅ Yes    |
| Insertion Sort | O(n)               | O(n²)              | ✅ Yes  | ✅ Yes    |
| Merge Sort   | O(n log n)         | O(n log n)         | ✅ Yes  | ❌ No     |
| Quick Sort   | O(n log n)         | O(n²)              | ❌ No   | ✅ Yes    |

## License

This project is open-source. Feel free to modify and use it as needed.

