import random
from words import word_list
from tkinter import *
window=Tk()

#THIS MAKES CANVAS
canvas = Canvas(window, width =500, height=475, borderwidth=1, bg="white")
canvas.place(x=80, y=180)

def elliptical_arc(canvas, x, y, r1, r2, t0, t1, width):
    return canvas.create_arc(x-r1, y-r2, x+r1, y+r2, start=t0, extent=t1-t0,
                             style='arc', width=width, outline="black")

# Function to return a random word from a list of words
def random_word():
    word = random.choice(word_list) 
    return word.lower()


tries = 7
word = random_word()
word_completion = '_' * len(word)
guessed_letters = []

def draw_hangman(canvas, tries):
    canvas.create_line(10, 450, 150, 450, fill="black", width=5)
    canvas.create_line(80, 450, 80, 40, fill="black", width=5)
    canvas.create_line(78, 40, 270, 40, fill="black", width=5)
    canvas.create_line(270, 38, 270, 85, fill="black", width=5)
    if tries == 7:
        return
    canvas.create_oval(220, 85, 320, 185, fill="white", outline="black", width=5)#Head
    if tries == 6:
        return
    canvas.create_line(270, 185, 270, 300, fill="black", width=5)#torso
    if tries == 5:
        return
    canvas.create_line(270, 300, 225, 375, fill="black", width=5)#Leg L
    if tries == 4:
        return
    canvas.create_line(270, 300, 315, 375, fill="black", width=5)#Leg R
    if tries == 3:
        return
    canvas.create_line(270, 200, 190, 250, fill="black", width=5)#arm L
    if tries == 2:
        return   
    canvas.create_line(270, 200, 350, 250, fill="black", width=5)#arm R
    if tries == 1:
        return
    elliptical_arc(canvas, midx, midy, r1, r2, 60, 180-60, 3)
    canvas.create_line(315, 375, 345, 375, fill="black", width=5)#foot R
    canvas.create_line(225, 375, 195, 375, fill="black", width=5)#foot L
    if tries == 0:
        return
    canvas.create_line(285, 115, 295, 125, fill="black", width=5)
    canvas.create_line(285, 125, 295, 115, fill="black", width=5)
    canvas.create_line(255, 115, 245, 125, fill="black", width=5)
    canvas.create_line(255, 125, 245, 115, fill="black", width=5)
    midx, midy = 270, 200
    r1, r2 = 50, 50
    if tries <= 0:
        return
    






def reset_game():
    global tries, word, word_completion, guessed_letters
    tries = 7
    word = random_word()
    word_completion = '_' * len(word)
    guessed_letters = []
    completion.config(text='')
    guess_entry.delete(0, END)
    letters_guessed.config(text='')
    set_word_status(word_completion)
    play_again_btn.place_forget()
    yes_btn.place_forget()
    no_btn.place_forget()
    canvas.delete("all")
    draw_hangman(canvas, tries)

def set_word_status(completion):
    information.config(text=' '.join(completion))


# guess_entry = top entry
# completion = bottom entry
# btn = the button 
# infromation = the very bottom entry
def when_they_click_guess_button():
    print(guessed_letters)
    completion.config(text='')
    guess = guess_entry.get().lower()
    guess_entry.delete(0,END)    
    global tries

    if tries <= 0: 
        completion.config(text='')
        completion.config(text="You lose! You used up all your guesses")
        information.config(text="The word was " + word)
        play_again_btn.place(x=875, y=285)
        no_btn.place(x=980, y=350)
        yes_btn.place(x=880, y=350)

        return
    if len(guess) == 0:
        completion.config(text='Invalid')
        return
    if guess in guessed_letters:
        completion.config(text=f"You've already guessed {guess}")
        return
    if len(guess) == 1:
        guessed_letters.append(guess)
        # We know the guess is 1 character long
        # Check if the character is in the word
        if guess in word:
            completion.config(text=guess + ' is in the word')
        else:
            completion.config(text=guess + ' is not in the word')
            tries -= 1
        letters_guessed.config(text=' '.join(guessed_letters))        
        # character is in the word:
        # Then update word_completion
        word_completion = ''
        for letter in word:
            if letter in guessed_letters:
                word_completion += letter
            else:
                word_completion += '-'
        set_word_status(word_completion)
    elif guess == word:
        # The guess is the entire word
        completion.config(text='')
        completion.config(text='Congrats you guessed the word!')
        word_completion = word
        set_word_status(word_completion)
        play_again_btn.place(x=875, y=285)        
        no_btn.place(x=980, y=350)
        yes_btn.place(x=880, y=350)

    else:
        completion.config(text=guess +' was not the word')
        tries -= 1 

    if set(word) <= set(guessed_letters):
        completion.config(text='')
        completion.config(text='You Win! You guessed the word')
        word_completion = word
        set_word_status(word_completion)
        play_again_btn.place(x=875, y=285)
        no_btn.place(x=980, y=350)
        yes_btn.place(x=880, y=350)

        # Algo:
        # Look at each letter in the real word
        # Check if that letter is the guess
        # If its the guess, keep it.
        # If its not the guess, use a -
    draw_hangman(canvas, tries)


# This creates a button on the screen
# The 'command' parameter, says what code to run when it's clicked.
btn = Button(window, text="Guess", fg='blue', command=when_they_click_guess_button, font=('Arial',30))
btn.place(x=900, y=175)

#This creates the play again button
play_again_btn = Label(window, text= 'Play Again?', font=('Arial',25))

#This creates the 'yes' button for play again
yes_btn = Button(window, text ='Yes', command=reset_game, font=('Arial',25))

#This creates the 'no' button for play again
no_btn = Button(window, text ='No', command=window.destroy, font=('Arial',25))

# This creates an entry box on the screen
guess_entry = Entry(window, width = 20,text="Write your guess here", bd=2, font= ('Arial', 30))
guess_entry.place(x=750, y=100)

# This creates an entry box on the screen to store the current result
completion = Label(window, width = 30, text='', bd=2, font= ('Arial', 20))
completion.place(x=700, y=475)

# This creates an entry box on the screen to store the information for the user
information = Label(window, width = 30, text=word_completion, bd=2, font= ('Arial', 30))
information.place(x=600, y=580)

#This creates the entry for the guessed letters
letters_guessed = Label(window, width = 40, text='', bd=2, font= ('Arial', 23) )
letters_guessed.place(x=150, y=32)

#This creates the lable for the guessed letters
letters_guessed_title = Label(window, width = 15, text="Guessed Letters:", font= ('Arial', 30))
letters_guessed_title.place(x=25, y=30)

draw_hangman(canvas=canvas, tries=tries)

set_word_status(word_completion)

window.title('Hangman')
window.geometry("1275x690")
window.mainloop()
