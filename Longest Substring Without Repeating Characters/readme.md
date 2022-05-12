### **Longest Substring Without Repeating Characters**

##### Difficulty: **Medium**

Given a string s, find the length of the longest substring without repeating characters.

```python
def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        totalL = []
        for i in range(len(s)):
            news = str(s[i])
            for j in range(i+1, len(s)):
               if s[j] not in news:
                   news += s[j]
               else:
                   break
                    
           totalL.append(len(news))
            
       return max(totalL)


       or


       l = 0
        mx = 0
        for i  in range(0, len(s)):
            while s[i] in s[l:i]:
                l += 1
            mx = max(mx, i+1-l)
        return mx
```

```html
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
