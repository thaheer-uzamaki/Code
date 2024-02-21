def count_letter_pairs(string):
    # Initialize a dictionary to store letter counts
    letter_counts = {}
    # Count occurrences of each letter
    for letter in string:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    # Calculate the number of pairs
    pair_count = 0
    for count in letter_counts.values():
        pair_count += count // 2  # Integer division to get the number of pairs
    return pair_count
 
# Example usage:
input_string = "mmmmebae"
pair_count = count_letter_pairs(input_string)
print(pair_count)  # Output: 2