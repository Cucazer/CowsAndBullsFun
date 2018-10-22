digit_possibilities = [0] * 10
digit_place_possibilities = [[0] * 4 for i in range(10)]

current_guess = [0,1,2,3]
print(current_guess)
cows = int(input("Cows: "))
bulls = int(input("Bulls: "))

for number in current_guess:
    digit_possibilities[number] = (cows + bulls) / 4

for i in range(4):
    for j in range(4):
        if i == j:
            digit_place_possibilities[current_guess[i]][i] = bulls / 4
        else:
            digit_place_possibilities[current_guess[i]][j] = cows / 4

print(digit_possibilities)
print(digit_place_possibilities)