'''
You are given two strings 'S' and 'T' of length 'N' and 'M'. You are creating an infinite length sequence by concatenating 'S' and 'T' in the following order:

The sequence would look like: " S + S + T + T + S + S + T + T ... "

Here, two copies of 'S' and 'T' are concatenating in an alternating order.

You are also given an integer 'X'. You have to find the 'Xth' character of the given sequence by considering '0' based indexing.

Your task is to find the 'Xth' character of the given sequence and return it.

Example:

N = 3

M = 2

S = 'abc'

T = 'xy'

X = 9

he final sequence would look like: "abcabcxyxyabcabc...

So, the 19th character of this sequence is "y".
'''

def infinteSequence(n: int, m: int, x: int, s: str, t: str) -> str:

    #Write your code here

    st=s+s+t+t

    l=len(st)

    return st[x%l]

