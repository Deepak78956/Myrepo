'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''


class Solution(object):
    def isValid(self, s):
        mapping = {')':'(', '}':'{', ']':'['}           # checks for the closing of parenthesis
        stack = []                                      # tracks the opening of brackets
        for element in s:
            if element in mapping:                      # if any closing parenthesis found (mapping.keys)
                if stack:                               # if stack is not empty
                    top_element = stack.pop()           # pops off the most recent element
                else:
                    top_element = '#'                   # takes care for the cases "))()()" where closing parenthesis is on first
                if mapping[element] != top_element:     # if the recent element is not equal to the value of its opening (if opening is not equal to closing)
                    return False
            else:
                stack.append(element)                   # if there is an opening parenthesis append it in stack
        return not stack                                # True if atlast stack is empty or False
                