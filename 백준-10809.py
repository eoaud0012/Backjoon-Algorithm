alphabet_list = input()

for i in range(ord('a'), ord('z') + 1):
    if(chr(i) in alphabet_list):
        print(alphabet_list.index(chr(i)), end=' ')
    else:
        print(-1, end=' ')