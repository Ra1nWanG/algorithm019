# 学习笔记
## 1. 递归：

a. 递归模板：recursion terminator + process logic in current level + drill down + revert the current level states

b. 递归要点：找到最小重复项，类似于函数递推关系式

## 2. 分治、回溯：

a. 分治模板：recursion terminator + prepare data(process) + conquer subproblems(drill down separately) + process and generate the final result + revert the current level states

b. 分治的要点：找重复性并分解成子问题

c. 回溯要点：每一层添加新的要素去试，可通过剪枝提升效率，主要运用dfs的思想

## 3. 刷题相关：

a. 基本上稍微复杂一些的递归解法都有分治的影子

b. 当问题是要求满足某种性质（约束条件）的所有解或最优解时，往往使用回溯法

b. 本周课程的主课部分不长，概念点并不多，但相关题目难度确实很高，例题讲解反复看了4-5遍保证理解

c. 五毒神掌：近期发现之前做过的一些有难度的题再看见还是有“知道大概思路但无法完整写出细节”的情况，可能需要提高“五毒神掌”的频率

d. 做题难点：目前一般的递归题目可做可理解，但链表相关题目对于head在执行过程是如何变化会理解混乱，尤其是在python中类似*tmp=head*的浅拷贝时，某个变量的变化会导致其他变量一同变化，操作时需注意！