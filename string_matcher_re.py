import re

string = 'Python is good for Machine Learning and Data-Science'

"""
pass substrings separated by | as 1st argument
and main string value as 2nd argument.
Additionally, we can pass re.IGNORECASE paramter as
3rd argument to make matching case-insensitive.
"""
match_list = re.findall(r'python|machine|good|dinesh', string, re.IGNORECASE)

print(any(match_list))
