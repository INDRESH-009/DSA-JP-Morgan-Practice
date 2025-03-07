words = ["aee","mee","bcd","aef"]
pattern = "xyy"
def get_pattern(s):
    lookup = {}
    pattern_for_s = []
    i = 0
    for ch in s:
        if ch in lookup:
            pattern_for_s.append(lookup[ch])
        else:
            i += 1
            lookup[ch] = i
            pattern_for_s.append(i)
    return pattern_for_s
given_pattern = get_pattern(pattern)
print(given_pattern)
output = []
for word in words:
    if get_pattern(word)==given_pattern:
        output.append(word)
print(output)

