
class CowsAndBullsSolver:
    def __init__(self):
        self.possible_solutions = []
        for i in range(10000):
            a = i // 1000
            b= (i // 100) % 10
            c = (i // 10) % 10
            d = i % 10
            if a not in [b,c,d] and b not in [a,c,d] and c not in [a,b,d] and d not in [a,b,c]:
                self.possible_solutions.append((a, b, c, d))

    def is_solved(self):
        return len(self.possible_solutions) == 1

    def get_current_guess(self):
        return "".join(map(str, self.possible_solutions[0]))

    def make_guess(self, cows = None, bulls = None):
        print(f"{self.get_current_guess()}")
        if cows is None and bulls is None:
            cows = int(input("Cows: "))
            bulls = int(input("Bulls: "))
        self.possible_solutions = [x for x in self.possible_solutions if self.is_valid_solution(self.possible_solutions[0], cows, bulls, x)]
    
    def get_cows_bulls(self, guess, solution):
        cows = 0
        bulls = 0
        for i in range(len(guess)):
            if guess[i] == solution[i]:
                bulls += 1
            elif guess[i] in solution:
                cows += 1
        return cows, bulls

    def is_valid_solution(self, guess, cows, bulls, solution):
        return (cows, bulls) == self.get_cows_bulls(guess, solution)

    def solve(self):
        while not self.is_solved():
            self.make_guess()
        print(f"Answer: {''.join(map(str, self.possible_solutions[0]))}")

if __name__ == "__main__":
    solver = CowsAndBullsSolver()
    solver.solve()