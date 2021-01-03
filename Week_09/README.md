# 学习笔记

## 1. 复习递归、分治、动态规划

### a. 复习递归

```
1. 人肉递归低效
2. 找到最近最简方法，将其拆解成可重复解决的问题（感觉类似“最大公约数”）
3. 数学归纳法思想
4. **本质**：寻找重复性 --> 计算机指令集（for/while/递归调用）
```

### b. 复习分治

```
1. “分而治之”
2. 去除次优解，记忆化搜索
3. 可转化为动态规划
```

### c. 复习动态规划

```
1. 将复杂问题分解为简单子问题
2. 分治+最优子结构
3. 顺推形式：动态递推（数学归纳）
4. **关键点**：与递归、动态规划无根本区别（关键看有无最优子结构），共性：找到重复子问题，差异性：最优子结构、中途可以淘汰次优解
```

### d. 例题讲解

```
[爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)
[最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)
[打家劫舍](https://leetcode-cn.com/problems/house-robber/)
[股票买卖](https://github.com/eecrazy/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%9B%A2%E7%81%AD%E8%82%A1%E7%A5%A8%E9%97%AE%E9%A2%98.md)
```

## 2. 高级动态规划

### a. 复杂度来源

```
1. 状态拥有更多维度（二维、三维或更多，甚至需要压缩）
2. 状态方程更加复杂
3. **本质**：内功、逻辑思维、数学
```

### b. 例题讲解

```
1. 爬楼梯：n步，[x1,x2,xm]步，不能相邻重复步
2. [编辑距离](https://leetcode-cn.com/problems/edit-distance/)
```

## 3. 字符串基础

### a. 字符串

```
1. Python/Java/JS/C#/Go，字符串不可变
2. C/C++/Ruby/PHP，字符串可变
```

### b. 例题讲解

```
[字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)
[最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)
[反转字符串](https://leetcode-cn.com/problems/reverse-string/)
[翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/)
[找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)
```

### 4. 高级字符串算法

### a. 最长子串、子序列

```
[最长子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)
最长子串：连续不可跳过的是子串
[编辑距离](https://leetcode-cn.com/problems/edit-distance/)
```

### b. 字符串 + 递归/DP

```
[最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)
[正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/)
[不同的子序列](https://leetcode-cn.com/problems/distinct-subsequences/)
```

### 5. 字符串匹配算法

```
1. [暴力算法（brute force）](https://shimo.im/docs/8G0aJqNL86wWrPUE/read)
2. [Rabin-Karp算法](https://shimo.im/docs/1wnsM7eaZ6Ab9j9M/read)
3. [KMP算法](http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html) —— [视频](https://www.bilibili.com/video/av11866460?from=search&seid=17425875345653862171)
4. [Boyer-Moore算法](https://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html)
5. [Sunday算法](https://blog.csdn.net/u012505432/article/details/52210975)
```

