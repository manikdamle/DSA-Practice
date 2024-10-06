'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Approach: Sliding window to compare character frequencies in each substring of s2 with s1.
'''

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        k=len(str(s1))
        l=len(str(s2))
        i=0
        s=i+k
        if k>l:
            return False
        while(s<=l):
            x=s2[i:s]
            z=True
            for j in set(x):
                if x.count(j)==s1.count(j):
                    continue
                else:
                    z=False
                    break
            if z==True:
                return True
            i+=1
            s+=1
        return False
