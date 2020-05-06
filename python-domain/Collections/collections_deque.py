from collections import deque

q = deque()
for _ in range(int(input())):
    # append, pop, popleft and appendleft 
    command = input()
    if 'popleft' in command:
        q.popleft()
    elif 'appendleft' in command:
        q.appendleft(command.split()[1])
    elif 'pop' in command:
        q.pop()
    else:
        q.append(command.split()[1])
print(*q, sep=' ')
