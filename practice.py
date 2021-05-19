# 입력 : 1 2
# 출력 : 1 2
# a, b = map(int, input().split())
# print(a, b)

# 입력 : 
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# 출력 : 
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# MAP = [list(map(int, input().split())) for _ in range(int(input()))]

# 입력 : 
# 4 10 20 30 40
# 3 7 5 12
# 3 125 15 25
# 출력 : 
# [[10, 20, 30, 40], [7, 5, 12], [125, 15, 25]]
# N, *arr = map(int, input().split())

# 입력 :
# 3
# AAAA 
# ABCA 
# AAAA
# 출력 : 
# arr = [['A', 'A', 'A', 'A']
#        ['A', 'B', 'C', 'A']
#        ['A', 'A', 'A', 'A']]
# N = int(input())
# arr = [list(input()) for _ in range(N)]
# print(arr)

# 입력 : 배열 [1, 2, 3, 4]
# 출력 : 1234
# arr = [1, 2, 3, 4]
# print("".join(map(str, arr)))

# 입력 : 배열 [1, 2, 3, 4]
# 출력 : 1 2 3 4
# arr = [1, 2, 3, 4]
# print(*arr)

# 입력 : 배열 [1, 2, 3, 4]
# 출력 : 1
# import sys
# arr = [1, 2, 3, 4]
# ans = sys.maxsize
# for num in arr:
#     if num < ans:
#         ans = num
# print(ans)

# 입력 : 문자열 "AAAA"
# 출력 : 1
# 입력 : 문자열 "BABA"
# 출력 : 0
# alph = "AAAA"
# if(alph == alph[::-1]):
#     print(1)
# else: print(0)

# 2차원 배열 초기화
# N, M = map(int, input().split())
# arr = [[0] * N for _ in range(M)]
# print(arr)

# 배열 원소 거꾸로
# 입력 :
# 472
# 385
# 출력 : 2360
# a, b = map(int, input().split())
# arr_b = [int(i) for i in str(b)]
# 혹은
# a_string, b_string = input().split()
# a_int = list(map(int, a_string))
# b_int = list(map(int, b_string))
# arr_b. reverse()
# for i in range(len(arr_b)):
#     print(a * arr_b[i])
# print(a * b)

# 배열 원소 갯수 세기. 윷놀이 첫째 줄부터 셋째 줄까지 한 줄에 하나씩 결과를 출력
# 배 : 0 등 : 1
# 입력 : 
# 0 1 0 1
# 1 1 1 0
# 0 0 1 1
# 출력 : 

# def check(arr):
#     num_of_zero = arr.count(0)
#     if(num_of_zero == 1):
#         print('A')
#     elif(num_of_zero == 2):
#         print('B')
#     elif(num_of_zero == 3):
#         print('C')
#     elif(num_of_zero == 4):
#         print('D')
#     else: print('E')
#     return

# for i in range(3):
#     arr = list(map(int, input().split()))
#     check(arr)

# 입력 : 
# 3
# 1 2
# 1 2
# 1
# 이중 배열로 담아 -> [[1, 2], [1, 2], [1]]
# 중복 제거 후 출력 : [1, 2]

# import itertools
# arr = [list(map(int, input().split())) for _ in range(int(input()))]
# brr = list(itertools.chain(*arr))
# print(list(set(brr)))

# 좌표 정렬
# location = [list(map(int, input().split())) for _ in range(int(input()))]
# location.sort(key=lambda x:(x[0], x[1]))
# for x, y in location:
#     print(x, y)

# 국영수 점수 정렬 문제
# grade_list = [list(map(str, input().split())) for _ in range(int(input()))]
# print(grade_list)
# grade_list.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
# for x, y, j, z in grade_list:
#     print(x)

# 삼항 연산자
# res = a if a > b else b

# 조합
# [1, 2, 3, 4]로 만들 수 있는 조합
# from itertools import combinations
# print(list(combinations([1,2,3,4], 3)))

# 조합2
from itertools import combinations
N, M = map(int, input().split())
arr = [str(i+1) for i in range(N)]
for e in list(combinations(arr, M)):
    print(' '.join(e))


