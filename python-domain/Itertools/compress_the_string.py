from itertools import groupby

for ele in groupby(input()):
    print((len(list(ele[1])), int(ele[0])), end=" ")
