from collections import deque

developers = deque([int(x) for x in input().split(' ')])
hackers = deque([int(x) for x in input().split(' ')])

developers_start = len(developers)
hackers_start = len(hackers)
hackers_wins = 0
developers_wins = 0
last_developer = 0

while hackers and developers:
    last_developer = developers[-1]
    developers[-1] -= hackers[0]
    hackers[0] -= last_developer

    if hackers[0] <= 0 and developers[-1] <= 0:
        hackers.popleft()
        developers.pop()

    else:
        if hackers[0] <= 0:
            hackers.popleft()
            developers = deque([(x + 2) for x in developers])
            developers_wins += 1
            print(f'Developers Wins: {developers_wins}')
            for i in range(len(developers)):
                if developers[i] > 100:
                    developers[i] = 100

        else:
            if len(hackers) > 1:
                hackers.append(hackers.popleft())
        if developers[-1] <= 0:
            developers.pop()
            hackers = deque([(x + 2) for x in hackers])
            hackers_wins += 1
            print(f'Hackers Wins: {hackers_wins}')
            for i in range(len(hackers)):
                if hackers[i] > 100:
                    hackers[i] = 100
        else:
            if len(developers) > 1:
                developers.appendleft(developers.pop())

result = ''
if not developers and not hackers:
    print('Draw!')
if developers:
    if len(developers) == developers_start:
        result += 'Flawless Victory!\n'
    result += f"The Developers Team WIN!\nPlayers left: {len(developers)}\nTotal Health: {sum(developers)}"
    print(result)
    list_result = [print(f'Player {i + 1} Health: {x}') for i, x in enumerate(sorted(developers))]

if hackers:
    if len(hackers) == hackers_start:
        result += 'Flawless Victory!\n'
    result += f"The Hackers Team WIN!\nPlayers left: {len(hackers)}\nTotal Health: {sum(hackers)}"
    print(result)
    list_result = [print(f'Player {i + 1} Health: {x}') for i, x in enumerate(sorted(hackers, reverse=True))]

