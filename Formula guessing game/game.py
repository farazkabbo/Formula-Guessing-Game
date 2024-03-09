import random

def generate_formula():
    # Generate a random formula
    operators = ['+', '-', '*', '/']
    formula = ""
    for _ in range(3):
        formula += str(random.randint(1, 10)) + random.choice(operators)
    formula += str(random.randint(1, 10))
    return formula

def evaluate_formula(formula):
    # Evaluate the formula
    try:
        result = eval(formula)
        return result
    except ZeroDivisionError:
        return None

def play_game():
    formula = generate_formula()
    result = evaluate_formula(formula)
    if result is None:
        print("Error: Division by zero. Try again.")
        play_game()
    else:
        print("Guess the result of the formula:", formula)
        guess = float(input("Your guess: "))
        if guess == result:
            print("Congratulations! You guessed it right!")
        else:
            print("Sorry, the correct answer was:", result)

if __name__ == "__main__":
    play_game()