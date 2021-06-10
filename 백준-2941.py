# 특정 요소 다 지우는 방법 
# https://hashcode.co.kr/questions/1158/%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%95%88%EC%97%90-%ED%8A%B9%EC%A0%95%EA%B0%92%EC%9D%84-%EB%8B%A4-%EC%A7%80%EC%9A%B0%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%9D%B4-%EA%B6%81%EA%B8%88%ED%95%A9%EB%8B%88%EB%8B%A4
# x = [1,2,3,2,2,2,3,4]
# filter(lambda a: a != 2, x)
#
# x = [1,2,3,2,2,2,3,4]
# list(filter((2).__ne__, x))

# def remove_values_from_list(the_list, val):
#    return [value for value in the_list if value != val]
# x = [1, 2, 3, 4, 2, 2, 3]
# removeAllOccur(x,10)

# def removeAllOccur(l, i):
#     try:
#         while True : l.remove(i)
#     except ValueError:
#         pass
# x = [1, 2, 3, 4, 2, 2, 3]
# x = remove_values_from_list(x, 2)

count = 0
word = input()

croatia_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for alphabet in croatia_alphabet:
    while(alphabet in word):
        count += 1
        word = word.replace(alphabet, ' ', 1)

word_list_space_remained = list(word)
word_list_space_removed = list(filter((' ').__ne__, word_list_space_remained))
count += len(word_list_space_removed)
print(count)



