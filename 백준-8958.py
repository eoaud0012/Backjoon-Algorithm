testcase_count = int(input())
testcase_list = [list(input()) for _ in range(testcase_count)]

# 원래 작성했던 함수. 직관적이지 않음.
# def score_inspector():
#     i = 0
#     j = 0
#     score_sum = 0
#     common_difference = 0
#     for i in range(len(problem_list)):

#         for j in range(len(problem_list[i])):
#             if(problem_list[i][j] == 'O'):
#                 common_difference += 1
#                 score_sum += common_difference
#             else:
#                 common_difference = 0

#         print(score_sum)
#         score_sum = 0
#         common_difference = 0
#     return


# 변경한 후 함수. 좀 더 직관적임.
def score_inspector():
    i = 0
    j = 0
    score_sum = 0
    common_difference = 0
    for test_case in testcase_list:
        for answer in test_case:
            if(answer == 'O'):
                common_difference += 1
                score_sum += common_difference
            else:
                common_difference = 0

        print(score_sum)
        score_sum = 0
        common_difference = 0
    return


score_inspector()

    



# 파이썬에서 H x W 2차원 리스트를 0으로 초기화 하려면 다음과 같이 하면 됩니다.

# arr = [[0 for i in range(w)] for j in range(h)]

# 혹은

# arr = [[0]*w for j in range(h)]​

# 당연히 1차원 리스트는 다음과 같이.

# list1 = [0 for i in range(w)]

# 2차원 리스트 선언만 하려면 아래와 같이.

# data = [[] * n for i in range(n)]    # data: [[], [], [], []]

# * 추가 

#  - 1차원배열 초기화 

#     arr = [0] * n 
# [출처] [Python] 2차원 리스트 초기화|작성자 뚝이파파
#