# Uses python3

'''
You are given a string of digits num, such as "123456579". We can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:

0 <= f[i] < 231, (that is, each integer fits in a 32-bit signed integer type),
f.length >= 3, and
f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.
Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.

 

Example 1:

Input: num = "1101111"
Output: [11,0,11,11]
Explanation: The output [110, 1, 111] would also be accepted.
Example 2:

Input: num = "112358130"
Output: []
Explanation: The task is impossible.
Example 3:

Input: num = "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
 

Constraints:

1 <= num.length <= 200
num contains only digits.
'''

from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        # Start the backtracking from index 0 with an empty sequence
        return self.validFibonacciSeq(0, num, [])
    
    
    def validFibonacciSeq(self, i: int, num: str, fibonacciSequence: List[int]) -> List[int]:
        n = len(num)
        # Base case: if we've processed all digits
        if i == n:
            # Return the sequence if it's valid (length >= 3), otherwise return empty list
            return fibonacciSequence if len(fibonacciSequence) >= 3 else []
        
        val = 0
        # Try all possible splits starting from index i
        for choice in range(i, n):
            # Handle leading zeros: if current digit is '0' and we're trying to make a multi-digit number, break
            if num[i] == '0' and choice > i:
                break
            
            # Build the current number digit by digit
            val = val * 10 + ord(num[choice]) - ord('0')
            
            # Check if the number exceeds 32-bit signed integer limit
            if val > 2**31 - 1:
                break
            
            # If we have at least 2 numbers in the sequence, check Fibonacci property
            if len(fibonacciSequence) >= 2:
                next_seq = fibonacciSequence[-1] + fibonacciSequence[-2]
                # If current number is larger than expected next in sequence, no need to check further
                if val > next_seq:
                    break
                # If current number is smaller than expected, try adding more digits
                if val < next_seq:
                    continue
            
            # Add current number to the sequence
            fibonacciSequence.append(val)
            
            # Recursively check if this choice leads to a valid sequence
            result = self.validFibonacciSeq(choice + 1, num, fibonacciSequence)
            if len(result) >= 3:
                return result
            
            # Backtrack: remove the last number and try the next possibility
            fibonacciSequence.pop()
                
        # No valid sequence found from this path
        return []
            
            
            
        

        