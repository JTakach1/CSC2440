def input_strings():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    return s1, s2

def uncommonConcat(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    common_chars = set1.intersection(set2)
    uncommon_s1 = ''.join(char for char in s1 if char not in common_chars)
    uncommon_s2 = ''.join(char for char in s2 if char not in common_chars)
    result = uncommon_s1 + uncommon_s2
    return result

if __name__ == "__main__":
    s1, s2 = input_strings()
    result = uncommonConcat(s1, s2)
    print("Output:", result)
