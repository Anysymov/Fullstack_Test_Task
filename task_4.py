with open("input.txt", "r") as reader:
    list_of_strings = list()
    for i in reader:
        edited_line = i.replace("\r\n","").replace("\n","")
        list_of_strings.append(edited_line)

sorted_list_incr = sorted(list_of_strings, key=len)
sorted_list_decr = sorted(list_of_strings, key=len, reverse=True)

print(sorted_list_incr)
print(sorted_list_decr)
