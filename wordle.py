import random 


def load_dictionary(file_path):
    print("Loading dict")
    with open(file_path) as file: 
        words = [line.strip() for line in file]
    return words

#dont need this for now, accept any 5 letter 'word'
def is_valid_guess(guess, guesses):
    pass

def evaluate_guess(guess, goal) -> str: 
    eval = ""

    for i in range(5):
        if guess[i] == goal[i]:
            eval += "\033[32m" + guess[i]
        elif guess[i] in goal:
            eval += "\033[33m" + guess[i]
        else: 
            eval += "\033[0m" + guess[i]

    return eval + "\033[0m"

def wordle(answers): 
    print("Welcome to wordle, enter a word to begin!")
    goal = random.choice(answers)
    attempts = 0

    while attempts <= 6:
        guess = input("").lower()
       
        if len(guess) != 5: 
            print("Please enter a 5 letter word!")
            continue 

        if guess == goal: 
            print("\nCongratulations you guessed the word!!")
            break 

        evaluated_guess = evaluate_guess(guess, goal)
        print(evaluated_guess)
        attempts += 1

    print("You failed! The word was: " + goal)



if __name__ == "__main__":
    answers = load_dictionary("answers.txt")
    wordle(answers)
