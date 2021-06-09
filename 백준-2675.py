# 원래 내코드 # --> 테스트 케이스 입력을 한꺼번에 받고 한꺼번에 출력하려다보니 잘 되지 않음.
# test_case_count = int(input())
# repeat_number = [0 for _ in range(test_case_count)]
# test_case = [0 for _ in range(test_case_count)]

# for i in range(test_case_count):
#     repeat_number[i], *test_case[i] = list(input().split())

# print(repeat_number)
# print(len(test_case[1]))
# # print(len(test_case[0][0][0]))

# for j in range(test_case_count):
#     for k in range(len(test_case[j][0])):
#         print(test_case[j][0][k], end='')


# https://ooyoung.tistory.com/69#comment17933605 참고 후 작성.
# 테스트 케이스 출력과 관련해서는 해당 페이지 참고. https://www.acmicpc.net/blog/view/70
# https://www.acmicpc.net/blog/view/55
# 입력과 출력은 분리되어 있으므로 테스트케이스를 받을 때마다 출력해도 되고, 전부 받은 뒤 전부 출력해도 되고, 심지어 받기 전에 출력해도 된다. 하지만 출력 자체의 순서는 지켜야 합니다.

# 각 테스트 케이스에 대해 P를 출력한다.

testcase_count = int(input())

for _ in range(testcase_count):
    repeat_count, word = input().split()
    for tmp_word in word:
        print(tmp_word*int(repeat_count), end='')
    print()