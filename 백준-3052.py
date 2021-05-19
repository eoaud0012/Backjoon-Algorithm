import copy

input_list = [0 for _ in range(10)]
remain_list = copy.deepcopy(input_list)
result_list = copy.deepcopy(input_list)
input_number = 0

for i in range(len(input_list)):
    input_list[i] = int(input())

for j in range(len(input_list)):
    input_number = input_list[j]
    remain = input_number % 42
    remain_list[j] = remain

result_list = list(set(remain_list))
print(len(result_list))
