# Algorithms

## 排序算法

| 排序算法   | 平均时间复杂度 | 最好情况    | 最坏情况    | 空间复杂度 | 排序方式 | 稳定性 |
|------------|----------------|-------------|-------------|------------|----------|--------|
| 冒泡排序   | O(n²)          | O(n)        | O(n²)       | O(1)       | 内排序   | 稳定   |
| 选择排序   | O(n²)          | O(n²)       | O(n²)       | O(1)       | 内排序   | 不稳定 |
| 插入排序   | O(n²)          | O(n)        | O(n²)       | O(1)       | 内排序   | 稳定   |
| 希尔排序   | O(n^1.3)       | O(n)        | O(n²)       | O(1)       | 内排序   | 不稳定 |
| 归并排序   | O(n log n)     | O(n log n)  | O(n log n)  | O(n)       | 外排序   | 稳定   |
| 快速排序   | O(n log n)     | O(n log n)  | O(n²)       | O(log n)   | 内排序   | 不稳定 |
| 堆排序     | O(n log n)     | O(n log n)  | O(n log n)  | O(1)       | 内排序   | 不稳定 |
| 计数排序   | O(n + k)       | O(n + k)    | O(n + k)    | O(k)       | 外排序   | 稳定   |
| 桶排序     | O(n + k)       | O(n + k)    | O(n²)       | O(n + k)   | 外排序   | 稳定   |
| 基数排序   | O(n * k)       | O(n * k)    | O(n * k)    | O(n + k)   | 内排序   | 稳定   |


## 模拟退火
- 基于爬山算法，爬山算法只有是凸函数才有可能找到最优，不然的话会陷入局部最优。
- 而模拟退火在进入某个最优的时候，会有一定概率跳出最优寻找其他点位，从而跳出局部最优。这个概率是衰竭的，在一次一次跳出后，衰竭为0。

## Python
```python
# 字典：有就返回，没有就是0
dict.get(i,0)
# 经常用
dict[i] = dict.get(i,0) + 1

# 从小到大排序, 时间复杂度O(nlogn)
sorted(list)

# 从大到小排序
sorted(list, reverse=True)

# 把list变成字符串
list = []
str = ''.join(list)
```

## Stack
- **Last In, First Out (LIFO)**
    ```python
    # Last In, First Out (LIFO) 
    stack = []

    # Push elements onto the stack
    stack.append(1)
    stack.append(2)
    stack.append(3)

    print("Stack after pushes:", stack)

    # Pop elements from the stack
    top = stack.pop()
    print("Popped element:", top)
    print("Stack after pop:", stack)

    class Stack:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            if not self.is_empty():
                return self.items.pop()
            raise IndexError("Pop from an empty stack")

        def peek(self):
            if not self.is_empty():
                return self.items[-1]
            raise IndexError("Peek from an empty stack")

        def is_empty(self):
            return len(self.items) == 0

        def size(self):
            return len(self.items)

    # Example usage
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Top element:", stack.peek())
    print("Stack size:", stack.size())

    stack.pop()
    print("Stack after pop:", stack.items)

    ```

## Queue
-  **First In, First Out (FIFO)**
    ```python
    queue = []

    # Enqueue elements
    queue.append(1)
    queue.append(2)
    queue.append(3)

    print("Queue after enqueues:", queue)

    # Dequeue elements
    front = queue.pop(0)
    print("Dequeued element:", front)
    print("Queue after dequeue:", queue)

    class Queue:
        def __init__(self):
            self.items = []

        def enqueue(self, item):
            self.items.append(item)

        def dequeue(self):
            if not self.is_empty():
                return self.items.pop(0)
            raise IndexError("Dequeue from an empty queue")

        def peek(self):
            if not self.is_empty():
                return self.items[0]
            raise IndexError("Peek from an empty queue")

        def is_empty(self):
            return len(self.items) == 0

        def size(self):
            return len(self.items)

    # Example usage
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Front element:", queue.peek())
    print("Queue size:", queue.size())

    queue.dequeue()
    print("Queue after dequeue:", queue.items)

    ```


## Is Subsequence (按顺序的子字符串)

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


## Is Subsequence (不按顺序的子字符串)
本质是两个子字符串的计数问题
- 时间复杂度为：O(m+n)
- 需要用到python的`dict.get(i,1)` 
```python
# 如果存在就+1，如果不存在就是 0 + 1
dict[i] = dict.get(i,0) + 1
```


## 双指针
https://zhuanlan.zhihu.com/p/657981698