import re
for _ in range(int(input())):
    try:
        regex = input()
        re.compile(regex)
        print("True")
    except Exception as e:
        print("False")
        pass
