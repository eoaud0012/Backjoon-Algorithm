# a = "734"
# a[::-1] --> 437
# 이항연산자 https://wikidocs.net/20701

num_one, num_two = input().split()

num_one_reverse = num_one[::-1]
num_two_reverse = num_two[::-1]

print(num_one_reverse if num_one_reverse > num_two_reverse else num_two_reverse)