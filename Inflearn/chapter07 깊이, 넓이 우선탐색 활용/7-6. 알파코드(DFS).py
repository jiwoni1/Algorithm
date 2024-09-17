# 7-6. 알파코드(DFS)


def dfs(l, ans):
    global cnt
    if l < len(code) and code[l] == "0":   # 0일 경우
        if ans[-1].isalpha():   # 0 혼자는 존재할 수 없으므로 앞에 숫자가 있어야해
            return
    if l == len(code):
        if ans[-1].isalpha():   # 마지막이 알파벳인것만 유효한 코드
            print(ans)
            cnt += 1
            return
    else:
        if len(ans) == 0 or ans[-1].isalpha():  # 알파벳 또는 처음
            dfs(l + 1, ans + chr(int(code[l]) + 64))  # 바로 변환
            dfs(l + 1, ans + code[l])  # 두개씩 변환
        else:   # 숫자라면
            num = int(ans[-1] + code[l])
            if 1 <= num <= 26:    # 범위 체크
                new_code = ans[:-1] + chr(num + 64)  # 합해서 만든 코드
                dfs(l+1, new_code)


code = list(input())
cnt = 0
dfs(0, '')
print(cnt)


# 선생님 풀이
def dfs(l, p):
    global cnt
    if l == len(code)-1:
        for j in range(p):
            print(chr(res[j]+64), end='')
        cnt += 1
        print()
        return
    else:
        for i in range(1, 27):
            if code[l] == i:   # 한자리수
                res[p] = i    # l은 포인터, p는 자리
                dfs(l+1, p+1)
            elif i >= 10 and code[l] == i//10 and code[l+1] == i%10:  # 두자리수
                res[p] = i
                dfs(l+2, p+1)  # 두자리했으니까 포인터 +2



code = list(map(int, input()))
code += [-1]
cnt = 0
res = [0] * (len(code))
dfs(0, 0)








