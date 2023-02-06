class Solution(object):
    def plusOne(self, digits):
        text = ""
        for v in digits: text += str(v)
        return list(map(int,list(str(int(text)+1))))