## Lists in Python defined by [] Sqaure Brackets

list_num = [20, 30, 40, 50, 60, 70, 80]

print(list_num)
print(type(list_num))
print(list_num[1:4])  ##Index Printing

list_string = ['Jagan', 'Mohan', 'Krishna', 'Gudela', 'Ravi', 'Teja']
print(list_string)
print(type(list_string))
print(list_string[0:2])
list_string.sort()
print(list_string)

list_num.append(90)  ## append will add a num at final value
list_num.extend(
    list_string)  # # output will be [20, 30, 40, 50, 60, 70, 80, 90, 'Jagan', 'Mohan', 'Krishna', 'Gudela', 'Ravi',
# 'Teja']
list_num.insert(3, 99)  ## inserts a value at particular index unlike append

print(list_num)

another_list_nums = [7, 38, 1, 90, 74, 51, 820, 0, 91, 79, 11, 98, 54]

another_list_nums.sort(reverse=True)  # output will be descending order to ascending [820, 98, 91, 90, 79, 74, 54, 51,
# 38, 11, 7, 1, 0]
another_list_nums.sort()  ## [0, 1, 7, 11, 38, 51, 54, 74, 79, 90, 91, 98, 820] from small to highest
print(another_list_nums)

list_num.pop(0)

print(list_num)