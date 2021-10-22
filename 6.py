word = input()
mx = max([word.count(x) for x in word])
s = set(filter(lambda x: word.count(x) == mx, word))
print('Наиболее встречающийся символ(символы): {}'. format(', '.join(sorted(list(s)))))
