def count_substring(string, sub_string):
    counter = 0
    for i in range(0, len(string)):
        if (string[i:i+len(sub_string)]) == sub_string:
            counter += 1

    return counter
    
count_substring("ABCDCDC", "CDC")