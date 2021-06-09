# 알파벳 대문자, 소문자 갯수 = 총 52개
# 52개짜리 배열 생성 -> 한 글자씩 체크
# 대문자부터

# print(ord('A')) # 65
# print(ord('a')) # 97
# print(ord('z')) # 122

# 리스트를 딕셔너리로 변환 https://security-nanglam.tistory.com/427
# 딕셔너리 요소 중 최대값(다수 존재시) https://bio-info.tistory.com/40

upper_alpha = [chr(alphabet) for alphabet in range(ord('A'), ord('Z') + 1)]

upper_alpha_freq = [0 for _ in range(26 + 1)]

input_word = list(input().upper())

for input_alphabet in input_word:
    upper_alpha_freq[upper_alpha.index(input_alphabet)] += 1

freq_dict = dict(zip(upper_alpha, upper_alpha_freq))

max_in_freq_dict = [alphabet for alphabet, frequency in freq_dict.items() if max(freq_dict.values()) == frequency]

if(len(max_in_freq_dict) == 1):
    print(max_in_freq_dict[0])
else:
    print('?')
