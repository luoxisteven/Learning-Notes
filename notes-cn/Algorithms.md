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