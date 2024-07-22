class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        capacity = -1

        for item in s:
            if (item == '(' or item == '{' or item == '['):
                stack.append(item)
                capacity += 1
            if (item == ')' or item == '}' or item == ']'):
                if (capacity == -1):
                    return False
            if (item == ')'):
                capacity -= 1
                if (stack.pop() != '('):
                    return False
            if (item == '}'):
                capacity -= 1
                if (stack.pop() != '{'):
                    return False
            if (item == ']'):
                capacity -= 1
                if (stack.pop() != '['):
                    return False

        if (capacity != -1): return False
        return True
