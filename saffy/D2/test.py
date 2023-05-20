# Prompt the user for input and parse the resulting string into a list of integers
input_str = input("Enter a list of numbers, separated by commas: ")
input_list = [int(x) for x in input_str.split(',')]

# Compute the ranks of the input values using a custom function
n = len(input_list)

ranks = [0] * n
for i in range(n):
    rank = 1
    for j in range(n):
        if input_list[j] > input_list[i]:
            rank += 1
    ranks[i] = rank

print(ranks)  # Output: [3, 2, 4, 1]