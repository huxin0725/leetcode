class Solution:
    def isValid(self, s: str) -> bool:
        i =0
        strs = []
        for a in range(len(s)):
            if s[a] == '(' or s[a] == '[' or s[a] == '{':
                strs.append(s[a])
                i=i+1
            elif s[a] == ')':
                if i-1 <0:
                    return False
                if strs[i-1] == '(':
                    strs.pop()
                    i = i-1
                else:
                    return False

            elif s[a] == ']':
                if i-1 <0:
                    return False
                if strs[i-1] == '[':
                    strs.pop()
                    i = i - 1
                else:
                    return False

            elif s[a] == '}':
                if i-1 <0:
                    return False
                if strs[i-1] == '{':
                    strs.pop()
                    i = i - 1
                else:
                    return False

        if len(strs) == 0:
            return True
        else:
            return False

s = Solution()
print(s.isValid("()[]"))



# 用栈 hashmap

# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#
#         # The stack to keep track of opening brackets.
#         stack = []
#
#         # Hash map for keeping track of mappings. This keeps the code very clean.
#         # Also makes adding more types of parenthesis easier
#         mapping = {")": "(", "}": "{", "]": "["}
#
#         # For every bracket in the expression.
#         for char in s:
#
#             # If the character is an closing bracket
#             if char in mapping:
#
#                 # Pop the topmost element from the stack, if it is non empty
#                 # Otherwise assign a dummy value of '#' to the top_element variable
#                 top_element = stack.pop() if stack else '#'
#
#                 # The mapping for the opening bracket in our hash and the top
#                 # element of the stack don't match, return False
#                 if mapping[char] != top_element:
#                     return False
#             else:
#                 # We have an opening bracket, simply push it onto the stack.
#                 stack.append(char)
#
#         # In the end, if the stack is empty, then we have a valid expression.
#         # The stack won't be empty for cases like ((()
#         return not stack
