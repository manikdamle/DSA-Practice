'''
You are given a string 'S' of 'N' character numbered from '0' to 'N-1' and integer 'X'. Every character of the string 'S' is either 'E' or 'O'.

Let's call the array 'A' of 'N' positive integers numbered from '0' to 'N-1' good if the sum of the elements of the array is 'X' and 'A[i]' is odd if 'S[i]' is 'O' and even. otherwise. Note that each 'A[i]' must be positive. ('A' > '0')

Determine whether there exists any good array. Return '1' if any good array exists and '0' otherwise.

Example:

N=3

X=5

S="EOE"

One good array exists ["2", "1", "2"]

So, the answer for this case is 1.
'''

def isThereGoodArray(n: int, x: int, s: str) -> int: 
    # Write your code here

    x=x-(s.count('E')*2)
    if x<0:
        return 0
    if x>=s.count('O') and x%2!=0 and s.count('O')%2!=0:
        return 1 
    elif x>=s.count('O') and x%2==0 and s.count('O')%2==0:
        return 1
    else:
        return 0