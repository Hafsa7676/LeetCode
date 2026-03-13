class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # If the list is None or empty, there is no common prefix
        if strs == None or len(strs) == 0:
            return ""
        
        # Loop through each character index of the first string
        # We treat the first string as the reference string
        for i in range(len(strs[0])):
            
            # Get the character at index i from the first string
            c = strs[0][i]
            
            # Compare this character with the character at the same index
            # in all the remaining strings
            for j in range(1, len(strs)):
                
                # Two situations where the common prefix must stop:
                
                # 1️⃣ i == len(strs[j])
                # This means we have reached the end of the current string.
                # Example:
                # strs = ["flower", "flow", "flight"]
                # If i = 4 and we check "flow", its length is 4.
                # Index 4 does not exist in "flow", so the prefix cannot continue.
                
                # 2️⃣ strs[j][i] != c
                # This means the character at position i in the current string
                # does not match the character from the first string.
                # Example:
                # "flower", "flow", "flight"
                # At i = 2 → characters are: o, o, i
                # Since 'i' != 'o', the prefix must stop.
                
                # If either of these conditions happens, return the prefix
                # from the start of the first string up to index i (not including i)
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        
        # If we finish the loop without returning, it means
        # the entire first string is the common prefix
        return strs[0]