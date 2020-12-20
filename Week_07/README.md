# 学习笔记

## 1. 字典树（Trie）

### a. 结构特点

#### i. 又称单词查找树、键树，树形结构

#### ii. 典型应用：用于统计和排序大量的字符串，常被搜索引擎系统用于文本词频统计

#### iii. 优点：最大限度地减少无谓字符串比较，查询效率比哈希表高

### b. 基本性质

#### i. 结点本身不存完整单词

#### ii. 从根节点到某一结点，路径上经过的字符连接起来，成为该结点对应的字符串

#### iii. 每个结点的所有子结点路径代表的字符都不相同

#### iv. 结点可存储额外信息，如单词访问频次等

### c. 代码模板

```
# Python 
class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
```

## 2. 并查集

### a. 基本操作

#### i. makeSet(s)：建立一个新的并查集，其中包含s个单元素集合

#### ii. unionSet(x, y)：合并x和y所在集合，相交则不合并

#### iii. find(x)：找到x所在集合的代表，不同集合的代表不同，可用于判断两个元素是否位于同一个集合

#### iv. 路径压缩：提高查询效率

### b. 代码模板

```
# Python 
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩
		i, p[i] = p[i], root 
	return root
```

### c. 优质练习题

```
朋友圈：547
岛屿数量：200
被环绕的区域：130
```

## 3. 高级搜索

### a. 优化方法：不重复（斐波那契）、剪枝（重复、非最优）

### b. 搜索方向：双向搜索（广度）、启发式搜索（优先级）

### c. A*代码模板：

```
# Python
def AstarSearch(graph, start, end):
	pq = collections.priority_queue() # 优先级 —> 估价函数
	pq.append([start]) 
	visited.add(start)
	while pq: 
		node = pq.pop() # can we add more intelligence here ?
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		unvisited = [node for node in nodes if node not in visited]
		pq.push(unvisited)
```

### d. 优质练习题
```
单词接龙：487，223
数独：36，37
```
## 4. 高级树、AVL和红黑树

### a. AVL树：带有平衡条件（左右子树高度差在1之内）的二叉搜索树

### b. 红黑树：特化AVL树，进行插入和删除操作时通过特定操作保持二叉查找树的平衡，从而获得较高的查找性能

