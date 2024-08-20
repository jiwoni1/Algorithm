# 4-3. 뮤직비디오(결정알고리즘)
import sys
# sys.stdin = open("input.txt", "r")


def find_dvd(s, e, res):
    if s > e:
        return res

    mid = (s + e) // 2
    cnt = 1  # dvd 그룹은 1을 더해야함
    tmp = 0  # dvd 크기

    for song in songs:
        if tmp + song <= mid:   # dvd 용량을 넘지 않아야함
            tmp += song
        else:
            cnt += 1
            tmp = song
            continue

    if cnt <= m:
        res = mid
        return find_dvd(s, mid - 1, res)
    else:
        return find_dvd(mid + 1, e, res)


n, m = map(int, (input().split()))
songs = list(map(int, input().split()))

print(find_dvd(max(songs), sum(songs), 0))  # 무조건 제일 긴 노래의 길이보다 dvd의 크기가 같거나 커야함
