# Swapping the first and last number
my_list = [12, 23, 34, 45, 56, 78, 11]
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)

# Print Even String

word = "Who am I is"


new_word = word.split()
for i in new_word:
    if len(i) % 2 == 0:
        print(i)
