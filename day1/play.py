list1 = [3, 4, 2, 1, 3, 3]
list2 = [4, 3, 5, 3, 9, 3]

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

total_difference = []

print(sorted_list1)
print(sorted_list2)

for i in range(len(sorted_list1)):
    total_difference.append(sorted_list2[i] - sorted_list1[i])


print(sum(total_difference))
