# 学习笔记

## 1. 位运算

### a. 位操作

```
左移（ << ）
右移（ >> ）
按位或（ | ）
按位与（ & ）
按位取反（ ~ ）
按位异或（ ^ ）
取反加一（ - ）
```

### b. 异或操作

```
x ^ 0 = x
x ^ 1s = ~x	// 注意1s = ~0
x ^ (~x) = 1s
x ^ x = 0
c = a ^ b => a ^ c = b, b ^ c = a	// 交换两个数
a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c	// 结合律
```

### c. 制定位置的位运算

```
1. 将x最右边的n位清零：x & (~0 << n)
2. 获取x的第n位值（0或者1）：(x >> n) & 1
3. 获取x的第n位的幂值：x & (1 << n)
4. 仅将第n位为1：x | (1 << n)
5. 仅将第n位为0：x & (~(1 << n))
6. 将x最高位至第n位（含）清零：x & ((1 << n) - 1)
```

### d. 实战位运算

```
1. 判断奇偶：
	x % 2 == 1 --> (x & 1) == 1
	x % 2 == 0 --> (x & 1) == 0
2. 求中值：
	x >> 1 --> x // 2
3. 清零最低位1：
	x = x & (x - 1)
4. 得到最低位的1：
	x & -x
5. x & ~x => 0
```

## 2. 布隆过滤器

### a. 优点：空间效率和查询时间都远远超过一般算法

### b. 缺点：有一定的误识别率和删除困难

### c. 示例代码

```
# Python 
from bitarray import bitarray 
import mmh3 
class BloomFilter: 
	def __init__(self, size, hash_num): 
		self.size = size 
		self.hash_num = hash_num 
		self.bit_array = bitarray(size) 
		self.bit_array.setall(0) 
	def add(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			self.bit_array[result] = 1 
	def lookup(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			if self.bit_array[result] == 0: 
				return "Nope" 
		return "Probably" 
bf = BloomFilter(500000, 7) 
bf.add("dantezhao") 
print (bf.lookup("dantezhao")) 
print (bf.lookup("yyj")) 
```

## 3. LRU Cache

### a. 两个要素：大小、替换策略

### b. 实现算法：Hash Table + Double LinkedList

### c. 复杂度：查询（O(1)），修改更新（O(1)）

### d. 替换策略

#### i. LFU - Least Frequently Used

#### ii. LRU - Least Recently Used

### e. 示例代码

```
# Python 

class LRUCache(object): 

	def __init__(self, capacity): 
		self.dic = collections.OrderedDict() 
		self.remain = capacity

	def get(self, key): 
		if key not in self.dic: 
			return -1 
		v = self.dic.pop(key) 
		self.dic[key] = v   # key as the newest one 
		return v 

	def put(self, key, value): 
		if key in self.dic: 
			self.dic.pop(key) 
		else: 
			if self.remain > 0: 
				self.remain -= 1 
			else:   # self.dic is full
				self.dic.popitem(last=False) 
		self.dic[key] = value
```
详见[例题](https://leetcode-cn.com/problems/lru-cache/)

## 4. 排序算法

### a. 分类

```
1. 比较类排序：时间复杂度>O(nlogn)
	a. 交换排序：冒泡、快速
	b. 插入排序：简单插入、希尔
	c. 选择排序：简单选择、堆
	d. 归并排序：二路归并、多路归并
2. 非比较类排序：线性时间
	a. 计数排序
	b. 桶排序
	c. 基数排序
```

### b. 十大经典算法排序

[相关链接](https://www.cnblogs.com/onepixel/p/7674659.html)

### c. 初级排序

```
1. 选择排序
2. 插入排序
3. 冒泡排序

```

### d. 高级排序

```
1. [快速排序](https://shimo.im/docs/TX9bDbSC7C0CR5XO/read)
2. [归并排序](https://shimo.im/docs/sDXxjjiKf3gLVVAU/read)
3. [堆排序](https://shimo.im/docs/M2xfacKvwzAykhz6/read)
```

### e. 特殊排序

```
1. 计数排序
2. 桶排序
3. 基数排序
```


