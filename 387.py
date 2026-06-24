class Solution(object):
    def firstUniqChar(self, s):
        seen = {}
        for st in s:
            if st in seen:
                seen[st] = 1
            else:
                seen[st] = 0

        for i, st in enumerate(s):
            if seen[st] == 0:
                return i

        return -1
