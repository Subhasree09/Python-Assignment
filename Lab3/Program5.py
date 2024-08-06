def reverse_list(list,n):
    st = 0
    end = n-1
    while (st < end) :
        temp = list[st]
        list[st] = list[end]
        list[end] = temp
        st = st + 1
        end = end - 1
    return list


n = int(input("Enter the number of elements in the list: "))
list = []
print("Enter the elements")
for i in range(n):
    e = int(input())
    list.append(e)

reverse = (reverse_list(list,n))

print("The Reversed list is: ")
for i in range (n):
    print(reverse[i], end=" ")