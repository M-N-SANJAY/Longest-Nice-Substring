'''
Testcase 1:
    Input: s = "YazaAay"
    Output: "aAa"
    Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
    "aAa" is the longest nice substring.

Then if we see, all the characters have their lowercase and uppercase variants except only "z".

This means that we can never have a valid subarray with "z" in it.

So, we need to look for a valid subarray before "z" and after "z" only.

In this string there is only one invalid character but there can be multiple. So, we simply create a set of all the characters and then, while looping over the string, 
just check if that character has its case variation in the set or not. If not, that means it is an invalid character and we need to find the valid substring before and after this character's index. 
So we will make two recursive calls. One for frnding a valid substring from beginning to the invalid character's index (excluding it) and
the other to find a valid substring from the invalid character's index + 1 to the end of the string.

And if we get a valid substring out of both or even from just one, that means, just return the one that's longer.

It is also possible that a string is already nice. e.g. "aAa". In this case, the recursive calls won't be made since they are only made when we encounter an invalid character. 
So in such cases, we can return the string itself at the end.
'''
def longestNiceSubstring(s):
        
        # If length of string is less than 2, there is no way we can get a nice substring out of it
        if len(s) < 2 : return ""
        
        # A set of all characters in the given string
        t = set(s)
        
        for i,c in enumerate(s):
            # If character is lowercase and the set does not have its uppercase variation or vice versa
            # It means that we need to not consider this character at all and so, find the longest substring till this character and after this character
            # Repeat this till we reach the end
            if (c.islower() and (c.upper() not in t)) or (c.isupper() and (c.lower() not in t)):

                s1 = self.longestNiceSubstring(s[0:i])
                s2 = self.longestNiceSubstring(s[i+1:])

                if len(s2) > len(s1):
                    return s2
                else s1
        
        
        # If the above recursive calls don't happen that means our string has each character in lowercase and uppercase already so we can return it
        return s
'''
Time Complexity : O(2^n) [for one specific case, where recursive splittings grows exponentially when the condition fails again and again until the very end recursive call stack for both the rear end recursive calls]
                  but ultimately for any other cases its just ~O(n^2), Since I've personally tried it for multiple generative testcases against decision trees which grow exponentially.
Space Complexity : O(n) 
'''
