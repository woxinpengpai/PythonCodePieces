# You should be as smart to make sure you behave yourself.
# Radix sorted

# part 1: radix sort demo
import random

def generate_test_cases(n):
    """generate a list of random integers of size n """
    nums = []
    for i in range(n):
        nums.append(str(random.randint(100, 999)))
    return nums
    
def radix_sort(nums):
    """sort a list using radix sorting method """
    # 这里假定了 nums 中都是三位数
    index = list(range(len(nums)))
    bucket = []
    for i in range(10):
        bucket.append([])
    DIGIT_NUMBER = 3
    for i in range(DIGIT_NUMBER):
        for j in range(10):
            bucket[j].clear()
        for j in index:
            # 将nums[i]放入对应 bucket 中 
            bucket[ord(nums[j][DIGIT_NUMBER - 1 - i]) - ord('0')].append(j)
        # update index
        index.clear()
        for b in bucket:
            for d in b:
                index.append(d)
    ans = []
    for i in index:
        ans.append(nums[i])
    # nums = ans 
    return ans
    
    
def check(nums):
    # check if nums is ascending
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            print("XXXXXXXXXXXXXX")
            return 
    print("√√√√√√√√√√√√√√√√√√√")
    

def run():
    nums = generate_test_cases(100)
    nums = radix_sort(nums)
    check(nums)
    print("************************")
    return
    
    
for i in range(20):
    run() # all is well 
    
    

    
# **********************************

# part 2: Solution to Leetcode 2343 https://leetcode.cn/problems/query-kth-smallest-trimmed-number/ 

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        # queries[i] = [ki, trimi] ki start from 1
        index = list(range(len(nums)))
        ans = [0] * len(queries)
        # 使用基数排序的思想， 从后向前逐位排序
        l = len(nums[0])
        temp = []
        for i in range(10):
            temp.append([])
        for i in range(l): # i 表示从后向前数的位数，每一轮所依据的位
            # clear temp
            for j in range(10):
                temp[j].clear()
            '''
            for j in index... 这里值得说一下
            index 中存放的始终是下标，如最开始是 0 1 2 3
            j 代表的是下标的值
            每次排序都会更新 index ,比如将其变为 2 0 3 1
            反正必须得弄清楚变量含义
            '''
            for j in index:
                # nums[j][l-1-i] 就是此轮排序依据的位
                # 始终使用 index 里面存放的下标 
                temp[ord(nums[j][l-1-i])-ord('0')].append(j)
            # print("temp is \n", temp)
            index.clear()
            for j in range(10):
                for k in temp[j]:
                    index.append(k)
            for j in range(len(queries)):
                if queries[j][1] == i + 1:
                    ans[j] = index[queries[j][0] - 1]
        return ans 

