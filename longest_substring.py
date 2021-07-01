"""
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        maxlength = 0
        current_length = 0
        for i in s:
            if i not in substring:
                substring = substring + i
                current_length = current_length + 1
            else:
                # repetitive char is found
                if current_length > maxlength:
                    maxlength = current_length

                # remove the string till the repetitive
                substring = substring[substring.find(i) + 1:] + i
                # substring = i
                current_length = len(substring)

        return maxlength if maxlength > current_length else current_length


# Testing
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("dvdf"))
print(sol.lengthOfLongestSubstring(" "))
print(sol.lengthOfLongestSubstring(""))
