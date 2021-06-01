count = 10001
number = [x for x in range(count)]
not_self_number = []
self_number = []

def digit_sum(num):
    return num + sum(map(int, str(num)))

for i in range(count):
    not_self_number.append(digit_sum(i))

self_number = list(set(number) - set(not_self_number))
self_number.sort()

for j in self_number:
    print(j)


# (파이썬 각 자리수 합) https://velog.io/@joygoround/test%EC%9E%90%EB%A6%BF%EC%88%98-%EB%8D%94%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC