# a = 121
# print(list(str(a)))
# 숫자 121 -> ['1', '2', '1']

hansoo_count = 0

def check_arithmetic_sequence(num_int):

    global hansoo_count



    if(len(str(num_int)) == 1 or len(str(num_int)) == 2):
        hansoo_count += 1

    else:
        num_str = list(str(num_int))
        if( sum(map(int, num_str)) == ( ( int(num_str[0]) + int(num_str[len(num_str) - 1]) ) * len(num_str) ) / 2 ):
            hansoo_count += 1
    
    return

input_count = int(input())

for i in range(1, input_count+1):
    check_arithmetic_sequence(i)

print(hansoo_count)
