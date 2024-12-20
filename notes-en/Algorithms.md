# Algorithms

## Sorting Algorithms

| Sorting Algorithm | Average Time Complexity | Best Case  | Worst Case | Space Complexity | Sorting Type | Stability |
|-------------------|-------------------------|------------|------------|------------------|--------------|-----------|
| Bubble Sort       | O(n²)                   | O(n)       | O(n²)      | O(1)             | In-place     | Stable    |
| Selection Sort    | O(n²)                   | O(n²)      | O(n²)      | O(1)             | In-place     | Unstable  |
| Insertion Sort    | O(n²)                   | O(n)       | O(n²)      | O(1)             | In-place     | Stable    |
| Shell Sort        | O(n^1.3)                | O(n)       | O(n²)      | O(1)             | In-place     | Unstable  |
| Merge Sort        | O(n log n)              | O(n log n) | O(n log n) | O(n)             | External     | Stable    |
| Quick Sort        | O(n log n)              | O(n log n) | O(n²)      | O(log n)         | In-place     | Unstable  |
| Heap Sort         | O(n log n)              | O(n log n) | O(n log n) | O(1)             | In-place     | Unstable  |
| Counting Sort     | O(n + k)                | O(n + k)   | O(n + k)   | O(k)             | External     | Stable    |
| Bucket Sort       | O(n + k)                | O(n + k)   | O(n²)      | O(n + k)         | External     | Stable    |
| Radix Sort        | O(n * k)                | O(n * k)   | O(n * k)   | O(n + k)         | In-place     | Stable    |

## Simulated Annealing
- Based on the hill-climbing algorithm, which can only find the optimal solution if the function is convex; otherwise, it may get stuck in a local optimum.
- Simulated annealing, however, has a certain probability of escaping the current optimum to explore other solutions, thus avoiding local optima. This probability gradually decreases until it reaches zero after multiple iterations.
