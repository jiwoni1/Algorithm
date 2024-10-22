# 퀵정렬(O(nlogn))
# 전위순회

lst = [11, 13, 3, 54, 21, 10, 9]

def quick_sort(lt, rt):
    # 본문(파티션 작업)
    if lt < rt:
        pivot = rt
        pointer = lst[lt]
        for i in range(rt-lt):
            if lst[lt+i] < pivot:
                lst[pointer], lst[lt+i] = lst[lt+i], lst[pointer]
                pointer += 1
        lst[pointer], lst[rt] = lst[rt], lst[pointer]
        # 분할
        quick_sort(lt, pointer-1)
        quick_sort(pointer+1, rt)


quick_sort(0, 6)
print(lst)



