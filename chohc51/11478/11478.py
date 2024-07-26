sentence = input()
result = set()
for i in range(1,len(sentence)+1):
    start = 0
    end = i
    while end<=len(sentence):
        result.add(sentence[start:end])
        start+=1
        end+=1
print(len(result))