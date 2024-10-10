def permute(s, path="", result=[]):
    if len(path) == len(s):
        result.append(path)
        return
    
    for i in range(len(s)):
        if s[i] in path:  # Skip if already in the current path
            continue
        permute(s, path + s[i], result)

    return result


s = "ab"
permutations = permute(s)
print(permutations)
