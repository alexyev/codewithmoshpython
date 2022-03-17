sentence = 'This is a common interview question'
char_frequency = {}

for char in sentence:
    if char.lower() in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char.lower()] = 1

most_common = 'a'
for key in char_frequency:
    if char_frequency[key] > char_frequency[most_common]:
        most_common = key

print(char_frequency)
print('Most Common:', most_common)
