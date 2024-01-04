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



'''
2129. Capitalize the Title
You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:

If the length of the word is 1 or 2 letters, change all letters to lowercase.
Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
Return the capitalized title.

Example 1:
Input: title = "capiTalIze tHe titLe"
Output: "Capitalize The Title"
Explanation:
Since all the words have a length of at least 3, the first letter of each word is uppercase, and the remaining letters are lowercase.
'''
def capitalizeTitle(title: str) -> str:
    result = []
    for word in title.split(" "):
        if len(word) <= 2:
            result.append(word.lower())
        else:
            word = word.lower()
            char1 = word[0].upper()
            remaining = word[1:]
            result.append(char1 + remaining)

    sentence = ""
    for word in result:
        sentence += word
        sentence += " "
    # don't consider last character which is extra space
    return sentence[:-1]

# Optimal Solution
def capitalizeTitle(title: str) -> str:
    words = title.split()
    for index, word in enumerate(words):
        if len(word) <= 2:
            words[index] = word.lower()
        else:
            words[index] = word[0].upper() + word[1:].lower()
    space = ' '
    return space.join(words)


'''
2399. Check Distances Between Same Letters

You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of length 26.
Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).
In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored.
Return true if s is a well-spaced string, otherwise return false.

Example 1:
Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: true
Explanation:
- 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
- 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
- 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
Return true because s is a well-spaced string.

Example 2:
Input: s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: false
Explanation:
- 'a' appears at indices 0 and 1 so there are zero letters between them.
Because distance[0] = 1, s is not a well-spaced string.
'''
def checkDistances(self, s: str, distance: List[int]) -> bool:
    for index, char in enumerate(s):
        '''
        ord() function in Python is used to convert a single Unicode character into its integer representation, 
        i.e., it takes a single string character as an input and returns an integer (representing the Unicode equivalent of the character) as an output.'''
        char_index = ord(char) - ord('a')
        next_dist = index + distance[char_index] + 1
        if distance[char_index] != -1:
            if next_dist >= len(s) or s[next_dist] != char:
                return False
            else:
                distance[char_index] = -1
    return True


if __name__ == '__main__':
    # findWordsContaining()

    # nums = [1, 2, 3, 4, 5]
    # getConcatenation(nums)

    # nums = [1,15,6,3]
    # print(f"Result : {differenceOfSum(nums)}");

    print(f"Result : {capitalizeTitle('capiTalIze tHe titLe')}")
