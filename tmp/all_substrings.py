def find_substrings_with_pattern(input_string, pattern):
    substrings = []
    pattern_length = len(pattern)
    input_length = len(input_string)
    
    for i in range(input_length):
        for j in range(i + 1, input_length + 1):
            substring = input_string[i:j]
            if pattern in substring:
                substrings.append(substring)
    
    return substrings

input_string = "dineshprasasd"
pattern = "pra"
result = find_substrings_with_pattern(input_string, pattern)
print(result)
