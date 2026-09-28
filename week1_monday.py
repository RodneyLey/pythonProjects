from collections import Counter


# converting list to set to drop duplicates, then back to a sorted list
my_numbers = [1, 2, 2, 3, 4, 6, 6, 9, 5, 7]
to_set = set(my_numbers)
back_to_list = sorted(to_set)
print(back_to_list)


# trying to update the tuple component does not work since tuples are unchangeable
my_tuple = (25, 52, 78)
# my_tuple[1] = 55
print(my_tuple)

my_dict1 = {
    "name": "Rodney",
    "age": 31,
    "city": "Nyeri"
}
my_dict2 = {
    "IT": 60,
    "Cybersecurity": 30,
    "Networking": 40
}


def merge_into_one(dict1, dict2):
    return {**dict1, **dict2}  # unpacking dict1 and dict2 into a new dictionary


merged = merge_into_one(my_dict1, my_dict2)
print(merged)

words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple",
    "orange",
    "banana",
    "banana"
]

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

word_count2 = Counter(words)
print(word_count2)