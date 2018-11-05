import random

def number_check(myNumberStr):
    # check if is a number
    try:
        _ = int(myNumberStr)
    except ValueError:
        return False
    # check that is 4-digit
    if len(myNumberStr) != 4:
        return False
    # check that all digits are different
    for digit in myNumberStr:
        if myNumberStr.count(digit) > 1:
            return False
    return True

class CowsAndBullsGame:
    """Cows&Bulls game

    Main game class
    """
    def __init__(self, secret_number = None):
        if secret_number:
            if not number_check(secret_number):
                raise ValueError(f"Incorrect number {secret_number}")
            self.secret_number = secret_number
        else:
            self.secret_number = str(random.randint(1000, 9999))
            while not number_check(self.secret_number):
                self.secret_number = str(random.randint(1000, 9999))
        self.cows = 0
        self.bulls = 0
        self.steps = 0

    def detect_cows_bulls(self, myNumberStr):
        self.bulls = sum(1 if myNumberStr[i] == self.secret_number[i] else 0 for i in range(4))
        self.cows = sum(1 if myNumberStr[i] in self.secret_number and myNumberStr[i] != self.secret_number[i] else 0 for i in range(4))
        self.steps += 1

    def is_solved(self):
        return self.bulls == 4

    def game_step(self):
        myNumberStr = input()
        if number_check(myNumberStr):
            self.detect_cows_bulls(myNumberStr)
        else:
            print("Invalid input!")
            return
        if self.bulls < 4:
            print("Cows: %d" % self.cows)
            print("Bulls: %d" % self.bulls)

if __name__ == '__main__':
    game = CowsAndBullsGame()
    print("Welcome to cows&bulls game! Enter your first guess:")
    while not game.is_solved():
        game.game_step()
    print("Congratulations, you guessed number %s in %d steps" % (game.secret_number, game.steps))
