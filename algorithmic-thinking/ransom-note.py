'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

class Solution:
    def canConstruct(self, ransomNote, magazine):
        dict = {}
        for c in magazine:
            if(c in dict):
                dict[c] += 1
            else:
                dict[c] = 1
        return dict
    
s = Solution
o = s.canConstruct("aa", "asdb", "abhs")
print(o)