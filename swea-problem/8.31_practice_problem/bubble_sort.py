# 버블 정렬 : 인접한 두 요소를 비교하여 교환하여 정렬하는 방식
#
# 핵심 : 왼쪽이 더 크면 오른쪽과 서로 교환한다.
#
#   BubbleSort(a, N)                # 정렬할 배열과 배열의 크기
#       for i : N-1 -> i            # 정렬할 구간의 끝
#           for j : 0 -> i-1        # 비교할 원소 중 왼쪽 원소의 인덱스
#               if a[j] > a[j+1]    # 왼쪽 원소가 더 크면
#                   a[j] <-> a[j+1] # 오른쪽 원소와 교환
#
#     다음은 버블정렬의 예시 코드입니다.
#
# 다음 배열을 하드코딩해 주세요.
#
# arr = [12, 3, 9, 1, 15, 7]
#
# 버블 정렬 함수를 정의하여 호출해 보세요.
#
# 출력은 정렬된 결과를 출력합니다.

# a : 정렬할 리스트, N : element 개수
# 매개변수(parameter)로 a 넣는 이유 : 디버깅 하면서 배열 상태 보려고
def bubble_sort(a, N):
    # 버블 정렬 로직
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


arr = [12, 3, 9, 1, 15, 7]

# 함수 호출
result = bubble_sort(arr, len(arr))
print(*result)

# 강사님 풀이
# def bubble_sort(a, N):
#     for i in range(N-1, 0, -1):
#         for j in range(i):
#             if a[j] > a[j+1]:   #왼쪽이 더 크다면
#                 a[j], a[j+1] = a[j+1], a[j] #교환
#     return a
#
# arr = [12, 3, 9, 1, 15, 7]
#
# result = bubble_sort(arr, len(arr))
# print(*result)