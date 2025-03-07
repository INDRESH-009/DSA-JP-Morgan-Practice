# set prefix to first str by default
strs = ["flower","flow","flight"]
prefix = strs[0]
# prefix can't be longer than the shortest str, so we need to find it
for s in strs: # O(n)
    prefix = prefix if len(prefix) < len(s) else s
for s in strs:
    iP, iS = 0, 0 # index of prefix, index of current string
    while iP < len(prefix) and iS < len(s): # make sure neither index is out of bounds
        if prefix[iP] == s[iS]: # match? simply increment both indices
            iP+=1
            iS+=1
        else: # first mismatch
            if len(prefix[0:iP]) < len(prefix):
                prefix = prefix[0:iP] # set prefix to the shorter of two
            iP = len(prefix) # exit while loop

    return prefix   