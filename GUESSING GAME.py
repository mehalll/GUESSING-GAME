guess_word = "elephant"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False



while guess != guess_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter the guess")
        guess_count += 1
    else:
            out_of_guesses = True




if out_of_guesses:
    print("OUT OF GUESSES")
    print("YOU LOSE")

else:
    print("CONGRATUALTIONS")
    print("YOU HAVE WON")
