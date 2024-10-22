# 병합정렬

lst = [11, 13, 3, 54, 21, 10, 9]

def merge_sort(s, e):
    if s < e:
        mid = (s + e) // 2
        merge_sort(s, mid)  # 반가르기
        merge_sort(mid+1, e)
        # 합치기(본연의 일)
        lt = s
        rt = mid+1
        tmp = []
        while lt < mid + 1 and rt < e+1:
            if lst[lt] <= lst[rt]:
                tmp.append(lst[lt])
                lt += 1
            else:
                tmp.append(lst[rt])
                rt += 1
        if lt < mid+1:
            tmp = tmp + lst[lt:mid+1]
        elif rt < e+1:
            tmp = tmp + lst[rt:e + 1]
        lst[s:e+1] = tmp


merge_sort(0, 6)
print(lst)


