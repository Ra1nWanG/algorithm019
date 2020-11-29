# 学习笔记
# 深度优先搜索 & 广度优先搜索
## 1. 遍历搜索
### a. 每个节点均访问一次
### b. 每个节点仅访问一次
### c. 对于节点的访问顺序不限

i. 深度优先

ii. 广度优先

### d. 其他搜索：优先级搜索——“启发式搜索”
## 2. 深度优先遍历
### a. 递归写法

```
visited = set()

def dfs(node, visited):
    if node in visited: # terminator
        # already visited
        return
        
    visited.add(node)
    
    # process current node
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
```

### b. 非递归写法（栈）

```
def DFS(self, tree):

    if tree.node if None:
        return []
        
    visited, stack = [], [tree.root]
    
    while stack:
        node = stack.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)
        
    # other processing work
    ...
        
```

## 3. 广度优先遍历
### 非递归写法（用队列）

```
def BFS(graph, st, ed):
    
    queue = []
    queue.append([st])
    visited.add(st)
    
    while queue:
        node = queue.popleft()
        visitied.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
        
    # other processing work
    ...
        
```
## 4. DFS和BFS的对比
### a. 对于树的遍历：dfs（前序遍历） vs bfs（层序遍历）
### b. 很多题目中可以同时使用两种遍历方式

# 贪心算法 

## 1. 选择当前状态下最优 => 希望得到全局最优

## 2. 区别

### a. 贪心：局部最优判断，不能回退

### b. 回溯：可以回退

### c. 动态规划：最优判断 + 回退

## 3. 实际应用

### a. 局部贪心，全局搜索递归

### b. 选最优、选最近、选最好时，如最小生成树、哈夫曼编码等

### c. 高效、接近最优解，可用作辅助算法

## 4. 要点

### a. 问题可分解成子问题，子问题的最优解能递推到最终最优解 => 找出最优子结构

### b. 可用贪心的题目：能证明贪心可得全局最优；贪心的角度——从前往后？从局部开始？

# 二分查找

## 1. 三个前提条件

### a. 目标函数的单调性（有序）

### b. 存在上下界

### c. 能够通过索引访问（单链表不可）

## 2. 代码模板

```
# 假设是上升数组
left, right = 0, len(array) - 1
while left <= right: # 注意等号问题
    mid = (left + right) / 2
    # mid = left + (right - left) / 2 # 注意边界问题
    if array[mid] == target:
        # find the target!!!
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

# 刷题相关

## 1. BFS的题目存在双向解法，且效率更高（[单词接龙](https://leetcode-cn.com/problems/word-ladder/)）

## 2. 贪心算法可从局部出发，达成全局最优解（[跳跃游戏](https://leetcode-cn.com/problems/jump-game/)）

## 3. 二分查找注意边界和left>=right的情况

## 4. 一天7道题有点难顶，继续坚持！！！