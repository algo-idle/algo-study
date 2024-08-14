class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (len(s.replace(" ",'')) == 0 or len(s) == 1): return True

        alphanumeric = []

        for char in s:
            if ((ord(char) >= 48 and ord(char) <= 57)):
                alphanumeric.append(char)
                continue
            if ((ord(char) >= 65 and ord(char) <= 90)):
                alphanumeric.append(char.lower())
                continue
            if ((ord(char) >= 97 and ord(char) <= 122)):
                alphanumeric.append(char)

        if len(alphanumeric) == 0: return True
        
        length = len(alphanumeric)
        for i in range(length):
            if (i > length // 2): break
            if (alphanumeric[i] != alphanumeric[length - i - 1]): return False
        