Regex_Pattern = 'hackerrank'	# Do not delete 'r'.
# or          = r'hackerrank' both gives the same result
import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
