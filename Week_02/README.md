# 学习笔记
## 1. 哈希表、映射、集合

a. 哈希表：使用hash function（可能会出现哈希碰撞——拉链式解决冲突法）；查询、添加、删除均为O(1)

b. 映射：key-value对，key不重复

c. 集合：不重复的元素的集合

## 2. 树、二叉树、二叉搜索树

a. 树：无环，有环叫图；链表是特殊化的树，树是特殊化的图

b. 二叉树：前、中、后续遍历，查询复杂度O(n)——递归&迭代，统一解题模板见：
> https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/python3-er-cha-shu-suo-you-bian-li-mo-ban-ji-zhi-s/

c. 二叉搜索树：左子树上**所有结点**的值 < 根结点的值 < 右子树上**所有结点**的值，查询、添加、删除均O(logn)

## 3. 堆、二叉堆

a. 堆：用于取最大值或最小值，查找O(1)、删除O(logn)、插入O(logn)orO(1)

b. 二叉堆：相对比较容易实现，但效率不高；特性——完全二叉树+父节点值>=子节点值

## 4. 刷题相关：

a. 树的题目大都是递归的方法？可能由于树可以看出成是无数“parentNode + childNodes”的最小重复结构组成的，符合递归的思路

b. 堆排序：属于选择排序，主要步骤为——构建初始堆+交换堆顶和末尾元素并重建堆，复杂度平均为O(nlogn)
> https://www.geeksforgeeks.org/heap-sort/

c. 五毒神掌：目前每天需要刷题近6道，重在坚持！