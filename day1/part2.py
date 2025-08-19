list1, list2 = [], []

filename = "./rows.txt"
with open(filename, "r") as file:
    for line in file:
        #  first number add to list list 1 and second number add to list list 2
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

similarity_score = 0

for i in range(len(list1)):
    print(i)
    count = list2.count(list1[i])
    print(count)
    if count > 0:
        similarity_score += list1[i] * count
print(similarity_score)
