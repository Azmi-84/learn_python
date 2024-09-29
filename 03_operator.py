integer_character = "Assalamualaikum" + " " + "Azmi"
print(integer_character)

another_integer_character = "Assalamualaikum " * 3
# it will print Assalamualaikum three times
print(another_integer_character)

even_num = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odd_num = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
all_num = even_num + odd_num
print(all_num)
print(len(all_num))

all_num = all_num * 2
print(all_num)

# length of list
print(len(all_num))

first_list = object()
second_list = object()

first_list_item = [first_list] * 10
second_list_item = [second_list] * 10
big_list = first_list_item + second_list_item

print("first_list_item contains %d objects" % len(first_list_item))
print("second_list_item contains %d objects" % len(second_list_item))
print("big_list contains %d objects" % len(big_list))

if first_list in big_list:
    print("first_list is an element of big_list")
else:
    print("first_list is not an element of big_list")

if second_list in big_list:
    print("second_list is an element of big_list")
else:
    print("second_list is not an element of big_list")

if first_list_item.count(first_list) == 10:
    print("first_list_item contains 10 elements")
else:
    print("first_list_item does not contain 10 elements")

if big_list.count(first_list) == 10:
    print("big_list contains 10 elements")
else:
    print("big_list does not contain 10 elements")
