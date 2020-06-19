# ------------------
# --  Regular Expressions Part 6 Re Module Search & FindAl --
# search() => search string for A match and Return A first Match Only
# fidall() => Return alists of all matches and empty list if no match
# -----------------------------------------------------------------------
# email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|info|net|org)
# ------------------

import re

my_string = re.search(r"[A-Z]{3}", "OOOsama Elzero")
print(my_string)
print(my_string.span())
print(my_string.string)
print(my_string.group())

get_email = input("Type Your Email : ").strip()
is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", get_email)
if is_email:
    print("this is A vaild Email")
    print(is_email.span())
    print(is_email.string)
    print(is_email.group())

else:
    print("Not Email")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", get_email)
empty_list = []
if search != []:
    empty_list.append(search)
    print("email Add")
else:
    print("invaild Email")

for email in empty_list:
    print(email)
