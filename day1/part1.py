list1 = []
list2 = []


filename = "./rows.txt"
with open(filename, "r") as file:
    for line in file:
        #  first number add to list list 1 and second number add to list list 2
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))


sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

result = sum(abs(sorted_list2[i] - sorted_list1[i]) for i in range(len(sorted_list1)))

print(result)
