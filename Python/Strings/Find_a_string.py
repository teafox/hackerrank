def count_substring(string, sub_string):
    count = 0
    for c in range(len(string)):
        if string[c] == sub_string[0]:
            if string[c:c+len(sub_string)] == sub_string:
                count += 1
    return count
