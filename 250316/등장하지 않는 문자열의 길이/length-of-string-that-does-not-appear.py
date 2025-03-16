import re

n = int(input())
s = input()

# # Please write your code here.
# def min_unique_word_length(s):
#     words = re.findall(r'\b[A-Z]+\b', s)
#     unique_words = [word for word in words if not re.search(r'(.).*\1', word)]
#     return min(len(word) for word in unique_words)

# print(len(min_unique_word_length(string)) + 1)


# words = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}

# for c in string:
#     words[c] += 1

# dup_str = sum(1 for val in words.values() if val >= 2)

# print(dup_str + 1)

dup_str = ""
cut_idx = 0
for i in range(n):
    if s[i] not in dup_str:
        dup_str += s[i]
        cut_idx = i

res = 0
for i in range(cut_idx + 1, n):
    if s[i] in dup_str:
        res += 1

print(res + 1)