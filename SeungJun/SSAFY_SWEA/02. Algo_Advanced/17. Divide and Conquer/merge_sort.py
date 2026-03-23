# 병합하기
# 좌우 리스트 중 작은 원소부터 정답 리스트에 추가
def merge(left, right):
    result = [0] * (len(left) + len(right))
    l = r = 0 # 포인터 설정

    # 좌우 리스트 비교해서 작은 값부터 넣기
    while l < len(left) and r < len(right): # 포인터 양쪽에 비교할 게 남아 있을 때
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # 남은것들 result에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result

# 분할하기
# depth -> 리스트 길이가 1이면 끝
# branch -> 두 그룹으로 분할(2개)
def merge_sort(li):
    # 분할하기
    if len(li) == 1:
        return li

    mid = len(li)//2
    left = li[:mid]
    right = li[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    # 병합
    merged_list = merge(left_list,right_list)
    return merged_list

arr = [10, 20, 50, 30, 70, 40, 60, 80]
sorted_arr = merge_sort(arr)
print(sorted_arr)

