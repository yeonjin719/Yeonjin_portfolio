num = int(input())
word_list = []
for i in range(num):
    word_list.append(input())
word_list = list(set(word_list))

word_list.sort()
word_list.sort(key = lambda x :len(x))

for j in range(len(word_list)):
    print(word_list[j])