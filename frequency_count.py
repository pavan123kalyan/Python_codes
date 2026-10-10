#1) finding frequency of characters ,without using hashmap

# Approach 1
s = input()
for ch in set(s):
    print(ch, ":", s.count(ch))

# Approach 2
s = input()
visited = ""
for i in range(len(s)):
    if s[i] not in visited:
        count = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1
        print(s[i], ":", count)
        visited += s[i]
