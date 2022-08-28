/*
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
*/

class Solution {
    public int summer(int sum)
    {
        int sum1=0,rem=0;
        
        while(sum>0)
        {
            rem = sum%10;
            
            sum1 = sum1+rem;
            
            sum = sum/10;
        }
        return sum1;
    }
    public int addDigits(int num) {
        int sum=0,rem=0;
        
        while(num>0)
        {
            rem = num%10;
            
            sum = sum+rem;
            
            num = num/10;
            
             if(sum>9)
            {
              sum=summer(sum);
            }
        }
       
        return sum;
    }
}
