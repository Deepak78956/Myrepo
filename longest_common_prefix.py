'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

'''


# strs = ["flowers", "flow", "flight"]
# list(zip(*strs)) == [('f','f','f'), ('l','l','l'), ('o','o','i'), ('w','w','g')] 
# len(set('f','f','f')) == 1
class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        for i in list(zip(*strs)):
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix