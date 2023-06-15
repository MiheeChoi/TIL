numbers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQSR', 'TUV', 'WXYZ']
sum = 0
input_alphabet = input()
for i in input_alphabet:
    for j in numbers:
        if i in j:
            sum += numbers.index(j) + 3
print(sum)
