import cowsandbulls
import cowsandbulls_solver

if __name__ == "__main__":
    game_count = 10
    max_guesses = 0
    total_guesses = 0
    for i in range(game_count):
        game = cowsandbulls.CowsAndBullsGame()
        solver = cowsandbulls_solver.CowsAndBullsSolver()
        while not game.is_solved():
            game.detect_cows_bulls(solver.get_current_guess())
            solver.make_guess(game.cows, game.bulls)
        print(f"Game is solved in {game.steps} steps")
        max_guesses = max(max_guesses, game.steps)
        total_guesses += game.steps
    print(f"Average guesses to solve: {total_guesses / game_count}")