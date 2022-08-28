/*
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
*/
class Solution {
    
    public boolean isVowel(char[] arr,int i)
    {
        
            if(arr[i]=='a' || arr[i]=='e' || arr[i]=='i' || arr[i]=='o' ||arr[i]=='u'||                    arr[i]=='A' || arr[i]=='E' || arr[i]=='I' || arr[i]=='O' ||arr[i]=='U' )
            {
                return true;
            }
            else
            {
                return false;
            }
        
    }
    public void swap(char arr[],int i,int j)
    {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    public String reverseVowels(String s) {
        
        char arr[] = s.toCharArray();
        int left = 0;
        int right = arr.length-1;
        
        while(left<right)
        {
            while(left<right && isVowel(arr,left)==false)
            {
                left++;
            }
            while(left<right && isVowel(arr,right)==false)
            {
                right--;
            }
            
            swap(arr,left,right);
            left++;
            right--;
        }
        String str="";
        for(char ch:arr)
        {
            str+=ch;
        }
        return str;
    }
    
}
