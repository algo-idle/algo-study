class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for i in s:
            if i in parentheses:
                stack.append(parentheses[i])
            else:
                if not stack or stack.pop() != i:
                    return False
        return False if stack else True


sol = Solution()
print(sol.isValid("()"))