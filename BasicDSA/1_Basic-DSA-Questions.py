from typing import List

'''
Find words containing character
Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
'''
def findWordsContaining(self, words: List[str], x: str) -> List[int]:
    result = []
    for index, word in enumerate(words):
        if word.__contains__(x):
            result.append(index)
    return result


'''
Concatenation of two arrays
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
'''
def getConcatenation( nums: List[int]) -> List[int]:
    result = []
    required_size = len(nums) * 2
    for index in range(required_size):
        result.append(nums[index % len(nums)])

    print(f"Result : {result}")
    return result


'''
Build Array from Permutations
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
'''
def buildArray(self, nums: List[int]) -> List[int]:
    # result = []
    # for index in range(len(nums)):
    #     result.append(nums[nums[index]])
    # return result

    # List comprehension
    return [nums[nums[index]] for index in range(len(nums))]



'''
Input: nums = [1,15,6,3]
Output: 9
Explanation: 
The element sum of nums is 1 + 15 + 6 + 3 = 25.
The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
The absolute difference between the element sum and digit sum is |25 - 16| = 9.
'''
def differenceOfSum( nums: List[int]) -> int:
    sum1 = 0
    sum2 = 0
    for num in nums:
        sum1 += num
        for digit in str(num):
            sum2 += int(digit)
    print(f"{sum1} | {sum2}")
    return abs(sum1 - sum2)


'''
Counting words with given prefix
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
'''
def prefixCount(self, words: List[str], pref: str) -> int:
    counter = 0
    for word in words:
        if word.startswith(pref):
            counter += 1
    return counter
    # list comprehension
    # return sum([ word.startswith(pref) for word in words])


'''
2500. Delete Greatest Value in Each Row
You are given an m x n matrix grid consisting of positive integers.
Perform the following operation until grid becomes empty:
Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.
'''
def deleteGreatestValue(self, grid: List[List[int]]) -> int:
    for row in grid:
        row.sort()

    result = 0
    col = 0
    while col < len(grid[0]):
        max_element = 0
        for index in range(len(grid)):
            max_element = max(max_element, grid[index][col])
        result += max_element
        col += 1
    return result



if __name__ == '__main__':
    # findWordsContaining()

    nums = [1, 2, 3, 4, 5]
    # getConcatenation(nums)

    nums = [1,15,6,3]
    print(f"Result : {differenceOfSum(nums)}");

