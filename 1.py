# 化简表达式：
# s = 1-2+3-4+5-6+...±N
# =(1-2)+(3-4)+(5-6)...(N-1-N) =-1-1-1-1-1...-1=-N/2 (N为偶数)
# =(1-2)+(3-4)+(5-6)...+N = -1-1-1-1-1-1...-1+N=-(N-1)/2+N=N/2+1/2=(N+1)/2 (N为奇数)
def sumFunction(n: int):
     return (n+1)/2 if n%2==1 else -n/2
print(sumFunction(666666))

# 如果n为1，则直接返回True
# 如果n重新出现在集合中，则跳出循环，返回False
def isHappy(n):
    num = set()
    while n not in num:
        num.add(n)
        temp = 0
        for i in str(n):
            temp += int(i) ** 2
        if temp == 1:
            return True
        else:
            n = temp
    return False
print(isHappy(19))

# 题解
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         return [*map(s.index, s)] == [*map(t.index, t)]
# 同构代表两个字符串中每个位置上字符在自身第一次出现的索引相同
# 细节补充
# str 类型数据拥有内置函数 index，输入一个子字符串，可以返回子字符串在 str 中第一次出现的索引，若不存在则报错
# map(函数，可迭代对象) 将会对（参数2：可迭代对象）中的每个元素运用（参数1：函数）并将结果按顺序储存在一个迭代器中，返回这个迭代器
# 使用 [*……] 可对对象解包，本题中 [*map……] 等效于 list(map……)
def mapping( s, t):
    return list(map(s.index, s)) == list(map(t.index, t))
    # return [*map(s.index, s)] == [*map(t.index, t)]
print(mapping(s="egg1",t="add"))

def isIsomorphic( s, t):
    if len(s) == len(t):
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True
print(isIsomorphic("ab","bb"))
