def letter_counter(string):
    # new dictionary
    counts = {}
    for l in string:
        # if it is a new letter...
        if (l not in counts):
            counts[l] = 1
        # else increment the count for that letter
        else:
            counts[l] += 1
    return counts

# tests
word_to_count = "banana"

result = letter_counter(word_to_count)

print(result)
