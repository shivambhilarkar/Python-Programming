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


if __name__ == '__main__':
    # findWordsContaining()

    nums = [1, 2, 3, 4, 5]
    getConcatenation(nums)
