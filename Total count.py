'''
You are given an array arr[] of positive integers and a threshold value k. For each element in the array, divide it into the minimum number of small integers such that each divided integer is less than or equal to k. Compute the total number of these integer across all elements of the array.
'''

class Solution:
    def totalCount(self, k, arr):
        # code here
        count=0
        for i in arr:
            if i<k:
                count+=1
            else:
                if i%k==0:
                    count+=i//k
                else:
                    count+=i//k+1
        return count