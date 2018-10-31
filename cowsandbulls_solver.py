digit_possibilities = [0] * 10
digit_place_possibilities = [[0] * 4 for i in range(10)]

def get_cows_bulls(guess, solution):
    cows = 0
    bulls = 0
    for i in range(len(guess)):
        if guess[i] == solution[i]:
            bulls += 1
        elif guess[i] in solution:
            cows += 1
    return cows, bulls

def is_valid_solution(guess, cows, bulls, solution):
    return (cows, bulls) == get_cows_bulls(guess, solution)

possible_solutions = []
for i in range(10000):
    a = i // 1000
    b= (i // 100) % 10
    c = (i // 10) % 10
    d = i % 10
    if a not in [b,c,d] and b not in [a,c,d] and c not in [a,b,d] and d not in [a,b,c]:
        possible_solutions.append((a, b, c, d))

while len(possible_solutions) > 1:
    print(possible_solutions[0])
    cows = int(input("Cows: "))
    bulls = int(input("Bulls: "))
    possible_solutions = [x for x in possible_solutions if is_valid_solution(possible_solutions[0], cows, bulls, x)]

# for number in current_guess:
#     digit_possibilities[number] = (cows + bulls) / 4

# for i in range(4):
#     for j in range(4):
#         if i == j:
#             digit_place_possibilities[current_guess[i]][i] = bulls / 4
#         else:
#             digit_place_possibilities[current_guess[i]][j] = cows / 4

# print(digit_possibilities)
# print(digit_place_possibilities)