from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Word Raider!")

title_lbl = Label(
    
)

btn_frm = Frame()

def dupe_finder(sequence):
    seen = set()
    seen_add = seen.add
    seen_twice = set(x for x in sequence if x in seen or seen_add(x))
    return list(seen_twice)

def player_guess():
    guess = input(f"({guesses_left} guesses left) Enter your guess: ").lower()
    
    if len(guess) != 5:
        print("Your guess must be a 5-letter word.")
        player_guess()
    if not guess.isalpha():
        print("Your guess must contain only letters.")
        player_guess() 
    else:
        return guess

playing = True

while playing == True:
    
    guesses_left = 5
    guesses = 0
    game_over = False
    dupe_letter_seen = False
    dupe_letter1_seen = False
    dupe_letter2_seen = False
    dupe_letter3_seen = False
    dupe_letter4_seen = False
    dupe_letter5_seen = False
    dupe_letter6_seen = False
    dupe_letter7_seen = False
    dupe_letter8_seen = False
    ind = 0
    correct_set = set()

    print(f"\nWelcome to Word Raider!\nYou have {guesses_left} tries to correctly guess a random 5-letter English word.\n")
    
    with open("fixed_words.txt", "r") as f:
        words = list(f)
    
    answer = random.choice(words).rstrip().lower()

    while game_over == False:
        if guesses_left - guesses == 0:
            print(f"You have run out of guesses.\nThe word was {answer}.\n")
            game_over = True
            break
        
        guess = input(f"\n({guesses_left - guesses} guesses remaining) Enter your guess: ").lower()
        print("\n")
    
        if len(guess) != 5:
            print("Your guess must be a 5-letter word.\n")
            continue
    
        if not guess.isalpha():
            print("Your guess may only contain letters.\n")
            continue
    
        guesses += 1
    
        if guess == answer:
            print(f"Congratulations! You correctly guessed the word in {guesses} guesses!\n")
            game_over = True
            break
        
        else:
        
            guess_tup = tuple(guess)
            if len(set(guess_tup)) != 5:
                guess_dupe = True
                guess_dupe_letter = dupe_finder(guess_tup)
                if len(guess_dupe_letter) == 1:
                    guess_dupe_number = 5 - len(set(guess) - set(guess_dupe_letter))
            else:
                guess_dupe = False
            
            answer_tup = tuple(answer)
            if len(set(answer_tup)) != 5:
                answer_dupe = True
                answer_dupe_letter = dupe_finder(answer_tup)
                if len(answer_dupe_letter) == 1:
                    answer_dupe_number = 5 - len(set(answer) - set(answer_dupe_letter))
            else:
                answer_dupe = False
            
            try:
                if guess_dupe_number >= answer_dupe_number:        
                    diff = guess_dupe_number - answer_dupe_number
                
                if len(guess_dupe_letter)  == 2:
                    guess_dupe1_number = 5 - len(set(guess) - set(guess_dupe_letter[0]))
                    guess_dupe2_number = 5 - len(set(guess) - set(guess_dupe_letter[1]))
                
                    if len(answer_dupe_letter) == 1:
                        if guess_dupe_letter[0] in answer_dupe_letter:
                            if guess_dupe1_number >= answer_dupe_number:
                                diff1 = guess_dupe1_number - answer_dupe_number
                    
                        if guess_dupe_letter[1] in answer_dupe_letter:
                            if guess_dupe2_number >= answer_dupe_number:
                                diff2 = guess_dupe2_number - answer_dupe_number
                
                if len(answer_dupe_letter) == 2:
                    answer_dupe1_number = 5 - len(set(answer) - set(answer_dupe_letter[0]))
                    answer_dupe2_number = 5 - len(set(answer) - set(answer_dupe_letter[1]))
                    
                    if len(guess_dupe_letter) == 2:
                        if guess_dupe_letter[0] == answer_dupe_letter[0]:
                            if guess_dupe1_number >= answer_dupe1_number:
                                diff3 = guess_dupe1_number - answer_dupe1_number
                        if guess_dupe_letter[0] == answer_dupe_letter[1]:
                            if guess_dupe1_number >= answer_dupe2_number:
                                diff4 = guess_dupe1_number - answer_dupe2_number                    
                        if guess_dupe_letter[1] == answer_dupe_letter[0]:
                            if guess_dupe2_number >= answer_dupe1_number:
                                diff5 = guess_dupe2_number - answer_dupe1_number
                        if guess_dupe_letter[1] == answer_dupe_letter[1]:
                            if guess_dupe2_number >= answer_dupe2_number:
                                diff6 = guess_dupe2_number - answer_dupe2_number
                                
                    if len(guess_dupe_letter) == 1:
                        if guess_dupe_letter == answer_dupe_letter[0]:
                            if guess_dupe_number >= answer_dupe1_number:
                                diff7 = guess_dupe_number - answer_dupe1_number
                                      
                        if guess_dupe_letter == answer_dupe_letter[1]:
                            if guess_dupe_number >= answer_dupe2_number:
                                diff8 = guess_dupe_number - answer_dupe2_number
            except NameError:
                pass
            
            ind = 0
            
            for letter in guess_tup:
                if letter == answer_tup[guess_tup.index(letter, ind)]:
                    correct_set.add(letter)
                    
                ind += 1
                
            ind = 0    
                                     
            for letter in guess_tup:
                checks = {letter}
                checks.add(answer_tup[guess_tup.index(letter, ind)])
                ind += 1
                
                if len(checks) == 1:
                    print(f"{letter}: Correct letter at correct position.")
                    continue
                
                if letter in answer_tup:
                    
                    if guess_dupe == False:
                        print(f"{letter}: Correct letter at incorrect position.")
                        continue
                    
                    if guess_dupe == True and answer_dupe == False:
                        if letter in correct_set:
                            print(f"{letter}: Incorrect letter.")
                            continue
                        
                        if letter in guess_dupe_letter:
                            if len(guess_dupe_letter) == 1:
                                if dupe_letter_seen == False:
                                    dupe_letter_seen = True
                                    print(f"{letter}: Correct letter at incorrect position.")
                                    continue
                                else:
                                    print(f"{letter}: Incorrect letter.")
                                    continue
                            if len(guess_dupe_letter) == 2:
                                if letter == guess_dupe_letter[0]:
                                    if dupe_letter1_seen == False:
                                        dupe_letter1_seen = True
                                        print(f"{letter}: Correct letter at incorrect position.")
                                        continue
                                    else:
                                        print(f"{letter}: Incorrect letter.")
                                        continue
                                if letter == guess_dupe_letter[1]:
                                    if dupe_letter2_seen == False:
                                        dupe_letter2_seen = True
                                        print(f"{letter}: Correct letter at incorrect position.")
                                        continue
                                    else:
                                        print(f"{letter}: Incorrect letter.")
                                        continue                                    
                        else:
                            print(f"{letter}: Correct letter at incorrect position.")
                            continue
                            
                    if guess_dupe == True and answer_dupe == True:                        
                        if letter in guess_dupe_letter:
                            if letter in answer_dupe_letter:
                                if len(answer_dupe_letter) == 1 and len(guess_dupe_letter) == 1:
                                    if diff != 0:
                                        print(f"{letter}: Incorrect letter.")
                                        diff -= 1
                                        continue
                                    else:
                                        print(f"{letter}: Correct letter at incorrect position.")
                                        continue
                                
                                if len(answer_dupe_letter) == 1 and len(guess_dupe_letter) == 2:
                                    if guess_dupe_letter in answer_dupe_letter:                                            
                                        if guess_dupe_letter[0] in answer_dupe_letter:    
                                            if letter == guess_dupe_letter[0]:
                                                if diff1 != 0:
                                                    print(f"{letter}: Incorrect letter.")
                                                    diff1 -= 1
                                                    continue
                                                else:
                                                    print(f"{letter}: Correct letter at incorrect position.")
                                                    continue
                                            else:
                                                if dupe_letter3_seen == False:
                                                    dupe_letter3_seen = True
                                                    print(f"{letter}: Correct letter at incorrect position.")
                                                    continue
                                                else:
                                                    print(f"{letter}: Incorrect letter.")
                                                    continue
                                    
                                        if guess_dupe_letter[1] in answer_dupe_letter:
                                            if letter == guess_dupe_letter[1]:
                                                if diff2 != 0:
                                                    print(f"{letter}: Incorrect letter.")
                                                    diff2 -= 1
                                                    continue
                                                else:
                                                    print(f"{letter}: Correct letter at incorrect position.")
                                                    continue
                                            else:
                                                if dupe_letter4_seen == False:
                                                    dupe_letter4_seen = True
                                                    print(f"{letter}: Correct letter at incorrect position.")
                                                    continue
                                                else:
                                                    print(f"{letter}: Incorrect letter.")
                                                    continue
                                    else:
                                        if letter == guess_dupe_letter[0]:
                                            if dupe_letter5_seen == False:
                                                dupe_letter5_seen = True
                                                print(f"{letter}: Correct letter at incorrect position.")
                                                continue
                                            else:
                                                print(f"{letter}: Incorrect letter.")
                                                continue
                                        else:
                                            if dupe_letter6_seen == False:
                                                dupe_letter6_seen = True
                                                print(f"{letter}: Correct letter at incorrect position.")
                                                continue
                                            else:
                                                print(f"{letter}: Incorrect letter.")
                                                continue
                                            
                                if len(answer_dupe_letter) == 2 and len(guess_dupe_letter) == 1:
                                    if guess_dupe_letter in answer_dupe_letter:
                                        if guess_dupe_letter == answer_dupe_letter[0]:
                                            if diff7 != 0:
                                                print(f"{letter}: Incorrect letter.")
                                                diff7 -= 1
                                                continue
                                            else:
                                                print(f"{letter}: Correct letter at incorrect position.")
                                                continue
                                            
                                        if guess_dupe_letter == answer_dupe_letter[1]:
                                            if diff8 != 0:
                                                print(f"{letter}: Incorrect letter.")
                                                diff8 -= 1
                                                continue
                                            else:
                                                print(f"{letter}: Correct letter at incorrect position.")
                                                continue
                                    else:
                                        if letter in correct_set:
                                            print(f"{letter}: Incorrect letter.")
                                            continue
                                                                
                                        if letter in guess_dupe_letter:
                                            if len(guess_dupe_letter) == 1:
                                                if dupe_letter_seen == False:
                                                    dupe_letter_seen = True
                                                    print(f"{letter}: Correct letter at incorrect position.")
                                                    continue
                                                else:
                                                    print(f"{letter}: Incorrect letter.")
                                                    continue
                                            if len(guess_dupe_letter) == 2:
                                                if letter == guess_dupe_letter[0]:
                                                    if dupe_letter1_seen == False:
                                                        dupe_letter1_seen = True
                                                        print(f"{letter}: Correct letter at incorrect position.")
                                                        continue
                                                    else:
                                                        print(f"{letter}: Incorrect letter.")
                                                        continue
                                                if letter == guess_dupe_letter[1]:
                                                    if dupe_letter2_seen == False:
                                                        dupe_letter2_seen = True
                                                        print(f"{letter}: Correct letter at incorrect position.")
                                                        continue
                                                    else:
                                                        print(f"{letter}: Incorrect letter.")
                                                        continue                                    
                                        else:
                                            print(f"{letter}: Correct letter at incorrect position.")
                                            continue
                                                                                                                       
                                if len(answer_dupe_letter) == 2 and len(guess_dupe_letter) == 2:
                                    if guess_dupe_letter in answer_dupe_letter:
                                        if letter == guess_dupe_letter[0]:
                                            if guess_dupe_letter[0] == answer_dupe_letter[0]:
                                                if diff3 != 0:
                                                    print(f"{letter}: Incorrect letter.")
                                                    diff3 -= 1
                                                    continue
                                                else:
                                                    print(f"{letter}: Correct letter at incorrect position.")
                                                    continue
                                            if guess_dupe_letter[0] == answer_dupe_letter[1]:
                                                if diff4 != 0:
                                                    print(f"{letter}: Incorrect letter.")
                                                    diff4 -= 1
                                                    continue
                                                else:
                                                    print(f"{letter}: Correct letter at incorrect position.")
                                                    continue
                                        if letter == guess_dupe_letter[1]:
                                            if guess_dupe_letter[1] == answer_dupe_letter[0]:
                                                if diff5 != 0:
                                                    print(f"{letter}: Incorrect letter.")
                                                    diff5 -= 1
                                                    continue
                                                else:
                                                    print(f"{letter}: Correct letter at incorrect position.")
                                                    continue
                                            if guess_dupe_letter[1] == answer_dupe_letter[1]:
                                                if diff6 != 0:
                                                    print(f"{letter}: Incorrect letter.")
                                                    diff6 -= 1
                                                else:
                                                    print(f"{letter}: Correct letter at incorrect position.")
                                                 
                                    else:
                                        if letter == guess_dupe_letter[0]:
                                            if dupe_letter7_seen == False:
                                                dupe_letter7_seen = True
                                                print(f"{letter}: Correct letter at incorrect position.")
                                            else:
                                                print(f"{letter}: Incorrect letter.")
                                        else:
                                            if dupe_letter8_seen == False:
                                                dupe_letter8_seen = True
                                                print(f"{letter}: Correct letter at incorrect position.")
                                            else:
                                                print(f"{letter}: Incorrect letter.")
                                              
                            else:
                                if letter in correct_set:
                                    print(f"{letter}: Incorrect letter.")
                                    continue
                                    
                                if len(guess_dupe_letter) == 1:
                                    if dupe_letter_seen == False:
                                        dupe_letter_seen = True
                                        print(f"{letter}: Correct letter at incorrect position.")
                                    else:
                                        print(f"{letter}: Incorrect letter.")

                                else:
                                    if letter == guess_dupe_letter[0]:
                                        if dupe_letter1_seen == False:
                                            dupe_letter1_seen = True
                                            print(f"{letter}: Correct letter at incorrect position.")
                                        else:
                                            print(f"{letter}: Incorrect letter.")
                                    else:
                                        if dupe_letter2_seen == False:
                                            dupe_letter2_seen = True
                                            print(f"{letter}: Correct letter at incorrect position.")
                                        else:
                                            print(f"{letter}: Incorrect letter.")

                        else:
                            if letter in correct_set:
                                print(f"{letter}: Incorrect letter.")
                            else:    
                                print(f"{letter}: Correct letter at incorrect position.")
                else:
                    print(f"{letter}: Incorrect letter.")
                        
    play_again = input("Would you like to play again? (Y/N): ").lower()
    print("\n")
    if play_again == "y":
        game_over = False
    else:
        exit()