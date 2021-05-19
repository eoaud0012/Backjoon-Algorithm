a = int(input())
b = int(input())
c = int(input())

result = a*b*c
count_list = [0 for _ in range(10)] # 1차원배열 초기화  -- > arr = [0] * n 


while(result > 0):
    remain = int(result % 10)
    count_list[remain] += 1
    result = int(result / 10)

for index in range(len(count_list)):
    print(count_list[index])