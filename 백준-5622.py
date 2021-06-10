num_dict = {2 : ['A', 'B', 'C']
           ,3 : ['D', 'E', 'F']
           ,4 : ['G', 'H', 'I']
           ,5 : ['J', 'K', 'L']
           ,6 : ['M', 'N', 'O']
           ,7 : ['P', 'Q', 'R', 'S']
           ,8 : ['T', 'U', 'V']
           ,9 : ['W', 'X', 'Y', 'Z']}

# UNUCIC
alphabet_list = list(input())
number_list = []

# [number for number, alhphabet in num_dict.items() if alhphabet = 'Something']
for input_alphabet in alphabet_list:
    for number, alphabet_keys in num_dict.items():
        if(input_alphabet in alphabet_keys):
            number_list.append(number)

#1을 걸려면 2초, 2를 걸려면 3초 ... 9를 걸려면 10초.
print(sum(number_list)+len(number_list))
