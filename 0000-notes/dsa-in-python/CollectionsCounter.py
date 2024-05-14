from collections import Counter

# Create a new Counter object
counts = Counter()
print(counts)  # Counter()
print(type(counts))  # <class 'collections.Counter'>

# What does the Counter do?
s = 'a quick brown fox jumps over the lazy dog'
dict_1 = {}
for ch in s:
    dict_1[ch] = dict_1.get(ch, 0) + 1

print(dict_1)

dirt_2 = Counter(s)
print(dirt_2)   # count the number of each character in the string

# Count numbers
count_nums = Counter([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
print(count_nums)

# Count words
count_words = Counter(['a', 'each', 'can', 'a', 'boy', 'can', 'a', 'boy', 'change', 'a'])
print(count_words)
print(count_words['z'])  # return 0 if it doesn't exist

# Most common item
print(count_words.most_common())    # return a list of tuples, the order is from the most common to the least common
print(count_words.most_common()[0])  # ('a', 4)
print(count_words.most_common()[0][0])  # a
print(count_words.most_common(1))  # [('a', 4)], a list containing the most common item

# Least common item
print(count_words.most_common()[-1])  # ('change', 1)
print(count_words.most_common()[-1][0])  # change

# Update the counter
count_words.update(['can', 'can', 'can'])
print(count_words)  # Counter({'can': 5, ...

# Delete item
del count_words['can']
print(count_words)

# Add two counters
count_words_2 = Counter(['can', 'can', 'can'])
count_words += count_words_2
print(count_words)

# Subtract two counters
diff_1 = count_words - count_words_2
diff_2 = count_words_2 - count_words
print(diff_1, diff_2)

# bitwise operation
print(count_words & count_words_2)
print(count_words | count_words_2)
