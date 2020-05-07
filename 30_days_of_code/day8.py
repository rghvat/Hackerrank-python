mapping = dict()
for _ in range(int(input())):
    name, value = input().split()
    mapping[name] = value

while True:
    try:
        line = input()
        if line in mapping:
            print("{}={}".format(line, mapping[line]))
        else:
            print('Not found')
    except:
        break
