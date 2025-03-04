word1 = "abc"
word2 = "pqrrr"
output = ""
i=0
for i in range(len(word1) or len(word2)):
    if i<len(word1):
        output = output + word1[i]
    if i<len(word2):
        output = output + word2[i]
print(output)