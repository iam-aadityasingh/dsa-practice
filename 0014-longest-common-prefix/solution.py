def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    small = min(strs, key=len)
    
    for s in strs:
        while not s.startswith(small):
            small = small[:-1]
            if not small:
                return ""  #if small reduces to "", return ""
    
    return small
