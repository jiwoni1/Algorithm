# 4-10. 역수열(그리디)
import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
reverse = list(map(int, input().split()))

# 1~n 보다 큰 수로 배열을 초기화해서 자기보다 큰 수의 갯수를 세면서 자리 찾아가기
# 원래 수열에서 역수열을 구하는 방식 적용

ans = [n+1] * n
cnt = 0  # 자기보다 큰 수의 갯수

for i in range(n):
    for j in range(n):
        if i + 1 < ans[j]:   # 자기보다 큰 수라면
            if cnt == reverse[i]:
                ans[j] = i + 1  # 자리 찾아가기
                cnt = 0
                break
            else:
                cnt += 1

print(*ans)


# 2번째 방법. 거꾸로 index 써서 넣기
# n = int(input())
# a = list(map(int, input().split()))
# a = a[::-1]  # n부터 생각하기
# ans = []
#
# # 거꾸로 n부터 하면, 앞에 넣었던 숫자들은 나보다 큰 수이므로 다 카운트됨
# # a의 값이 자기보다 큰 수의 갯수 = 인덱스로 넣으면 됨 (자기 앞에 있던 수는 다 자기보다 큰 수이므로)
# for x in a:
#     ans.insert(x, n)   # x 인덱스에 n 추가
#     n -= 1
#
# print(ans)





