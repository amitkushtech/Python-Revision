list1 = [12, 13, 14, 15, 16, 17]
list2 = [56, 57, 58, 59, 35, 56, 22]
final_list = []
countLoop = 0
for i in list1:
    if countLoop % 2 == 1:
        final_list.append(i)

    countLoop += 1

for i in list2:
    if countLoop % 2 == 0:
        final_list.append(i)

    countLoop += 1

print(final_list)
print("****************************************")
# Reemove Duplicate the list

new_list = [12, 23, 45, 66, 12, 45, 77, 66, 89, 67, 66]
print("Before:", new_list)
a = set(new_list)
b = tuple(a)

print("After: ", b)
maximum = max(a)
print("Max in tuple: ", maximum)
minimum = min(a)
print("Minimum in tuple: ", minimum)
