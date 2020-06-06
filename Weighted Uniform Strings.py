import string


# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    letter_dict = {}
    for index, letter in enumerate(string.ascii_lowercase):
        letter_dict[letter] = index + 1

    curr_ele = s[0]
    curr_val = letter_dict[s[0]]

    cache = set([curr_val])

    for i in range(1, len(s)):
        if curr_ele == s[i]:
            curr_val += letter_dict[curr_ele]
        else:
            curr_ele = s[i]
            curr_val = letter_dict[curr_ele]
        cache.add(curr_val)

    result = []
    for x in queries:
        if x in cache:
            result.append('Yes')
        else:
            result.append('No')

    return result


if __name__ == '__main__':
    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    print('\n'.join(result))