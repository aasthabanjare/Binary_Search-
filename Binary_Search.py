def binary_search(lis, lower, higher, number):
  if higher >= lower:
        mid = (lower + higher) // 2
        if lis[mid] == number:
            return mid
        elif lis[mid] > number:
            return binary_search(lis, lower, mid-1, number)
        else:
            return binary_search(lis, mid+1, higher, number)

  else:
    return -1



list =[]
no_of_elements = int(input("Enter the numbers of integer  you want  in list : "))
for i in range(0, no_of_elements):
  elements = int(input())
  list.append(elements)

list.sort()
print(list)

n = len(list)
number = int(input("Enter the integer you want to search: "))

result = binary_search(list, 0, len(list)-1, number)

if result != -1:
    print(f"Number is present in the list at index {result}")
else:
    print("Number is not present in list")






