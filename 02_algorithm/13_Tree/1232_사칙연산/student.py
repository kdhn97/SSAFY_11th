import sys
sys.stdin = open('input.txt')

# 왼 -> 부 -> 오 순서대로 방문한 후
# result에 값을 담음
def postorder(now) :
    if now != 0 :
        postorder(tree[now][0])
        postorder(tree[now][1])
        result.append(now)
    return result

# 테스트케이스의 개수만큼 반복한다
for tc in range(1, 11) :
    # N : 정점의 개수
    N = int(input())

    # 한 줄씩 리스트로 입력받음
    arr = [list(input().split()) for _ in range(N)]


    # 부모노드와 자식노드를 저장할 리스트
    temp = []
    for i in range(len(arr)) :
        # arr[i]의 길이가 4개면 부모 노드와 자식 노드가 있다는 뜻이니까
        # 부모노드와 자식노드를 temp에 추가함
        if len(arr[i]) == 4 :
            temp.append(int(arr[i][0]))
            temp.append(int(arr[i][2]))
            temp.append(int(arr[i][0]))
            temp.append(int(arr[i][3]))


    # 트리를 만들어서 부모노드를 인덱스로 하고
    # 왼쪽 자식 노드랑 오른쪽 자식 노드를 만듦
    tree = [[0, 0] for _ in range(N+1)]

    for idx in range(len(temp)//2) :
        if tree[temp[idx*2]][0] == 0 :
            tree[temp[idx*2]][0] = temp[idx*2+1]
        else :
            tree[temp[idx*2]][1] = temp[idx*2+1]

    # 중위순서를 해서 방문할 노드를 순서대로 담을 리스트
    result = []
    print(tree)

    # postorder함수에 1대입
    postorder(1)
    print(result)


    # result에는 정점의 번호가 담기니까
    # 정점에 뭐가 있는지 담아줄 리스트 필요
    num = []
    for k in range(len(arr)) :
        for l in range(len(arr)) :
            # 정점의 번호랑 arr[i]의 제일 처음에 있는 값이랑 같으면
            # num에 그 정점에 있는 값을 담아줌
            if result[k] == int(arr[l][0]) :
                num.append(arr[l][1])
    print(num)
    # 후위 표기식
    cal = []
    for c in num :
        # 숫자면 cal 리스트에 담고
        if c.isdigit() == True :
            cal.append(c)
        # 연산자면 cal 리스트에서 제일 위에 있는 두 수를 꺼내서
        else :
            second = cal.pop()
            first = cal.pop()

            # 연산하고 그 값을 cal에 추가함
            if c == '+' :
                cal.append(int(first) + int(second))
            elif c == '-' :
                cal.append(int(first) - int(second))
            elif c == '*' :
                cal.append(int(first) * int(second))
            elif c == '/' :
                cal.append(int(first) / int(second))

    # cal 리스트에 최종적으로 남은 값을 구함
    print(f'#{tc} {int(cal.pop())}')