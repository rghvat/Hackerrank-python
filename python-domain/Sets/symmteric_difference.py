input()
english = set(map(int, input().split(' ')))
input()
french = set(map(int, input().split(' ')))
print(*sorted(english.symmetric_difference(french)), sep='\n')
