# create a game in which store a secrete word and user should guess the secret word
secret_word = "University"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guess = False

while guess != secret_word and not (out_of_guess):
    if guess_count < guess_limit:
        guess = input("enter guess values")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("Out of guess!, you have lose the game")
else:
    print("you have Win the game!")


