def solution(array, commands):
    result = []
    for c in range(len(commands)): # for command in commands:
        i = commands[c][0]         #     i,j,k = command
        j = commands[c][1]
        k = commands[c][2]
        result.append(sorted(array[i-1:j])[k-1])
    return result