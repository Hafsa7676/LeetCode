class Solution:
   def longestCommonPrefix(self, strs: List[str]) -> str:
    
    # If the list of strings is empty, there cannot be any common prefix
    if len(strs) == 0:
        return ""
    
    # Assume the first string is the longest possible common prefix
    prefix = strs[0]
    
    # Loop through the remaining strings one by one
    for i in range(1, len(strs)):
        
        # This loop keeps running as long as the current string
        # does NOT start with the current prefix
        #
        # find(prefix) returns the index where the substring first appears.
        # If the string starts with the prefix, find(prefix) returns 0.
        #
        # Examples:
        # "flower".find("flo")  -> 0  (prefix matches at start)
        # "flower".find("low")  -> 1  (not at start)
        # "flower".find("abc")  -> -1 (not present)
        #
        # Therefore, if find(prefix) != 0, the prefix is not at the start
        # of the current string, so we must shorten the prefix.
        while strs[i].find(prefix) != 0:
            
            # Remove the last character of the prefix
            # This gradually shrinks the prefix until it matches
            # the start of the current string
            #
            # Example shrinking process:
            # "flower" -> "flowe" -> "flow" -> "flo" -> "fl"
            prefix = prefix[0 : len(prefix) - 1]
            
            # If the prefix becomes empty, it means there is
            # no common prefix among the strings
            if prefix == "":
                return ""
    
    # After checking all strings, return the remaining prefix
    # which is the longest common prefix
    return prefix   