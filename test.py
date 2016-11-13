file_name = "09sefds12"
translation_table = dict.fromkeys(map(ord, "0987654321"), None)
new_name = file_name.translate(translation_table)
print(new_name)

print(file_name)
new_name2 = file_name.translate({ord(c): None for c in '0987654321'})
print(new_name2)
